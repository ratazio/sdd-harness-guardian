#!/usr/bin/env python3
"""Regression coverage for the copy-only skeleton initializer."""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

from validate_brief_candidate_inheritance import read_surface

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "instantiate_brief_skeleton.py"


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        initiative = Path(directory) / "specs" / "001-demo"
        initiative.mkdir(parents=True)
        (initiative / "run-state.yaml").write_text("brief_phase: not_rendered\n", encoding="utf-8")
        result = subprocess.run(["python", str(SCRIPT), str(initiative)], text=True, capture_output=True)
        assert result.returncode == 0, result.stderr
        skeleton = initiative / "brief-candidates" / "stakeholder-brief.skeleton.html"
        content = skeleton.read_text(encoding="utf-8")
        assert 'data-harness-template-kind="skeleton"' in content
        assert 'data-brief-phase="skeleton"' in content
        assert 'data-harness-brief-structure="executive-brief-v3"' in content
        assert "a preencher" in content
        assert not read_surface(skeleton).raw_scaffold_outside_slots, (
            "every visible scaffold placeholder must be inside a composition slot"
        )
        assert not re.search(r'<section[^>]*\bdata-source=', content), (
            "immutable route panels must not declare partial source provenance"
        )
        repeated = subprocess.run(["python", str(SCRIPT), str(initiative)], text=True, capture_output=True)
        assert repeated.returncode != 0
    print("Brief skeleton initializer passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
