# Tasks: 002-sdd-harness-audit-process

**Status:** in_progress  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-07-25

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | needs_evaluation | Add SDD/harness audit capability | none | medium | codex-builder | unassigned | evidence/T-001.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires approved evidence, distinct identities and synchronized state.

### T-001 - Add SDD/harness audit capability

**Status:** needs_evaluation  
**Objective:** Add a reusable audit process and report contract to the bundle.  
**Requirement IDs:** FR-001, FR-002, FR-003, FR-004, FR-005  
**Acceptance criteria IDs:** AC-001, AC-002, AC-003, AC-004, AC-005, AC-006  
**Outcome served:** maintainers can run a deep SDD/harness audit.  
**Demonstrable increment or reduced uncertainty:** new registered audit skill,
workflow, agents, rule, template and knowledge framework.  
**Expected artifact/behavior:** bundle exposes a discoverable audit capability
and validates structurally.  
**Validation method:** V-001 through V-004.  
**Why now:** human requested audit process creation after spec numbering update.  
**Max subtasks before validation:** 3  
**Dependencies:** provided HTML knowledge sources  
**Risk:** medium  
**Builder:** codex-builder  
**Evaluator:** unassigned  
**Human approval:** not_required  
**Evidence:** evidence/T-001.md

#### Scope

- audit agents, rule, workflow, skill and HTML report template;
- docs framework and memory/reference updates;
- manifest, README, AGENTS and validator wiring.

#### Out of scope

- deterministic graph parser;
- hosted UI;
- consumer repository mutation.

#### Outcome linkage

- Requirement/AC/discovery question: all ACs.
- Vertical slice relation: delivers.
- Priority source or human decision: human request.

#### Expected files and contracts

See evidence pack for final file list.

#### Implementation constraints

Keep the bundle vendor-neutral and passive. Report is agent-authored from the
template; scripts may assist but not replace judgment.

#### Validation IDs and commands

- V-004: `python scripts/validate_bundle.py`
- V-004: `python scripts/smoke_test_scaffolder.py`

#### Evidence requirements

- structural validation output;
- smoke test output;
- summary of semantic checks;
- residual risk and evaluator requirement.

#### Exit criteria

- [x] outcome linkage, demonstrable increment and why-now rationale are recorded;
- [x] scoped implementation is complete;
- [x] required validation executed or approved exception recorded;
- [x] evidence draft covers ACs and exit criteria;
- [ ] distinct evaluator decided `approve`;
- [ ] evidence pack records decision and residual risk;
- [x] task, run-state and progress are synchronized.

#### Readiness decision

**Task Ready:** yes  
**Reviewed by:** codex / Orchestrator role  
**Blocking conditions:** none before evaluation.
