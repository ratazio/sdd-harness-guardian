#!/usr/bin/env python3
"""Exercise the minimum Guardian wiring expected from a Factory scaffold."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "scripts" / "fixtures" / "factory-guardian-consumer"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run(*command: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)
    require(result.returncode == 0, "command failed: " + " ".join(command) + "\n" + result.stdout + result.stderr)
    return result


def text(root: Path, relative: str) -> str:
    path = root / relative
    require(path.is_file(), f"Factory fixture missing: {relative}")
    return path.read_text(encoding="utf-8")


def create_guardian_repository(root: Path) -> tuple[Path, str]:
    guardian = root / "guardian-source"
    (guardian / "scripts").mkdir(parents=True)
    shutil.copy2(ROOT / "scripts" / "validate_human_visibility.py", guardian / "scripts" / "validate_human_visibility.py")
    run("git", "init", str(guardian))
    run("git", "-C", str(guardian), "config", "user.email", "fixture@example.test")
    run("git", "-C", str(guardian), "config", "user.name", "Fixture")
    run("git", "-C", str(guardian), "add", ".")
    run("git", "-C", str(guardian), "commit", "-m", "guardian fixture")
    commit = run("git", "-C", str(guardian), "rev-parse", "HEAD").stdout.strip()
    return guardian, commit


def create_valid_v1_initiative(consumer: Path) -> None:
    """Historical/pinned v1 remains accepted by the installed validator."""
    initiative = consumer / "specs" / "001-v1-example"
    initiative.mkdir(parents=True)
    for name in ("spec.md", "impact-map.md", "plan.md", "validation-plan.md"):
        (initiative / name).write_text(f"# {name}\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("brief_lineage: \"v1\"\nquality_gates:\n  human_visibility_ready: true\n", encoding="utf-8")
    (initiative / "stakeholder-brief.html").write_text("""<html data-harness-brief-design="v1"><body class="brief-shell"><header class="brief-header"></header>
<div id="decision-snapshot"></div><div id="scope" class="impact-evidence"></div><div id="validation"></div><div id="decision" class="decision-actions"></div><div class="decision-register"></div>
<a href="spec.md"></a><a href="impact-map.md"></a><a href="plan.md"></a><a href="validation-plan.md"></a></body></html>""", encoding="utf-8")


def create_valid_v2_initiative(consumer: Path) -> None:
    """New Factory consumers get the v2 source/review/propagation contract."""
    initiative = consumer / "specs" / "002-v2-example"
    initiative.mkdir(parents=True)
    sources = ("spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md", "decision-log.md", "progress.md")
    for name in sources:
        (initiative / name).write_text(f"# {name}\n", encoding="utf-8")
    (initiative / "decision-log.md").write_text(
        "| ID | Decision |\n|---|---|\n| D-001 | Meeting decision propagated to canonical sources before regenerated brief and Tasks Ready. |\n",
        encoding="utf-8",
    )
    (initiative / "run-state.yaml").write_text("""brief_lineage: "v2"
quality_gates:
  tasks_drafted: true
  brief_coverage_ready: true
  human_visibility_ready: true
  tasks_ready: true
brief_review:
  author: "factory-builder"
  coverage_reviewer: "factory-reviewer"
  reviewed_at: "2026-08-19"
  review_record: "decision-log.md#D-001"
  findings_status: "pass_after_propagation"
""", encoding="utf-8")
    source_rows = []
    blocks = []
    for index, source in enumerate((*sources, "run-state.yaml")):
        target = f"source-{index}"
        blocks.append(f'<section id="{target}" data-source="{source}" data-source-section="principal" data-coverage="represented"></section>')
        source_rows.append(f'<tr><td>{source} #principal</td><td><a href="#{target}">target</a></td><td>represented: Factory fixture</td></tr>')
    (initiative / "stakeholder-brief.html").write_text(
        "<html data-harness-brief-design=\"v2\"><body class=\"brief-shell\"><header class=\"brief-header\"></header>"
        "<div id=\"decision-snapshot\"></div><section id=\"scope\" class=\"impact-evidence\"></section><section id=\"architecture\"></section><section id=\"impact\"></section><section id=\"execution\"></section><section id=\"validation\"></section><section id=\"evolution\" class=\"decision-register\"></section><section id=\"decision\" class=\"decision-actions\"></section><section id=\"coverage\"></section>"
        + "".join(blocks)
        + "<table id=\"coverage-register\"><tr><th>Source / heading</th><th>Target</th><th>Disposition</th></tr>"
        + "".join(source_rows)
        + "</table></body></html>",
        encoding="utf-8",
    )


def main() -> int:
    bridge = text(FIXTURE, "AGENTS.md")
    require("vendor/sdd-harness-guardian/.harness/AGENTS.md" in bridge, "fixture lacks root instruction bridge")
    require("before task breakdown or implementation" in bridge, "bridge does not block pre-task work")
    require("validate_human_visibility.py" in text(FIXTURE, "scripts/check_human_visibility.py"), "fixture lacks consumer validation command")
    lock_template = text(FIXTURE, "guardian-lock.json")
    require("__GUARDIAN_REPOSITORY__" in lock_template and "__GUARDIAN_COMMIT__" in lock_template, "fixture lock must expose Factory materialization placeholders")
    workflow = text(FIXTURE, ".github/workflows/human-visibility.yml")
    require("install_guardian.py" in workflow and "check_human_visibility.py" in workflow and "--base-ref" in workflow, "fixture lacks configured install and invocation point")

    with tempfile.TemporaryDirectory(prefix="sdd-factory-fixture-") as temporary:
        temporary_root = Path(temporary)
        guardian, commit = create_guardian_repository(temporary_root)
        consumer = temporary_root / "consumer"
        shutil.copytree(FIXTURE, consumer)
        shutil.rmtree(consumer / "vendor", ignore_errors=True)
        lock = {"repository": str(guardian), "commit": commit}
        (consumer / "guardian-lock.json").write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
        create_valid_v1_initiative(consumer)
        create_valid_v2_initiative(consumer)
        run(sys.executable, "scripts/install_guardian.py", cwd=consumer)
        installed = run("git", "-C", str(consumer / "vendor" / "sdd-harness-guardian"), "rev-parse", "HEAD").stdout.strip()
        require(installed == commit == lock["commit"], "installed Guardian HEAD does not match materialized lock")
        installed_validator = consumer / "vendor" / "sdd-harness-guardian" / "scripts" / "validate_human_visibility.py"
        for initiative in ("specs/001-v1-example", "specs/002-v2-example"):
            run(sys.executable, str(installed_validator), "--consumer-root", str(consumer), "--initiative", initiative, "--write-baseline")
            run(sys.executable, "scripts/check_human_visibility.py", initiative, cwd=consumer)
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
