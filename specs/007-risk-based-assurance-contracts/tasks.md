# Tasks: 007-risk-based-assurance-contracts

**Status:** validation_done  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-25

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Decide profiles, compatibility and minimal deterministic core | D-003 | high | Codex / Builder-007 | Codex / Evaluator-007-T001 | evidence/T-001.md |
| T-002 | done | Add guidance-first assurance contracts to existing artifacts | T-001 | high | Codex / Builder-007-T002 | Codex / Evaluator-007-T002-reconciliation | evidence/T-002.md |
| T-003 | done | Build fictional 006 fixture, decision brief and focused mirrors | T-001, T-002 | high | Codex / Builder-007-T003 | Codex / Evaluator-007-T003 | evidence/T-003.md |
| T-004 | done | Integrate docs, consumer adoption and independent proof | T-003 | medium | Codex / Builder-007-T004 | Codex / Evaluator-007-T004 | evidence/T-004.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

T-001 is ready after D-003, coverage review and decision propagation. T-002–T-004
remain preliminary until their dependencies are terminal; ready never permits a
parallel bypass of this order.

## T-001 — Decide profiles, compatibility and minimal deterministic core

**Status:** done  
**Objective:** resolve the policy decisions that determine proportionality and
prevent over-enforcement before any template/script change.  
**Requirement IDs:** FR-001–004, FR-011–012  
**Acceptance criteria IDs:** AC-001, AC-008, AC-009  
**Outcome served:** the bundle has an approved, bounded assurance model.  
**Demonstrable increment:** decision record for A1/A2/A3 (or escalation
alternative), adoption boundary and candidate minimal-core register.  
**Validation method:** V-DEC-001 and `python scripts/validate_bundle.py`; fixture/compatibility proof remains T-003/T-004.  
**Why now:** all subsequent changes depend on these boundaries.  
**Max subtasks before validation:** 3  
**Dependencies:** D-003 human approval.  
**Risk:** high  
**Builder:** Codex / Builder-007  
**Evaluator:** Codex / Evaluator-007-T001 (independent agent)  
**Human approval:** approved by D-003  
**Evidence:** evidence/T-001.md

### Scope

- Decide profile names/triggers and A3 escalation semantics.
- Prove whether existing v2 can carry conditional fields without a new lineage.
- Classify every proposed hard mirror as approve/reject/defer with its cost and
  deletion/downgrade condition.

### Out of scope

- Template, script, docs or consumer changes.

### Expected files and contracts

Decision log, plan/impact unknown resolution, policy guidance draft and
compatibility fixture notes.

### Implementation constraints

No mirror may be accepted merely because a field is easy to parse. The decision
must identify the concrete unsafe failure that it prevents.

### Validation IDs and commands

V-DEC-001 and `python scripts/validate_bundle.py`. V-001/V-008/V-009 are
mapped to T-003/T-004 because they require the implemented fixture/mirror.

### Evidence requirements

Decision alternatives, explicit rejected complexity, compatibility result and
distinct evaluator decision.

### Exit criteria

- [ ] Q-001–Q-003 are resolved or the task remains blocked;
- [ ] profile and escalation ownership are recorded;
- [ ] each candidate mirror has necessity/cost/removal reasoning;
- [ ] no template or validator implementation occurs;
- [ ] distinct evaluator approves evidence.

## T-002 — Add guidance-first assurance contracts to existing artifacts

**Status:** done  
**Objective:** make risk, architecture delta and task proof choices visible in
existing sources before adding enforcement.  
**Requirement IDs:** FR-002–008, FR-011  
**Acceptance criteria IDs:** AC-001–005  
**Outcome served:** agents can construct a proportionate contract without a
separate system.  
**Demonstrable increment:** updated templates/rules/skills and a concise A1
example plus an elevated A2 example.  
**Validation method:** V-GUIDE-001 and `python scripts/validate_bundle.py`; AC fixture proof remains T-003.  
**Why now:** visibility and judgment must precede deterministic checks.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001.  
**Risk:** high  
**Builder:** Codex / Builder-007-T002  
**Evaluator:** Codex / Evaluator-007-T002 (independent agent)  
**Human approval:** approved by D-003  
**Evidence:** evidence/T-002.md

### Scope

- Add as-is/target/delta and envelope guidance to the plan.
- Separate impact/risk/control ledgers and add task assurance contract fields.
- Extend Planner/Evaluator guidance for risk-selected checks, UI evidence and
  failure/exception behavior.

### Out of scope

