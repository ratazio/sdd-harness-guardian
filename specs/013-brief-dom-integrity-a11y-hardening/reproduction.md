# Reproduction: 013-brief-dom-integrity-a11y-hardening

**Status:** reproduced  
**Observed in version/revision:** bundle baseline before SPEC 013 implementation (2026-08-27)  
**Environment:** local Python validator, generated mock briefs  
**Captured by/date:** independent mock-lab review / 2026-08-27

## Observed behavior

Independent review of M-006, M-007 and M-008 found rendered duplicate
`coverage-register` ids and non-whitespace content after the document close.
M-007 and M-008 also exposed click-only tabs. The deterministic Human
Visibility validator passed these packages because it did not yet enforce
generic rendered-id uniqueness, the terminal document boundary, or the full
static tab interaction contract.

## Expected behavior

The validator rejects each malformed rendered v2 fixture with a concise,
content-safe diagnostic, while accepting v1, non-tab v2, permitted
whitespace/comments, and literal markup in inert subtrees.

## Minimal steps

1. Start from a valid v2 fixture accepted by `scripts/test_validate_human_visibility.py`.
2. Repeat any non-empty rendered `id`, append a rendered element after the final `</html>`, or remove keyboard/focus handler evidence from a declared tablist.
3. Run `python scripts/test_validate_human_visibility.py`.
4. Before this SPEC, the malformed variant can pass; after it, the focused test must fail the variant and retain green controls.

## Inputs, fixtures and preconditions

The regression fixtures live in the existing focused Human Visibility test
suite. Their bodies contain only minimal structural markup; diagnostics name
the contract or id and never echo a document body.

## Baseline evidence

| Artifact/check | Location/result |
|---|---|
| Independent mock findings | `testes/mock-runs/20260827-full-suite/` M-006 through M-008 |
| Current regression command | `python scripts/test_validate_human_visibility.py` passed before implementation, demonstrating the gap |

## Suspected area and uncertainty

`scripts/validate_human_visibility.py`, specifically the parser model and v2
shell/tab checks. The parser must distinguish rendered from inert content;
static evidence is a bounded surrogate for browser execution, not proof of
usability.

## Regression check

**Validation IDs:** V-001 through V-005  
**Failing command/steps before fix:** malformed fixture accepted by the current focused suite.  
**Expected pass after fix:** malformed fixtures fail and all stated controls pass.
