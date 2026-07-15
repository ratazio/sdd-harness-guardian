# Rule: Outcome Readiness

## Soft rule

The harness does not decide commercial value, roadmap priority or product
strategy. It does require enough outcome context to know whether a spec, task or
next step is connected to a declared delivery result.

Before implementation or expansion of a task list, the agent must be able to
state the product/user outcome, the demonstrable increment, the related
requirements or acceptance criteria, and the validation that will prove progress.

## Required contract

Each non-trivial initiative declares:

- product or user outcome;
- affected users, actors or operational owner;
- demonstrable increment or reduced uncertainty expected from the next slice;
- MVP/slice boundary when applicable;
- anti-scope;
- priority source or `human_decision_required` when priority is unclear.

Each implementation task declares:

- requirement IDs and acceptance criteria IDs, or `not_applicable` with reason;
- expected artifact or behavior change;
- validation method;
- why this task is the next safe step;
- whether it delivers a vertical slice, enables one directly, or is bounded
  discovery that reduces a named uncertainty.

## Blocking conditions

Block or request clarification when:

- the initiative cannot name the delivery outcome it is meant to advance;
- the task cannot declare a demonstrable increment, expected artifact or reduced
  uncertainty;
- the task is only process expansion, documentation churn or backlog growth
  without new evidence, validation or risk reduction;
- the task is not traceable to a requirement, acceptance criterion, approved
  plan step or explicit discovery question;
- more than one task-refinement pass is proposed without new evidence or a
  human decision;
- the next step depends on a business/product priority that is not recorded.

When blocked for missing priority or business context, ask for the missing
decision. Do not infer commercial value.

## Allowed exception

Purely mechanical maintenance may record `not_applicable` when it is
formatting-only, comment-only or release-administrative and does not change
behavior. The task still needs scope, validation and evidence.

## Hard mirror recommendation

Use an outcome-readiness validator before `spec_ready`, `tasks_ready` and
`ready -> in_progress`. Validate required fields, AC links, expected artifact,
validation method and `why_now`. Flag repeated task generation without evidence.

Recommended check: `validate-outcome-readiness`.
