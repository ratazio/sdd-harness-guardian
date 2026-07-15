#!/usr/bin/env python3
"""Safely scaffold project-local SDD initiative artifacts from this bundle."""

from __future__ import annotations

import argparse
import re
import tempfile
from datetime import date
from pathlib import Path


TEMPLATE_MAP = {
    "spec.md": "spec.md",
    "impact-map.md": "impact-map.md",
    "plan.md": "plan.md",
    "validation-plan.md": "validation-plan.md",
    "tasks.md": "tasks.md",
    "run-state.yaml": "run-state.yaml",
    "progress.md": "progress.md",
    "decision-log.md": "decision-log.md",
    "ratchet.md": "ratchet.md",
    "handoff.md": "handoffs/latest-handoff.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create specs/<initiative> without overwriting existing work."
    )
    parser.add_argument(
        "initiative",
        help="lowercase slug using letters, numbers, dots, underscores, or hyphens",
    )
    parser.add_argument(
        "--kind",
        choices=("feature", "bugfix", "refactor"),
        default="feature",
        help="initiative workflow kind (default: feature)",
    )
    parser.add_argument(
        "--consumer-root",
        type=Path,
        default=Path.cwd(),
        help="consumer repository root (default: current directory)",
    )
    return parser.parse_args()


def render_template(source: Path, initiative: str, kind: str) -> str:
    text = source.read_text(encoding="utf-8")
    replacements = {
        "<initiative>": initiative,
        "<feature-or-change-name>": initiative,
        "<YYYY-MM-DD>": date.today().isoformat(),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    if source.name == "run-state.yaml":
        text = text.replace('initiative_kind: "feature"', f'initiative_kind: "{kind}"')
    return text


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", args.initiative):
        raise SystemExit(
            "Invalid initiative slug. Use lowercase letters, numbers, dots, "
            "underscores, or hyphens; path separators are forbidden."
        )

    bundle_root = Path(__file__).resolve().parent.parent
    templates = bundle_root / ".harness" / "templates"
    consumer_root = args.consumer_root.resolve()
    specs_root = consumer_root / "specs"
    target = specs_root / args.initiative

    if target.exists():
        raise SystemExit(f"Refusing to overwrite existing target: {target}")

    specs_root.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(prefix=f".{args.initiative}-", dir=str(specs_root))
    )

    mapping = dict(TEMPLATE_MAP)
    if args.kind == "bugfix":
        mapping["reproduction.md"] = "reproduction.md"

    try:
        (staging / "evidence").mkdir()
        (staging / "handoffs").mkdir()
        for template_name, relative_target in mapping.items():
            source = templates / template_name
            if not source.is_file():
                raise FileNotFoundError(f"Missing bundle template: {source}")
            destination = staging / relative_target
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(
                render_template(source, args.initiative, args.kind),
                encoding="utf-8",
            )
        staging.rename(target)
    except Exception:
        raise SystemExit(
            f"Scaffolding failed. Partial staging was preserved for inspection: {staging}"
        )

    print(f"Created {args.kind} initiative: {target}")
    print("Next step: complete spec.md and request Outcome/Spec Guardian review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
