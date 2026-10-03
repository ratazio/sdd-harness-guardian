---
name: spec-review
description: Use when reviewing a feature, bugfix, refactor or initiative spec for clarity, completeness, testability and readiness before implementation.
version: "0.3.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Spec Review

## When to use

A spec needs readiness assessment before planning/execution, or the user asks
whether it is ready. Do not use for formatting or brainstorming only.

## Procedure

1. Read spec, local rules and brief/state when applicable.
2. Identify objective, product/user outcome, demonstrable increment, non-goals
   and assumptions; detect hidden decisions or invented business priority.
3. Check AC testability, relevant edge cases, risks/dependencies and validation.
4. Check source-authoring Plan Ready architecture obligations under the
   applicable rules. This is spec assessment, not repair of brief inputs.
5. Dispatch brief lineage via `.harness/rules/brief-contract.md` BC-002:
   - **v3:** confirm the protocol record BC-009/BC-010/BC-025. Record actual
     disposition/limits; do not run another rendered review, demand a model,
     pre-render approval, source rewrite or reapproval.
   - **v2 historical:** confirm pass (a) model/construction and pass (b)
     loopback HTML under BC-009/BC-016 with independent identity BC-010.
     Confirm BC-003–BC-006 and architecture BC-012/BC-014. Recoverable legacy
     findings return to composition and the relevant historical review.
   - **v1 historical:** keep BC-002's lifecycle without v2/3 gates.
   - **explicit owner dispensation:** cite the exact decision as N/A, without
     claiming rendering/review happened.
6. Classify spec issues as blocking/non-blocking and report readiness. Brief
   findings/limits use BC-015/BC-020; no third validation after B.

## Output contract

Return summary, blocking/non-blocking spec issues, missing fields, recommended
spec revisions and Outcome Ready/Spec Ready yes/no. Report applicable Human
Visibility disposition; v3 completion is a repair record under BC-025, not
independent approval. v2 additionally reports `tasks_drafted`,
`brief_coverage_ready`, review identities and pending meeting propagation.
Never invent task/evidence/owner authorization (BC-010/BC-018).

## Quality bar

Precise spec findings make the source-authoring decision actionable.
Confirming the brief protocol does not repeat its semantic assessment.
