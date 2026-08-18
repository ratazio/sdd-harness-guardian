# Validation Plan: 004-consumer-enforcement-contract

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-18

## 1. Strategy

Use isolated temporary consumer fixtures to prove each machine-detectable
contract and CLI exit behavior. Review documentation as an executable adoption
contract. Use an independent evaluator for semantic boundaries and the absence
of silent bypasses. No LLM judge or screenshot scoring is used.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | integration fixture | valid consumer + CLI | exit 0 | evidence/T-001.md | builder |
| V-002 | AC-002 | negative fixtures | omit each structural element | non-zero + precise diagnostic | evidence/T-001.md | builder |
| V-003 | AC-003 | Git/baseline fixtures | source-only change; approved exception | fail then controlled pass | evidence/T-001.md | builder |
| V-004 | AC-004 | output contract | inspect valid result | HUMAN REVIEW remains explicit | evidence/T-001.md | evaluator |
| V-005 | AC-005 | doc review | inspect INSTALL and consumer prompt | generic, invocable pattern | evidence/T-002.md | evaluator |
| V-006 | AC-006 | Factory-contract fixture/doc | inspect generated-contract fixture | vendor, bridge, command, invocation point represented | evidence/T-002.md | evaluator |
| V-007 | AC-007 | prompt review | inspect Factory guidance | blocks premature task/implementation | evidence/T-002.md | evaluator |
| V-008 | AC-008 | regression | `validate_bundle.py`, smoke, new tests | all pass | evidence/T-003.md | builder/evaluator |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | stdlib portability | run test suite on Windows Python | no third-party runtime dependency | evidence/T-003.md |
| V-REG-002 | safe diagnostics | inspect negative output | paths/IDs only, no source content | evidence/T-001.md |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_human_visibility.py --help` | bundle root | exit 0 | T-001 |
| test command added by implementation | bundle root | all consumer fixtures pass | T-001/T-003 |
| `python scripts/validate_bundle.py` | bundle root | exit 0 | T-003 |
| `python scripts/smoke_test_scaffolder.py` | bundle root | exit 0 | T-003 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Read CLI's successful output and docs. | It states that human semantic/rendered review remains required. | evidence/T-002.md |
| M-002 | Read Factory-oriented contract. | It requires bundle pin, root bridge, command and invocation point without claiming unavailable capabilities. | evidence/T-002.md |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | This plan and ACs | final diff/tests | every AC covered; no silent bypass or false claim of semantic approval | independent evaluator |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Real Agentic Factory generation | Factory is out of scope until this bundle change is delivered. | Contract only, not end-to-end Factory proof. | Human follow-up / Factory owner |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex acting as Harness Planner  
**Blocking gaps:** none for bundle implementation; Factory execution remains a declared follow-up.
