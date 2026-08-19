# Tasks: <initiative>

**Status:** draft | tasks_ready | in_progress | complete  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:**

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | pending | | none | low | unassigned | unassigned | evidence/T-001.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires approved evidence, distinct identities and synchronized state.
`tasks_drafted` may contain the same task rows for meeting discussion, but they
remain `pending` until the post-meeting `tasks_ready` gate permits `ready`.

## Task template

### T-XXX — <title>

**Status:** pending  
**Objective:**  
**Requirement IDs:** FR-... | not_applicable  
**Acceptance criteria IDs:** AC-... | not_applicable  
**Outcome served:**  
**Demonstrable increment or reduced uncertainty:**  
**Expected artifact/behavior:**  
**Validation method:**  
**Why now:**  
**Max subtasks before validation:** 3  
**Dependencies:**  
**Risk:** low | medium | high | unknown  
**Builder:** unassigned  
**Evaluator:** unassigned  
**Human approval:** not_required | pending | approved  
**Evidence:** evidence/T-XXX.md

#### Scope

#### Out of scope

#### Outcome linkage

- Requirement/AC/discovery question:
- Vertical slice relation: delivers | directly enables | bounded discovery
- Priority source or human decision:

#### Expected files and contracts

#### Implementation constraints

#### Validation IDs and commands

#### Evidence requirements

#### Exit criteria

- [ ] outcome linkage, demonstrable increment and why-now rationale are recorded;
- [ ] scoped implementation is complete;
- [ ] required validation executed or approved exception recorded;
- [ ] evidence draft covers ACs and exit criteria;
- [ ] distinct evaluator decided `approve`;
- [ ] evidence pack records decision and residual risk;
- [ ] task, run-state and progress are synchronized.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:**  
**Blocking conditions:**
