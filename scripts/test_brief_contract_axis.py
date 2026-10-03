#!/usr/bin/env python3
"""Regression coverage for the unified brief version axis (T-005, BC-002).

Proves three things:

1. The unified `data-brief-contract="N"` axis resolves to the correct v1/v2
   lineage, and the unified axis wins when a document somehow carries both.
2. The legacy three-axis combination it replaces
   (`data-harness-brief-design`, `data-harness-brief-structure`,
   `data-brief-shell-contract`) still resolves correctly on its own, per the
   BC-002 mapping table, so a historical brief keeps reading the same way.
3. A real historical/pinned brief keeps validating under its recorded
   contract with its bytes byte-for-byte unchanged (NG-004, FR-015, AC-011).

This deliberately does not touch, migrate or rewrite any brief under
`specs/**`; it only reads them.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from validate_bundle import (
    CONTRACT_AXIS_TO_LINEAGE,
    brief_contract_lineage,
    stakeholder_brief_errors,
)
from validate_human_visibility import brief_lineage


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / ".harness" / "templates" / "stakeholder-brief.html"

# Real, already-rendered pinned briefs (NG-004: never written to by this test).
PINNED_V1_BRIEF = ROOT / "specs" / "004-consumer-enforcement-contract" / "stakeholder-brief.html"
PINNED_V2_BRIEF = ROOT / "specs" / "010-stakeholder-brief-composition-kit" / "stakeholder-brief.html"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_unified_axis_mapping() -> None:
    """BC-002 table: `data-brief-contract` values resolve to the declared lineage."""
    require(CONTRACT_AXIS_TO_LINEAGE == {"1": "v1", "2": "v2", "3": "v3"}, "unexpected contract-axis mapping table")

    for value, lineage in CONTRACT_AXIS_TO_LINEAGE.items():
        html = f'<html data-brief-contract="{value}"><body></body></html>'
        require(brief_contract_lineage(html) == lineage, f"contract axis {value!r} did not resolve to {lineage!r}")

    require(
        brief_contract_lineage('<html data-brief-contract="9"><body></body></html>') is None,
        "an unrecognized contract axis value must not resolve to a lineage",
    )
    require(
        brief_contract_lineage("<html><body></body></html>") is None,
        "a document with no version axis at all must resolve to no lineage",
    )


def check_legacy_axis_fallback() -> None:
    """A historical document keeps resolving via the three legacy axes alone."""
    v1_only = '<html data-harness-brief-design="v1"><body></body></html>'
    v2_only = '<html data-harness-brief-design="v2"><body></body></html>'
    v2_full_legacy_combo = (
        '<html data-harness-brief-design="v2" '
        'data-harness-brief-structure="executive-brief-v3" '
        'data-brief-shell-contract="v1"><body></body></html>'
    )
    require(brief_contract_lineage(v1_only) == "v1", "legacy v1 marker alone must resolve to v1")
    require(brief_contract_lineage(v2_only) == "v2", "legacy v2 marker alone must resolve to v2")
    require(
        brief_contract_lineage(v2_full_legacy_combo) == "v2",
        "the full historical three-axis v2 combination must still resolve to v2",
    )
    # scripts/validate_human_visibility.py's brief_lineage must agree exactly:
    # it is the same lookup, reused, not a second implementation to drift.
    for sample, expected in ((v1_only, "v1"), (v2_only, "v2"), (v2_full_legacy_combo, "v2")):
        require(
            brief_lineage(sample) == expected == brief_contract_lineage(sample),
            "validate_human_visibility.brief_lineage must delegate to validate_bundle.brief_contract_lineage",
        )


def check_unified_axis_takes_precedence() -> None:
    """If a document somehow carries both axes, the unified one is authoritative."""
    contradictory = (
        '<html data-brief-contract="1" data-harness-brief-design="v2"><body></body></html>'
    )
    require(
        brief_contract_lineage(contradictory) == "v1",
        "the unified data-brief-contract axis must win over a conflicting legacy marker",
    )


def check_template_declares_unified_axis_only() -> None:
    html = TEMPLATE.read_text(encoding="utf-8")
    require('data-brief-contract="3"' in html, "template must declare the unified axis data-brief-contract=\"3\"")
    for legacy_attribute in (
        "data-harness-brief-design",
        "data-harness-brief-structure",
        "data-brief-shell-contract",
    ):
        require(
            legacy_attribute not in html,
            f"template must no longer declare the superseded legacy axis {legacy_attribute}",
        )
    require(brief_contract_lineage(html) == "v3", "template must resolve to v3 lineage via the unified axis")
    require(
        stakeholder_brief_errors(html, rendered=False) == [],
        "template must pass the current structural brief checks under the unified axis",
    )


def check_pinned_historical_brief(path: Path, expected_lineage: str) -> None:
    """AC-011/V-011: a historical pinned brief keeps passing, bytes unchanged."""
    require(path.is_file(), f"pinned fixture brief is missing: {path}")
    digest_before = sha256_of(path)
    html = path.read_text(encoding="utf-8")

    require(
        brief_contract_lineage(html) == expected_lineage,
        f"{path} must still resolve to lineage {expected_lineage!r} under its legacy marker",
    )
    require(
        brief_lineage(html) == expected_lineage,
        f"{path} must resolve identically through validate_human_visibility.brief_lineage",
    )
    errors = stakeholder_brief_errors(html, rendered=True)
    require(errors == [], f"{path} must still pass current structural checks unchanged: {errors}")

    digest_after = sha256_of(path)
    require(
        digest_before == digest_after,
        f"{path} bytes changed during validation; a historical brief must never be rewritten (NG-004)",
    )


def main() -> int:
    check_unified_axis_mapping()
    check_legacy_axis_fallback()
    check_unified_axis_takes_precedence()
    check_template_declares_unified_axis_only()
    check_pinned_historical_brief(PINNED_V1_BRIEF, "v1")
    check_pinned_historical_brief(PINNED_V2_BRIEF, "v2")
    print("Unified brief contract axis (BC-002) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
