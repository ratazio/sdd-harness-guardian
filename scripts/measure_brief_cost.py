#!/usr/bin/env python3
"""Honest, minimal cost instrumentation for SPEC 029 T-009 (FR-013/FR-014).

This is NOT a precise profiler. It wraps the two deterministic checks a
composing agent runs on every iteration (`validate_brief_model.py`,
`project_brief.py`) and records wall-clock time and exit status for each
call, appended to a per-mock JSON log. "Agent calls" are counted by the
caller (one call per attempted validate-or-project cycle) because this
script is invoked BY a human/agent doing the authoring, not by an
autonomous loop -- there is no token/API-call meter available in this
context, so token cost is NOT measured here and evidence must say so
explicitly rather than invent a number.

Usage:
    python scripts/measure_brief_cost.py validate <model.yaml> <log.json>
    python scripts/measure_brief_cost.py project <initiative> <model.yaml> <output.html> <log.json>
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _append_log(log_path: Path, entry: dict) -> None:
    entries = []
    if log_path.exists():
        try:
            entries = json.loads(log_path.read_text(encoding="utf-8"))
        except Exception:
            entries = []
    entries.append(entry)
    log_path.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def run_step(step: str, argv: list[str], log_path: Path) -> int:
    start = time.monotonic()
    proc = subprocess.run(
        [sys.executable, *argv],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    elapsed = time.monotonic() - start
    entry = {
        "step": step,
        "argv": argv,
        "elapsed_seconds": round(elapsed, 4),
        "exit_code": proc.returncode,
        "stdout_tail": proc.stdout[-2000:],
        "stderr_tail": proc.stderr[-2000:],
        "measurement_note": (
            "wall_clock is a REAL measured value (time.monotonic around the "
            "subprocess). Iteration/call count is counted by the invoking "
            "agent, one unit per attempted check, not estimated. Token/LLM "
            "cost is NOT measured by this script -- no meter is available "
            "in this context; do not treat its absence as zero cost."
        ),
    }
    _append_log(log_path, entry)
    print(proc.stdout, end="")
    print(proc.stderr, end="", file=sys.stderr)
    return proc.returncode


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(
            "usage: measure_brief_cost.py validate <model.yaml> <log.json>\n"
            "       measure_brief_cost.py project <initiative> <model.yaml> <output.html> <log.json>",
            file=sys.stderr,
        )
        return 2
    mode = argv[1]
    if mode == "validate":
        model_path, log_path = argv[2], argv[3]
        return run_step("validate", ["scripts/validate_brief_model.py", model_path], Path(log_path))
    if mode == "project":
        initiative, model_path, output_path, log_path = argv[2], argv[3], argv[4], argv[5]
        return run_step(
            "project",
            ["scripts/project_brief.py", initiative, model_path, output_path],
            Path(log_path),
        )
    print(f"unknown mode: {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
