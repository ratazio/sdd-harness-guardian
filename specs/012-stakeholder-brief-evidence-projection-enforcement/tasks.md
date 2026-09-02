# Tasks: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** tasks_ready — T-001/T-002 done; T-003 needs_evaluation; T-004–T-005 remain pending  
**Spec / plan / validation:** ./spec.md / ./plan.md / ./validation-plan.md  
**Last updated:** 2026-08-26

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Inventory canonical grammar and regression fixtures | none | medium | spec012_t001_builder | spec012_t001_evaluator | evidence/T-001.md |
| T-002 | done | Enforce safe referenced-evidence existence | T-001 | high | spec012_t002_builder | spec012_t002_evaluator | evidence/T-002.md |
| T-003 | done | Enforce risk and API route projection | T-001,T-002 | high | spec012_t003_builder2 | spec012_t003_evaluator2 | evidence/T-003.md |
| T-004 | done | Synchronize templates, fixture and baseline checks | T-002,T-003 | medium | spec012_t004_builder2 | spec012_t004_evaluator2 | evidence/T-004.md |
| T-005 | done | Independent rendered-review and release validation | T-004 | medium | spec012_t005_release_builder | spec012_t005_evaluator | evidence/T-005.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires complete evidence, distinct builder/evaluator identities, approved decision and synchronized state. These rows are preliminary: no row may change from `pending` before v2 coverage review, refreshed brief and the post-meeting `tasks_ready` gate.

### T-001 — Inventory grammar and fixture matrix

**Status:** done  
**Objective:** Bound supported evidence, risk and HTTP source syntax before parser code exists.  
**Requirement IDs / AC IDs:** FR-003,FR-006 / AC-003,AC-005  
**Outcome and increment:** prevent speculative parser rules through a documented source inventory and synthetic complete, negative and compatibility fixtures.  
**Expected behavior:** U-001 resolved or explicitly narrowed; focused tests pass/fail by design.  
**Validation / why now:** V-003,V-005,V-REG-001; grammar is a prerequisite for a safe parser.  
**Dependencies / risk:** none / medium  
**Builder / evaluator:** validation builder / independent evaluator  
**Evidence:** evidence/T-001.md  
**Scope / out of scope:** source inventory and fixtures only / no validator behavior change.  
**A2 assurance:** record grammar, oracle, false-positive control and evaluator result.  
**Exit criteria:** source forms, fixture outcomes and U-001 decision are in evidence.

**Evaluation decision:** approved by `spec012_t001_evaluator` on 2026-08-27; D-009 and evidence/T-001.md record the distinct decision.

### T-002 — Enforce safe evidence references

**Status:** done  
**Objective:** Add in-initiative evidence validation before baseline acceptance.  
**Requirement IDs / AC IDs:** FR-001,FR-004 / AC-001,AC-006  
**Outcome and increment:** cited planning proof cannot be absent or escape the selected root.  
**Expected behavior:** missing/unsafe locator is non-zero and names its source path.  
**Validation / why now:** V-001,V-006; this establishes the pre-baseline failure discipline.  
**Dependencies / risk:** T-001 / high  
**Builder / evaluator:** spec012_t002_builder / security evaluator  
**Evidence:** evidence/T-002.md  
**Scope / out of scope:** existing validator, tests and synthetic fixtures / anchor-content and arbitrary-link validation.  
**A2 assurance:** test absolute/traversal containment with independent security evaluation.  
**Exit criteria:** contained resolver, diagnostic tests and approved evidence.

**Builder handoff:** the evaluator's `./evidence/...` bypass is repaired and regression-tested in `evidence/T-002.md`; await a fresh distinct security evaluation. No risk/API projection was changed.

### T-003 — Enforce risk and API projection

