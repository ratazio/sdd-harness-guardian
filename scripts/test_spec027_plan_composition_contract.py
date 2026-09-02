#!/usr/bin/env python3
"""Focused static contract checks for SPEC 027 T-001.

This validates that the reusable scaffold and independent-review instructions
remain present. It deliberately does not assess a plan's narrative or choose a
visual form.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read(relative: str) -> str:
    path = ROOT / relative
    assert path.is_file(), f"missing {relative}"
    return path.read_text(encoding="utf-8")


def require(text: str, *needles: str) -> None:
    for needle in needles:
        assert needle in text, f"missing contract text: {needle}"


def main() -> int:
    plan = read(".harness/templates/plan.md")
    composition = read(".harness/skills/executive-brief-composition/SKILL.md")
    review = read(".harness/skills/executive-brief-experience-review/SKILL.md")
    workflow = read(".harness/workflows/sdd-lifecycle.md")

    require(
        plan,
        "Brief thesis and global choices",
        "Decision and audience",
        "`scope`",
        "`architecture.global`",
        "`impact.<id>`",
        "`execution.task.<id>`",
        "`validation.proof.<id>`",
        "`evolution`",
        "`decision`",
        "`coverage`",
        "Chosen visual form and reason",
        "Repetition / required fields",
        "Absence, uncertainty or discovery",
        "Closing action",
        "Independent construction review — before skeleton instantiation",
        "`APPROVE` or `REVISE`",
        "source → loss or ambiguity → decision",
        "prejudiced → canonical correction",
    )
    require(composition, "Coverage mapping", "all eight routes", "Independent plan review")
    require(review, "Pre-skeleton construction-plan review", "fixed number of cards")
    require(workflow, "Independent Coverage and Construction Review", "only after the construction review is `APPROVE`")
    print("SPEC 027 T-001 plan-composition contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
