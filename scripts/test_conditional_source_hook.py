#!/usr/bin/env python3
"""Static contract fixtures for corpus-driven conditional-source review.

The assertions only protect recoverability and review-record shape.  They do
not infer materiality, classify a domain, score prose or approve a candidate.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "scripts" / "fixtures" / "conditional-source-hook"
TEMPLATE = ROOT / ".harness" / "templates" / "conditional-source-semantic-review.md"


def read(path: Path) -> str:
    assert path.is_file(), f"missing conditional-source fixture: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def require(text: str, *tokens: str) -> None:
    for token in tokens:
        assert token in text, f"missing contract token: {token}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_manifest(case: str, entries: tuple[tuple[str, str], ...]) -> str:
    root = FIXTURES / case
    review = read(root / "review.md")
    require(review, "## Corpus manifest", "| Path | Scope / locator | SHA-256 |")
    for relative_path, locator in entries:
        digest = sha256(root / relative_path)
        require(review, f"`{relative_path}`", f"`{locator}`", f"`sha256:{digest}`")
    return review


def inventory_row(review: str, disposition: str) -> str:
    for line in review.splitlines():
        if "| `ratchet.md`" in line and f"`{disposition}`" in line:
            return line
    raise AssertionError(f"missing conditional inventory row: {disposition}")


def main() -> int:
    template = read(TEMPLATE)
    require(
        template,
        "Reviewer-declared inputs", "material_rule", "empty_with_reason",
        "Decision still impossible from HTML", "source path + locator",
        "source-backed reason", "must not infer missing sources",
        "not a classifier, score, visual quota, or automatic approval",
    )

    material_source = read(FIXTURES / "ratchet-material" / "ratchet.md")
    material_html = read(FIXTURES / "ratchet-material" / "stakeholder-brief.html")
    material_review = assert_manifest("ratchet-material", (
        ("request.md", "#Release request"), ("ratchet.md", "#R-42"),
        ("stakeholder-brief.html", "#ratchet"),
    ))
    require(material_source, "Trigger:", "Check:", "Owner:", "Consequence:")
    require(material_html, 'data-source="ratchet.md"', "data-source-section=\"R-42\"", f'data-source-digest="sha256:{sha256(FIXTURES / "ratchet-material" / "ratchet.md")}"', "Trigger:", "Check:", "Owner:", "Consequence:")
    material_inventory = inventory_row(material_review, "material_rule")
    require(material_inventory, "material_rule", "ratchet.md#R-42", f"sha256:{sha256(FIXTURES / 'ratchet-material' / 'ratchet.md')}", "stakeholder-brief.html#ratchet")
    require(material_review, "Decision still impossible from HTML", "APPROVE")

    empty_source = read(FIXTURES / "ratchet-empty" / "ratchet.md")
    empty_html = read(FIXTURES / "ratchet-empty" / "stakeholder-brief.html")
    empty_review = assert_manifest("ratchet-empty", (
        ("request.md", "#First controlled rollout request"), ("ratchet.md", "#Entries"),
        ("stakeholder-brief.html", "#ratchet"),
    ))
    require(empty_source, "No active preventive entries", "first controlled rollout")
    require(empty_html, 'data-source="ratchet.md"', f'data-source-digest="sha256:{sha256(FIXTURES / "ratchet-empty" / "ratchet.md")}"', "Ratchet state:", "Reason:")
    empty_inventory = inventory_row(empty_review, "empty_with_reason")
    require(empty_inventory, "empty_with_reason", "ratchet.md#Entries", f"sha256:{sha256(FIXTURES / 'ratchet-empty' / 'ratchet.md')}", "stakeholder-brief.html#ratchet")
    require(empty_review, "N/A dispositions:", "because", "APPROVE")

    revise_review = assert_manifest("omitted-relation", (
        ("request.md", "#Shift handoff request"), ("plan.md", "#Reconciliation"),
        ("stakeholder-brief.html", "#summary"),
    ))
    require(revise_review, "Decision still impossible from HTML", "Source:", "Candidate:", "Impact:", "Repair:", "rerender", "re-review", "N/A dispositions:", "REVISE")

    print("Conditional-source hook fixtures passed; materiality and approval remain independent human judgment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
