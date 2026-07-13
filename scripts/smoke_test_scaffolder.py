#!/usr/bin/env python3
"""Reproducible, isolated smoke tests for the initiative scaffolder."""

from __future__ import annotations

import hashlib
import platform
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCAFFOLDER = ROOT / "scripts" / "new_initiative.py"
FEATURE_FILES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "validation-plan.md",
    "tasks.md",
    "run-state.yaml",
    "progress.md",
    "decision-log.md",
    "ratchet.md",
    "handoffs/latest-handoff.md",
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(SCAFFOLDER), *args]
    print("COMMAND:", " ".join(command))
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    print("EXIT:", result.returncode)
    if result.stdout:
        print("STDOUT:", result.stdout.strip())
    if result.stderr:
        print("STDERR:", result.stderr.strip())
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    print("PYTHON:", sys.version.split()[0])
    print("PLATFORM:", platform.platform())
    with tempfile.TemporaryDirectory(prefix="sdd-guardian-smoke-") as temporary:
        consumer_root = Path(temporary)
        print("TEMP_ROOT:", consumer_root)

        feature = run("sample-feature", "--consumer-root", str(consumer_root))
        require(feature.returncode == 0, "feature scaffold failed")

        bugfix = run(
            "sample-bug",
            "--kind",
            "bugfix",
            "--consumer-root",
            str(consumer_root),
        )
        require(bugfix.returncode == 0, "bugfix scaffold failed")

        feature_root = consumer_root / "specs" / "sample-feature"
        for relative in FEATURE_FILES:
            require((feature_root / relative).is_file(), f"missing {relative}")
        require(
            (consumer_root / "specs" / "sample-bug" / "reproduction.md").is_file(),
            "bugfix lacks reproduction.md",
        )

        feature_spec = feature_root / "spec.md"
        hash_before = sha256(feature_spec)
        duplicate = run("sample-feature", "--consumer-root", str(consumer_root))
        hash_after = sha256(feature_spec)
        print("HASH_BEFORE:", hash_before)
        print("HASH_AFTER:", hash_after)
        require(duplicate.returncode != 0, "duplicate scaffold unexpectedly succeeded")
        require(hash_before == hash_after, "duplicate scaffold changed existing spec")

        bugfix_state = (
            consumer_root / "specs" / "sample-bug" / "run-state.yaml"
        ).read_text(encoding="utf-8")
        require(
            'initiative_kind: "bugfix"' in bugfix_state,
            "bugfix kind was not rendered",
        )

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
