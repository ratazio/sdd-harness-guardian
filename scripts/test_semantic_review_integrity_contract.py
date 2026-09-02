#!/usr/bin/env python3
"""T-003 regressions for the non-semantic reviewer-record integrity contract."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "scripts" / "validate_semantic_review_record.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "semantic-review-integrity"


def run(record: Path, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), str(record), "--root", str(root)], text=True, capture_output=True, check=False)


def require(result: subprocess.CompletedProcess[str], expected: int, message: str) -> None:
    assert result.returncode == expected, f"{message}\nstdout: {result.stdout}\nstderr: {result.stderr}"


def main() -> int:
    # Both human outcomes have valid wiring: this code does not convert APPROVE
    # into an automatic semantic clearance or REVISE into a score.
    require(run(FIXTURE / "approve.json", FIXTURE), 0, "approved human record should bind")
    require(run(FIXTURE / "revise.json", FIXTURE), 0, "revise human record should also bind")

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        for source in FIXTURE.iterdir():
            if source.is_file() and source.suffix != ".json":
                (root / source.name).write_bytes(source.read_bytes())
        base = json.loads((FIXTURE / "approve.json").read_text(encoding="utf-8"))
        cases = {
            "same-identity": lambda value: value.update(reviewer_identity="composer-021"),
            "candidate-digest": lambda value: value["candidate"].update(sha256="sha256:" + "0" * 64),
            "corpus-locator": lambda value: value["corpus_manifest"][0].update(locator=""),
            "rendered-scope": lambda value: value.update(record_scope="candidate_only"),
            "path-traversal": lambda value: value["corpus_manifest"][0].update(path="../source.md"),
            "automatic-field": lambda value: value.update(automatic_approval=True),
        }
        for name, mutate in cases.items():
            value = json.loads(json.dumps(base))
            mutate(value)
            record = root / f"{name}.json"
            record.write_text(json.dumps(value), encoding="utf-8")
            require(run(record, root), 1, f"{name} must be refused")

    source = VALIDATOR.read_text(encoding="utf-8").lower()
    # Narrative boundary terms are allowed in documentation, but executable
    # semantic machinery is not part of this structural validator.
    for signature in ("def score", "def classify", "def infer_material", "def approve_semantic"):
        assert signature not in source, f"unexpected semantic mechanism: {signature}"
    assert "human verdict remains decisive" in VALIDATOR.read_text(encoding="utf-8")
    print("T-003 semantic-review integrity contract passed; no semantic decision is automated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
