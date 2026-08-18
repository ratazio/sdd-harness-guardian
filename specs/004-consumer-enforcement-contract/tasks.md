# Tasks: 004-consumer-enforcement-contract

**Status:** complete  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-18

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Implement consumer Human Visibility validator and fixtures | plan, validation | medium | Terra 5.6 | Terra 5.6 independent | evidence/T-001.md |
| T-002 | done | Document consumer and Factory integration contract | T-001 | medium | Terra 5.6 | Terra 5.6 independent | evidence/T-002.md |
| T-003 | done | Run regression suite and assemble evidence | T-001, T-002 | low | Terra 5.6 | Terra 5.6 independent | evidence/T-003.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires approved evidence, distinct identities and synchronized state.

## T-001 — Implement consumer Human Visibility validator and fixtures

**Status:** done  
**Objective:** Add a stdlib-only CLI that verifies a consumer initiative's
structural, gate-state and freshness contract without claiming semantic review.  
**Requirement IDs:** FR-001, FR-002, FR-003, FR-004, FR-008  
**Acceptance criteria IDs:** AC-001, AC-002, AC-003, AC-004  
**Outcome served:** Non-trivial work cannot silently proceed with an invalid or stale brief.  
**Demonstrable increment or reduced uncertainty:** Valid and negative consumer fixtures prove CLI behavior and safe failure.  
**Validation method:** V-001, V-002, V-003, V-004, V-REG-001, V-REG-002.  
**Why now:** The portable command is the prerequisite for any consumer or Factory wiring.  
**Max subtasks before validation:** 3  
**Dependencies:** plan and validation plan ready  
**Risk:** medium  
**Builder:** Terra 5.6 implementation agent  
**Evaluator:** Terra 5.6 independent validation agent  
**Human approval:** approved — user authorized execution  
**Evidence:** evidence/T-001.md

#### Scope

CLI, template/state support when required, test fixtures and deterministic
diagnostics. Git base-ref plus hash-baseline fallback; reviewed exceptions only.

#### Out of scope

Factory code, CI-provider integration, LLM judging and screenshot checks.

#### Exit criteria

- [x] CLI and fixtures cover V-001 through V-004.
- [x] Exit codes and human-review limitation are observable.
- [x] Independent evaluator decided `approve`; see `evidence/T-001.md`.

## T-002 — Document consumer and Factory integration contract

**Status:** done  
**Objective:** Make the bundle's command invocable from a generic consumer and
unambiguous for future Factory generation.  
**Requirement IDs:** FR-005, FR-006, FR-007  
**Acceptance criteria IDs:** AC-005, AC-006, AC-007  
**Outcome served:** Correct adoption is generated and reviewable rather than implied.  
**Validation method:** V-005, V-006, V-007, M-001, M-002.  
**Why now:** The command contract must exist before writing its adoption guidance.  
**Dependencies:** T-001  
**Risk:** medium  
**Builder:** Terra 5.6 implementation agent  
**Evaluator:** Terra 5.6 independent validation agent  
**Human approval:** approved  
**Evidence:** evidence/T-002.md

#### Exit criteria

- [x] Guides contain an actual portable command and failure behavior.
- [x] Factory contract does not claim a real Factory integration was performed.
- [x] Independent evaluator decided `approve`; see `evidence/T-002.md`.

## T-003 — Run regression suite and assemble evidence

**Status:** done  
**Objective:** Prove the change preserves bundle/scaffolder behavior and leaves
reproducible evidence for independent approval.  
**Requirement IDs:** FR-001 through FR-008  
**Acceptance criteria IDs:** AC-008  
**Outcome served:** Consumers can adopt the contract without breaking the bundle.  
**Validation method:** V-008 and `git diff --check`.  
**Why now:** Terminal evidence must reflect the complete implementation.  
**Dependencies:** T-001, T-002  
**Risk:** low  
**Builder:** Terra 5.6 implementation agent  
**Evaluator:** Terra 5.6 independent validation agent  
**Human approval:** approved  
**Evidence:** evidence/T-003.md

#### Exit criteria

- [x] Regression commands pass.
- [x] Evidence documents commands, output and residual risks.
- [x] Independent evaluator decided `approve`; see `evidence/T-003.md`.
