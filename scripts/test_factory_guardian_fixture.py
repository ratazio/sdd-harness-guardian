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


def create_valid_initiative(consumer: Path) -> None:
    initiative = consumer / "specs" / "001-example"
    initiative.mkdir(parents=True)
    for name in ("spec.md", "impact-map.md", "plan.md", "validation-plan.md"):
        (initiative / name).write_text(f"# {name}\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("quality_gates:\n  human_visibility_ready: true\n", encoding="utf-8")
    (initiative / "stakeholder-brief.html").write_text("""<div id="decision-snapshot"></div><div id="scope"></div><div id="validation"></div><div id="decision"></div>
<a href="spec.md"></a><a href="impact-map.md"></a><a href="plan.md"></a><a href="validation-plan.md"></a>""", encoding="utf-8")


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
        create_valid_initiative(consumer)
        run(sys.executable, "scripts/install_guardian.py", cwd=consumer)
        installed = run("git", "-C", str(consumer / "vendor" / "sdd-harness-guardian"), "rev-parse", "HEAD").stdout.strip()
        require(installed == commit == lock["commit"], "installed Guardian HEAD does not match materialized lock")
        installed_validator = consumer / "vendor" / "sdd-harness-guardian" / "scripts" / "validate_human_visibility.py"
        run(sys.executable, str(installed_validator), "--consumer-root", str(consumer), "--initiative", "specs/001-example", "--write-baseline")
        run(sys.executable, "scripts/check_human_visibility.py", "specs/001-example", cwd=consumer)
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
