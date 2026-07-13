---
name: task-breakdown
description: Use when converting an approved spec and technical plan into small, ordered, testable implementation tasks.
version: "0.1.0"
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

1. Read spec, plan, impact map and validation plan.
2. Identify dependencies.
3. Split into tasks that can be completed and validated independently.
4. Assign exit criteria and evidence requirement to each task.
5. Assign distinct builder/evaluator slots and mark required human approval.
6. Produce the ordered task list and keep tasks pending until readiness is checked.

## Output contract

Return tasks with id, title, objective, dependencies, files likely touched, validation, evidence, risk and done criteria.

## Quality bar

Every task must be small enough to complete in one focused session and must have objective done criteria.
