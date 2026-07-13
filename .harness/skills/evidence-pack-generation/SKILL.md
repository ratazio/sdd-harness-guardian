---
name: evidence-pack-generation
description: Use when collecting and formatting proof that a task or initiative was completed and validated.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Evidence Pack Generation

## When to use

- A task is about to be marked done.
- A PR or handoff needs proof.
- An evaluator needs structured evidence.

## When not to use

- No work was performed.
- Validation was not run.
- The user asks for a rough status only.

## Procedure

1. Read task, validation plan and command outputs.
2. Collect changed files.
3. Collect tests and results.
4. Collect screenshots/logs if relevant.
5. Record assumptions and missing checks.
6. Create `evidence/<task-id>.md` as a draft.
7. Request independent evaluation; do not mark the task done.

## Output contract

Use the evidence-pack template with identities, current revision/working tree,
files changed, AC and exit-criteria coverage, validations, results, artifacts,
skipped checks, gaps, residual risk and evaluator decision.

## Quality bar

Evidence must be sufficient for a separate evaluator to approve or reject without reconstructing the whole session.
