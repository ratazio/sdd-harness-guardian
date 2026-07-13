# Rule: State and Memory

## Soft rule

Long-running work must be safely resumable from project-local artifacts. Do not
store consumer execution state inside the vendored bundle.

## Required artifacts

```txt
specs/<initiative>/
  run-state.yaml
  progress.md
  tasks.md
  validation-plan.md
  decision-log.md
  evidence/
  handoffs/latest-handoff.md
```

## Session start order

1. `run-state.yaml`;
2. `progress.md`;
3. `handoffs/latest-handoff.md`;
4. repository/working-tree status;
5. `tasks.md` and current evidence;
6. `validation-plan.md` and `decision-log.md`.

Reconcile discrepancies before changing files.

## Session end requirements

Record current phase/task, task ledger, last safe checkpoint, work since that
checkpoint, files changed, validations/evidence, blockers, approvals, risks,
next safe step and exact resume instructions. Set `interrupted: true` and
`resume_required: true` when work is partial.

## Blocking conditions

Block continuation when state is missing, contradictory, stale relative to the
working tree or lacks a safe next step. Resolve through inspection, a discovery
task, rollback plan or human decision.

## Hard mirror recommendation

Validate `run-state.yaml` against a schema, enforce allowed status transitions,
and add a session-close check requiring progress/handoff timestamps and a
checkpoint whenever `resume_required == true`.

Recommended check: `validate-resumable-state`.
