# `run-state.yaml` contract

Copy `run-state.yaml`, not this document, into the initiative.

## Allowed initiative status

```txt
draft
outcome_ready
spec_ready
plan_ready
validation_ready
tasks_drafted
brief_coverage_ready
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

- `schema_version`, `initiative_id`, `initiative_sequence` and
  `initiative_slug` are present;
- `brief_lineage` is `v1`, `v2` or null before the brief exists; v1 historical
  or pinned initiatives retain legacy Human Visibility/task ordering until a
  material refresh migrates them or records a reviewed legacy exception;
- `initiative_id` matches `NNN-slug` and agrees with its directory and
  `specs/INDEX.md` row;
- artifact paths resolve inside the initiative;
- `outcome_ready` requires declared outcome, demonstrable increment and
  priority source or human decision;
- non-trivial initiatives include `stakeholder-brief.html` synchronized with
  source artifacts;
- `tasks_drafted` means preliminary tasks exist for the meeting and are visibly
  unauthorised; it never permits implementation;
- `brief_coverage_ready` requires the applicable-source composition and a
  distinct author/reviewer record in `brief_review`; a named human may replace
  an unavailable independent reviewer;
- `human_visibility_ready` for v2 requires the corrected render after coverage
  review; `tasks_ready` additionally requires post-meeting decision propagation,
  refreshed coverage/freshness and the regenerated brief;
- before changing `tasks_ready` for v2, record the meeting decision in
  `decision-log.md`, update every affected canonical source, rerun the
  applicable checks and regenerate the derived brief in that order;
- v1 historical initiatives may omit or leave false the v2 fields until material
  refresh or explicit migration; newly authored v2 initiatives must record them;
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
