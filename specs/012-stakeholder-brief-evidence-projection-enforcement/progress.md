# Progress: 012-stakeholder-brief-evidence-projection-enforcement

**Current phase/status:** validation_done — T-001–T-005 independently approved  
**Current task:** none  
**Last safe checkpoint:** D-018 approved the release and diverse local-kiosk fixture; final baseline/rechecks and bundle pass.  
**Last updated/by:** 2026-08-27 / delivery orchestrator  
**Run-state:** ./run-state.yaml  
**Stakeholder brief:** ./stakeholder-brief.html

## Outcome context

The goal is a narrow guard against missing cited evidence and missing material risk/API projections in v2 briefs, while preserving independent semantic/rendered review.

## Task summary

| Status | Task IDs |
|---|---|
| pending | none |
| done | T-001,T-002,T-003,T-004,T-005 |
| in progress/evaluation/revision/blocked | none |

## Validations and evidence

| Date | Task | Check/result | Evidence |
|---|---|---|---|
| 2026-08-26 | planning | `001-news-blog-auth` audit reproduced three blind spots and approved manual repair. | `testes/specs/001-news-blog-auth/evidence/planning-review.md` |
| 2026-08-27 | T-001 | Evaluator returned needs_revision: table context, empty inventory and out-of-context route controls are incomplete. | `evidence/T-001.md` |
| 2026-08-27 | T-001 | Re-evaluator returned needs_revision P4: heading-only API/contract table needs an Endpoint positive control. | `evidence/T-001.md` |
| 2026-08-27 | T-001 | Re-evaluator returned needs_revision P5: support for header-only Route/Method needs a dedicated fixture. | `evidence/T-001.md` |
| 2026-08-27 | T-001 | Independent evaluator approved grammar inventory and all P1–P5 controls. | `evidence/T-001.md` |
| 2026-08-27 | T-002 | `py_compile`, focused Human Visibility regression suite and task-owned `git diff --check` passed; evidence resolver awaits distinct security evaluation. | `evidence/T-002.md` |
| 2026-08-27 | T-002 | Security evaluator found `./evidence` baseline bypass; builder normalized the prefix and added normal/baseline negative regressions, all passing. Fresh evaluator decision pending. | `evidence/T-002.md` |
| 2026-08-27 | T-003 | Projection parser, exact missing-risk/route diagnostics, baseline blocking and v1/no-inventory compatibility regressions passed. The real synthetic fixture has no projection errors; its separate missing future-evidence failures remain for T-004 fixture synchronization. | `evidence/T-003.md` |
| 2026-08-27 | T-003 | Evaluator P1 repaired: `script`, `style` and `template` tokens no longer count as rendered projection; inert-node-only baseline regression fails as required. Fresh distinct evaluation pending. | `evidence/T-003.md` |
| 2026-08-27 | T-004 | Canonical block ledger matrix proves `pending`/`ready`/`in_progress`/`blocked` defer only future evidence, while `needs_evaluation`/`approved`/`done` fail without its pack, in normal and baseline modes. Fixture and SPEC 012 baseline write/rechecks, focused suite, bundle, compile and whitespace checks pass. | `evidence/T-004.md` |
| 2026-08-27 | T-005 | Focused suite, bundle (267 checks), compile and diff checks passed. Both repaired fixture/SPEC 012 baseline rechecks passed. A new no-route/no-formal-risk local-kiosk fixture passed baseline/recheck and static v2 brief review. | `evidence/T-005.md` |
| 2026-08-27 | T-005 | Evaluator tab-contract finding repaired: stable IDs, labelled focusable panels, roving focus, keyboard navigation, hash and print restore added; inline script check plus release/baseline checks passed. | `evidence/T-005.md` |

## Decisions and approvals

| ID/date | Summary | Link |
|---|---|---|
| D-001–D-011 / 2026-08-27 | Corrective scope, coverage approval, T-001 approval, T-002 finding and repaired builder handoff are recorded. | ./decision-log.md |

## Blockers and residual risks

| ID | Reason/impact | Owner | Next action |
|---|---|---|---|
| T-005 evaluation | Deterministic output and static markup must not be mistaken for decision-useful rendered review. | semantic evaluator | Evaluate the recorded rendered-review boundary and evidence; do not modify it during review. |

## Exact next safe step

SPEC 012 is complete; use its regression suite when changing Human Visibility behavior.

## Resume instructions

Read `run-state.yaml`, this file, `handoffs/latest-handoff.md`, `reproduction.md`, repository status, `validation-plan.md` and `decision-log.md` before any state transition.
