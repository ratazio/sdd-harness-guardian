#!/usr/bin/env python3
"""Guard the narrow autonomous-recovery instruction for executive briefs.

This test does not score prose, generate HTML, or weaken lifecycle evidence.
It protects the operational instruction that a recoverable composition finding
is repaired and re-reviewed by agents in the same run instead of becoming a
routine requester-approval wait.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def require(path: str, *phrases: str) -> None:
    content = (ROOT / path).read_text(encoding="utf-8")
    for phrase in phrases:
        assert phrase in content, f"{path} is missing autonomous-composition instruction: {phrase}"


def main() -> int:
    require(
        ".harness/skills/executive-brief-composition/SKILL.md",
        "## Autonomous completion rule",
        "## Whole-brief authorship check",
        "not a reason to leave a\nsource-backed brief half-built",
        "Only `approved`/Human\nVisibility claims wait",
    )
    require(
        ".harness/skills/executive-brief-experience-review/SKILL.md",
        "visit each of its eight route URLs",
        "untouched scaffold prose",
    )
    require(
        ".harness/skills/rendered-brief-decision-review/SKILL.md",
        "do not stop to ask the\nuser for routine approval",
        "automatic recovery attempted",
    )
    require(
        ".harness/workflows/sdd-lifecycle.md",
        "does not\n   wait for routine requester approval",
        "must not become a passive reason to stop\n   authoring",
    )
    print("SPEC 028 autonomous composition-recovery instruction contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
