# Independent Evaluation: T-003 and T-004

**Initiative:** 027-brief-composition-plan-and-skeleton-integrity  
**Evaluator ID:** `/root/spec027_eval_t001` (distinct from the R2 planners,
compositors and recorded candidate reviewers)  
**Run audited:** `testes/mock-runs/20260901-spec027-composition-r2/`  
**Date:** 2026-09-01  
**Verdict:** `approve`

## Scope and evidence reviewed

The complete heterogeneous R2 corpus was audited: M-001 news, M-002
reconciliation, M-003 offline inspections, M-004 learning, M-005 local AI,
M-006 financial reporting, M-007 public kiosk and M-008 event inventory.
For every case I inspected the canonical plan/run state, local skeleton,
candidate, latest approved pre-skeleton review and latest candidate-experience
review. I also read `manual-adjustments.md` and the SPEC, validation plan,
T-003/T-004 evidence and relevant inheritance test contract.

| Case | Pre-skeleton plan | Skeleton/candidate | Guard | Final qualitative review |
|---|---|---|---|---|
| M-001 | `plan-composition-rereview-r2.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-002 | `plan-composition-rereview-r2.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-003 | `plan-composition-review-r2-final.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-004 | `plan-composition-rereview-r2.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-005 | `plan-composition-review.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-006 | `plan-composition-review.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-007 | `plan-composition-finalreview-r2.md` — APPROVE | 1 / 1 | pass | APPROVE |
| M-008 | `plan-composition-finalreview-r2.md` — APPROVE | 1 / 1 | pass | APPROVE |

Each of the eight consumers reports `brief_coverage_ready: true` and
`brief_phase: not_rendered`. A recursive audit found **zero**
`stakeholder-brief.html` files under their initiative `specs/` directories:
these are non-promoted candidates, as required.

## Requirement-by-requirement findings

| Requirement / acceptance criterion | Finding | Result |
|---|---|---|
| FR-027-07, AC-027-04 | Each candidate is paired with an initiative-local v3 skeleton. Re-running the inheritance guard against all eight exact pairs passed; this proves retained shell/stylesheet/navigation contract while allowing slot composition. | pass |
| FR-027-08, AC-027-05 | Each final review compares source package, plan §9.1 and candidate, and checks eight addressable tab/panel routes plus retained URL, keyboard and print behavior. It initially returned `REVISE` when the visible slot scaffold prompt persisted, then approved only after a candidate-local slot override removed it. | pass, with desktop limitation below |
| FR-027-09 | No final `stakeholder-brief.html` was created under any R2 initiative. The run retains only skeletons and candidates, so no renderer/promotion recomposed or silently replaced reviewed bytes. | pass |
| FR-027-10, AC-027-06 | The suite spans web/news, backend batch reconciliation, Android offline, multiplatform learning, local AI, financial documents, public accessibility kiosk and event inventory. The tracked bundle/script diff contains no R2 case identifier or mock-specific rule. | pass |
| AC-027-07 | Guard regression, skeleton initializer, plan-composition contract and existing editorial contract all passed; `validate_bundle.py` passed with 282 checks; `git diff --check` found no whitespace error (only the known CRLF normalization warning for `specs/INDEX.md`). | pass |

## Manual adjustments and residual risk

`testes/mock-runs/20260901-spec027-composition-r2/manual-adjustments.md`
records all three repairs. MA-001 and MA-002 synchronize stale run-state
projections after already-approved evidence, without changing source facts or
candidates. MA-003 adds the same candidate-local, permitted slot override to
M-001..M-004 to suppress the inherited scaffold pseudo-content; it leaves the
base shell/stylesheet and source content intact. This is appropriately recorded
as a possible future guidance improvement, not embedded as a fixture-specific
bundle rule.

The available browser blocks local `file://` navigation. Consequently no
review claims a live desktop screenshot or interactive browser observation.
Static markup/JS review remains sufficient for this R2 regression because T-004
expressly calls for browser/capture **when available**, and it independently
verifies the retained desktop-oriented route, URL, keyboard and print contract.
It is not a substitute for a future live-browser visual review when the runtime
supports local candidates.

## Validations executed by this evaluator

```text
8 × python scripts/validate_brief_candidate_inheritance.py
      <candidate> --initiative <initiative> --skeleton <local skeleton>  # PASS
python scripts/test_brief_candidate_inheritance.py                         # PASS
python scripts/test_instantiate_brief_skeleton.py                           # PASS
python scripts/test_spec027_plan_composition_contract.py                    # PASS
python scripts/test_executive_brief_editorial_contract.py                   # PASS
python scripts/validate_bundle.py                                           # PASS (282 checks)
git diff --check                                                            # PASS; known CRLF warning only
```

## Decision and next safe action

T-003 and T-004 satisfy their exits and may transition through `approved` to
`done`. The SPEC regression is complete; retain the recorded manual-adjustment
observations as input to a future improvement decision, rather than changing
this generalized contract or promoting any mock candidate.
