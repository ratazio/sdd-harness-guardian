#!/usr/bin/env python3
"""Regression proof that scaffolding cannot materialize a fake brief."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAFFOLDER = ROOT / "scripts" / "new_initiative.py"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="sdd-brief-integrity-") as temporary:
        consumer = Path(temporary)
        command = [sys.executable, str(SCAFFOLDER), "delivery-integrity", "--consumer-root", str(consumer)]
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        require(result.returncode == 0, "fixture scaffold failed: " + result.stderr.strip())
        initiative = consumer / "specs" / "001-delivery-integrity"
        brief = initiative / "stakeholder-brief.html"
        require(not brief.exists(), "scaffolding must not create an HTML brief")
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        require('brief_phase: "not_rendered"' in state, "scaffold state must disclose that no brief exists")

    print("RESULT: scaffolding creates canonical sources only; no HTML brief can be mistaken for delivery")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
