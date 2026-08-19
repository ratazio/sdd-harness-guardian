# Rule: State and Memory

## Soft rule

Long-running work must be safely resumable from project-local artifacts. Do not
store consumer execution state inside the vendored bundle.

## Required artifacts

```txt
specs/INDEX.md
specs/NNN-slug/
  run-state.yaml
  progress.md
  tasks.md
  validation-plan.md
  decision-log.md
  evidence/
  handoffs/latest-handoff.md
```

For v2 Human Visibility, keep the coverage composition in the existing plan,
the independent review record in the existing decision log, and the
author/reviewer/reference fields in `run-state.yaml`. Do not add a coverage
sidecar, permanent agent state or duplicate JSON index. `tasks_drafted` and
`brief_coverage_ready` are explicit quality gates; they are not task terminal
statuses and do not permit implementation.

## Session start order

1. `specs/INDEX.md`;
2. `run-state.yaml`;
3. `progress.md`;
4. `handoffs/latest-handoff.md`;
5. repository/working-tree status;
6. `tasks.md` and current evidence;
7. `validation-plan.md` and `decision-log.md`.

Reconcile discrepancies before changing files.

Use the index and state files as the compact context boundary. Read full specs,
plans, evidence packs or semantically retrieved documents only when they are
needed for the active gate or decision.

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
