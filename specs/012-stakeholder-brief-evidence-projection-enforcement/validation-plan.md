# Validation Plan: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** validation_ready  
**Spec / plan:** ./spec.md / ./plan.md  
**Owner / updated:** platform-engineering / 2026-08-26

## 1. Strategy

Use A2 proportionate validation: direct Python unit/fixture assertions for
every new failure branch, a real repaired fixture as a positive integration
control, legacy/no-contract compatibility cases, and separate independent
review of diagnostics plus rendered-review guidance. The oracle for a negative
fixture is exact non-zero status and diagnostic token; the oracle for a
positive fixture is zero status and no new baseline/freshness inconsistency.

| Profile/task | Risk or claim | Technique selected/inapplicable rationale | Oracle and evidence | Executor | Evaluator | Failure/waiver behavior |
|---|---|---|---|---|---|---|
| A2 / T-001–T-003 | New parser/resolver can overmatch or escape root. | Unit + negative/compatibility fixtures; manual path-boundary inspection. | Exit code, group and precise token in task evidence. | builder | independent evaluator + security reviewer | Block approval; no waiver for containment. |
| A2 / T-004 | End-to-end bundle contract remains sound. | Bundle + Human Visibility baseline/recheck. | PASS output and baseline hash in evidence. | builder | independent evaluator | Return to revision on any failure. |
| A2 / T-005 | Deterministic check is not semantic approval. | Independent rendered-review rubric. | Signed review finding/decision. | reviewer | separate final evaluator | Block completion on material finding. |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | Unit/negative fixture | Run focused Human Visibility tests with absent evidence and unsafe locators. | Non-zero; names locator; no out-of-root read. | evidence/T-002.md | validation maintainer |
| V-002 | AC-002 | Unit/negative fixture | Omit each declared IR token from Impact. | Non-zero; names each missing IR and Impact view. | evidence/T-003.md | validation maintainer |
| V-003 | AC-003 | Unit/negative fixture | Omit each canonical method/path from Architecture and Validation. | Non-zero; names normalized route and allowed views. | evidence/T-003.md | validation maintainer |
| V-004 | AC-004 | Integration/baseline | Run repaired fixture with `--write-baseline`, then recheck. | Both zero; baseline only after checks pass. | evidence/T-004.md | builder |
| V-005 | AC-005 | Regression fixture | Run existing valid v2, v1 and no-risk/no-API cases. | Preserved intended pass/fail behavior. | evidence/T-004.md | evaluator |
| V-006 | AC-006 | Security unit/manual | Test absolute, drive-rooted, traversal and symlink/resolve boundary cases supported by runtime. | Fail closed without content exposure. | evidence/T-002.md | security reviewer |
| V-007 | AC-007 | Independent review | Inspect template/guidance and rendered fixture after deterministic PASS. | Distinct-review requirement remains explicit/useful. | evidence/T-005.md | semantic reviewer |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | IR-002 | Parser grammar inventory and prose false-positive fixture. | Only canonical risk/API forms create obligations. | evidence/T-001.md |
| V-REG-002 | IR-005 | Negative fixture runs with `--write-baseline`. | Fails before a success baseline is accepted. | evidence/T-004.md |
| V-REG-003 | Offline/reliability | Repeat focused suite and bundle validation locally. | Deterministic identical results; no network use. | evidence/T-004.md |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/test_validate_human_visibility.py` | repository root, local Python | Focused tests PASS, including new positive/negative fixtures. | T-001–T-004 |
| `python scripts/validate_bundle.py` | repository root | Bundle contract PASS. | T-004,T-005 |
| `python scripts/validate_human_visibility.py --consumer-root testes --initiative specs/001-news-blog-auth --write-baseline` | repository root, synthetic consumer fixture | PASS only after full projection/evidence checks. | T-004 |
| `python scripts/validate_human_visibility.py --consumer-root testes --initiative specs/001-news-blog-auth` | repository root | Recheck PASS; baseline synchronized. | T-004,T-005 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Read one failure each for missing evidence/risk/route. | Source, missing token and target view are understandable without source-code debugging. | evidence/T-005.md |
| M-002 | Render the repaired fixture with JS disabled and normal viewport/print controls. | The existing brief contract remains usable; validation change did not alter fixture semantics. | evidence/T-005.md |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Does deterministic scope stay narrow and does guidance clearly preserve semantic/rendered review? | Validator diagnostics, template/guidance and repaired brief. | Approve only if no automated PASS is claimed as independent approval. | distinct semantic reviewer |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Browser E2E automation | Validator is local Python and DOM behavior is unchanged; manual rendered fixture review is proportionate. | Low residual visual regression risk. | semantic reviewer records M-002. |
| Mutation testing | Parser branches have explicit negative and compatibility fixtures; repository does not establish a mutation baseline. | Medium residual parser-gap risk. | validation maintainer records N/A rationale. |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Harness Planner / 2026-08-26  
**Blocking gaps:** U-001 bounds implementation grammar; final independent evaluation remains required.
