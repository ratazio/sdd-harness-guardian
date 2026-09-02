#!/usr/bin/env python3
"""T-001 fixture wiring for source-grounded executive editorial maps.

The check protects declared evidence and negative boundaries. It intentionally
does not score narrative, choose a visual representation, infer materiality or
turn an APPROVE record into automatic semantic approval.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "scripts" / "fixtures" / "executive-brief-editorial-contract"


def read(path: Path) -> str:
    assert path.is_file(), f"missing T-001 fixture: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(text: str, *tokens: str) -> None:
    for token in tokens:
        assert token in text, f"missing declared contract token: {token}"


def assert_case(case: str, required: tuple[str, ...]) -> None:
    root = FIXTURES / case
    source = read(root / "source.md")
    editorial_map = read(root / "editorial-map.md")
    review = read(root / "review.md")
    require(editorial_map, "| Projection | Source / locator |", "`source.md#")
    require(review, "**Composer identity:**", "**Reviewer identity:**", "**Verdict:** APPROVE")
    composer = review.split("**Composer identity:**", 1)[1].splitlines()[0].strip()
    reviewer = review.split("**Reviewer identity:**", 1)[1].splitlines()[0].strip()
    assert composer != reviewer, f"{case} reviewer must remain independent"
    for token in required:
        require(source + editorial_map + review, token)
    assert digest(root / "source.md"), "source fixture must be hashable for an external review record"


def assert_explicit_discovery_absence(case: str, forbidden: tuple[str, ...]) -> None:
    """Preserve the absent-authority disposition without inventing an assignment."""
    root = FIXTURES / case
    source = read(root / "source.md")
    editorial_map = read(root / "editorial-map.md")
    review = read(root / "review.md")
    require(editorial_map, "Discovery owner/path: not established by source")
    require(editorial_map, "Needed fact:", "decision impact:")
    require(review, "does not establish", "owner", "resolution path")
    for token in forbidden:
        assert token not in editorial_map, f"{case} map invents unsupported discovery ownership/path: {token}"
        assert token not in source, f"{case} negative boundary must be absent from source: {token}"


def assert_discovery_disposition_contract() -> None:
    """The reusable contract allows only source-supported or explicit-absence ownership."""
    composition = read(ROOT / ".harness" / "skills" / "executive-brief-composition" / "SKILL.md")
    reviewer = read(ROOT / ".harness" / "skills" / "executive-brief-experience-review" / "SKILL.md")
    require(composition, "If the source supports a discovery", "owner/path are not", "established")
    require(reviewer, "source supports a discovery owner/path", "owner/path are not", "established")


def main() -> int:
    readme = read(FIXTURES / "README.md")
    require(readme, "do not choose a diagram", "does not decide")
    assert_discovery_disposition_contract()
    assert_case("learning-release", ("#Decision boundary", "3 changed source-supported surfaces / 4 named surfaces", "#Learner-shell zoom"))
    assert_case("reservoir-operations", ("#Turbidity recovery procedure", "not a software/frontend architecture claim", "unknown — source does not enumerate affected physical assets", "N/A"))
    assert_explicit_discovery_absence("reservoir-operations", ("before rollout", "identifies affected asset count"))
    assert_case("missing-internal-detail", ("#Gateway boundary", "Never render `0` changed modules", "discovery required"))
    assert_explicit_discovery_absence("missing-internal-detail", ("settlement architect", "approved implementation design"))
    invalid = read(FIXTURES / "missing-internal-detail" / "invalid-fabricated-map.md")
    for fabricated in ("React reducer", "API adapter", "0 other modules"):
        assert fabricated in invalid, "negative fixture must retain the explicit unsupported claim"
        assert fabricated not in read(FIXTURES / "missing-internal-detail" / "editorial-map.md"), "positive map must not fabricate internals"
    print("T-001 editorial-contract fixtures passed; semantic adequacy remains an independent review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
