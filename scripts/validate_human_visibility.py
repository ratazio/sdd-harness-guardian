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
from html.parser import HTMLParser
from pathlib import Path


V1_REQUIRED_SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")
V2_REQUIRED_SOURCES = (
    "spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md",
    "decision-log.md", "progress.md", "run-state.yaml",
)
V1_REQUIRED_SECTION_IDS = ("decision-snapshot", "scope", "validation", "decision")
V2_REQUIRED_SECTION_IDS = (
    "decision-snapshot", "scope", "architecture", "impact", "execution", "validation",
    "evolution", "decision", "coverage",
)
CORE_V2_SOURCES = frozenset(V2_REQUIRED_SOURCES[:6])
ALLOWED_COVERAGE = frozenset({"represented", "synthesized", "not_applicable", "link_only"})
REQUIRED_SHELL_HOOKS = ("brief-shell", "brief-header", "decision-register", "impact-evidence", "decision-actions")
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


class BriefParser(HTMLParser):
    """Keep just enough DOM shape for deterministic, non-semantic checks."""

    def __init__(self) -> None:
        super().__init__()
        self.nodes: list[tuple[str, dict[str, str]]] = []
        self.coverage_rows: list[list[tuple[str, list[str]]]] = []
        self._in_coverage_table = False
        self._row: list[tuple[str, list[str]]] | None = None
        self._cell_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self.nodes.append((tag, values))
        if tag == "table" and values.get("id") == "coverage-register":
            self._in_coverage_table = True
        elif self._in_coverage_table and tag == "tr":
            self._row = []
        elif self._in_coverage_table and tag in {"td", "th"} and self._row is not None:
            self._cell_parts = []
        elif self._in_coverage_table and tag == "a" and self._cell_parts is not None:
            href = values.get("href", "")
            if href.startswith("#"):
                self._cell_parts.append(href)

    def handle_data(self, data: str) -> None:
        if self._cell_parts is not None:
            self._cell_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._in_coverage_table and tag in {"td", "th"} and self._row is not None and self._cell_parts is not None:
            self._row.append((" ".join(self._cell_parts).strip(), [part for part in self._cell_parts if part.startswith("#")]))
            self._cell_parts = None
        elif self._in_coverage_table and tag == "tr" and self._row is not None:
            self.coverage_rows.append(self._row)
            self._row = None
        elif self._in_coverage_table and tag == "table":
            self._in_coverage_table = False


def brief_lineage(html: str) -> str | None:
    marker = re.search(r'\bdata-harness-brief-design\s*=\s*["\'](v1|v2)["\']', html)
    return marker.group(1) if marker else None


def required_sources(lineage: str) -> tuple[str, ...]:
    return V2_REQUIRED_SOURCES if lineage == "v2" else V1_REQUIRED_SOURCES


def yaml_scalar(content: str, key: str, *, indent: int | None = None) -> str | None:
    prefix = rf"^\s{{{indent}}}" if indent is not None else r"^\s*"
    match = re.search(rf"(?m){prefix}{re.escape(key)}:\s*(.*?)\s*$", content)
    if not match:
        return None
    return match.group(1).split(" #", 1)[0].strip().strip('"\'')


def yaml_bool(content: str, key: str) -> bool | None:
    value = yaml_scalar(content, key, indent=2)
    if value is None:
        return None
    return value.lower() == "true"


def baseline_metadata(state: str) -> dict[str, str | None]:
    """Keep review and prior-change identity explicit in the one v2 baseline."""
    reviewer = yaml_scalar(state, "coverage_reviewer", indent=2)
    review_record = yaml_scalar(state, "review_record", indent=2)
    return {
        "review_record": review_record,
        "reviewed_by": reviewer,
        "coverage_reviewer": reviewer,
        "reviewed_at": yaml_scalar(state, "reviewed_at", indent=2),
        "prior_change_anchor": review_record,
    }


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
    if scope not in {"not_applicable", "freshness", "legacy"}:
        report.gate.append("unapproved Human Visibility exception: scope must be not_applicable, freshness or legacy")
        return None
    return str(scope)


