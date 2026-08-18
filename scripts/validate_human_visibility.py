#!/usr/bin/env python3
"""Validate the deterministic part of a consumer stakeholder-brief contract.

This script deliberately does not score prose, render screenshots, or decide
whether a stakeholder brief is useful.  Those remain independent human review
responsibilities at the Human Visibility gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


REQUIRED_SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")
REQUIRED_SECTION_IDS = ("decision-snapshot", "scope", "validation", "decision")
PLACEHOLDERS = ("<initiative>", "<YYYY-MM-DD>")
BASELINE_FILE = "human-visibility-baseline.json"
EXCEPTION_FILE = "human-visibility-exception.yaml"


@dataclass
class Report:
    structural: list[str] = field(default_factory=list)
    gate: list[str] = field(default_factory=list)
    freshness: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    human_review: list[str] = field(default_factory=lambda: [
        "Independent reviewer must confirm the brief is accurate, decision-useful, "
        "proportional, and visually legible in its rendered form.",
        "A structural pass is not Human Visibility approval and does not replace "
        "the required independent semantic/rendered review.",
    ])

    @property
    def failures(self) -> list[str]:
        return self.structural + self.gate + self.freshness


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, report: Report, label: str) -> dict[str, object] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        report.structural.append(f"invalid {label}: {path.name} ({error})")
        return None
    if not isinstance(value, dict):
        report.structural.append(f"invalid {label}: {path.name} must contain an object")
        return None
    return value


def load_exception_yaml(path: Path, report: Report) -> dict[str, str] | None:
    """Read the deliberately tiny, portable exception contract without PyYAML."""
    values: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        report.structural.append(f"invalid Human Visibility exception: {path.name} ({error})")
        return None
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z_]+):\s*(.+)", stripped)
        if not match:
            report.structural.append(f"invalid Human Visibility exception: unsupported line {stripped!r}")
            return None
        value = re.split(r"\s+#", match.group(2).strip(), maxsplit=1)[0].strip()
        values[match.group(1)] = value.strip('"\'')
    return values


def approved_exception(initiative: Path, report: Report) -> str | None:
    path = initiative / EXCEPTION_FILE
    if not path.is_file():
        return None
    exception = load_exception_yaml(path, report)
    if exception is None:
        return None
    scope = exception.get("scope")
    required = ("reason", "owner", "human_visibility_status")
    missing = [key for key in required if not isinstance(exception.get(key), str) or not exception[key].strip()]
    if missing or exception.get("human_visibility_status") != "reviewed":
        report.gate.append(
            "unapproved Human Visibility exception: requires non-empty reason, owner, "
            "and human_visibility_status: reviewed"
        )
        return None
    if scope not in {"not_applicable", "freshness"}:
        report.gate.append("unapproved Human Visibility exception: scope must be not_applicable or freshness")
        return None
    return str(scope)


def check_gate_state(initiative: Path, report: Report) -> None:
    state = initiative / "run-state.yaml"
    if not state.is_file():
        report.gate.append("missing required source artifact: run-state.yaml")
        return
    content = state.read_text(encoding="utf-8")
    match = re.search(r"(?m)^\s{2}human_visibility_ready:\s*(\S+)\s*$", content)
    if not match:
        report.gate.append("run-state.yaml lacks quality_gates.human_visibility_ready")
    elif match.group(1).lower() != "true":
        report.gate.append("Human Visibility gate is not declared ready in run-state.yaml")


def check_brief(initiative: Path, report: Report, not_applicable: bool) -> None:
    brief = initiative / "stakeholder-brief.html"
    if not brief.is_file():
        if not not_applicable:
            report.structural.append("missing stakeholder brief: stakeholder-brief.html")
        return
    html = brief.read_text(encoding="utf-8")
    for section_id in REQUIRED_SECTION_IDS:
        if not re.search(rf'\bid\s*=\s*["\']{re.escape(section_id)}["\']', html):
            report.structural.append(f"missing stakeholder brief section id: {section_id}")
    for source in REQUIRED_SOURCES:
        if not re.search(rf'href\s*=\s*["\']{re.escape(source)}["\']', html):
            report.structural.append(f"missing stakeholder brief source link: {source}")
    for placeholder in PLACEHOLDERS:
        if placeholder in html:
            report.structural.append(f"unresolved stakeholder brief placeholder: {placeholder}")


def changed_paths_from_git(root: Path, base_ref: str, initiative: Path) -> tuple[set[str] | None, str | None]:
    relative = initiative.relative_to(root).as_posix()
    result = subprocess.run(
        ["git", "-C", str(root), "diff", "--name-only", base_ref, "--", relative],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        return None, result.stderr.strip() or "git diff failed"
    prefix = relative + "/"
    return {path[len(prefix):] for path in result.stdout.splitlines() if path.startswith(prefix)}, None


def check_baseline_freshness(sources: dict[str, Path], initiative: Path, report: Report, exception_scope: str | None) -> None:
    baseline_path = initiative / BASELINE_FILE
    if not baseline_path.is_file():
        if exception_scope == "freshness":
            report.limitations.append("freshness baseline absent; explicit reviewed freshness exception accepted")
        else:
            report.freshness.append(
                f"missing freshness baseline: {BASELINE_FILE}; run with --write-baseline after independent review or record a reviewed freshness exception"
            )
        return
    baseline = load_json(baseline_path, report, "freshness baseline")
    if baseline is None:
        return
    recorded = baseline.get("source_sha256")
    if not isinstance(recorded, dict):
        report.freshness.append(f"invalid freshness baseline: {BASELINE_FILE} lacks source_sha256")
        return
    changed = [name for name, path in sources.items() if recorded.get(name) != digest(path)]
    if changed:
        if exception_scope == "freshness":
            report.limitations.append("changed source artifact(s) accepted by explicit reviewed freshness exception: " + ", ".join(changed))
        else:
            report.freshness.append("stakeholder brief is stale for changed source artifact(s): " + ", ".join(changed))


def check_freshness(initiative: Path, root: Path, base_ref: str | None, report: Report, exception_scope: str | None) -> None:
    sources = {name: initiative / name for name in REQUIRED_SOURCES}
    for name, path in sources.items():
        if not path.is_file():
            report.structural.append(f"missing required source artifact: {name}")
    if report.structural:
        return
    if base_ref:
        changed, error = changed_paths_from_git(root, base_ref, initiative)
        if changed is None:
            report.limitations.append(
                f"cannot compare freshness against Git base ref {base_ref!r}; falling back to {BASELINE_FILE}: {error}"
            )
            check_baseline_freshness(sources, initiative, report, exception_scope)
            return
        changed_sources = sorted(set(REQUIRED_SOURCES) & changed)
        if changed_sources and "stakeholder-brief.html" not in changed:
            if exception_scope == "freshness":
                report.limitations.append("Git freshness failure accepted by explicit reviewed freshness exception: " + ", ".join(changed_sources))
            else:
                report.freshness.append("stakeholder brief was not refreshed in Git diff after changed source artifact(s): " + ", ".join(changed_sources))
        return
    check_baseline_freshness(sources, initiative, report, exception_scope)


def write_baseline(initiative: Path, root: Path) -> None:
    missing = [name for name in REQUIRED_SOURCES if not (initiative / name).is_file()]
    if missing:
        raise ValueError("cannot write freshness baseline; missing source artifact(s): " + ", ".join(missing))
    report = validate(initiative, root, None, skip_freshness=True)
    if report.structural or report.gate:
        failures = report.structural + report.gate
        raise ValueError("deterministic structure/gate must pass before writing baseline: " + "; ".join(failures))
    payload = {
        "schema_version": 1,
        "source_sha256": {name: digest(initiative / name) for name in REQUIRED_SOURCES},
    }
    (initiative / BASELINE_FILE).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def validate(initiative: Path, root: Path, base_ref: str | None, *, skip_freshness: bool = False) -> Report:
    report = Report()
    if not initiative.is_dir():
        report.structural.append(f"initiative path does not exist: {initiative}")
        return report
    exception_scope = approved_exception(initiative, report)
    check_gate_state(initiative, report)
    check_brief(initiative, report, exception_scope == "not_applicable")
    if not skip_freshness and exception_scope != "not_applicable":
        check_freshness(initiative, root, base_ref, report, exception_scope)
    elif exception_scope == "not_applicable":
        report.limitations.append("stakeholder brief structural/freshness checks are not applicable under the explicit reviewed exception")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--consumer-root", type=Path, required=True)
    parser.add_argument("--initiative", required=True, help="Path relative to consumer root, e.g. specs/004-example")
    parser.add_argument("--base-ref", help="Compare source/brief changes against this Git ref; use the local baseline if Git/ref comparison is unavailable")
    parser.add_argument("--write-baseline", action="store_true", help="Write local source hashes after the required independent review")
    args = parser.parse_args()
    root = args.consumer_root.resolve()
    initiative = (root / args.initiative).resolve()
    try:
        initiative.relative_to(root)
    except ValueError:
        parser.error("--initiative must resolve inside --consumer-root")
    if args.write_baseline:
        try:
            write_baseline(initiative, root)
        except ValueError as error:
            print(f"Human Visibility validation FAILED: {error}")
            return 1
        print(f"Wrote freshness baseline: {initiative / BASELINE_FILE}")
        return 0
    report = validate(initiative, root, args.base_ref)
    print("Human Visibility deterministic validation")
    for label, entries in (("STRUCTURAL FAILURES", report.structural), ("GATE/STATE INCONSISTENCIES", report.gate), ("FRESHNESS FAILURES", report.freshness), ("LIMITATIONS", report.limitations), ("HUMAN REVIEW REQUIRED", report.human_review)):
        print(f"\n{label}:")
        for entry in entries or ("none",):
            print(f"- {entry}")
    if report.failures:
        print(f"\nRESULT: FAIL ({len(report.failures)} deterministic failure(s))")
        return 1
    print("\nRESULT: PASS (deterministic structure only; independent review still required)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
