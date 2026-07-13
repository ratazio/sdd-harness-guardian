# Tasks: build-the-guardian

**Status:** complete  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-07-13

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Harden governance contracts | none | medium | codex-root | codex-independent-evaluator-2 | evidence/T-001.md |
| T-002 | done | Make templates and tooling operational | T-001 — sequencing waived by D-005 | medium | codex-root | codex-independent-evaluator-2 | evidence/T-002.md |
| T-003 | done | Complete installation and architecture docs | T-001/T-002 — sequencing waived by D-005 | low | codex-root | codex-independent-evaluator-2 | evidence/T-003.md |
| T-004 | done | Validate and close release checklist | T-001/T-002/T-003 — sequencing waived by D-005 | medium | codex-root | codex-independent-evaluator-2 | evidence/T-004.md |

## Task contracts

### T-001 — Harden governance contracts

Scope: manifest, entrypoint, agents, rules, skills and workflows.  
Exit: registries resolve; critical rules have mirrors; terminal gates are
explicit; builder/evaluator separation has no self-approval path.

### T-002 — Make templates and tooling operational

Scope: all required templates, direct run-state, scaffolder and validator.  
Exit: feature/bugfix scaffold succeeds, duplicate refuses, scripts parse,
consumer state remains outside bundle.

### T-003 — Complete installation and architecture docs

Scope: README, INSTALL, docs, prompts, changelog and bundle progress.  
Exit: install/pin/clone/update/rollback/release/resume paths are documented and
vendor/provider/engine neutrality is explicit.

### T-004 — Validate and close release checklist

Scope: run all checks, capture evidence, obtain evaluator review and update
state/checklist.  
Exit: validator passes, evidence packs are complete, evaluator approves or
findings are resolved, checklist reflects verified truth.

## Readiness decision

**Tasks Ready:** yes  
**Reviewed by:** Codex / Delivery Orchestrator role  
**Blocking conditions:** none. Cycle 2 approved and State Keeper applied
`needs_evaluation -> approved -> done` in T-001, T-002, T-003, T-004 order.

## Bootstrap dependency waiver

Decision `D-005` records that T-001–T-004 were implemented as one integrated
initial-release slice before a distinct evaluator was available. The waiver
applies only to implementation sequencing for this source bootstrap; it does
not waive evidence, independent evaluation or terminal ordering. No task was
marked `approved` or `done`. A fresh evaluator must review the full slice, and
State Keeper must close T-001, T-002, T-003, then T-004 in that order.
