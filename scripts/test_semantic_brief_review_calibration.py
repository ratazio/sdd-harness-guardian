#!/usr/bin/env python3
"""Static calibration-fixture wiring; it deliberately does not judge prose quality."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "scripts" / "fixtures" / "semantic-brief-review"
CASES = {
    "software-release": ("spec.md", "plan.md", "validation-plan.md", "decision-log.md"),
    "field-operations": ("spec.md", "plan.md", "validation-plan.md", "decision-log.md"),
    "shallow-negative": ("spec.md", "validation-plan.md", "decision-log.md"),
}


def read(path: Path) -> str:
    assert path.is_file(), f"missing calibration fixture: {path.relative_to(ROOT)}"
    content = path.read_text(encoding="utf-8")
    assert "{{" not in content and "State the outcome" not in content, f"placeholder in {path.relative_to(ROOT)}"
    return content


def assert_review_contract(review: str) -> None:
    for token in ("Product", "Architecture/operations", "Delivery", "Decision impossible from the brief"):
        assert token in review, f"review lacks required semantic-review locator: {token}"
    assert "Source:" in review or "Source/example" in review, "review lacks source locator"


def main() -> int:
    guidance = read(ROOT / ".harness" / "skills" / "spec-review" / "SKILL.md")
    for token in ("recoverable", "superficial", "absent", "lost/weakened fact", "automatic semantic gate"):
        assert token in guidance, f"spec-review guidance lacks calibration contract: {token}"

    read(FIXTURES / "README.md")
    for case, source_files in CASES.items():
        case_root = FIXTURES / case
        for source in source_files:
            read(case_root / source)
        brief = read(case_root / "stakeholder-brief.html")
        assert 'data-harness-brief-design="v2"' in brief, f"{case} lacks v2 fixture marker"
        assert_review_contract(read(case_root / "rendered-review.md"))

    negative = read(FIXTURES / "shallow-negative" / "rendered-review.md")
    for token in ("`superficial`", "`absent`", "Lost fact:", "Recovery action:"):
        assert token in negative, f"negative fixture does not demonstrate shallow synthesis: {token}"

    print("Semantic brief-review calibration fixtures passed; semantic adequacy remains independent review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
