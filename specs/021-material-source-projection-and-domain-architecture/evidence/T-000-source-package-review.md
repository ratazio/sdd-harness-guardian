# Source package review — SPEC 021

**Builder:** codex-orchestrator · **Evaluator:** `/root/spec021_source_review`
· **Date:** 2026-08-28 · **Verdict:** APPROVE.

## Scope reviewed

The evaluator read the source-only package, the T-004 reproduction from SPEC
020 and the amended decision boundary for the corpus-driven semantic hook.

## Findings and repair

The first independent pass returned `REVISE P1`: D-021-002/D-021-003 formed a
supersedence cycle and the phrase “corpus completo” could imply that code would
infer materiality. The builder repaired both: D-021-002 remains accepted for
conditional ratchet/source-driven relations, D-021-003 complements it without
a cycle, and the deterministic contract now binds only the reviewer-declared
input manifest, identity, digests and record scope.

The re-review returned `APPROVE`: the reviewer confirmed that materiality and
semantic sufficiency remain with the distinct natural-language reviewer, with
no domain taxonomy, expected-answer prompt, prose/visual score or automatic
semantic approval.

## Validation

`python scripts/validate_bundle.py` — PASS (272 checks).

## Next safe step

Compose coverage and a real candidate brief, then obtain a pre-render review
distinct from its composer. This record does not authorize T-001 yet.
