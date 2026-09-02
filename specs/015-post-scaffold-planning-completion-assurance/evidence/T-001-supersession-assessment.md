# Supersession assessment — SPEC-015 T-001

**Date:** 2026-08-31  
**Assessor:** `/root/assess_spec019_t004`  
**Task execution decision:** not authorized; no duplicate implementation was
created.

## Authoritative state

SPEC-015 is explicitly `superseded` in `run-state.yaml`, has neither Spec
Ready nor Tasks Ready, and names SPEC-018 as its required next reference.
Under the bundle's protected lifecycle, its blank scaffold task cannot be
made ready merely to repeat work that a later approved initiative already
contains.

## Requirement crosswalk

| SPEC-015 claim | Adopted implementation/evidence in SPEC-018 |
|---|---|
| FR-001 / AC-001: fresh scaffold remains cheap but cannot cross readiness/delivery boundaries | `evidence/T-002.md` establishes explicit scaffold lifecycle; `evidence/T-003.md` and `test_brief_delivery_integrity_reproduction.py` enforce source-only scaffold/no fake HTML and Human Visibility rejection. |
| FR-002: actionable gap without source-body leakage | SPEC-018 T-003 diagnostic is lifecycle/category-based, and its evidence records sanitised diagnostics. Current `test_validate_human_visibility.py` passes. |
| FR-003 / AC-002: varied authored packages without a fixed stack/layout/schema | SPEC-018 T-002 defines the flexible completeness contract and T-004 exercises eight varied disposable domains. |
| AC-003: historical/pinned packages are not retroactively blocked | SPEC-018 FR-003/EC-004 and T-003's lineage-compatible enforcement preserve historic v1/pinned behavior. |

## Current regression check

| Command | Result |
|---|---|
| `python scripts/test_brief_delivery_integrity_reproduction.py` | PASS — scaffold creates canonical sources only, never a delivery-like HTML file. |
| `python scripts/test_brief_composition_contract.py` | PASS |
| `python scripts/smoke_test_scaffolder.py` | PASS |
| `python scripts/test_validate_human_visibility.py` | PASS |
| `python scripts/validate_bundle.py` | PASS — 272 checks |

## Boundary and next action

This is an audit of adoption, not a SPEC-015 task evidence pack and not an
approval of T-001. Reopening SPEC-015 would need an explicit decision that
SPEC-018 does not cover a concrete remaining requirement. Until then, retain
the superseded state and use SPEC-018's approved evidence as the authoritative
implementation record.
