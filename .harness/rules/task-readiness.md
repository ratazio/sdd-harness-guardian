# Rule: Task Readiness

## Soft rule

Only a `ready` task may enter implementation. Tasks must be small, ordered,
bounded, outcome-linked and independently verifiable.

For v2 non-trivial work, preliminary task rows may exist under
`tasks_drafted`, but remain `pending` until the coverage review, final brief,
meeting decision propagation and `tasks_ready` gate are complete.

## Required contract

Each task declares ID, objective, requirement IDs, acceptance criteria IDs,
delivery outcome, demonstrable increment or reduced uncertainty, scope, out of
scope, dependencies, expected files/surfaces, expected artifact, risk, builder,
evaluator, validation method, evidence path, why-now rationale and exit
criteria. Dependencies must be `done` or explicitly waived with rationale.

A task should fit one focused session. If it cannot, split it or create a
discovery task with its own evidence.

## Blocking conditions

Block when the task:

- contains multiple independently releasable outcomes;
- is not traceable to a requirement, AC, plan step or explicit discovery
  question;
- cannot state its demonstrable increment, artifact or reduced uncertainty;
- exists only to expand process artifacts without new evidence or risk
  reduction;
- has unresolved dependency, risk `high`/`unknown` or human approval;
- lacks objective exit criteria or an evidence destination;
- expands beyond the approved spec/plan;
- has the same builder and evaluator identity.
- belongs to a v2 initiative without `tasks_ready`, even if it appears in the
  preliminary task draft.

## Hard mirror recommendation

Use a task contract validator and state-transition guard. Permit
`ready -> in_progress` only when required fields exist, dependencies are
terminal, outcome linkage is recorded and risk approvals are recorded.

Recommended check: `validate-task-readiness`.
