# Workflow: SDD Refactor

## Entry condition

Structure should improve while externally observable behavior remains unchanged.

## Required spec statement

```txt
External behavior must remain unchanged.
```

The spec identifies the behavior baseline, structural objective and explicit
non-goals. Behavior change requires a feature/bugfix spec instead.

## Flow

1. Capture regression baseline before modification.
2. Execute Common SDD Lifecycle gates 1–6.
3. Split work into small reversible tasks.
4. Implement one task and rerun the relevant baseline.
5. Draft `evidence/<task-id>.md` and set `needs_evaluation`.
6. A distinct Evaluator compares baseline, contracts, diff and evidence.
7. On revision, return to Builder; on `approve`, State Keeper records
   `approved -> done`.
8. Repeat per task, then execute initiative-level validation and close/handoff.

## Blocking conditions

Block when there is no credible regression baseline, behavior changes are
hidden in refactor, affected contracts are unknown, rollback is absent or
evidence/evaluator is missing.

## Exit condition

Structural objective is met, external behavior remains unchanged by mapped
checks, every task has approved evidence, all tasks are `done` and
`validation_done: true`.