def approved_design_exception(initiative: Path, report: Report) -> bool:
    """A material custom layout is reviewed in the canonical decision log."""
    path = initiative / "decision-log.md"
    if not path.is_file():
        report.structural.append("missing decision-log.md required for design exception review")
        return False
    for row in (line.lower() for line in path.read_text(encoding="utf-8").splitlines() if "|" in line):
        if (("design exception" in row or "layout exception" in row)
                and ("reviewed" in row or "accepted" in row)
                and ("rationale" in row or "reason" in row)
                and "decision surface" in row):
            return True
    return False


def check_gate_state(initiative: Path, report: Report) -> None:
    state = initiative / "run-state.yaml"
    if not state.is_file():
        report.gate.append("missing required source artifact: run-state.yaml")
        return
    content = state.read_text(encoding="utf-8")
    human_visibility = yaml_bool(content, "human_visibility_ready")
    if human_visibility is None:
        report.gate.append("run-state.yaml lacks quality_gates.human_visibility_ready")
    elif not human_visibility:
        report.gate.append("Human Visibility gate is not declared ready in run-state.yaml")


def check_v2_gate_state(initiative: Path, report: Report) -> None:
    """Enforce v2-only readiness and distinct review metadata.

    This intentionally reads a small, fixed YAML shape instead of introducing a
    YAML dependency or a parallel review-state file.
    """
    state_path = initiative / "run-state.yaml"
    content = state_path.read_text(encoding="utf-8")
    state_lineage = yaml_scalar(content, "brief_lineage")
    if state_lineage != "v2":
        report.gate.append("v2 brief requires run-state.yaml brief_lineage: v2")
    gates = {key: yaml_bool(content, key) for key in (
        "tasks_drafted", "brief_coverage_ready", "human_visibility_ready", "tasks_ready",
    )}
    for key, value in gates.items():
        if value is None:
            report.gate.append(f"run-state.yaml lacks quality_gates.{key} required by v2")
        elif not value:
            report.gate.append(f"v2 gate is not declared ready: {key}")
    author = yaml_scalar(content, "author", indent=2)
    reviewer = yaml_scalar(content, "coverage_reviewer", indent=2)
    reviewed_at = yaml_scalar(content, "reviewed_at", indent=2)
    review_record = yaml_scalar(content, "review_record", indent=2)
    findings = yaml_scalar(content, "findings_status", indent=2)
    if not author:
        report.gate.append("v2 brief_review.author is required")
    if not reviewer:
        report.gate.append("v2 brief_review.coverage_reviewer is required")
    if author and reviewer and author == reviewer:
        report.gate.append("v2 brief_review author and coverage_reviewer must be distinct identities")
    if not reviewed_at:
        report.gate.append("v2 brief_review.reviewed_at is required")
    if not review_record or not review_record.startswith("decision-log.md#"):
        report.gate.append("v2 brief_review.review_record must locate a decision-log.md record")
    if not findings or "pass" not in findings.lower():
        report.gate.append("v2 brief_review.findings_status must record a resolved pass")
    decision_log = initiative / "decision-log.md"
    if review_record and review_record.startswith("decision-log.md#"):
        record_id = review_record.partition("#")[2]
        record = decision_record(decision_log, record_id) if decision_log.is_file() else None
        if record is None:
            report.gate.append("v2 brief_review.review_record does not resolve in decision-log.md")
        elif gates.get("tasks_ready") is True:
            if "propagat" not in record.lower():
                report.gate.append("v2 Tasks Ready review record does not confirm decision propagation")


