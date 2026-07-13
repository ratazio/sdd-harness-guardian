# Spec: build-the-guardian

**Status:** spec_ready  
**Owner:** bundle maintainers  
**Created:** 2026-07-13  
**Last updated:** 2026-07-13  
**Risk:** medium

## 1. Problem

The initial source bundle has the right SDD concepts but leaves terminal gates,
copyable state, hard-mirror coverage and consumer installation partly implicit.
A second agent could not reliably execute the full lifecycle without inference.

## 2. Objective

Make version `0.1.0` a self-contained, vendor-neutral Git submodule bundle from
which a consumer agent can scaffold an initiative, execute SDD, preserve state
and produce independently evaluated evidence without external instructions.

## 3. Users or actors

- consumer coding agents;
- independent evaluator agents or humans;
- platform maintainers installing and versioning the bundle.

## 4. Observable outcomes

- O-001: every required artifact has a canonical copyable template.
- O-002: every workflow enforces evidence and evaluation before `done`.
- O-003: installation, update, rollback, resume and release are operational.
- O-004: deterministic source validation and safe scaffolding pass.

## 5. Non-goals

- NG-001: no SaaS, frontend or hosted service.
- NG-002: no workflow engine implementation.
- NG-003: no mandatory LangGraph, IDE, LLM provider or consumer-domain rule.
- NG-004: no consumer knowledge base inside skills or bundle memory.

## 6. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | The bundle SHALL define roles, rules, skills and workflows for the complete SDD lifecycle. | Executable governance |
| FR-002 | Workflows SHALL require `needs_evaluation -> approved -> done`. | Prevent false completion |
| FR-003 | Critical rules SHALL include soft and hard-mirror sections. | Layered enforcement |
| FR-004 | Templates SHALL scaffold the mandatory initiative state. | Safe consumption |
| FR-005 | Interruption and ratchet behavior SHALL be explicit. | Resumability and learning |

## 7. Acceptance criteria

| ID | Criterion | Validation |
|---|---|---|
| AC-001 | Manifest registry and version resolve to existing bundle components. | V-001 |
| AC-002 | Every critical rule contains soft rule, hard mirror and check name. | V-001 |
| AC-003 | Feature, bugfix and refactor contain evidence/evaluator terminal gates. | V-001 |
| AC-004 | A fresh feature and bugfix initiative can be scaffolded without overwrite. | V-002, V-003 |
| AC-005 | Run-state is direct YAML with evaluation, evidence, validation and resume fields. | V-001, V-004 |
| AC-006 | Installation and release docs cover pin, upgrade, rollback and consumer operation. | V-005 |
| AC-007 | Bundle remains engine/provider/IDE neutral and consumer state stays outside vendor. | V-005 |
| AC-008 | Final release checklist and source evidence are complete. | V-006 |

## 8. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Initiative target exists | scaffolder refuses overwrite |
| EC-002 | Evaluator unavailable | task remains `needs_evaluation` |
| EC-003 | Resume state conflicts with repository | recovery blocks and reconciles |
| EC-004 | High/unknown or destructive change | human review/approval gate |

## 9. Constraints and non-functional requirements

- Architecture: passive Git bundle; optional standard-library scripts only.
- Security/privacy: no secrets or consumer living knowledge.
- Compatibility: installable at `vendor/sdd-harness-guardian`.
- Operational: immutable version tags and explicit evidence.

## 10. Assumptions

| Assumption | Validation/owner |
|---|---|
| Consumer agents can read Markdown/YAML | documented contract |
| Git is present for submodule installation | INSTALL prerequisite |
| Python may be absent | manual copying remains supported |

## 11. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Duplicated contracts drift | medium | medium | manifest validator + canonical templates |
| R-002 | Docs claim readiness without independent review | medium | high | separate evaluator gate |
| R-003 | Scripts overwrite consumer state | low | high | slug restriction + existing-target refusal |

## 12. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Python 3 for optional checks | available locally | maintainer | no for consumers |
| Independent evaluator | pending | evaluator | yes for release |

## 13. Validation notes

Use standard-library validator, syntax checks and temporary consumer smoke tests.

## 14. Spec Guardian decision

**Spec Ready:** yes  
**Reviewer:** Codex / Spec Guardian role  
**Reviewed at:** 2026-07-13  
**Blocking issues:** none  
**Required revisions:** none  
**Decision evidence/link:** this section
