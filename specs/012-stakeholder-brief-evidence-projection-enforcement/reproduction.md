# Reproduction: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** reproduced  
**Observed in revision:** local bundle validation run on 2026-08-26  
**Environment:** Windows, Python local runtime, repository root  
**Captured by/date:** independent `sandbox_spec_audit` / 2026-08-26

## Observed behavior

`testes/specs/001-news-blog-auth` initially cited `evidence/planning-review.md` in run-state, progress, handoff and decisions, but the file did not exist. Its Impact brief omitted IR-005 and its API contracts were abbreviated. `validate_human_visibility.py` nevertheless returned PASS and wrote a baseline.

## Expected behavior

The validator must fail a missing initiative-relative evidence locator and a v2 brief that omits a material `IR-*` source risk or canonical HTTP method/path contract. It must report source/target details and still state that semantic/rendered review remains required after PASS.

## Minimal steps

1. Create a v2 consumer initiative whose source cites `evidence/planning-review.md` but omit that file.
2. Declare `IR-001` and `IR-002` in `impact-map.md`, but project only IR-001 in the brief Impact table.
3. Declare `GET /api/v1/example` in `plan.md`, but omit it from the rendered Architecture and Validation sections.
4. Run Human Visibility validation for that consumer initiative.
5. Before the fix it incorrectly returns PASS; afterwards it must report all three failures and refuse a baseline write.

## Inputs, fixtures and preconditions

Use synthetic content, `brief_lineage: v2`, provenance and a structurally valid brief so failures isolate these rules. A no-risk/no-API fixture and an existing v1 fixture are compatibility controls.

## Baseline evidence

| Artifact/check | Location/result |
|---|---|
| Independent audit | `testes/specs/001-news-blog-auth/evidence/planning-review.md` — initial needs revision, then approved after manual repair. |
| Pre-fix deterministic result | Human Visibility returned PASS despite all three omissions, as recorded by the audit. |
| Control validation | `python scripts/validate_bundle.py` passed 267 checks after repair; it did not exercise the missing rules. |

## Suspected area and uncertainty

`scripts/validate_human_visibility.py` validates structure/provenance/freshness but treats coverage labels as declarations, not a minimum projection inventory. T-002/T-003 decide parser boundaries with negative tests before validator code changes.

## Regression check

**Validation IDs:** V-001 through V-007.  
**Failing command/steps before fix:** `python scripts/validate_human_visibility.py --consumer-root <fixture-root> --initiative specs/001-negative` returns zero.  
**Expected pass after fix:** negative fixtures return non-zero with named missing locator/identifier; complete and compatibility fixtures return zero, and `python scripts/validate_bundle.py` passes.
