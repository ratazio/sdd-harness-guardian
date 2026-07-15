# `run-state.yaml` contract

Copy `run-state.yaml`, not this document, into the initiative.

## Allowed initiative status

```txt
draft
outcome_ready
spec_ready
plan_ready
validation_ready
human_visibility_ready
tasks_ready
implementation_in_progress
needs_evaluation
needs_revision
blocked
interrupted
resumed
validation_done
closed
```

## Required invariants

- `schema_version` and `initiative_id` are present;
- artifact paths resolve inside the initiative;
- `outcome_ready` requires declared outcome, demonstrable increment and
  priority source or human decision;
- non-trivial initiatives include `stakeholder-brief.html` synchronized with
  source artifacts;
- `current_task` matches the task ledger and `tasks.md`;
- `builder_id != evaluator_id` for an evaluated task;
- `evidence_pack_ready` requires an existing approved evidence path;
- `validation_done` requires all tasks `done` and all ACs covered;
- `resume_required` requires checkpoint, work summary, handoff and next step;
- status and quality gates never move backward without a recorded decision.

## Task ledger item

```yaml
- id: "T-001"
  status: "pending"
  builder_id: null
  evaluator_id: null
  evidence: "evidence/T-001.md"
  last_transition_at: null
```

Consumers may extend the schema, but protected fields and invariants remain.
