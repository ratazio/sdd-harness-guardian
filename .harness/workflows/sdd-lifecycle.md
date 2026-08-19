# Workflow: Common SDD Lifecycle

## Purpose

Define the mandatory gates shared by feature, bugfix and refactor workflows.
Specialized workflows may add requirements but may not skip these gates.

## Entry condition

An initiative exists under `specs/NNN-slug/` using the canonical templates and
is represented in `specs/INDEX.md`. Legacy `specs/<slug>/` initiatives must be
inventoried and normalized before new conflicting work is scaffolded.

## Lineage branch

Inspect the brief lineage before selecting the Human Visibility path. A
historical/pinned `data-harness-brief-design="v1"` brief retains the legacy
sequence: source artifacts ready → concise v1 brief → Human Visibility review
→ task breakdown → Tasks Ready → implementation. Do not require v2
`tasks_drafted`, `brief_coverage_ready`, provenance or coverage composition for
that path. A material v1 refresh follows the migration diagnostic and either
migrates to v2 or records a reviewed legacy exception.

The numbered flow and v2 rows below apply only to
`data-harness-brief-design="v2"`. The evidence, independent evaluation and
terminal task gates apply to both lineages unchanged.

## Flow

1. **Specify** — create/revise `spec.md`.
2. **Outcome Review** — confirm outcome, demonstrable increment, priority source
   or required human decision.
3. **Spec Review** — Spec Guardian records `Outcome Ready: yes/no` and
   `Spec Ready: yes/no`.
4. **Impact Map** — map non-trivial surfaces, unknowns and risk.
5. **Technical Plan** — define approach, architecture-readiness profile,
   decisions and rollback. Missing profile information blocks Plan Ready or
   creates a bounded discovery task.
6. **Validation Plan** — map every AC to checks and evidence.
7. **Preliminary Task Draft** — draft outcome-linked tasks before the final
   brief, label them as unauthorised, and set `tasks_drafted: true`. This is a
   discussion input, not `tasks_ready` and not an implementation permission.
8. **Coverage Composition** — inventory applicable sources and principal
   headings; record each disposition, locator, rendered target/reason and the
   planned provenance blocks in the existing plan or decision log.
9. **Independent Coverage Review** — a distinct reviewer compares the
   composition against source headings, reports gaps/contradictions/unknowns
   and records the review. Set `brief_coverage_ready: true` only with no
   unresolved blocking finding. A named human substitutes when no independent
   agent is available; author self-review does not qualify.
10. **Stakeholder Brief** — render/refresh the derived final brief from the
    corrected sources and composition plan. Run structural checks and the
    Spec Guardian's source/rendered-meaning review before declaring
    `human_visibility_ready`.
11. **Decision Meeting and Propagation** — append meeting decisions to
    `decision-log.md`, update every affected canonical source, re-run the
    applicable readiness/coverage checks and regenerate the brief. HTML is not
    an authoring record.
12. **Tasks Ready** — only after propagation and refreshed Human Visibility,
    the Orchestrator may set `tasks_ready` and transition one task to `ready`.
13. **Implementation** — Builder implements only that task.
14. **Evidence Draft** — Builder writes `evidence/<task-id>.md` and moves the
    task to `needs_evaluation`.
15. **Independent Evaluation** — distinct Evaluator returns `approve`,
    `request_revision`, `block` or `escalate_to_human`.
16. **Revision loop** — `request_revision` returns to the Builder; new evidence
    and evaluation are required.
17. **Evidence Gate** — on `approve`, State Keeper records the decision and
    changes `needs_evaluation -> approved -> done`.
18. **Initiative Validation** — after every task is `done`, confirm AC coverage,
    residual risks and `validation_done: true`.
19. **Ratchet** — record serious first-time or recurring preventable failures.
20. **Close/Handoff** — update progress, state, decisions and final handoff.

## Gate matrix

| Transition | Required evidence | Owner |
|---|---|---|
| draft → outcome_ready | outcome, demonstrable increment, priority source or human decision | Spec Guardian/Orchestrator |
| outcome_ready → spec_ready | Spec Guardian decision | Spec Guardian |
| spec_ready → plan_ready | impact + architecture-readiness profile + plan + rollback | Orchestrator |
| validation_ready → human_visibility_ready (v1) | synchronized concise v1 brief + Human Visibility review | Spec Guardian/Orchestrator |
| human_visibility_ready → tasks_ready (v1) | validation mapping + atomic tasks | Harness Planner/Orchestrator |
| validation_ready → tasks_drafted (v2) | preliminary tasks, outcome linkage, draft labels and no authorization | Harness Planner/Orchestrator |
| tasks_drafted → brief_coverage_ready (v2) | applicable-source composition + distinct coverage review record | Spec Guardian/Orchestrator |
| brief_coverage_ready → human_visibility_ready (v2) | corrected final brief, structural check and source/rendered review | Spec Guardian/Orchestrator |
| human_visibility_ready → tasks_ready (v2) | meeting decision propagation, refreshed coverage/freshness and atomic tasks | Orchestrator/State Keeper |
| ready → in_progress | readiness record with outcome linkage and `tasks_ready` | Builder/Orchestrator |
| in_progress → needs_evaluation | implementation + evidence draft | Builder |
| needs_evaluation → approved | independent `approve` | Evaluator |
| approved → done | approved `evidence/<task-id>.md` + state sync | State Keeper |
| all done → validation_done | all ACs covered, no blockers | Evaluator |

## Non-negotiable terminal rule

No workflow, local override or tool may set `done` from `in_progress` or
`needs_evaluation`. Missing evidence or evaluator means the task remains
non-terminal.

## Failure routes

- unclear intent or outcome → return to Specify or request human decision;
- missing architecture profile or source fact in v2 → return to Plan Ready or make a
  bounded discovery task;
- missing/stale coverage composition or review in v2 → return to Coverage Composition;
- missing/stale stakeholder brief → refresh the applicable lineage's Human Visibility before Tasks Ready;
- post-meeting source change → append/propagate decision and repeat affected
  coverage and Human Visibility checks;
- process-only task expansion without evidence → return to Outcome/Task
  Readiness;
- unknown/high impact → discovery or human review;
- missing validation → return to Validation Plan;
- oversized task → return to Task Breakdown;
- failed implementation/check → `needs_revision` or `blocked`;
- unsafe/destructive action → human approval gate;
- interruption → Interruption Recovery workflow;
- serious/recurring preventable failure → Ratchet workflow.
