# Initiative templates

Canonical templates for consumer-local initiatives. Never store consumer state
inside `vendor/sdd-harness-guardian`. Brief doctrine is
`.harness/rules/brief-contract.md` BC-001–BC-025.

## Target layout

```txt
specs/INDEX.md
specs/NNN-slug/
  spec.md
  impact-map.md
  plan.md
  validation-plan.md
  tasks.md
  run-state.yaml
  progress.md
  decision-log.md
  ratchet.md
  evidence/
  handoffs/latest-handoff.md
```

Sequence is identity/chronology, not priority; do not reuse numbers.
Bugfix also uses `reproduction.md`; task evidence copies `evidence-pack.md`
to `evidence/<task-id>.md`; ratchet entries use `ratchet-entry.md`.

## Safe scaffolding

From the consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py <initiative>
```

Use `--kind bugfix`; slug or explicit NNN-slug accepted. Existing targets,
reused numbers and duplicate slugs are refused. Output is source-only
`brief_phase: not_rendered`; no HTML/preview shell/brand asset or readiness
claim. Manual setup copies canonical sources, `run-state.yaml` (not
`run-state.yaml.md`), `handoff.md` to the handoff path and an empty evidence
directory. Replace source placeholders before source-authoring review.

## Contract 3 entrypoint — new generation

Read existing canonical sources, contract BC-002 and the three local skills:

1. A uses `executive-brief-composition` to fill the canonical HTML template
   under BC-008/BC-024.
2. B receives HTML/sources and executes `rendered-brief-decision-review`
   under BC-009/BC-025.
3. The same B executes `executive-brief-experience-review`; record the final
   report/disposition in existing evidence/state or the response.

The documented entrypoint is this skill chain, not a legacy projector call.
Operational state uses `brief_repair` in `run-state.yaml.md`; sources remain
read-only per BC-001/BC-015. Native executor configuration supplies effective
effort; BC-025 defines honest treatment of unsupported/medium execution.
Human Visibility disposition follows the actual record, never a fabricated
independent review or task approval (BC-010). No post-B command/reapproval
is required. Technical materialization may occur during the skills without
becoming another semantic stage.

## Historical 1/2 utilities

BC-002 dispatch preserves pinned bytes and recorded lineage. The v2 utilities
remain for explicit legacy work: `brief-model.yaml` schema,
`validate_brief_model.py`, `validate_source_sufficiency.py`,
`project_brief.py` and guarded promotion. v2 composition requires BC-009
pass (a), followed by its projector and pass (b); these do not gate v3.

Legacy promotion example, from consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/render_stakeholder_brief.py \
  specs/NNN-slug --candidate /absolute/path/to/reviewed-candidate.html
```

For this v2 command, use `brief_phase: ready_to_render` and
`brief_coverage_ready: true`. The review_record resolves to a named
decision-log section with distinct author/reviewer, approved composition,
`Composition provenance: verified`, exact candidate/manifest SHA-256 and
current source digests. Candidate binds `data-composition-review-record`,
`data-composition-provenance="pending"` (historical reviewed accepted) and
composed template identity. BC-005 legacy fragments bind source/visible fact.
`quality_review_required: true` records mandatory v2 pass (b); legacy
editorial exceptions follow BC-017. Scaffold relabeling is not composition.
Selected legacy Pearson assets retain the local hash/no-overwrite boundary
of BC-011; v3 single-file embedding follows BC-024 instead.

v1 retains its historical Human Visibility/task order. Meeting decisions and
explicit refreshes follow BC-018, never an HTML-only source of authority.

## Evidence destinations

Pending/ready/in_progress/blocked tasks may cite future packs in the block-item
`task_ledger`. At needs_evaluation/approved/done, cited evidence must exist;
mechanical PASS is not approval. Builder/evaluator remain distinct.

## Template change policy

Synchronize templates, rules, workflows and readers when protected fields
change. Before bundle release run `python scripts/validate_bundle.py`;
consumers pin a bundle tag. Template changes never silently migrate histories.
