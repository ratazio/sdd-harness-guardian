# Validation Plan: 008-semantic-brief-review-calibration

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-25

## 1. Strategy

Deterministic checks prove file structure, lineage and fixture wiring only. Independent qualitative review answers what cannot be truthfully scored: whether a decision remains recoverable, whether an `N/A` is justified, and whether rendered synthesis lost a material fact. The shallow negative fixture must be structurally formal enough to demonstrate why structural pass is not semantic approval.

### Assurance selection

| Profile/task | Risk or claim | Technique selected/inapplicable rationale | Oracle and evidence | Executor | Evaluator | Failure/waiver behavior |
|---|---|---|---|---|---|---|
| A2 / T-001 | Review contract is actionable, not generic. | Fixture review with source→fact→action rubric. | Finding records and reviewer decision. | builder | distinct reviewer | Block/revise guidance; no waiver for missing action. |
| A2 / T-002 | Examples generalize beyond software. | Static fixture/test + 60-second rendered review. | Software and non-software review records. | builder | distinct reviewer | Revise examples if a lens is forced/omitted. |
| A2 / T-003 | No semantic score is introduced. | Diff review and focused tests. | Diff has no score/parser; tests pass. | builder | distinct evaluator | Reject; human approval for waiver. |
| A2 / T-004 | Bundle remains coherent. | Bundle validation and rendered review. | Commands and review record. | builder | distinct evaluator | Return to revision; no release baseline. |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | fixture + qualitative review | Review a fixture using three lenses and justified N/A. | Each lens has judgment, source/example and recovery action when needed. | evidence/T-001.md | reviewer |
| V-002 | AC-002 | negative fixture review | Feed shallow-but-formal brief to review. | Finding names lost risk/validation/decision/next-step fact and source correction. | evidence/T-002.md | reviewer |
| V-003 | AC-003 | lifecycle/fixture test | Assert distinct pre-render and post-render records. | Different purposes; no new permanent role. | evidence/T-001.md | evaluator |
| V-004 | AC-004 | paired example review | Read software and non-software cases. | Equivalent decision surfaces; irrelevant lens gets reasoned N/A. | evidence/T-002.md | reviewer |
| V-005 | AC-005 | negative diff review | Inspect changed scripts/templates and run focused tests. | No score, prose parser or semantic deterministic gate. | evidence/T-003.md | evaluator |
| V-006 | AC-006 | compatibility fixture | Run legacy v1 fixture path. | v1 stays valid absent material refresh. | evidence/T-003.md | evaluator |
| M-001 | AC-007 | rendered review | 60-second, keyboard/no-script/print checks. | Outcome, risk/control, state, decision and next step recover without MD. | evidence/T-004.md | reviewer |
| V-007 | AC-008 | release review | Mantenedor revisa E-001–003 e o evidence pack de T-004. | Aceita ou devolve a mudança com razão registrada. | evidence/T-004.md + decision-log.md | maintainer |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | IR-002 false semantic approval | Review shallow negative after structural validation. | Structural outcome is explicitly limited; semantic review rejects it. | T-002 review record |
| V-REG-002 | IR-003 deterministic creep | Search diff for score/threshold/word-count semantics. | No acceptance relies on numeric/prose parsing. | T-003 diff review |
| V-REG-003 | IR-005 v1 regression | Execute v1 tests and bundle validation. | Existing v1 contract remains valid. | T-003 output |
| V-REG-004 | AC-007 accessibility/readability | Desktop/390px/keyboard/no-script/print review. | Readable progressive disclosure and local overflow. | T-004 notes |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | bundle root | exit 0 | T-004 |
| `python -m unittest scripts.test_validate_human_visibility` | bundle root | exit 0 | T-003 |
| focused fixture command added by T-002 | bundle root | exit 0, checks both examples | T-002 |
| `python scripts/validate_human_visibility.py --consumer-root . --initiative specs/008-semantic-brief-review-calibration` | bundle root | structural/state/freshness pass after review/baseline | T-004 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Read each rendered example for 60 seconds without MD. | State outcome, scope, risk/control, validation, decision and next safe step. | evidence/T-004.md |
| M-002 | Ask “what material decision cannot be made without MD?” after render. | No loss, or source-linked correction finding. | decision-log.md + evidence/T-004.md |
| M-003 | Keyboard, JS-disabled, print preview and 390px viewport. | Native details/text equivalents/local overflow work. | evidence/T-004.md |

Outputs planned: T-002 stores fictional source, review and HTML examples under its fixture directory; T-004 stores the source-to-rendered review result in `evidence/T-004.md` and the gate/release decision in `decision-log.md`. These are planned checks, not installed controls.

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Product, architecture/operations, delivery; N/A needs reason. | Sources, composition, rendered brief. | No material lens superficial/absent without source-linked correction or accepted reason. | distinct Spec Guardian |
| E-002 | Generalization, not software vocabulary. | Paired fixtures. | Non-software is judged by real operating surfaces, not fake APIs. | distinct Spec Guardian |
| E-003 | Loss-aware rendered meaning. | 60-second brief. | No material decision is impossible solely from compression. | distinct reviewer/human |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Load/performance test | No runtime/network/execution loop changes. | none expected | not applicable |
| Automated semantic oracle | False precision and violates FR-006. | Human inconsistency managed by examples. | future sponsor under AD-005 |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex / Harness Planner  
**Blocking gaps:** none for preliminary task drafting. Independent semantic/rendered review remains required before Human Visibility and task authorization.
