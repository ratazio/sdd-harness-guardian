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
    "stakeholder-brief.html": "stakeholder-brief.html",
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

SLUG_PATTERN = r"[a-z0-9][a-z0-9._-]*"
NUMBERED_INITIATIVE_PATTERN = re.compile(rf"(?P<sequence>\d{{3}})-(?P<slug>{SLUG_PATTERN})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create specs/NNN-<initiative> without overwriting existing work."
    )
    parser.add_argument(
        "initiative",
        help=(
            "lowercase slug, or explicit NNN-slug, using letters, numbers, dots, "
            "underscores, or hyphens"
        ),
    )
    parser.add_argument(
        "--sequence",
        type=int,
        help="explicit sequence number to use instead of the next available number",
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


def parse_initiative(value: str) -> tuple[int | None, str]:
    numbered = NUMBERED_INITIATIVE_PATTERN.fullmatch(value)
    if numbered:
        return int(numbered.group("sequence")), numbered.group("slug")
    if re.fullmatch(SLUG_PATTERN, value):
        return None, value
    raise SystemExit(
        "Invalid initiative. Use lowercase letters, numbers, dots, underscores, "
        "or hyphens; optionally prefix with NNN-. Path separators are forbidden."
    )


def existing_numbered_initiatives(specs_root: Path) -> list[tuple[int, str, Path]]:
    if not specs_root.is_dir():
        return []
    initiatives: list[tuple[int, str, Path]] = []
    for child in specs_root.iterdir():
        if not child.is_dir():
            continue
        match = NUMBERED_INITIATIVE_PATTERN.fullmatch(child.name)
        if match:
            initiatives.append((int(match.group("sequence")), match.group("slug"), child))
    return sorted(initiatives)


def next_sequence(specs_root: Path) -> int:
    existing = existing_numbered_initiatives(specs_root)
    return max((sequence for sequence, _, _ in existing), default=0) + 1


def render_template(
    source: Path,
    initiative_id: str,
    initiative_slug: str,
    initiative_sequence: int,
    kind: str,
) -> str:
    text = source.read_text(encoding="utf-8")
    replacements = {
        "<initiative>": initiative_id,
        "<initiative-id>": initiative_id,
        "<initiative-slug>": initiative_slug,
        "<initiative-sequence>": f"{initiative_sequence:03d}",
        "<feature-or-change-name>": initiative_id,
        "<YYYY-MM-DD>": date.today().isoformat(),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    if source.name == "run-state.yaml":
        text = text.replace('initiative_kind: "feature"', f'initiative_kind: "{kind}"')
    return text


def index_row(initiative_sequence: int, initiative_id: str, kind: str) -> str:
    today = date.today().isoformat()
    return (
        f"| {initiative_sequence:03d} | `{initiative_id}` | {kind} | draft | "
        f"human_decision_required |  | {today} | `specs/{initiative_id}/spec.md` |"
    )


def ensure_index(specs_root: Path, initiative_sequence: int, initiative_id: str, kind: str) -> None:
    index_path = specs_root / "INDEX.md"
    row = index_row(initiative_sequence, initiative_id, kind)
    if not index_path.exists():
        index_path.write_text(
            "\n".join(
                (
                    "# Specs Index",
                    "",
                    "This index is the first-read map for humans and agents. Keep one",
                    "row per initiative and update it when status, outcome or ownership",
                    "changes.",
                    "",
                    "| Sequence | Initiative | Kind | Status | Outcome summary | Owner | Last updated | Spec |",
                    "|---|---|---|---|---|---|---|---|",
                    row,
                    "",
                )
            ),
            encoding="utf-8",
        )
        return

    current = index_path.read_text(encoding="utf-8")
    if f"`{initiative_id}`" in current:
        return
    separator = "" if current.endswith("\n") else "\n"
    index_path.write_text(f"{current}{separator}{row}\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    requested_sequence, initiative_slug = parse_initiative(args.initiative)
    if requested_sequence is not None and requested_sequence < 1:
        raise SystemExit("Initiative sequence must be between 001 and 999.")
    if args.sequence is not None:
        if args.sequence < 1 or args.sequence > 999:
            raise SystemExit("--sequence must be between 1 and 999.")
        if requested_sequence is not None and requested_sequence != args.sequence:
            raise SystemExit("Conflicting initiative prefix and --sequence value.")
        requested_sequence = args.sequence

    bundle_root = Path(__file__).resolve().parent.parent
    templates = bundle_root / ".harness" / "templates"
    consumer_root = args.consumer_root.resolve()
    specs_root = consumer_root / "specs"
    initiative_sequence = requested_sequence or next_sequence(specs_root)
    if initiative_sequence > 999:
        raise SystemExit("No available three-digit initiative sequence remains.")
    initiative_id = f"{initiative_sequence:03d}-{initiative_slug}"
    target = specs_root / initiative_id

    if target.exists():
        raise SystemExit(f"Refusing to overwrite existing target: {target}")
    if (specs_root / initiative_slug).exists():
        raise SystemExit(
            f"Refusing to create numbered duplicate for legacy target: {specs_root / initiative_slug}. "
            "Normalize the existing initiative into NNN-slug first."
        )
    for existing_sequence, existing_slug, existing_path in existing_numbered_initiatives(specs_root):
        if existing_sequence == initiative_sequence:
            raise SystemExit(
                f"Refusing to reuse existing sequence {initiative_sequence:03d}: {existing_path}"
            )
        if existing_slug == initiative_slug:
            raise SystemExit(
                f"Refusing to create duplicate initiative slug '{initiative_slug}': {existing_path}"
            )

    specs_root.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(prefix=f".{initiative_id}-", dir=str(specs_root))
    )

    mapping = dict(TEMPLATE_MAP)
    if args.kind == "bugfix":
        mapping["reproduction.md"] = "reproduction.md"

    renamed = False
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
                render_template(
                    source,
                    initiative_id,
                    initiative_slug,
                    initiative_sequence,
                    args.kind,
                ),
                encoding="utf-8",
            )
        staging.rename(target)
        renamed = True
        ensure_index(specs_root, initiative_sequence, initiative_id, args.kind)
    except Exception as error:
        if renamed:
            raise SystemExit(
                f"Scaffolding failed after target creation. Inspect target: {target}. "
                f"Cause: {error}"
            )
        raise SystemExit(
            f"Scaffolding failed. Partial staging was preserved for inspection: {staging}. "
            f"Cause: {error}"
        )

    print(f"Created {args.kind} initiative: {target}")
    print(
        "Next step: complete spec.md, update stakeholder-brief.html, "
        "and request Outcome/Spec Guardian review."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