**Status:** done  
**Objective:** Require every material source risk and canonical method/path in its proper v2 brief view.  
**Requirement IDs / AC IDs:** FR-002,FR-003,FR-004 / AC-002,AC-003,AC-005  
**Outcome and increment:** green brief includes every declared risk and route.  
**Expected behavior:** missing IR or route causes non-zero before baseline with exact diagnostics.  
**Validation / why now:** V-002,V-003,V-005,V-REG-001; directly remedies audited omissions.  
**Dependencies / risk:** T-001,T-002 / high  
**Builder / evaluator:** validation builder / independent evaluator  
**Evidence:** evidence/T-003.md  
**Scope / out of scope:** v2 risk table and method/path projection / quality score or mandatory API matrix where absent.  
**A2 assurance:** positive, negative, legacy and no-contract controls.  
**Exit criteria:** all controls evidenced and a distinct evaluator approves.

**Builder handoff:** implementation is complete and the evidence pack records
the narrow parser, exact diagnostics and regression results. A distinct
evaluator must now inspect false-positive boundaries, panel scoping and v1/no-
inventory compatibility; the builder cannot approve this task.

### T-004 — Synchronize guidance, fixture and baseline

**Status:** done  
**Objective:** Align templates/guidance and repaired fixture with the strengthened contract.  
**Requirement IDs / AC IDs:** FR-005,FR-006 / AC-004,AC-005,AC-007  
**Outcome and increment:** authors/reviewers use the new boundary without ambiguity.  
**Expected behavior:** no stale source implies a deterministic PASS is human approval.  
**Validation / why now:** V-004,V-005,V-REG-002,V-REG-003; code cannot release until guidance and fixture agree.  
**Dependencies / risk:** T-002,T-003 / medium  
**Builder / evaluator:** fixture builder / independent evaluator  
**Evidence:** evidence/T-004.md  
**Scope / out of scope:** bundle templates, tests/fixtures and commands / consumer implementation or broad brief redesign.  
**A2 assurance:** bundle plus baseline write/recheck proof.  
**Exit criteria:** required commands pass and baseline synchronization is recorded.

**Builder handoff:** canonical block-form task-ledger guidance, the repaired
planning fixture, complete normal-and-baseline lifecycle matrix, bundle and
baseline/recheck proof are in `evidence/T-004.md`. A distinct evaluator must verify that exactly
`pending`, `ready`, `in_progress` and `blocked` defer a missing destination;
that `needs_evaluation`, `approved` and `done` require it; and that guidance
retains the T-002 containment boundary.

**Evaluation decision:** approved by `spec012_t004_evaluator2` on 2026-08-27.
The evaluator verified all seven states in normal and baseline modes, retained
path containment and the independent semantic-review boundary; D-017 records
the distinct approval.

### T-005 — Independent release review

**Status:** needs_evaluation  
**Objective:** Independently assess diagnostics, rendered-review boundary and release proof.  
**Requirement IDs / AC IDs:** FR-005,FR-006 / AC-004,AC-005,AC-007  
**Outcome and increment:** a release claim is evidence-backed rather than self-approved.  
**Expected behavior:** a distinct evaluator records approve or needs-revision with residual risks.  
**Validation / why now:** V-007,M-001,M-002; final evaluator gate.  
**Dependencies / risk:** T-004 / medium  
**Builder / evaluator:** spec012_t005_release_builder / semantic evaluator  
**Evidence:** evidence/T-005.md  
**Scope / out of scope:** read-only evaluation and evidence decision / fixing during evaluation.  
**A2 assurance:** independent semantic/rendered review.  
**Exit criteria:** decision, residual risks, command results and state synchronization are recorded.

**Builder handoff:** Release commands, both existing baseline/rechecks and a second, no-route/no-formal-risk synthetic fixture baseline/recheck passed. Static review confirms v2 panels, provenance/coverage, no-script fallback, keyboard tabs and print behavior are present. The builder recorded no approval; a distinct semantic evaluator must decide whether the rendered briefs are decision-useful.
