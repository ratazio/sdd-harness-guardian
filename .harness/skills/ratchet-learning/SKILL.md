---
name: ratchet-learning
description: Use when a repeated or serious agent failure should be converted into a permanent rule, test, template update, skill update or evaluation case.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Ratchet Learning

## When to use

- The agent repeats a mistake.
- Evaluation finds a preventable failure.
- A task failed due to vague spec, missing validation or state loss.

## When not to use

- One-off harmless typo.
- The issue is purely subjective.
- There is no actionable prevention.

## Procedure

1. Classify the failure.
2. Identify root cause.
3. Propose prevention.
4. Decide artifact to update: rule, hook, test, template, skill or eval.
5. Assign an owner and implementation status.
6. Add the entry to the initiative-local `ratchet.md`.
7. Link and run the regression check before marking it implemented.

## Output contract

Use ratchet-entry.md with failure, cause, prevention, artifact update and regression check.

## Quality bar

The same mistake should become harder to repeat after the ratchet entry.
