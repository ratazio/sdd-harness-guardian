# Validation Plan: 006-stakeholder-brief-complete-decision-surface

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-19

## 1. Strategy

Use three complementary layers:

1. deterministic contract tests for versioning, source/heading inventory,
   coverage/provenance, state order, freshness, review identity and migration;
2. rendered accessibility/layout review at desktop, narrow and print/no-script;
3. role-based semantic evals for product, architecture and delivery recovery of
   the decision packet.

No structural pass may claim semantic, aesthetic or meeting approval. Existing
bundle/scaffolder/consumer suites are the regression floor.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | template/design contract inspection + render | Compare v1/v2 executive shell and enumerate eight progressive views. | v1 strengths retained; v2 views present and navigable. | evidence/T-002.md | design reviewer |
| V-002 | AC-002 | unit/integration fixtures | Inventory headings in applicable sources; compare DOM provenance and human coverage register. | Every principal heading has one valid disposition and rendered target. | evidence/T-001.md | Harness Planner |
| V-003 | AC-003 | negative validator fixtures | Remove tasks/decision source, heading mapping, provenance or review record one at a time. | Each fixture fails with one precise actionable diagnostic. | evidence/T-003.md | Evaluator |
| V-004 | AC-004 | workflow/state contract test + source inspection | Assert ordered states/transitions and unchanged terminal task gates. | Task draft precedes brief; Tasks Ready remains after decision propagation; implementation gate unchanged. | evidence/T-001.md | Delivery Orchestrator |
| V-005 | AC-005 | template/skill fixtures and rubrics | Evaluate S, M and L/high examples including missing-architecture behavior. | Proportional dimensions/views selected; missing facts block or become discovery, never invention. | evidence/T-001.md | architect reviewer |
| V-006 | AC-006 | cross-role semantic eval | Product, architect and delivery reviewers answer the rubric from rendered v2 HTML only. | Each recovers required decisions/details and evidence states without normal source lookup. | evidence/T-005.md | independent reviewers |
| V-007 | AC-007 | rendered/state inspection | Inspect task view and run-state before approval. | Draft label, dependencies/outcome/validation visible; Tasks Ready false. | evidence/T-002.md | Orchestrator |
| V-008 | AC-008 | change-baseline fixture | Change scope, AC, task and decision status; regenerate delta. | Material changes and supersession appear; freshness invalidates old brief. | evidence/T-003.md | State Keeper |
| V-009 | AC-009 | post-meeting workflow fixture | Apply a mock transcript decision through log/source/brief refresh. | No HTML-only decision; all affected sources and delta synchronize. | evidence/T-004.md | Spec Guardian |
| V-010 | AC-010 | compatibility fixtures | Validate historical v1, new v2 and material v1 refresh cases. | Historical v1 passes old contract; new scaffold is v2; refresh receives migration diagnostic. | evidence/T-003.md | bundle maintainer |
| V-011 | AC-011 | manual/rendered accessibility review | Desktop 1440px, narrow 390px, keyboard, JS-disabled and print/PDF inspection. | All content reachable/searchable/printable; no global overflow or color-only meaning. | evidence/T-005.md | accessibility reviewer |
| V-012 | AC-012 | full regression suite | Run required commands below. | Existing and new suites exit 0; negative fixtures fail as designed. | evidence/T-005.md | Evaluator |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | v1 compatibility / R-007 | Run historical v1 fixtures through version-aware validator. | No unplanned v1 failure. | T-003 pack |
| V-REG-002 | false authorization / R-004 | Attempt transition from task draft/brief review to implementation without human approval and Tasks Ready. | Blocked with precise state reason. | T-001/T-004 pack |
| V-REG-003 | readability / R-001 | Measure executive path separately; inspect progressive deep sections. | 60-second orientation remains possible without deleting deep content. | T-002/T-005 pack |
| V-REG-004 | hallucinated architecture / R-005 | Remove required architecture source detail from L fixture. | Plan/Human Visibility blocks; no generated diagram claim. | T-001 pack |
| V-REG-005 | accessibility / R-008 | Keyboard, no-script, narrow and print traversal of every view. | Equivalent content remains available. | T-005 pack |
| V-REG-006 | privacy / NG-008 | Scan fixtures/diagnostics for injected secret/PII sentinel. | Sentinel is redacted or rejected and never emitted to HTML diagnostic. | T-003 pack |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | bundle root; Python 3 | exit 0 | T-001–T-005 |
| `python scripts/test_validate_human_visibility.py` | bundle root; Python 3 | exit 0 with v1/v2 positive and negative cases | T-003–T-005 |
| `python scripts/smoke_test_scaffolder.py` | bundle root; Python 3 | exit 0; new scaffold emits coherent v2 package | T-004–T-005 |
| `python scripts/test_factory_guardian_fixture.py` | bundle root; Git + Python 3 | exit 0; consumer invocation remains reproducible | T-004–T-005 |
| `python scripts/validate_human_visibility.py --consumer-root . --initiative specs/006-stakeholder-brief-complete-decision-surface` | bundle root | exit 0 only after independent review is recorded and gate is ready | T-002–T-005 |

If implementation adds focused test files, list and run them in the relevant
task evidence before relying on the aggregate commands.

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Render populated v2 example at 1440×900 and 390×844. | Executive hierarchy remains strong; deep views do not cause global overflow. | `evidence/rendered/` referenced from T-005 |
| M-002 | Navigate all controls by keyboard with visible focus. | Every progressive view is reachable and state is announced/understandable. | T-005 evidence notes/screenshots |
| M-003 | Disable script and open/print the page. | Content remains readable/searchable and print exposes deep sections. | T-005 PDF/screenshots |
| M-004 | Ask product reviewer the decision/outcome/scope/change questions. | Correct answer from HTML only. | T-005 rubric |
| M-005 | Ask architect reviewer for boundaries, contracts/data/trust, failure/rollback, alternatives and unknowns. | Correct answer or explicit source-backed N/A/unknown from HTML only. | T-005 rubric |
| M-006 | Ask delivery reviewer for task sequence, dependencies, validation, evidence state and authorization. | Correct answer; drafts are not mistaken for ready work. | T-005 rubric |

## 6. Evals

Use evals only for meaning that deterministic checks cannot establish.

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Coverage fidelity: no material source claim missing, weakened, contradicted or unsupported. | Applicable sources + assembly plan + final HTML. | No blocker/high finding; all medium findings resolved or accepted with owner. | distinct coverage reviewer |
| E-002 | Architecture adequacy: depth matches profile and every node/edge/claim has source support. | Plan/impact + rendered diagrams/text equivalents. | Architect can explain boundaries, trade-offs and failure/rollback; no invented claim. | architect reviewer |
| E-003 | Meeting usability: executive orientation plus deep decision recovery for three audiences. | Final rendered HTML only. | Product, architecture and delivery rubric answers meet V-006. | named role reviewers |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Screenshot pixel-diff CI | Brittle and explicitly outside scope; rendered judgment remains human. | Visual regressions rely on manual/eval review. | accepted by spec NG-006; Evaluator confirms review artifacts |
| Automated prose/semantic approval | A machine check cannot prove meeting usefulness without false confidence. | Independent reviewers remain mandatory. | Spec Guardian |
| Cross-browser hosted farm | Bundle is offline and vendor-neutral; target local standards-compliant browser. | Browser-specific issue may escape. | accessibility reviewer records browser used |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex acting as Harness Planner  
**Blocking gaps:** none for planning. Execution remains blocked on explicit human
approval and assignment of independent Builder/Evaluator/reviewer identities.
