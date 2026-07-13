# Rule: SDD Quality

## Soft rule

Implementation requires a written spec with an explicit `Spec Ready: yes`
decision. The spec is the source of truth for intent, not a substitute for the
technical plan.

## Required contract

The spec declares title, status, owner, problem, objective, actors, observable
outcomes, non-goals, functional requirements, acceptance criteria, edge cases,
constraints, assumptions, risks, dependencies and validation notes.

Every acceptance criterion has a stable ID, one observable claim and at least
one validation path. Terms such as “fast”, “correct”, “friendly” or “secure”
need a measurable definition in context.

## Blocking conditions

Block when:

- objective or non-goals are absent;
- outcomes cannot be observed;
- an AC combines unrelated behavior or cannot be tested;
- scope is too broad to plan safely;
- product ambiguity is hidden as a technical choice;
- relevant edge cases, risk or validation paths are missing;
- `Spec Ready` was self-asserted without a review record.

## Allowed exception

Formatting-only or comment-only maintenance may record `not_applicable` with a
reason in the task. It may not use the exception to change behavior.

## Hard mirror recommendation

Validate required headings/frontmatter and unique AC IDs with a schema or
custom linter. Block the implementation state transition unless
`spec.spec_ready == true` and the Spec Guardian decision is recorded.

Recommended check: `validate-spec-readiness`.
