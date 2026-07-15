---
name: spec-review
description: Use when reviewing a feature, bugfix, refactor or initiative spec for clarity, completeness, testability and readiness before implementation.
version: "0.1.2"
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

1. Read the spec, stakeholder brief when present, and local rules.
2. Identify objective, product/user outcome, demonstrable increment, non-goals
   and assumptions.
3. Check acceptance criteria for testability.
4. Detect vague terms and hidden decisions.
5. Check whether the agent would need to infer commercial value or roadmap
   priority.
6. Check whether `stakeholder-brief.html` is present for non-trivial work,
   concise enough for review, and consistent with the spec.
7. Classify issues as blocking or non-blocking.
8. Return Outcome Ready yes/no, Spec Ready yes/no and Human Visibility Ready
   yes/no.

## Output contract

Return a report with: summary, blocking issues, non-blocking issues, missing
fields, recommended rewrite, Outcome Ready status and Spec Ready status.
Include Human Visibility Ready status when the initiative is non-trivial.

## Quality bar

A good review blocks vague or invisible work before code starts and gives
precise edits needed to make the spec executable and reviewable.
