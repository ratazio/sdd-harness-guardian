#!/usr/bin/env python3
"""Focused static contract checks for SPEC 027 T-001, updated by T-008.

SPEC 027 T-001 originally proved that the reusable construction-record
contract (thesis/audience, per-route content, review) was present in
`plan.md` §9.1 before a skeleton was instantiated. T-008 (SPEC 029) removed
that section and the skeleton mechanism: the construction record now lives in
`brief-model.yaml`, validated by `schemas/brief-model.schema.json` and
`scripts/validate_brief_model.py`, and reviewed as BC-009 pass (a) before
projection (not before a skeleton). This test now proves the same underlying
claim — a reusable construction-record contract exists and independent review
is required before the candidate is produced — against the artifacts that
actually implement it today.

It deliberately does not assess a model's narrative or choose a visual form.
"""

from __future__ import annotations

import json
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
    schema = json.loads(read("schemas/brief-model.schema.json"))
    contract = read(".harness/rules/brief-contract.md")
    composition = read(".harness/skills/executive-brief-composition/SKILL.md")
    review = read(".harness/skills/executive-brief-experience-review/SKILL.md")
    workflow = read(".harness/workflows/sdd-lifecycle.md")

    # The construction record's per-route/repeated-component contract now
    # lives in the schema (thesis, routes, closed route-ID vocabulary) rather
    # than as a hand-filled Markdown table.
    schema_text = json.dumps(schema)
    require(schema_text, "thesis", "routes", "scope", "architecture", "impact",
            "execution", "validation", "evolution", "decision", "coverage")
    require(contract, "## BC-007", "## BC-008", "## BC-013", "## BC-022")

    legacy_composition = composition.split("## Histórico 1/2", 1)[1]
    legacy_review = review.split("## Histórico 1/2", 1)[1]
    legacy_workflow = workflow.split("### Contract 2", 1)[1].split("### Contract 1", 1)[0]
    require(legacy_composition, "brief-model.yaml", "pass a", "BC-008/009")
    require(legacy_review, "pass (a)", "brief-model.yaml",
            "APPROVE", "REVISE")
    require(legacy_workflow, "model/construction pass (a)", "projection", "rendered pass (b)")
    direct = composition.split("## Histórico 1/2", 1)[0]
    require(direct, "HTML diretamente", "Handoff direto A → B", "Não crie `brief-model.yaml`")
    print("SPEC 027 T-001 plan-composition contract passed (re-based on the model by T-008).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
