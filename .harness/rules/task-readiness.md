# Rule: Task Readiness

## Soft rule

Only a `ready` task may enter implementation. Tasks must be small, ordered,
bounded and independently verifiable.

## Required contract

Each task declares ID, objective, scope, out of scope, dependencies, expected
files/surfaces, risk, builder, evaluator, validation, evidence path and exit
criteria. Dependencies must be `done` or explicitly waived with rationale.

A task should fit one focused session. If it cannot, split it or create a
discovery task with its own evidence.

## Blocking conditions

Block when the task:

- contains multiple independently releasable outcomes;
- has unresolved dependency, risk `high`/`unknown` or human approval;
- lacks objective exit criteria or an evidence destination;
- expands beyond the approved spec/plan;
- has the same builder and evaluator identity.

## Hard mirror recommendation

Use a task contract validator and state-transition guard. Permit
`ready -> in_progress` only when required fields exist, dependencies are
terminal and risk approvals are recorded.

Recommended check: `validate-task-readiness`.