- New validator, external test tool, permanent agent or new artifact type.

### Implementation constraints

For every added field, define profile applicability and concise N/A behavior.
Tool names and test techniques remain consumer decisions.

### Validation IDs and commands

V-GUIDE-001 and `python scripts/validate_bundle.py`. T-003 owns V-001–V-005
because it first creates the fictional fixture those validations require.

### Evidence requirements

Before/after examples, A1/A2 review, selected/inapplicable test rationale and
independent evaluator finding log.

### Exit criteria

- [x] existing artifact classes are reused;
- [x] A1 remains lighter than A2;
- [x] risk/control and visual/behavior evidence are distinct;
- [x] no hard mirror is added;
- [x] distinct evaluator approves evidence.

## T-003 — Build fictional 006 fixture, decision brief and focused mirrors

**Status:** done  
**Objective:** prove the enriched contract in a realistic, labelled example and
enforce only the approved minimal core.  
**Requirement IDs:** FR-009–012, FR-014  
**Acceptance criteria IDs:** AC-002–008  
**Outcome served:** a reviewer sees assurance data without hidden complexity,
and unsafe stable omissions cannot close work.  
**Demonstrable increment:** fictional 006 derivative, rendered brief,
positive/negative fixtures and only approved validators.  
**Validation method:** V-002–008, V-REG-001–004, E-002–003.  
**Why now:** enforcement must follow a proven source/brief contract.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001, T-002.  
**Risk:** high  
**Builder:** Codex / Builder-007-T003  
**Evaluator:** Codex / Evaluator-007-T003 (independent agent)  
**Human approval:** pending  
**Evidence:** evidence/T-003.md

### Scope

- Derive, do not alter, a fictional 006-like fixture with clear provenance.
- Render progressive as-is/target/delta, envelope, individual tasks, risk
  ledger and proof states.
- Implement precise negative checks only for mirrors approved in T-001.

### Out of scope

- Broad content scoring, safety certification, screenshot pixel-diff CI or
  enforcement of technique choices.

### Implementation constraints

Each validator diagnostic must name a stable missing fact and must state that it
does not prove semantic adequacy. A source-rich brief cannot collapse material
ledgers into summary cards.

### Validation IDs and commands

V-002–008 and all focused/new plus bundle commands.

### Evidence requirements

Fixture provenance, desktop/narrow/print artifacts, negative outputs, mirror
register, reviewer rubrics and distinct evaluator decision.

### Exit criteria

- [ ] original 006 remains unchanged;
- [ ] every material task/risk is recoverable from the fixture brief;
- [ ] approved negative cases fail precisely;
- [ ] A1 control fixture remains concise;
- [ ] distinct evaluator approves evidence.

## T-004 — Integrate docs, consumer adoption and independent proof

**Status:** done  
**Objective:** make the method understandable and safely adoptable by consumer
agents without overclaiming compliance.  
**Requirement IDs:** FR-013–014  
**Acceptance criteria IDs:** AC-009–010  
**Outcome served:** consumers can invoke the Guardian with the right depth and
understand when local authority is required.  
**Demonstrable increment:** theory docs, adoption guidance, scaffold/consumer
compatibility proof and final independent assessment.  
**Validation method:** V-009–010, V-REG-005, M-001–004, E-001–003.  
**Why now:** documentation should describe the implemented, proven contract.  
**Max subtasks before validation:** 3  
**Dependencies:** T-003.  
**Risk:** medium  
**Builder:** Codex / Builder-007-T004  
**Evaluator:** Codex / Evaluator-007-T004 (independent agent)  
**Human approval:** pending  
**Evidence:** evidence/T-004.md

### Scope

- Add market-reference theory and explicit non-certifying scope.
- Update consumer prompts/guidance and adoption/migration explanation.
- Run compatibility, privacy and cross-role final reviews.

### Out of scope

- Publishing/release without separately recorded human authorization.

### Implementation constraints

Keep citations primary where practical. Consumer agents choose concrete tools;
the Guardian describes capabilities, decision factors and evidence.

### Validation IDs and commands

V-009–010, V-REG-005 and all applicable bundle/consumer commands.

### Evidence requirements

Doc source map, compatibility output, review rubrics, residual risks and
release recommendation.

### Exit criteria

- [ ] docs make no certification claim;
- [ ] adoption remains version-aware;
- [ ] all approved mirrors and regressions pass;
- [ ] residual risks/waivers are explicit;
- [ ] distinct evaluator approves evidence.
