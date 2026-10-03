#!/usr/bin/env python3
"""T-008 / AC-013: no bundle artifact references what this task removed.

Scope is deliberately the **bundle surface** — `.harness/`, `scripts/` and
`docs/` — not `specs/**` or `testes/**`. Those trees hold historical spec
prose and pinned/replayed mock runs; NG-004 forbids rewriting a historical
byte, and a past task's own narrative ("we removed X because...") legitimately
names a file that no longer exists. A dangling reference in the *operative*
bundle is a different failure: an agent or script that still points at
something that is not there.

This also guards `.harness/templates/plan.md` §9.1, which T-008 removed as
prose (there is no filename to grep for), by checking its heading text
directly.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Exact names of the files T-008 removed. A hit on any of these strings
# anywhere in the bundle surface below is a dangling reference.
REMOVED_FILES = (
    "validate_brief_candidate_inheritance.py",
    "instantiate_brief_skeleton.py",
    "test_brief_candidate_inheritance.py",
    "test_instantiate_brief_skeleton.py",
    "test_renderer_skeleton_boundary.py",
)

# Prose removed without a filename to grep for (plan.md §9.1).
REMOVED_PROSE = (
    "Brief construction record — required before skeleton instantiation",
)

# Bundle surface per AC-013/plan.md §5 step 7. NOT specs/** or testes/**
# (historical, NG-004) and not this file itself (it must name what it checks
# for, or the check would be untestable).
SCAN_ROOTS = (ROOT / ".harness", ROOT / "scripts", ROOT / "docs")
SELF = Path(__file__).resolve()

# A record that these files existed and were removed is legitimate history,
# not a dangling reference. Exempt only the changelog and this test's own
# module-level docstring/constants (already excluded via SELF).
EXEMPT_FILES = (ROOT / "CHANGELOG.md",)

BINARY_SUFFIXES = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2"}


def _bundle_files() -> list[Path]:
    files: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix in BINARY_SUFFIXES or "__pycache__" in path.parts:
                continue
            if path.resolve() == SELF or path.resolve() in {p.resolve() for p in EXEMPT_FILES}:
                continue
            files.append(path)
    return files


def dangling_reference_errors() -> list[str]:
    errors: list[str] = []
    for path in _bundle_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for needle in REMOVED_FILES + REMOVED_PROSE:
            if needle in text:
                errors.append(f"{path.relative_to(ROOT)}: references removed artifact {needle!r}")
    return errors


def main() -> int:
    errors = dangling_reference_errors()
    if errors:
        print("Dangling reference to a T-008 removal FAILED:", *errors, sep="\n- ", file=__import__("sys").stderr)
        return 1
    print(
        f"No dangling reference to {len(REMOVED_FILES)} removed file(s) or plan.md "
        "section 9.1 across .harness/, scripts/ and docs/."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
