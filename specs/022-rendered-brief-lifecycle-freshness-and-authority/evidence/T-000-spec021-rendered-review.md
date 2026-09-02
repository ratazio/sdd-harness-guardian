# Reproduction — SPEC 021 rendered lifecycle failure

**Origin:** SPEC 021 `evidence/T-000-rendered-decision-review.md` · **Date:**
2026-08-28 · **Severity:** P1/blocking.

After `render_stakeholder_brief.py` promoted the reviewed candidate, canonical
state became `brief_phase: rendered`, but the target HTML still declared
`data-brief-phase="authored"`, called itself a composition candidate, named the
pre-render reviewer and bound `run-state.yaml` to pre-render bytes. System
designer, general stakeholder and delivery manager independently returned
REVISE P1; architect and executive approved the semantic content but did not
override the lifecycle failure.

The reproduction shows a renderer lifecycle defect: candidate copy occurs
before the state transition and no rendered-state provenance/text refresh
occurs. The remedy must synchronize only declared lifecycle facts before the
target is written, then repeat independent post-render review. It must not
score prose, infer domain materiality or modify the failed HTML in place.
