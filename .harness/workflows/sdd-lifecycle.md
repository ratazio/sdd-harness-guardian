# Workflow: Common SDD Lifecycle

## Purpose

Define the mandatory gates shared by feature, bugfix and refactor workflows.
Specialized workflows may add requirements but may not skip these gates.

## Entry condition

An initiative exists under `specs/<initiative>/` using the canonical templates.

## Flow

1. **Specify** — create/revise `spec.md`.
2. **Spec Review** — Spec Guardian records `Spec Ready: yes/no`.
3. **Impact Map** — map non-trivial surfaces, unknowns and risk.
4. **Technical Plan** — define approach, decisions and rollback.
5. **Validation Plan** — map every AC to checks and evidence.
6. **Task Breakdown** — create atomic tasks with exit/evidence criteria.
7. **Readiness Gate** — verify dependencies, risk and approvals for one task.
8. **Implementation** — Builder implements only that task.
9. **Evidence Draft** — Builder writes `evidence/<task-id>.md` and moves the
   task to `needs_evaluation`.
10. **Independent Evaluation** — distinct Evaluator returns `approve`,
    `request_revision`, `block` or `escalate_to_human`.
11. **Revision loop** — `request_revision` returns to the Builder; new evidence
    and evaluation are required.
12. **Evidence Gate** — on `approve`, State Keeper records the decision and
    changes `needs_evaluation -> approved -> done`.
13. **Initiative Validation** — after every task is `done`, confirm AC coverage,
    residual risks and `validation_done: true`.
14. **Ratchet** — record serious first-time or recurring preventable failures.
15. **Close/Handoff** — update progress, state, decisions and final handoff.

## Gate matrix

| Transition | Required evidence | Owner |
|---|---|---|
| draft → spec_ready | Spec Guardian decision | Spec Guardian |
| spec_ready → plan_ready | impact + plan + rollback | Orchestrator |
| plan_ready → tasks_ready | validation mapping + atomic tasks | Harness Planner/Orchestrator |
| ready → in_progress | readiness record | Builder/Orchestrator |
| in_progress → needs_evaluation | implementation + evidence draft | Builder |
| needs_evaluation → approved | independent `approve` | Evaluator |
| approved → done | approved `evidence/<task-id>.md` + state sync | State Keeper |
| all done → validation_done | all ACs covered, no blockers | Evaluator |

## Non-negotiable terminal rule

No workflow, local override or tool may set `done` from `in_progress` or
`needs_evaluation`. Missing evidence or evaluator means the task remains
non-terminal.

## Failure routes

- unclear intent → return to Specify;
- unknown/high impact → discovery or human review;
- missing validation → return to Validation Plan;
- oversized task → return to Task Breakdown;
- failed implementation/check → `needs_revision` or `blocked`;
- unsafe/destructive action → human approval gate;
- interruption → Interruption Recovery workflow;
- serious/recurring preventable failure → Ratchet workflow.
