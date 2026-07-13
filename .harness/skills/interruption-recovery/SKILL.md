---
name: interruption-recovery
description: Use when resuming SDD work after a session interruption, context reset, agent switch or failed run.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Interruption Recovery

## When to use

- Work was interrupted.
- A new agent is continuing a previous task.
- run-state or progress exists and must be interpreted.

## When not to use

- Starting a fresh initiative.
- No prior state exists.
- The user only asks for a summary unrelated to execution.

## Procedure

1. Read run-state.yaml.
2. Read progress.md.
3. Read latest handoff.
4. Verify repository status if available.
5. Identify last safe checkpoint.
6. Reconcile task, evidence and working-tree state.
7. Recommend the next safe step.

## Output contract

Return resume summary, current state, safe checkpoint, risks, next action and files to read next.

## Quality bar

A new agent must be able to continue without redoing discovery or guessing.
