# Fictional 006-derived task contract

## Assurance contract

**Objective/AC:** AC-003, AC-005 and AC-006 — make material UI proof and failure handling recoverable.
**Level/environment/data:** A2 / local static fixture / synthetic public-safe data.
**Entry criteria:** profile, rationale and source pointer are present; no unresolved trust/data change.
**Exit criteria:** behavior and visual evidence are linked; independent evaluator approves; incomplete waiver blocks closure.
**Conditional specialist:** accessibility reviewer for keyboard or contrast failure.

| Claim/risk | Technique and rationale | Oracle/evidence | Executor/evaluator | Failure path |
|---|---|---|---|---|
| Material brief UI remains decision-useful | UI behavior steps plus screenshot; screenshot alone is insufficient | keyboard steps, visible risk/task ledger and screenshot | Builder + independent evaluator | return to revision; no waiver without accountable human and expiry |

## Failure and waiver fixtures

| Case | Required data | Expected state |
|---|---|---|
| Missing oracle/evaluator/failure path | task contract fields | incomplete contract; evaluator requests revision |
| Waiver request | named human, reason, residual risk, compensating control, scope, expiry | missing field blocks `done` |

## Risk ledger

| Event | Trigger | Likelihood | Impact | Early signal | Mitigation | Contingency/rollback | Owner | Validation link |
|---|---|---|---|---|---|---|---|---|
| Brief hides a material task | task row omitted during synthesis | medium | high | task cannot be recovered from brief | source-to-brief recovery review | correct source and brief; repeat review | Spec Guardian | V-002 source-to-brief review |
| Waiver closes failed task | waiver lacks accountable fields | low | high | any required field is missing | evidence contract requires all six fields | block done; return to revision | Evaluator | V-006 waiver negative fixture |
