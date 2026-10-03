#!/usr/bin/env python3
"""Source sufficiency check for SPEC 029 T-006 (FR-011, AC-008).

A poor brief today is only discovered *after* `stakeholder-brief.html`
already exists -- that is the most expensive cycle in the current system.
This check moves the guarantee to *before* any composition happens, by
looking directly at the canonical Markdown sources of an initiative:
`spec.md`, `impact-map.md`, `plan.md`, `tasks.md` and `validation-plan.md`.

It verifies, structurally and without judging prose (NG-002 -- this is not a
quality score):

  * every acceptance criterion (AC-NNN) declared in `spec.md` has a
    validation path declared in `validation-plan.md`'s acceptance
    traceability table (a row naming that AC id, with a non-empty
    command/steps cell);
  * every material risk row in `impact-map.md`'s regression risks and
    controls table names an owner;
  * `plan.md` declares an architecture scope/size profile
    (`localized/S`, `S`, `M`, `L`, `high` or `unknown`);
  * every task in `tasks.md` has an exit criteria list and an evidence
    destination.

An absent item is absent -- there is no partial credit and no score. This
module reads only the five canonical Markdown sources named above and never
reads or produces `brief-model.yaml` or `stakeholder-brief.html`; it is
meant to run, as a CLI or as `source_sufficiency_errors()`, before any
model/HTML composition is attempted. It does not itself compose or judge
anything, and wiring it into a composition entry point is a separate,
later task.

Usage:
    python scripts/validate_source_sufficiency.py path/to/initiative-dir
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SOURCES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "tasks.md",
    "validation-plan.md",
)

_AC_ROW_RE = re.compile(r"^\|\s*(AC-\d+[a-z]?)\s*\|")
_TASK_HEADING_RE = re.compile(r"^###\s+(T-\d+)\b.*$", re.MULTILINE)
_PROFILE_HEADING_RE = re.compile(
    r"^###\s+Architecture scope/size profile.*$", re.MULTILINE | re.IGNORECASE
)
_PROFILE_VALUE_RE = re.compile(r"\*\*Profile:\*\*\s*(.+)")
_ALLOWED_PROFILE_VALUES = {"localized/s", "s", "m", "l", "high", "unknown"}
# Separator between a contingency action and its owner, e.g.
# "Revert the change -- Fixture maintainers": an em dash or double hyphen
# with at least one space on each side, so an ordinary in-sentence dash
# without surrounding spaces never qualifies.
_OWNER_SEPARATOR_RE = re.compile(r"\s+(?:—|--)\s+")
# A name-like owner segment: capitalized first word, up to five words total,
# no sentence-style lowercase opener (rejects prose continuations like
# "postpone release").
_OWNER_NAME_RE = re.compile(r"^[A-Z][A-Za-z0-9'.]*(?:\s+[A-Za-z0-9'.,&/]+){0,4}$")


def _read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _split_row_cells(line: str) -> list[str]:
    """Split one `| a | b |` row into cell strings, honoring `\\|` as a
    literal escaped pipe inside a cell (e.g. a shell/regex command cell)
    rather than a column boundary (F2 fix)."""
    raw_cells = re.split(r"(?<!\\)\|", line)
    if raw_cells and raw_cells[0] == "":
        raw_cells = raw_cells[1:]
    if raw_cells and raw_cells[-1] == "":
        raw_cells = raw_cells[:-1]
    return [c.strip().replace("\\|", "|") for c in raw_cells]


def _split_markdown_table(block: str) -> list[list[str]]:
    """Parse a GitHub-flavored Markdown pipe table into rows of cell text.

    Returns rows in source order, skipping the header and the `---`
    separator row. Each row is a list of trimmed cell strings. A `\\|`
    inside a cell (e.g. a shell/regex command) is treated as a literal pipe,
    not a column boundary -- known remaining gap: a cell containing raw
    `<br>`/HTML is still not handled specially.
    """
    rows: list[list[str]] = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = _split_row_cells(line)
        if all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
            continue  # separator row
        rows.append(cells)
    return rows[1:] if rows else rows  # drop header row


def _table_after_heading(text: str, heading_pattern: re.Pattern[str]) -> str:
    """Return the text slice from a heading match to the next `## `/`### ` heading."""
    match = heading_pattern.search(text)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^#{1,6}\s", text[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end]


def _extract_ac_ids(spec_text: str) -> list[str]:
    ids: list[str] = []
    for line in spec_text.splitlines():
        m = _AC_ROW_RE.match(line.strip())
        if m and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def _extract_ac_validation_paths(validation_text: str) -> dict[str, bool]:
    """Map every AC id named in the acceptance-traceability table to whether
    that row declares a non-empty command/steps cell."""
    heading = re.compile(r"^##\s*2\.\s*Acceptance traceability.*$", re.MULTILINE | re.IGNORECASE)
    block = _table_after_heading(validation_text, heading)
    if not block:
        # Fall back: any table with an "AC ID" header, in case numbering differs.
        heading = re.compile(r"^\|.*\bAC ID\b.*\|\s*$", re.MULTILINE)
        block = _table_after_heading(validation_text, heading)
    result: dict[str, bool] = {}
    for row in _split_markdown_table(block):
        if len(row) < 4:
            continue
        ac_cell, steps_cell = row[1], row[3]
        has_steps = bool(steps_cell.strip())
        for ac_id in re.findall(r"AC-\d+[a-z]?", ac_cell):
            result[ac_id] = result.get(ac_id, False) or has_steps
    return result


def _extract_material_risks(impact_text: str) -> list[tuple[str, str]]:
    """Return (risk_id, owner_cell) pairs from the regression risks table."""
    heading = re.compile(
        r"^##\s*5\.\s*Regression risks and controls.*$", re.MULTILINE | re.IGNORECASE
    )
    block = _table_after_heading(impact_text, heading)
    if not block:
        heading = re.compile(r"^\|.*\bContingency/owner\b.*\|\s*$", re.MULTILINE)
        block = _table_after_heading(impact_text, heading)
    risks: list[tuple[str, str]] = []
    for row in _split_markdown_table(block):
        if len(row) < 6:
            continue
        risk_id, owner_cell = row[0], row[5]
        if not risk_id:
            continue
        risks.append((risk_id, owner_cell))
    return risks


def _has_named_owner(owner_cell: str) -> bool:
    cell = owner_cell.strip().strip("`").strip()
    if not cell:
        return False
    placeholders = {"-", "n/a", "na", "tbd", "unknown", "unassigned", "not_applicable"}
    if cell.lower() in placeholders:
        return False
    # Convention in this bundle's Contingency/owner cells: "<contingency
    # action> -- <Owner name>" (em dash or double hyphen), the separator set
    # off by spaces on both sides -- not just any hyphen/dash that happens to
    # occur inside ordinary prose (e.g. "Investigate root cause -- postpone
    # release" is a single prose sentence, not an action/owner pair; treating
    # a bare dash as the separator would silently accept it as a "named
    # owner", which is the dangerous direction to fail in for this check).
    # Without a space-delimited separator there is no structurally
    # identifiable owner -- treat it as absent rather than guessing.
    parts = _OWNER_SEPARATOR_RE.split(cell, maxsplit=1)
    if len(parts) != 2:
        return False
    owner = parts[1].strip()
    if not owner or owner.lower() in placeholders:
        return False
    # The owner segment itself must look like a name, not a prose
    # continuation: capitalized first word, and short (this bundle's real
    # owners are role/team names like "Guardian maintainers", never a
    # sentence with a lowercase verb).
    return bool(_OWNER_NAME_RE.match(owner))


def _extract_architecture_profile(plan_text: str) -> str | None:
    block = _table_after_heading(plan_text, _PROFILE_HEADING_RE)
    if not block:
        return None
    m = _PROFILE_VALUE_RE.search(block)
    if not m:
        return None
    value = m.group(1).strip()
    return value or None


def _split_tasks(tasks_text: str) -> list[tuple[str, str]]:
    """Return (task_id, block_text) for every `### T-NNN` section."""
    headings = list(_TASK_HEADING_RE.finditer(tasks_text))
    blocks: list[tuple[str, str]] = []
    for i, m in enumerate(headings):
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(tasks_text)
        blocks.append((m.group(1), tasks_text[start:end]))
    return blocks


def _task_has_exit_criteria(block: str) -> bool:
    m = re.search(r"^####\s*Exit criteria\s*$", block, re.MULTILINE | re.IGNORECASE)
    if not m:
        return False
    rest = block[m.end():]
    next_heading = re.search(r"^#{1,6}\s", rest, re.MULTILINE)
    section = rest[: next_heading.start()] if next_heading else rest
    return bool(re.search(r"^\s*-\s*\[[ xX]\]\s*\S", section, re.MULTILINE))


def _task_evidence_destination(block: str) -> str | None:
    m = re.search(r"\*\*Evidence:\*\*\s*(.+)", block)
    if not m:
        return None
    value = m.group(1).strip()
    return value or None


def source_sufficiency_errors(initiative_dir: Path) -> list[str]:
    """Return actionable error strings for an initiative's canonical sources.

    An empty list means the sources are sufficient to proceed to composition.
    This function reads only the five canonical Markdown sources; it never
    reads or produces a brief-model or HTML artifact.
    """
    errors: list[str] = []
    texts: dict[str, str] = {}
    for name in REQUIRED_SOURCES:
        text = _read(initiative_dir / name)
        if text is None:
            errors.append(f"source-sufficiency: missing canonical source '{name}' in {initiative_dir}")
        else:
            texts[name] = text

    if "spec.md" in texts and "validation-plan.md" in texts:
        ac_ids = _extract_ac_ids(texts["spec.md"])
        validated = _extract_ac_validation_paths(texts["validation-plan.md"])
        for ac_id in ac_ids:
            if ac_id not in validated:
                errors.append(
                    f"source-sufficiency: {ac_id} (spec.md) has no row in "
                    f"validation-plan.md's acceptance traceability table -- "
                    f"add a Validation ID row naming {ac_id} with a command/steps cell"
                )
            elif not validated[ac_id]:
                errors.append(
                    f"source-sufficiency: {ac_id} (spec.md) is named in "
                    f"validation-plan.md but its command/steps cell is empty -- "
                    f"declare how {ac_id} is actually validated"
                )

    if "impact-map.md" in texts:
        for risk_id, owner_cell in _extract_material_risks(texts["impact-map.md"]):
            if not _has_named_owner(owner_cell):
                errors.append(
                    f"source-sufficiency: {risk_id} (impact-map.md) has no named owner "
                    f"in its Contingency/owner cell -- add who owns this risk"
                )

    if "plan.md" in texts:
        profile = _extract_architecture_profile(texts["plan.md"])
        if profile is None:
            errors.append(
                "source-sufficiency: plan.md does not declare an architecture "
                "scope/size profile -- add '**Profile:** S|M|L|high|unknown' "
                "under '### Architecture scope/size profile'"
            )
        else:
            normalized = profile.lower().split("|")[0].strip()
            if normalized not in _ALLOWED_PROFILE_VALUES:
                errors.append(
                    f"source-sufficiency: plan.md declares architecture profile "
                    f"'{profile}', which is not one of localized/S, S, M, L, high, unknown"
                )

    if "tasks.md" in texts:
        task_blocks = _split_tasks(texts["tasks.md"])
        if not task_blocks:
            errors.append("source-sufficiency: tasks.md has no '### T-NNN' task sections")
        for task_id, block in task_blocks:
            if not _task_has_exit_criteria(block):
                errors.append(
                    f"source-sufficiency: {task_id} (tasks.md) has no non-empty "
                    f"'#### Exit criteria' checklist"
                )
            destination = _task_evidence_destination(block)
            if not destination:
                errors.append(
                    f"source-sufficiency: {task_id} (tasks.md) has no evidence "
                    f"destination -- add '**Evidence:** evidence/{task_id}.md'"
                )

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/validate_source_sufficiency.py <initiative-dir>", file=sys.stderr)
        return 2
    initiative_dir = Path(argv[1])
    if not initiative_dir.is_dir():
        print(f"source-sufficiency: not a directory: {initiative_dir}", file=sys.stderr)
        return 2
    errors = source_sufficiency_errors(initiative_dir)
    if errors:
        print(f"source sufficiency check FAILED for {initiative_dir} ({len(errors)} issue(s)):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"source sufficiency check passed for {initiative_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
