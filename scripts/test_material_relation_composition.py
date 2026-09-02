#!/usr/bin/env python3
"""T-002 fixture wiring for source-driven material-relation composition.

This test verifies only reviewer-declared corpus binding and recoverability of
the two documented examples. It deliberately has no domain labels, scoring,
visual quotas, representation selector or semantic verdict logic.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "scripts" / "fixtures" / "material-relation-composition"


def read(path: Path) -> str:
    assert path.is_file(), f"missing T-002 fixture: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(text: str, *tokens: str) -> None:
    for token in tokens:
        assert token in text, f"missing required record token: {token}"


def assert_manifest(root: Path, review: str, files: tuple[tuple[str, str], ...]) -> None:
    require(review, "## Corpus manifest", "| Path | Scope / locator | SHA-256 |")
    for relative, locator in files:
        expected = digest(root / relative)
        require(review, f"`{relative}`", f"`{locator}`", f"sha256:{expected}")


def assert_positive(case: str, request_locator: str, source: str, source_locator: str, candidate_id: str, recovery: tuple[str, ...], representation_reason: str) -> None:
    root = FIXTURES / case
    review = read(root / "review.md")
    candidate = read(root / "candidate.html")
    rendered = read(root / "stakeholder-brief.html")
    assert_manifest(root, review, (("request.md", request_locator), (source, source_locator), ("candidate.html", candidate_id), ("stakeholder-brief.html", candidate_id)))
    require(review, "Composer identity:", "Reviewer identity:", "Disposition:", representation_reason, "Decision still impossible from HTML:** none", "N/A dispositions:", "Verdict:** APPROVE")
    element_id = candidate_id.removeprefix("#")
    require(candidate, f'id="{element_id}"', *recovery)
    source_digest = digest(root / source)
    require(rendered, f'id="{element_id}"', f'data-source="{source}"', "data-source-section=", f'data-source-digest="sha256:{source_digest}"', *recovery)
    assert "spec021_t002_builder" not in review.split("**Reviewer identity:**", 1)[1].splitlines()[0]


def assert_loss(case: str, request_locator: str, source: str, source_locator: str, missing: tuple[str, ...]) -> None:
    root = FIXTURES / case
    review = read(root / "review-lost.md")
    lost = read(root / "candidate-lost.html")
    assert_manifest(root, review, (("request.md", request_locator), (source, source_locator), ("candidate-lost.html", "#summary")))
    require(review, "Decision still impossible from HTML:", "Finding:", f"Source: `{source}{source_locator}`", "Candidate:", "Impact:", "Repair:", "rerender", "re-review", "N/A dispositions:", "Verdict:** REVISE")
    for token in missing:
        assert token not in lost, f"negative fixture accidentally recovers material relation: {token}"


def main() -> int:
    readme = read(FIXTURES / "README.md")
    require(readme, "not a representation", "taxonomy and not a production selection algorithm")
    assert_positive("clearing-boundary", "#Clearing instruction request", "architecture.md", "#Ledger admission boundary", "#ledger-boundary", ("Clearing gateway", "treasury approval", "returns refuse", "gateway receipt"), "boundary handoff")
    assert_loss("clearing-boundary", "#Clearing instruction request", "architecture.md", "#Ledger admission boundary", ("Clearing gateway", "treasury approval", "returns refuse"))
    assert_positive("reservoir-recovery", "#Reservoir recovery request", "operations.md", "#Turbidity recovery procedure", "#turbidity-recovery", ("Hold", "second sample", "Recover", "does not restart pumping"), "recovery progression")
    assert_loss("reservoir-recovery", "#Reservoir recovery request", "operations.md", "#Turbidity recovery procedure", ("second sample", "water-quality lead", "does not restart pumping"))
    print("T-002 material-relation fixtures passed; representation and sufficiency remain human judgment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
