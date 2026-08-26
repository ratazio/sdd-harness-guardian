# Rule: Validation Policy

## Soft rule

Validation is planned before implementation and traced from each acceptance
criterion to a reproducible check and evidence artifact.

## Validation order

Prefer:

1. deterministic assertion or schema validation;
2. automated unit, integration, contract or end-to-end test;
3. lint, typecheck and build;
4. controlled manual check with captured evidence;
5. LLM-as-judge only for criteria without an objective oracle.

Omitted checks require a reason, risk impact and evaluator acceptance. A passing
command unrelated to an AC does not satisfy that AC.

## Proportionate assurance

Choose assurance from the task's claim and risk, not a universal tool list.
A1 may be concise. A2 is required for high/unknown risk, public-contract,
data-migration, trust-boundary or material-UI work. A3 names accountable local
authority and applicable local/sector policy; this bundle does not certify it.

Each material task records selected/inapplicable technique rationale, oracle,
executor, independent evaluator, evidence and failure/waiver path. For UI,
visual evidence is paired with behavioral proof when behavior is material.
Gherkin, mutation and screenshots are options, never universal requirements.

## Blocking conditions

Block when:

- an AC has no validation path;
- expected result or evidence location is missing;
- a relevant regression check was skipped silently;
- nondeterministic judgment replaces an available deterministic check;
- `validation_done` is requested while an AC or blocking risk remains open.

## Hard mirror recommendation

Add a traceability check that compares AC IDs in `spec.md`,
`validation-plan.md` and evidence packs. Gate `validation_done` on complete
coverage and successful/accepted results.

Recommended check: `validate-acceptance-traceability`.
