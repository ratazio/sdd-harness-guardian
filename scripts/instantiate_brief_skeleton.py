#!/usr/bin/env python3
"""Instantiate an initiative-local, non-promotable v3 brief skeleton.

The command copies an already-designed blank shell and changes only its
lifecycle identity.  It intentionally does not inspect Markdown, select a
profile, write narrative, or add any visual/content block.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = ROOT / ".harness" / "templates" / "stakeholder-brief.html"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("initiative", type=Path, help="initiative directory that owns the skeleton")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="approved blank v3 shell to copy")
    args = parser.parse_args()
    initiative = args.initiative.resolve()
    template = args.template.resolve()
    destination = initiative / "brief-candidates" / "stakeholder-brief.skeleton.html"
    if not (initiative / "run-state.yaml").is_file():
        print("initiative must contain run-state.yaml", file=sys.stderr)
        return 2
    if not template.is_file():
        print(f"template does not exist: {template}", file=sys.stderr)
        return 2
    if destination.exists():
        print(f"refusing to overwrite existing skeleton: {destination}", file=sys.stderr)
        return 2
    content = template.read_text(encoding="utf-8")
    content = content.replace('data-harness-template-kind="scaffold"', 'data-harness-template-kind="skeleton"')
    content = content.replace('data-brief-phase="scaffold"', 'data-brief-phase="skeleton"')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8", newline="\n")
    print(f"Instantiated non-promotable skeleton: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
