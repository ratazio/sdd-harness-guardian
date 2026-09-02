# Decision Log: 020-source-render-isolation-and-canonical-brief-composition

Record decisions that change scope, architecture, validation, risk, precedence
or workflow. Do not rewrite prior rows; append a superseding decision.

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | | proposed/accepted/superseded | | | | | none |

## D-020-001 — T-002 promotion gate accepted

**Status:** accepted · **Date:** 2026-08-28 · **Owner:** platform-engineering

The promotion boundary resolves the exact `brief_review.review_record` section
instead of searching the decision log globally. It binds author/reviewer,
approved outcome, candidate SHA and current source digests; every declared
source block binds its own local digest. The decision-record digest deliberately
normalizes out only the candidate-SHA field to avoid a self-referential hash.

**Rationale/evidence:** `evidence/T-002.md`; final independent evaluation
`/root/t002_final_evaluation` reproduced the complete shell-reclassification
bypass and observed the required refusal. The check verifies provenance topology
only; it does not score narrative or visual quality.

**Supersedes:** the incomplete T-002 implementation that accepted cosmetic
reclassification after only declarative attributes/digests.

## D-020-002 — Pearson is explicit opt-in

**Status:** accepted · **Date:** 2026-08-28 · **Owner:** platform-engineering

The canonical v2 scaffold is vendor-neutral. Only a rendered root declaring
`data-client-identity-profile="pearson"` invokes the Pearson policy and copies
the approved local logo. The neutral path has no logo request, copy or reference.

**Rationale/evidence:** browser and policy regressions in `evidence/T-002.md`
confirm local asset SHA, focus, no-script, print, responsive and reduced-motion
behaviour when selected.

## D-020-003 — Source isolation requires a visible factual binding

**Status:** accepted · **Date:** 2026-08-28 · **Owner:** platform-engineering

Every declared material source block must name an allowed initiative-local
source and current source digest, retain its human locator, and carry a literal
source fragment plus SHA-256. The fragment must exist in that local source and
be visible inside the same well-nested HTML block. Malformed nesting is refused
rather than guessed.

**Rationale/evidence:** `evidence/T-003.md`; `/root/t003_nesting_evaluation`
reproduced the real news/blog `PATCH /api/v1/admin/posts/:id` fact against the
reconciliation fixture and verified rejection even when it was labelled with
the target `spec.md` and SHA. It also reproduced the malformed close-tag bypass
and verified refusal.

**Limit:** this protects factual provenance, not the sufficiency or persuasiveness
of surrounding prose. T-004 retains the independent two-pass semantic review.

## D-020-004 — Full mock run is evidence of systemic composition gaps

**Status:** accepted · **Date:** 2026-08-28 · **Owner:** platform-engineering

The r5 run generated all eight official mocks in new disposable consumers and
obtained seven independent two-pass reviews per case. No baseline is approved:
all cases have a material `REVISE`. The recurring causes are missing conditional
ratchet recovery and generic architecture representations that lose
domain-specific relations.

**Rationale/evidence:** `evidence/T-004.md`. The user pre-authorized a
corrective Guardian SPEC for systemic findings; source-only SPEC 021 records
the problem, ACs, pending tasks and validation. r5 is preserved as failed
evidence, not cosmetically patched.

## D-020-005 — T-004 execution evidence accepted without a mock baseline

**Status:** accepted · **Date:** 2026-08-28 · **Owner:** platform-engineering

The distinct `/root/t004_completion_audit` verified the complete r5 manifest,
all 24 request/source/HTML SHA-256 values, all 56 individual two-pass records,
the absence of a baseline, and the source-only corrective SPEC 021. It approved
completion of T-004 as an honest execution record only.

**Rationale/evidence:** `evidence/T-004.md`; `python scripts/validate_bundle.py`
passed 272 checks during the independent audit. This decision explicitly does
not approve any r5 stakeholder HTML or turn a deterministic promotion PASS into
human approval.
