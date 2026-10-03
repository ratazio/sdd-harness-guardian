---
name: validation-planning
description: Use when transforming acceptance criteria into concrete tests, commands, checks, evals and evidence requirements.
version: "0.3.0"
owner: platform-engineering
maturity: stable
risk_level: high
---

# Validation Planning

## When to use

- A spec has acceptance criteria.
- A task needs done criteria.
- A feature needs evidence pack requirements.

## When not to use

- No implementation will happen.
- The change has no observable behavior.
- The user only wants a conceptual explanation.

## Procedure

1. Read acceptance criteria.
2. Map each criterion to a validation method.
3. Prefer deterministic checks.
4. Define required commands.
5. Define evidence artifacts.
6. Define expected result and evidence destination for every check.
7. Identify manual checks or LLM-as-judge only when necessary.
8. Dispatch brief validation by `brief-contract.md` BC-002. Historical v2
   separates deterministic provenance/identity/lifecycle checks from BC-009
   qualitative passes. Contract 3 uses BC-009's content/visual repairs and
   BC-025 record; do not add a semantic review after B. One-time evaluation
   of bundle/skill implementation remains independent task acceptance, not
   a new runtime stage. Mechanical source/structure checks remain proportional.
9. Select A1/A2/A3 proportionally: identify risk trigger, selected or
   inapplicable technique, oracle, executor, independent evaluator, evidence
   and failure/waiver path. Do not impose Gherkin, mutation, screenshots or a
   universal coverage target.

## Output contract

Use validation-plan.md with criteria-to-validation mapping, commands, expected results and evidence.

## Quality bar

Every acceptance criterion must have at least one validation path or a clearly stated reason why not.
