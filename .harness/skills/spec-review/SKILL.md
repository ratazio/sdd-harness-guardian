---
name: spec-review
description: Use when reviewing a feature, bugfix, refactor or initiative spec for clarity, completeness, testability and readiness before implementation.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Spec Review

## When to use

- A spec needs approval before planning.
- A user asks whether a spec is ready.
- An agent is about to implement from a spec.

## When not to use

- The task is only formatting text.
- The task has no software delivery implications.
- A human explicitly asks for brainstorming only.

## Procedure

1. Read the spec and local rules.
2. Identify objective, outcomes, non-goals and assumptions.
3. Check acceptance criteria for testability.
4. Detect vague terms and hidden decisions.
5. Classify issues as blocking or non-blocking.
6. Return Spec Ready yes/no.

## Output contract

Return a report with: summary, blocking issues, non-blocking issues, missing fields, recommended rewrite, Spec Ready status.

## Quality bar

A good review blocks vague work before code starts and gives precise edits needed to make the spec executable.
