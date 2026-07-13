---
name: impact-analysis
description: Use when mapping the likely impact of a software change before implementation, including files, contracts, APIs, tests, risks and dependencies.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: high
---

# Impact Analysis

## When to use

- Any non-trivial feature, refactor, migration or bugfix is planned.
- The change may affect contracts, data, auth, billing, API, UI flow or infra.
- There is uncertainty about affected areas.

## When not to use

- Tiny documentation-only change.
- Formatting-only change.
- A human explicitly waives impact analysis for low-risk work.

## Procedure

1. Read spec and plan.
2. Inspect architecture and relevant files.
3. Identify affected domains.
4. Classify risk low/medium/high/unknown.
5. Recommend validations and reviewers.
6. Produce impact-map.md.

## Output contract

Use the impact map template with affected areas, risks, unknowns, tests and reviewers.

## Quality bar

The map must make hidden dependencies visible before implementation starts.
