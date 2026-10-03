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

Dispatch Human Visibility through `brief-contract.md` BC-002. For v3 keep
repair records in existing state/evidence under BC-025 (see
`templates/run-state.yaml.md`); never encode own `approve` in legacy reviewer
fields. Source snapshots cover read-only Markdown separately from mutable
operational state. Historical v2 keeps model/reviews under BC-008/BC-009
with existing author/reviewer/reference fields. `tasks_drafted` and
`brief_coverage_ready` remain v2 gates, never terminal statuses or v3
prerequisites. BC-010 protects implementation authority.

## Session start order

1. `specs/INDEX.md`;
2. `run-state.yaml`;
3. `progress.md`;
4. `handoffs/latest-handoff.md`;
5. repository/working-tree status;
6. `tasks.md` and current evidence;
7. `validation-plan.md` and `decision-log.md`.

Reconcile discrepancies before changing files.

## Execution-authorization checkpoint

When a direct stakeholder instruction changes authorization from planning to
execution, append the decision and synchronize `run-state.yaml`, `progress.md`
and `handoffs/latest-handoff.md` before the first implementation artifact is
changed. Refresh the stakeholder brief under its lineage when that state is
material, honoring explicit owner dispensation. The v3 repair operation keeps
source inputs read-only (BC-001/BC-018). If work is discovered before that
checkpoint, stop, record
the divergence and move affected tasks to `needs_evaluation`; never infer a
terminal approval from the completed diff.

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
