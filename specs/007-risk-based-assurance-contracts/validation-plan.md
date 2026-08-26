# Assurance & Validation Plan: 007-risk-based-assurance-contracts

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-20

## 1. Strategy

Validate the method itself in three layers:

1. source/fixture inspection for proportionality, risk distinction and complete
   task assurance contracts;
2. focused deterministic negative tests only for approved stable invariants;
3. independent human/agent review of usability, semantic honesty and whether
   the A1 path remains light enough.

The test suite must reject missing links or unsafe state, but it must not claim
that a populated field proves a correct test strategy, architecture or safety
case.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | source/fixture architecture review | Review high-risk fictional fixture against existing artifact layout. | Profile, delta and envelope exist without a sidecar/database. | evidence/T-003.md | architect reviewer |
| V-002 | AC-002 | semantic/source-to-brief review | Recover impact, risks and controls independently from sources and brief. | Distinct concepts and material risk fields remain visible. | evidence/T-003.md | risk reviewer |
| V-003 | AC-003 | task contract inspection + negative fixture | Remove oracle/evidence/evaluator/failure path one at a time. | Review or approved stable mirror blocks with precise gap. | evidence/T-003.md | Harness Planner |
| V-004 | AC-004 | risk-based strategy review | Compare logic/API/UI/non-UI fixtures and selected/inapplicable techniques. | Selection has rationale; no universal taxonomy or metric. | evidence/T-003.md | QA strategist |
| V-005 | AC-005 | UI/non-UI fixture review | Verify required UI evidence has visual plus behavior proof; inspect non-UI fixture. | No screenshot-only proof; no irrelevant UI overhead. | evidence/T-003.md | accessibility reviewer |
| V-006 | AC-006 | state/evidence negative fixtures | Simulate blocking failure and incomplete waiver. | `done` is blocked until revision or accountable exception. | evidence/T-003.md | Evaluator |
| V-007 | AC-007 | rendered cross-role eval | Product, architecture and delivery readers answer from brief alone. | Individual task assurance, delta/envelope and risks are recoverable. | evidence/T-003.md | distinct reviewers |
| V-008 | AC-008 | mirror decision audit | Inspect every proposed mirror against its justification and fixture. | Unjustified/semantic mirrors are rejected; approved mirrors have focused tests. | evidence/T-003.md | independent evaluator |
| V-009 | AC-009 | compatibility regression | Run v1/v2, scaffold and consumer fixtures as applicable. | No unintended legacy failure; adoption path is explicit. | evidence/T-004.md | bundle maintainer |
| V-010 | AC-010 | documentation source review | Check theory docs against primary references and wording boundaries. | Accurate citations; no compliance/certification claim. | evidence/T-004.md | docs reviewer |
| V-GUIDE-001 | T-002 increment | source/template review | Inspect updated templates, rules and skills against D-004/D-007/D-008. | Existing artifacts carry guidance; A1 remains concise; no hard mirror exists. | evidence/T-002.md | independent evaluator |
| V-DEC-001 | T-001 decision slice | decision/state audit | Inspect D-004–D-013, task lifecycle and changed-file boundary. | Policy is bounded, state is coherent, and no fixture/validator proof is claimed early. | evidence/T-001.md | independent evaluator |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | R-001 process bloat | Ask a reviewer to plan a simple local task using A1. | No added sidecar, specialist or irrelevant test demand. | T-003 review |
| V-REG-002 | R-002 brittle enforcement | Count and justify every new mirror and run its negative case. | No mirror encodes semantic completeness. | T-003 audit |
| V-REG-003 | R-004 provenance | Inspect fictional fixture labels and original 006 hashes/paths. | Original remains unchanged and fixture is unmistakably fictional. | T-003 evidence |
| V-REG-004 | R-006 readability/a11y | Desktop, narrow, no-script, print and keyboard review. | Progressive content remains reachable and readable. | T-003 render evidence |
| V-REG-005 | R-007 sensitive disclosure | Scan fixture/diagnostics with safe sentinel. | Sentinel is rejected/redacted. | T-004 output |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | bundle root, Python 3 | exit 0 after every implementation slice | T-001–T-004 |
| Existing brief/validator fixture commands | bundle root, Python 3 | v1/v2 compatibility behavior stays expected | T-003–T-004 |
| Focused new fixture command(s) | bundle root, Python 3 | positive case passes; each approved negative case fails precisely | T-002–T-004 |

Exact command names are deliberately deferred until T-003. The plan rejects a
new validator merely to make the matrix look complete.

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Review A1 planning against a local/reversible fixture. | Process remains concise and intelligible. | T-003 rubric |
| M-002 | Review A2 fixture from architecture, QA and stakeholder perspectives. | Delta, envelope, risks, task proof and uncertainty are recoverable. | T-003 rubric |
| M-003 | Render fictional 006 derivative desktop/narrow/no-script/print. | Deep ledgers remain accessible; executive path remains useful. | T-003 rendered artifacts |
| M-004 | Review proposed A3 escalation wording. | It directs to local/sectoral authority and makes no certification claim. | T-004 review |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Proportionality: is a test/profile choice justified by risk rather than checklist habit? | A1/A2/A3 fixtures and sources. | No material unnecessary requirement; all material omissions explained. | independent QA/architect reviewer |
| E-002 | Fidelity: does the brief retain material risk, delta and task contract data? | Sources plus rendered brief. | No blocker/high loss, weakening or unsupported claim. | distinct coverage reviewer |
| E-003 | Minimal-core audit: is every mirror stable, necessary and maintainable? | Rules, scripts and negative fixtures. | Every mirror passes its justification; otherwise remains soft guidance. | Evaluator |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Universal mutation/BDD/coverage benchmark | Explicitly inappropriate across all stacks/tasks. | Selection quality relies on task rationale/review. | Harness Planner |
| Automated semantic approval | Metadata cannot prove strategy adequacy or safety. | Independent review remains required. | Spec Guardian |
| Regulatory certification audit | Depends on consumer domain and authority. | A3 must escalate locally. | accountable human |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex acting as Harness Planner; human implementation authority D-003  
**Blocking gaps:** T-001 owns the detailed profile/compatibility/mirror choices;
they are planned discovery decisions, not a blocker to starting T-001.
