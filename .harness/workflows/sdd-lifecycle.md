# Workflow: Common SDD Lifecycle

## Purpose

Define the mandatory gates shared by feature, bugfix and refactor workflows.
Specialized workflows may add requirements but may not skip these gates.

## Entry condition

An initiative exists under `specs/<initiative>/` using the canonical templates.

## Flow

1. **Specify** — create/revise `spec.md`.
2. **Outcome Review** — confirm outcome, demonstrable increment, priority source
   or required human decision.
3. **Spec Review** — Spec Guardian records `Outcome Ready: yes/no` and
   `Spec Ready: yes/no`.
4. **Impact Map** — map non-trivial surfaces, unknowns and risk.
5. **Technical Plan** — define approach, decisions and rollback.
6. **Validation Plan** — map every AC to checks and evidence.
7. **Stakeholder Brief** — update `stakeholder-brief.html` as a concise,
   human-readable summary of outcome, scope, impact, validation, risks and next
   safe step.
8. **Task Breakdown** — create atomic, outcome-linked tasks with exit/evidence
   criteria.
9. **Readiness Gate** — verify outcome linkage, dependencies, risk and approvals
   for one task.
10. **Implementation** — Builder implements only that task.
11. **Evidence Draft** — Builder writes `evidence/<task-id>.md` and moves the
   task to `needs_evaluation`.
12. **Independent Evaluation** — distinct Evaluator returns `approve`,
    `request_revision`, `block` or `escalate_to_human`.
13. **Revision loop** — `request_revision` returns to the Builder; new evidence
    and evaluation are required.
14. **Evidence Gate** — on `approve`, State Keeper records the decision and
    changes `needs_evaluation -> approved -> done`.
15. **Initiative Validation** — after every task is `done`, confirm AC coverage,
    residual risks and `validation_done: true`.
16. **Ratchet** — record serious first-time or recurring preventable failures.
17. **Close/Handoff** — update progress, state, decisions and final handoff.

## Gate matrix

| Transition | Required evidence | Owner |
|---|---|---|
| draft → outcome_ready | outcome, demonstrable increment, priority source or human decision | Spec Guardian/Orchestrator |
| outcome_ready → spec_ready | Spec Guardian decision | Spec Guardian |
| spec_ready → plan_ready | impact + plan + rollback | Orchestrator |
| validation_ready → human_visibility_ready | synchronized stakeholder brief | Spec Guardian/Orchestrator |
| human_visibility_ready → tasks_ready | validation mapping + atomic tasks | Harness Planner/Orchestrator |
| ready → in_progress | readiness record with outcome linkage | Builder/Orchestrator |
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
- missing or stale stakeholder brief → update Human Visibility before tasks;
- process-only task expansion without evidence → return to Outcome/Task
  Readiness;
- unknown/high impact → discovery or human review;
- missing validation → return to Validation Plan;
- oversized task → return to Task Breakdown;
- failed implementation/check → `needs_revision` or `blocked`;
- unsafe/destructive action → human approval gate;
- interruption → Interruption Recovery workflow;
- serious/recurring preventable failure → Ratchet workflow.
