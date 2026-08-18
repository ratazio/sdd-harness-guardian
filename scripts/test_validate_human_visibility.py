#!/usr/bin/env python3
"""Isolated fixtures for the consumer-facing Human Visibility validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "scripts" / "validate_human_visibility.py"
SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")


def run(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), "--consumer-root", str(root), "--initiative", "specs/001-example", *extra], text=True, capture_output=True, check=False)


def git(root: Path, *args: str) -> None:
    result = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True, check=False)
    require(result.returncode == 0, result.stdout + result.stderr)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def write_fixture(root: Path) -> Path:
    initiative = root / "specs" / "001-example"
    initiative.mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        (initiative / source).write_text(f"# {source}\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("quality_gates:\n  human_visibility_ready: true\n", encoding="utf-8")
    (initiative / "stakeholder-brief.html").write_text("""<html data-harness-brief-design="v1"><body class="brief-shell">
<header class="brief-header"></header><div id="decision-snapshot"></div><section id="scope"></section>
<section id="validation"></section><section id="decision"></section><section class="decision-register"></section><section class="impact-evidence"></section><section class="decision-actions"></section>
<a href="spec.md">spec</a><a href="impact-map.md">impact</a>
<a href="plan.md">plan</a><a href="validation-plan.md">validation</a>
</body></html>""", encoding="utf-8")
    return initiative


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-") as temporary:
        root = Path(temporary)
        initiative = write_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        clean = run(root)
        require(clean.returncode == 0 and "HUMAN REVIEW REQUIRED:" in clean.stdout, clean.stdout)

        (initiative / "stakeholder-brief.html").unlink()
        absent = run(root)
        require(absent.returncode == 1 and "missing stakeholder brief" in absent.stdout, absent.stdout)
        (initiative / "human-visibility-exception.yaml").write_text("scope: not_applicable\nreason: release administrative work\nowner: reviewer\nhuman_visibility_status: reviewed\n", encoding="utf-8")
        not_applicable = run(root)
        require(not_applicable.returncode == 0 and "not applicable under the explicit reviewed exception" in not_applicable.stdout, not_applicable.stdout)
        (initiative / "human-visibility-exception.yaml").unlink()
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-harness-brief-design="v1"', "", 1), encoding="utf-8")
        missing_lineage = run(root)
        require(missing_lineage.returncode == 1 and "missing stakeholder brief design-lineage marker" in missing_lineage.stdout, missing_lineage.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('class="decision-actions"', 'class="custom-actions"', 1), encoding="utf-8")
        missing_shell = run(root)
        require(missing_shell.returncode == 1 and "missing stakeholder brief canonical shell hook: decision-actions" in missing_shell.stdout, missing_shell.stdout)
        (initiative / "decision-log.md").write_text("""# Decision Log

| ID | Status | Decision | Rationale/evidence | Owner/approver |
|---|---|---|---|---|
| D-001 | reviewed | Layout exception: retained decision surfaces | Rationale: accessibility audience needs a custom layout | reviewer |
""", encoding="utf-8")
        accepted_layout = run(root)
        require(accepted_layout.returncode == 0 and "custom stakeholder brief layout accepted" in accepted_layout.stdout, accepted_layout.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('id="scope"', "", 1), encoding="utf-8")
        missing_id = run(root)
        require(missing_id.returncode == 1 and "missing stakeholder brief section id: scope" in missing_id.stdout, missing_id.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('href="plan.md"', 'href="plan-missing.md"', 1), encoding="utf-8")
        missing_link = run(root)
        require(missing_link.returncode == 1 and "missing stakeholder brief source link: plan.md" in missing_link.stdout, missing_link.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8") + "<initiative>", encoding="utf-8")
        placeholder = run(root)
        require(placeholder.returncode == 1 and "unresolved stakeholder brief placeholder" in placeholder.stdout, placeholder.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        (initiative / "impact-map.md").unlink()
        missing_source = run(root)
        require(missing_source.returncode == 1 and "missing required source artifact: impact-map.md" in missing_source.stdout, missing_source.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        (initiative / "spec.md").write_text("# changed\n", encoding="utf-8")
        stale = run(root)
        require(stale.returncode == 1 and "stakeholder brief is stale" in stale.stdout, stale.stdout)
        (initiative / "human-visibility-exception.yaml").write_text("scope: freshness # documented inline comment\nreason: formatting only\nowner: reviewer\nhuman_visibility_status: reviewed\n", encoding="utf-8")
        exception = run(root)
        require(exception.returncode == 0 and "accepted by explicit reviewed freshness exception" in exception.stdout, exception.stdout)

    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-git-") as temporary:
        root = Path(temporary)
        initiative = write_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        git(root, "init")
        git(root, "config", "user.email", "fixture@example.test")
        git(root, "config", "user.name", "Fixture")
        git(root, "add", ".")
        git(root, "commit", "-m", "baseline")
        (initiative / "spec.md").write_text("# changed\n", encoding="utf-8")
        stale_git = run(root, "--base-ref", "HEAD")
        require(stale_git.returncode == 1 and "was not refreshed in Git diff" in stale_git.stdout, stale_git.stdout)
        (initiative / "stakeholder-brief.html").write_text((initiative / "stakeholder-brief.html").read_text(encoding="utf-8") + "<!-- refreshed -->", encoding="utf-8")
        refreshed_git = run(root, "--base-ref", "HEAD")
        require(refreshed_git.returncode == 0, refreshed_git.stdout)
        baseline_after_refresh = run(root, "--write-baseline")
        require(baseline_after_refresh.returncode == 0, baseline_after_refresh.stdout + baseline_after_refresh.stderr)
        fallback_git = run(root, "--base-ref", "missing-ref")
        require(fallback_git.returncode == 0 and "falling back to human-visibility-baseline.json" in fallback_git.stdout, fallback_git.stdout)
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
