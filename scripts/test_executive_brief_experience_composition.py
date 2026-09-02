#!/usr/bin/env python3
"""T-003 wiring checks for source-grounded executive architecture projections.

These checks preserve source locators and honest dispositions in three authored
examples. They intentionally do not decide whether a thesis, diagram or route
is sufficiently executive; that remains the distinct experience review.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "scripts" / "fixtures" / "executive-brief-editorial-contract"


class SourceBlocks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.blocks: dict[str, tuple[str, str, str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id") and values.get("data-source"):
            self.blocks[values["id"]] = (
                values["data-source"] or "",
                values.get("data-source-section") or "",
                values.get("data-coverage") or "",
            )


def candidate(case: str) -> SourceBlocks:
    parser = SourceBlocks()
    parser.feed((FIXTURES / case / "candidate.html").read_text(encoding="utf-8"))
    return parser


def require_case(case: str, expected: dict[str, tuple[str, str]]) -> None:
    parser = candidate(case)
    assert "architecture-opening" in parser.blocks, f"{case}: no architecture opening"
    for identifier, (section, coverage) in expected.items():
        source, actual_section, actual_coverage = parser.blocks[identifier]
        assert source == "source.md", f"{case}:{identifier}: unexpected source {source}"
        assert actual_section == section, f"{case}:{identifier}: locator lost"
        assert actual_coverage == coverage, f"{case}:{identifier}: disposition lost"


def main() -> int:
    require_case("learning-release", {
        "architecture-macro": ("Decision boundary", "represented"),
        "architecture-change-map": ("Change surfaces", "represented"),
        "architecture-scale": ("Change surfaces", "represented"),
        "learner-shell-zoom": ("Learner-shell zoom", "represented"),
    })
    require_case("reservoir-operations", {
        "architecture-macro": ("Turbidity recovery procedure", "represented"),
        "architecture-change-map": ("Turbidity recovery procedure", "represented"),
        "architecture-scale-discovery": ("Turbidity recovery procedure", "represented"),
        "architecture-zoom-na": ("Turbidity recovery procedure", "not_applicable"),
    })
    require_case("missing-internal-detail", {
        "architecture-macro": ("Gateway boundary", "represented"),
        "architecture-change-map-discovery": ("Gateway boundary", "not_applicable"),
        "architecture-scale-discovery": ("Gateway boundary", "not_applicable"),
        "architecture-zoom-discovery": ("Gateway boundary", "not_applicable"),
    })
    missing = (FIXTURES / "missing-internal-detail" / "candidate.html").read_text(encoding="utf-8")
    assert "settlement architect" not in missing and "approved implementation design" not in missing
    assert "not established by source" in missing and "It is not zero" in missing
    reservoir = (FIXTURES / "reservoir-operations" / "candidate.html").read_text(encoding="utf-8")
    assert "water-quality lead authorizes recovery" in reservoir
    assert "Scale is unknown" in reservoir and "it is not zero" in reservoir
    print("T-003 executive composition fixtures passed; semantic depth remains independently reviewed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
