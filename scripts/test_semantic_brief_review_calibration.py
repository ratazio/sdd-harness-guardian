#!/usr/bin/env python3
"""Static fixture wiring for independent human review; it never scores prose."""

from __future__ import annotations

import re
from pathlib import Path

from validate_bundle import stakeholder_brief_errors


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
    for token in (
        "Review ID:", "Request locator:", "Canonical source locators:",
        "Rendered HTML locator:", "Materiality", "Finding ID:",
        "Decision impossible from the brief", "Recovery action:",
        "Re-review:",
    ):
        assert token in review, f"review lacks required semantic-review locator: {token}"
    assert "Source:" in review or "Source/example" in review, "review lacks source locator"
    assert re.search(r"\*\*Reviewer:\*\*|\| Lens \| Reviewer ID \|", review), (
        "review lacks an independent reviewer identity"
    )


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
        review = read(case_root / "rendered-review.md")
        assert_review_contract(review)
        assert "<body" in brief, f"{case} fixture is not renderable HTML"

    negative = read(FIXTURES / "shallow-negative" / "rendered-review.md")
    for token in ("structurally valid", "`insufficient`", "Lost fact:", "Recovery action:", "REVISE"):
        assert token in negative, f"negative fixture does not demonstrate shallow synthesis: {token}"
    negative_html = read(FIXTURES / "shallow-negative" / "stakeholder-brief.html")
    assert stakeholder_brief_errors(negative_html, rendered=True) == [], (
        "decision-poor negative must remain structurally valid; its rejection belongs to human review"
    )
    css_scaffold_selector = negative_html.replace(
        "</style>", "html[data-harness-template-kind='scaffold'] .slot:after{content:'fixture'}</style>", 1
    )
    assert stakeholder_brief_errors(css_scaffold_selector, rendered=True) == [], (
        "a retained CSS selector must not be mistaken for the root template identity"
    )
    assert "`insufficient` / REVISE" in negative, (
        "negative fixture must retain an expected material review revision"
    )

    for case in ("software-release", "field-operations"):
        positive = read(FIXTURES / case / "rendered-review.md")
        assert "APPROVE" in positive, f"{case} must record an approval disposition"

    varied = read(FIXTURES / "field-operations" / "stakeholder-brief.html")
    assert 'role="tab"' not in varied and "<svg" not in varied, (
        "varied positive fixture must prove that neither tabs nor diagrams are universal requirements"
    )

    print("Semantic brief-review calibration fixtures passed; semantic adequacy remains independent review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
