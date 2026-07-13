# Rule: Evidence Policy

## Soft rule

No task is complete without a task-specific evidence pack reviewed by an
independent evaluator.

## Evidence minimum

Each `evidence/<task-id>.md` records:

- task, initiative, date, builder and evaluator identities;
- commit SHA or working-tree state;
- summary and files changed;
- AC and exit-criteria coverage;
- exact commands/checks, exit codes and relevant output locations;
- manual artifacts when applicable;
- skipped checks with reason and impact;
- known gaps and residual risk;
- evaluator findings and final decision.

Evidence must be sufficient to reproduce or audit the decision. “Looks good”,
an uncited summary or a command name without result is not evidence.

## Blocking conditions

Block `approved` or `done` when the pack is missing/incomplete, its results
cannot be tied to the current change, an AC is unmapped, or evaluator review is
absent. Failed checks remain blocking unless the evaluator documents why they
are unrelated and accepts the residual risk.

## Hard mirror recommendation

Require `evidence/<task-id>.md`, validate its headings and AC IDs, and verify
`decision: approve` before allowing `approved -> done`. In CI, attach immutable
logs or checksums where practical.

Recommended check: `validate-evidence-before-done`.
