# Workflow: Interruption Recovery

## Entry condition

Execution was interrupted, context changed, an agent/session was replaced or
`resume_required: true`.

## Recovery flow

1. Read `run-state.yaml`, `progress.md` and
   `handoffs/latest-handoff.md` in that order.
2. Inspect repository status and compare it with recorded files/checkpoint.
3. Read current task, validation plan, evidence, decisions and approvals.
4. Classify work since the checkpoint as complete, partial, unverified or
   unknown.
5. Reconcile contradictions without changing implementation.
6. Choose one route: resume, evaluate existing work, revise, rollback,
   discovery task or human decision.
7. Record the recovery decision and risks.
8. Set `status: resumed`, `interrupted: false` and
   `resume_required: false` only after a safe route exists.
9. Continue from the next allowed Common Lifecycle transition.

## Safety rules

- never infer that partial work is complete;
- never discard unknown changes automatically;
- never rerun destructive/non-idempotent work without verifying prior effect;
- work already at `needs_evaluation` goes to an evaluator, not a new builder;
- missing evidence keeps a task non-terminal.

## Output

```md
## Resume Report

Last recorded state:
Repository state:
Last safe checkpoint:
Partial/unverified work:
Evidence available:
Contradictions resolved:
Selected route:
Risks:
Exact next step:
```

## Blocking condition

If target, prior effect or next transition cannot be determined safely, remain
`blocked` and request human decision or create a bounded discovery task.