def decision_record(path: Path, record_id: str) -> str | None:
    """Return exactly one Markdown-table row, never an arbitrary log substring."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] == record_id:
            return line
    return None


def coverage_source(cell: str) -> tuple[str | None, str]:
    for source in V2_REQUIRED_SOURCES:
        if cell.startswith(source):
            return source, cell[len(source):].strip(" \t§:-")
    return None, ""


def check_v2_coverage_rows(parser: BriefParser, report: Report) -> None:
    provenance_by_id = {
        attrs.get("id"): attrs.get("data-source")
        for _, attrs in parser.nodes
        if attrs.get("id") and attrs.get("data-source")
    }
    rows_by_source: dict[str, list[tuple[str, list[str], str, str]]] = {}
    for row in parser.coverage_rows:
        if len(row) < 3 or row[0][0].lower() == "source / heading":
            continue
        source, heading = coverage_source(row[0][0])
        if source is None:
            continue
        target_text, targets = row[1]
        disposition_cell = row[2][0].strip()
        disposition, separator, reason = disposition_cell.partition(":")
        disposition = disposition.strip()
        rows_by_source.setdefault(source, []).append((heading, targets, disposition, reason.strip()))
        if not heading:
            report.structural.append(f"v2 coverage row missing heading locator for source {source}")
        if not targets:
            report.structural.append(f"v2 coverage row missing #target for source {source}")
        for target in targets:
            target_id = target[1:]
            if target_id not in provenance_by_id:
                report.structural.append(f"v2 coverage row target does not resolve for source {source}")
            elif disposition in {"represented", "synthesized"} and provenance_by_id[target_id] != source:
                report.structural.append(f"v2 coverage row target/provenance mismatch for source {source}")
        if disposition not in ALLOWED_COVERAGE:
            report.structural.append(f"v2 coverage row has invalid disposition for source {source}")
        elif disposition in {"not_applicable", "link_only"} and (not separator or not reason):
            report.structural.append(f"v2 coverage row missing reason for source {source}")
    for source in V2_REQUIRED_SOURCES:
        if source not in rows_by_source:
            report.structural.append(f"missing v2 coverage register entry: {source}")


def check_v2_provenance(html: str, report: Report) -> None:
    parser = BriefParser()
    try:
        parser.feed(html)
    except Exception:
        report.structural.append("invalid v2 stakeholder brief HTML")
        return
    ids = {attrs.get("id") for _, attrs in parser.nodes}
    if "coverage-register" not in ids:
        report.structural.append("missing v2 human-readable coverage register: coverage-register")
    check_v2_coverage_rows(parser, report)
    for tag, attrs in parser.nodes:
        if "data-source" not in attrs:
            continue
        identifier = attrs.get("id", "")
        location = f"#{identifier}" if re.fullmatch(r"[A-Za-z0-9_-]+", identifier) else f"<{tag}>"
        source = attrs["data-source"]
        if source not in V2_REQUIRED_SOURCES and not source.startswith(("evidence/", "handoffs/")):
            report.structural.append(f"unknown v2 provenance source at {location}")
        if not attrs.get("data-source-section"):
            report.structural.append(f"v2 provenance missing data-source-section for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")
        coverage = attrs.get("data-coverage")
        if coverage not in ALLOWED_COVERAGE:
            report.structural.append(f"v2 provenance has invalid data-coverage for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")
            continue
        if source in CORE_V2_SOURCES and coverage == "link_only":
            report.structural.append(f"v2 core source cannot be link_only: {source}")
        if coverage in {"not_applicable", "link_only"} and not attrs.get("data-coverage-reason"):
            report.structural.append(f"v2 coverage reason missing for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")


def check_brief(initiative: Path, report: Report, not_applicable: bool) -> str | None:
    brief = initiative / "stakeholder-brief.html"
    if not brief.is_file():
        if not not_applicable:
            report.structural.append("missing stakeholder brief: stakeholder-brief.html")
        return None
    html = brief.read_text(encoding="utf-8")
    lineage = brief_lineage(html)
    if lineage is None:
        report.structural.append("missing stakeholder brief design-lineage marker: data-harness-brief-design=\"v1\" or \"v2\"")
        return None
    for section_id in (V2_REQUIRED_SECTION_IDS if lineage == "v2" else V1_REQUIRED_SECTION_IDS):
        if not re.search(rf'\bid\s*=\s*["\']{re.escape(section_id)}["\']', html):
            report.structural.append(f"missing stakeholder brief section id: {section_id}")
    if lineage == "v1":
        for source in V1_REQUIRED_SOURCES:
            if not re.search(rf'href\s*=\s*["\']{re.escape(source)}["\']', html):
                report.structural.append(f"missing stakeholder brief source link: {source}")
    for placeholder in PLACEHOLDERS:
        if placeholder in html:
            report.structural.append(f"unresolved stakeholder brief placeholder: {placeholder}")
    design_errors: list[str] = []
    for hook in REQUIRED_SHELL_HOOKS:
        if not re.search(rf'\bclass\s*=\s*["\'][^"\']*\b{re.escape(hook)}\b', html):
            design_errors.append(f"missing stakeholder brief canonical shell hook: {hook}")
    if design_errors:
        if approved_design_exception(initiative, report):
            report.limitations.append("custom stakeholder brief layout accepted by reviewed design exception in decision-log.md; independent rendered review must confirm retained decision surfaces")
        else:
            report.structural.extend(design_errors)
    if lineage == "v2":
        check_v2_provenance(html, report)
    return lineage


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


def check_baseline_freshness(sources: dict[str, Path], initiative: Path, report: Report, exception_scope: str | None, lineage: str) -> None:
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
    expected_schema = 2 if lineage == "v2" else 1
    if baseline.get("schema_version") != expected_schema:
        if lineage == "v2":
            report.freshness.append(
                "v2 migration required: freshness baseline must use schema_version 2; run --write-baseline after independent review"
            )
        else:
            report.freshness.append("invalid v1 freshness baseline: human-visibility-baseline.json must use schema_version 1")
        return
    if lineage == "v2":
        if baseline.get("brief_lineage") != "v2":
            report.freshness.append("v2 migration required: freshness baseline lacks brief_lineage v2 metadata")
            return
        if baseline.get("source_set") != list(V2_REQUIRED_SOURCES):
            report.freshness.append("v2 migration required: freshness baseline lacks the expanded v2 source_set metadata")
            return
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        expected_metadata = baseline_metadata(state)
        for key, value in expected_metadata.items():
            if not value or baseline.get(key) != value:
                report.freshness.append(f"v2 freshness baseline metadata changed or missing: {key}; rerun --write-baseline after review")
                return
        prior_anchor = str(baseline["prior_change_anchor"])
        if not prior_anchor.startswith("decision-log.md#") or decision_record(
            initiative / "decision-log.md", prior_anchor.partition("#")[2]
        ) is None:
            report.freshness.append("v2 freshness baseline has an invalid prior_change_anchor")
            return
        if baseline.get("brief_sha256") != digest(initiative / "stakeholder-brief.html"):
            report.freshness.append("v2 stakeholder brief changed since the reviewed baseline; rerun independent review and --write-baseline")
            return
    recorded = baseline.get("source_sha256")
    if not isinstance(recorded, dict):
        report.freshness.append(f"invalid freshness baseline: {BASELINE_FILE} lacks source_sha256")
        return
    changed = [name for name, path in sources.items() if recorded.get(name) != digest(path)]
    if changed:
        if exception_scope == "freshness" or (lineage == "v1" and exception_scope == "legacy"):
            report.limitations.append("changed source artifact(s) accepted by explicit reviewed freshness exception: " + ", ".join(changed))
        else:
            if lineage == "v1":
                report.freshness.append(
                    "historical/pinned v1 stakeholder brief is stale for changed source artifact(s): "
                    + ", ".join(changed)
                    + "; migrate to v2 or record a reviewed legacy exception"
                )
            else:
                report.freshness.append("v2 stakeholder brief is stale for changed source artifact(s): " + ", ".join(changed))


def check_freshness(initiative: Path, root: Path, base_ref: str | None, report: Report, exception_scope: str | None, lineage: str) -> None:
    sources = {name: initiative / name for name in required_sources(lineage)}
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
            check_baseline_freshness(sources, initiative, report, exception_scope, lineage)
            return
        changed_sources = sorted(set(sources) & changed)
        if changed_sources and "stakeholder-brief.html" not in changed:
            if exception_scope == "freshness" or (lineage == "v1" and exception_scope == "legacy"):
                report.limitations.append("Git freshness failure accepted by explicit reviewed freshness exception: " + ", ".join(changed_sources))
            else:
                if lineage == "v1":
                    report.freshness.append(
                        "historical/pinned v1 stakeholder brief was not refreshed in Git diff after changed source artifact(s): "
                        + ", ".join(changed_sources)
                        + "; migrate to v2 or record a reviewed legacy exception"
                    )
                else:
                    report.freshness.append("v2 stakeholder brief was not refreshed in Git diff after changed source artifact(s): " + ", ".join(changed_sources))
        return
    check_baseline_freshness(sources, initiative, report, exception_scope, lineage)


def write_baseline(initiative: Path, root: Path) -> None:
    brief = initiative / "stakeholder-brief.html"
    if not brief.is_file():
        raise ValueError("cannot write freshness baseline; missing stakeholder brief: stakeholder-brief.html")
    lineage = brief_lineage(brief.read_text(encoding="utf-8"))
    if lineage is None:
        raise ValueError("cannot write freshness baseline; missing stakeholder brief design-lineage marker")
    sources = required_sources(lineage)
    missing = [name for name in sources if not (initiative / name).is_file()]
    if missing:
        raise ValueError("cannot write freshness baseline; missing source artifact(s): " + ", ".join(missing))
    report = validate(initiative, root, None, skip_freshness=True)
    if report.structural or report.gate:
        failures = report.structural + report.gate
        raise ValueError("deterministic structure/gate must pass before writing baseline: " + "; ".join(failures))
    payload: dict[str, object] = {
        "schema_version": 1 if lineage == "v1" else 2,
        "source_sha256": {name: digest(initiative / name) for name in sources},
    }
    if lineage == "v2":
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        payload.update({
            "brief_lineage": "v2",
            "source_set": list(V2_REQUIRED_SOURCES),
            "brief_sha256": digest(brief),
            **baseline_metadata(state),
        })
    (initiative / BASELINE_FILE).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def validate(initiative: Path, root: Path, base_ref: str | None, *, skip_freshness: bool = False) -> Report:
    report = Report()
    if not initiative.is_dir():
        report.structural.append(f"initiative path does not exist: {initiative}")
        return report
    exception_scope = approved_exception(initiative, report)
    check_gate_state(initiative, report)
    lineage = check_brief(initiative, report, exception_scope == "not_applicable")
    if lineage == "v2":
        check_v2_gate_state(initiative, report)
    if not skip_freshness and exception_scope != "not_applicable":
        if lineage is not None:
            check_freshness(initiative, root, base_ref, report, exception_scope, lineage)
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
    print("Human Visibility deterministic design-contract validation")
    for label, entries in (("STRUCTURAL FAILURES", report.structural), ("GATE/STATE INCONSISTENCIES", report.gate), ("FRESHNESS FAILURES", report.freshness), ("LIMITATIONS", report.limitations), ("HUMAN REVIEW REQUIRED", report.human_review)):
        print(f"\n{label}:")
        for entry in entries or ("none",):
            print(f"- {entry}")
    if report.failures:
        print(f"\nRESULT: FAIL ({len(report.failures)} deterministic failure(s))")
        return 1
    print("\nRESULT: PASS (deterministic design/structure contract only; independent review still required)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
