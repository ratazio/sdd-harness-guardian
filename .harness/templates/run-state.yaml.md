# `run-state.yaml` contract

Copy `run-state.yaml`, not this document, into the initiative.

## Initiative status

`draft`, `outcome_ready`, `spec_ready`, `plan_ready`,
`validation_ready`, `tasks_drafted`, `brief_coverage_ready`,
`human_visibility_ready`, `tasks_ready`, `implementation_in_progress`,
`needs_evaluation`, `needs_revision`, `blocked`, `interrupted`,
`resumed`, `validation_done`, `closed`.

## Required invariants

- schema_version, initiative_id/sequence/slug present; ID matches directory/index;
- artifact paths resolve inside initiative;
- outcome_ready has outcome, increment and source priority/human decision;
- `brief_lineage` is v1/v2/v3 or null before HTML exists; BC-002 governs
  historical/pinned dispatch and explicit migration;
- brief_phase honestly describes source-only/preparation/rendered state
  (BC-001); explicit owner dispensation records its decision without fake render;
- non-trivial rendered briefs stay source-synchronized under their lineage;
- brief repair completion is separate from task/owner/evidence approval
  (BC-010/BC-018); no terminal task follows from a brief disposition;
- current_task agrees with tasks/ledger; evaluated builder != evaluator;
- evidence_pack_ready requires an approved existing evidence path;
- validation_done requires all tasks done and ACs covered;
- resume_required has checkpoint, work summary, handoff and next step;
- status/gate regressions have recorded reasons.

## Contract 3 repair record

`brief_repair` belongs in existing operational state, not an editorial
sidecar or permanent agent file. It records BC-009/BC-010/BC-025; legacy
`brief_review` approval fields do not apply to v3. Both passes record the
same actor distinct from author and executor-provided effective effort.

```yaml
brief_repair:
  contract: 3
  author: null
  status: incomplete
  source_snapshot: {}
  content:
    actor: null
    effective_effort: null
    execution_ref: null
    completed_at: null
    status: incomplete
  visual:
    actor: null
    effective_effort: null
    execution_ref: null
    completed_at: null
    status: incomplete
  rendered_sha256: null
  report: null
```

Statuses, for overall record and each pass: completed,
completed_with_source_limitations or incomplete. Incomplete cannot claim the
flow concluded. No browser to open every tab means visual status incomplete
(BC-016); unsupported specific file/preview/no-JS context is a stated limit,
never permission to invent inspection. Source/environment limits stay explicit;
source absence is
BC-015, not a license to invent facts. `execution_ref` points to verifiable
executor configuration/trace; prompt promises do not prove effort.
`source_snapshot` maps every read Markdown path to SHA-256, before/after
unchanged; include auxiliary MD only when read materially. Mutable
`run-state.yaml` is inspected for authority, separately from immutable MD
snapshot. Snapshot proves integrity/freshness, not meaning. Final
`rendered_sha256` binds completed HTML, required only at final conclusion,
not initial A materialization. `report` optionally locates existing
evidence/response; no new report file is mandatory.

Human Visibility readiness may follow actual concluded repair with honest
limits. `tasks_drafted`, `brief_coverage_ready` and independent approve
fields remain legacy, never v3 prerequisites or outcomes to fabricate.

## Historical contract 2 record

Keep `brief_review` and gates per BC-009: tasks_drafted is preliminary
unauthorised input; brief_coverage_ready requires distinct pass (a); Human
Visibility requires corrected render/pass (b); Tasks Ready requires decision
propagation/refreshed brief (BC-018). If quality_review_required is true,
the existing evidence record is nonempty, says exact approve, names a
reviewer distinct from author and binds rendered locator/digest. This checks
record integrity, not automatic prose quality. v1 may omit/leave false these
fields until explicit migration; v3 uses the separate repair record.

## Task ledger item

```yaml
- id: "T-001"
  status: "pending"
  builder_id: null
  evaluator_id: null
  evidence: "evidence/T-001.md"
  last_transition_at: null
```

Use block-item form for every evidence destination. A missing future pack may
be deferred at pending/ready/in_progress/blocked; at needs_evaluation/approved/
done it must exist. Deferral waives no containment or independent evidence
evaluation. Consumers may extend schema, never reduce protected invariants.
