#!/usr/bin/env python3
"""Install the Guardian revision recorded in guardian-lock.json."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "guardian-lock.json"
TARGET = ROOT / "vendor" / "sdd-harness-guardian"


def run(*command: str) -> str:
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode:
        raise SystemExit(result.stderr.strip() or "Guardian install command failed")
    return result.stdout.strip()


def main() -> int:
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    repository, commit = lock.get("repository"), lock.get("commit")
    if not isinstance(repository, str) or not isinstance(commit, str) or len(commit) != 40:
        raise SystemExit("guardian-lock.json requires repository and a 40-character commit")
    if not TARGET.exists():
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        run("git", "clone", "--no-checkout", repository, str(TARGET))
    run("git", "-C", str(TARGET), "checkout", "--detach", commit)
    actual = run("git", "-C", str(TARGET), "rev-parse", "HEAD")
    if actual != commit:
        raise SystemExit(f"Guardian lock mismatch: expected {commit}, got {actual}")
    print(f"Installed Guardian at {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
