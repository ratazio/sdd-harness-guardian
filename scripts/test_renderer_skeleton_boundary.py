#!/usr/bin/env python3
"""Regression contract for v3 skeleton inheritance at promotion boundary."""

from __future__ import annotations

import hashlib
import subprocess
import tempfile
from pathlib import Path

from render_stakeholder_brief import candidate_skeleton_inheritance_error


ROOT = Path(__file__).resolve().parent.parent


def candidate_from(skeleton: Path, candidate: Path) -> str:
    content = skeleton.read_text(encoding="utf-8")
    content = content.replace('data-harness-template-kind="skeleton"', 'data-harness-template-kind="composed"', 1)
    content = content.replace('data-brief-phase="skeleton"', 'data-brief-phase="authored"', 1)
    content = content.replace(
        'data-composition-extension="inside-slot-only"',
        'data-composition-extension="inside-slot-only" '
        'data-composition-base="brief-candidates/stakeholder-brief.skeleton.html" '
        f'data-composition-base-sha256="{hashlib.sha256(skeleton.read_bytes()).hexdigest()}"',
        1,
    )
    head, body = content.split("</style>", 1)
    content = head + "</style>" + body.replace("a preencher", "source-backed fixture")
    candidate.write_text(content, encoding="utf-8")
    return content


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        consumer = Path(temporary)
        created = subprocess.run(
            ["python", str(ROOT / "scripts" / "new_initiative.py"), "renderer-boundary", "--consumer-root", str(consumer)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert created.returncode == 0, created.stderr
        initiative = consumer / "specs" / "001-renderer-boundary"
        initialized = subprocess.run(
            ["python", str(ROOT / "scripts" / "instantiate_brief_skeleton.py"), str(initiative)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert initialized.returncode == 0, initialized.stderr
        skeleton = initiative / "brief-candidates" / "stakeholder-brief.skeleton.html"
        candidate = initiative / "brief-candidates" / "stakeholder-brief.candidate.html"
        candidate_html = candidate_from(skeleton, candidate)
        inherited = candidate_skeleton_inheritance_error(initiative, candidate, candidate_html)
        assert inherited is None, inherited

        mutated = candidate_html.replace("</style>", "/* destructive shell rewrite */</style>", 1)
        candidate.write_text(mutated, encoding="utf-8")
        error = candidate_skeleton_inheritance_error(initiative, candidate, mutated)
        assert error and "does not retain the initiative-local skeleton" in error, error
    print("Renderer v3 skeleton-boundary contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
