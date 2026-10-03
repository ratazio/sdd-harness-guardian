# Workflow: Common SDD Lifecycle

## Purpose and entry

Mandatory gates for feature, bugfix and refactor. Initiative is under
`specs/NNN-slug/`, indexed in `specs/INDEX.md`; normalize conflicting
legacy unnumbered initiatives before scaffolding new work.

## Common source-authoring flow

1. **Specify** — create/revise spec; use `spec-depth-authoring` for
   conditional depth when available.
2. **Outcome Review** — outcome, demonstrable increment and priority source
   or human decision.
3. **Spec Review** — Guardian records Outcome Ready/Spec Ready.
4. **Impact Map** — affected surfaces, unknowns and risk.
5. **Technical Plan** — approach, architecture readiness, decisions, rollback;
   missing material information blocks Plan Ready or opens bounded discovery.
6. **Validation Plan** — every AC mapped to checks and evidence.
7. **Brief branch** — inspect `brief-contract.md` BC-002 and choose below.
8. **Tasks Ready** — source/owner authorization under BC-018, atomic tasks,
   validation/evidence; brief completion grants no execution permission.

## Brief branch

### Contract 3 — default for new generation

Use BC-008/BC-009: A runs `executive-brief-composition`; B runs
`rendered-brief-decision-review`, then the same B runs
`executive-brief-experience-review`; report BC-025 and end the brief
operation. The Orchestrator dispatches actor/effort under BC-010/BC-025.
No legacy model/coverage approval prerequisite applies. The record may support
Human Visibility readiness when completed, with visible source limitations;
it supplies no independent `approve` and no task/evidence authority.
Do not add another semantic gate between B and the report.
An explicit human dispensation is recorded as N/A with its decision, never
rendered/completed.

### Contract 2 — historical/pinned only

Preserve BC-009 historical flow: Preliminary Task Draft (unauthorised)
→ Coverage Composition/model → independent model/construction pass (a)
(`executive-brief-experience-review`) → projection
(`scripts/project_brief.py`) → rendered pass (b)
(`rendered-brief-decision-review`, BC-016) → meeting decision propagation
and refresh → Tasks Ready. Record `tasks_drafted`,
`brief_coverage_ready`, `human_visibility_ready` at their actual gates.
Relevant legacy re-review remains confined to this branch.

### Contract 1 — historical/pinned only

BC-002 preserves sources ready → concise brief → Human Visibility review
→ task breakdown → Tasks Ready. No 2/3 gates are imposed by an upgrade.
Refresh/migration follows explicit BC-002 disposition.

## Implementation flow — all lineages

1. Builder executes one ready task.
2. Builder writes `evidence/<task-id>.md`; task → `needs_evaluation`.
3. Distinct evaluator returns `approve`, `request_revision`, `block` or
   `escalate_to_human`. Revision returns to builder with updated evidence.
4. State Keeper records independent approval: `needs_evaluation -> approved
   -> done`, only with approved evidence and state synchronization.
5. When all tasks are done, validate all ACs and residual risks before
   `validation_done: true`.
6. Ratchet serious/recurring preventable failures; update progress/state/handoff.

Accepting implementation of the bundle/skills is independent task evaluation;
it never becomes a third validation in each contract-3 brief operation.

## Gate matrix

| Transition | Required evidence | Owner |
|---|---|---|
| draft → outcome_ready | outcome, increment, priority/decision | Guardian/Orchestrator |
| outcome_ready → spec_ready | spec decision | Guardian |
| spec_ready → plan_ready | impact, architecture profile, plan/rollback | Orchestrator |
| validation_ready → human_visibility_ready (v3) | concluded BC-009/BC-025 repair record and honest limits, without own approve | Orchestrator |
| validation_ready → tasks_drafted → brief_coverage_ready (v2) | draft labels, coverage/model and independent pass (a) | Orchestrator/reviewer |
| brief_coverage_ready → human_visibility_ready (v2) | final brief, technical checks, independent pass (b) | Orchestrator/reviewer |
| validation_ready → human_visibility_ready (v1) | synchronized concise brief and legacy review | Guardian/Orchestrator |
| human_visibility_ready → tasks_ready | applicable source/owner authority BC-018, atomic task contracts; v2 propagation/refresh | Orchestrator |
| ready → in_progress | readiness, outcome linkage and tasks_ready | Builder/Orchestrator |
| in_progress → needs_evaluation | implementation/evidence draft | Builder |
| needs_evaluation → approved | independent approve | Evaluator |
| approved → done | approved evidence/state sync | State Keeper |
| all done → validation_done | all ACs covered, no blockers | Evaluator |

## Failure routes

Unclear intent/outcome → Specify or human decision; missing source-authoring
architecture → Plan Ready/discovery; missing validation → Validation Plan;
oversized/process-only task → Task Readiness. v2 coverage/review failures
return to their historical gate. v3 repairs follow BC-015/BC-020/BC-025,
without rewriting sources or claiming medium effort as completion.
Post-meeting source changes follow BC-018. Unsafe/destructive operations
require human authorization; interruption uses recovery; serious/recurring
failure uses Ratchet.

## Non-negotiable terminal rule

Never set done directly from in_progress or needs_evaluation.
Missing evidence/evaluator leaves the task non-terminal.
