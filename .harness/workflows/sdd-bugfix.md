# Workflow: SDD Bugfix

## Entry condition

A defect exists and must be corrected without uncontrolled scope expansion.

## Additional required artifact

`reproduction.md` records observed behavior, expected behavior, environment,
minimal steps and baseline evidence. If reproduction is impossible, record
attempts, uncertainty and an evidence-producing discovery task.

## Flow

1. Write/review `spec.md` and `reproduction.md`.
2. Capture a failing regression check or justified baseline evidence.
3. Select `brief-contract.md` BC-002 lineage and the Common SDD Lifecycle
   brief branch. Contract 3 uses BC-009 repairs; historical v1/v2 retain
   their own gates. Impact/source-authoring/owner readiness remains required
   for non-trivial work; brief completion does not grant task authority.
4. Implement the smallest ready fix task.
5. Execute the regression check plus mapped validations.
6. Draft `evidence/<task-id>.md` and set `needs_evaluation`.
7. A distinct Evaluator verifies reproduction, fix scope, regressions and pack.
8. Only after `approve`, State Keeper sets `approved -> done`.
9. Complete initiative validation and update ratchet when the defect reveals a
   serious or recurring preventable pattern.

## Constraints

- do not broaden refactoring unless required and approved;
- do not change public behavior outside the expected behavior;
- do not close on disappearance of symptoms alone;
- do not mark `done` without regression evidence and independent evaluation.

## Exit condition

Original reproduction no longer fails for the stated reason, regression check
passes, adjacent behavior is covered proportionally to risk, evidence is
approved and all Common Lifecycle terminal gates are satisfied.
