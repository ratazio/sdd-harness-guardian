---
name: task-breakdown
description: Use when converting an approved spec and technical plan into small, ordered, testable implementation tasks.
version: "0.2.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Task Breakdown

## When to use

- A plan is approved and needs execution tasks.
- A task is too broad or not independently testable.
- A workflow needs safe sequencing.

## When not to use

- The spec is not approved.
- There is no plan.
- The user asks for high-level strategy only.

## Procedure

1. Read spec, plan, impact map and validation plan. For v2, this first output
   is an explicitly unauthorised preliminary task draft used for brief coverage.
2. Identify dependencies, outcome linkage and the next demonstrable increment.
3. Split into tasks that can be completed and validated independently.
4. Assign requirement IDs, AC IDs, exit criteria, evidence requirement and
   why-now rationale to each task.
5. Reject process-only task expansion unless it produces evidence, validation or
   named risk reduction.
6. For v2, keep task rows `pending`, set `tasks_drafted`, and require the
   composition/review/render/meeting-propagation path before `tasks_ready` or
   implementation. For v1, confirm the stakeholder brief is updated before
   expanding implementation tasks.
7. Assign distinct builder/evaluator slots and mark required human approval.
8. Produce the ordered task list and keep tasks pending until readiness is checked.

## Output contract

Return tasks with id, title, objective, requirement IDs, AC IDs, outcome served,
demonstrable increment, why-now rationale, dependencies, files likely touched,
validation, evidence, risk and done criteria.

## Quality bar

Every task must be small enough to complete in one focused session, trace to an
approved outcome and have objective done criteria.
