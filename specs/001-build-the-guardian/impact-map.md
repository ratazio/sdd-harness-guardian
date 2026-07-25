# Impact Map: 001-build-the-guardian

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex / Impact Mapper role  
**Reviewed at:** 2026-07-13  
**Overall risk:** medium

## 1. Change boundary

Changes affect only the reusable governance bundle, its templates, docs and
optional maintenance/scaffolding scripts. No consumer code or external state is
modified.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Entrypoint | `.harness/AGENTS.md` | direct | complete operating contract | medium | T-001 |
| Roles/rules/workflows | `.harness/{agents,rules,workflows,skills}` | direct | explicit gates and separation | medium | T-001 |
| Templates/state | `.harness/templates` | direct | canonical copyable artifacts | medium | T-002 |
| Tooling | `scripts/*.py` | direct | safe scaffold + validator | medium | T-002 |
| Installation/docs | top-level + `docs/` + prompt | direct | operational consumption/release | low | T-003 |
| Consumer repositories | `vendor/` and `specs/` contracts | indirect | clearer setup, no automatic write | medium | smoke test |

UI, backend, database, auth and deployment product surfaces are
`not_applicable` because this is a passive source bundle.

## 3. Dependency and data flow

```txt
manifest -> bundle files -> consumer entrypoint -> project-local initiative
templates -> optional scaffolder -> specs/NNN-<initiative>
spec/plan/tasks -> evidence draft -> evaluator -> done/state
```

## 4. Compatibility and migration

- Existing `0.1.0` consumers are not yet released; no migration.
- Bundle path and primary entrypoint remain unchanged.
- New templates add fields without imposing a workflow engine.
- Rollback: pin the prior commit/tag before release; after release publish a new
  SemVer tag rather than moving `v0.1.0`.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | manifest points to missing files | registry edits | structural validator | V-001 |
| IR-002 | scaffolder writes wrong location | path handling | temp-root smoke test | V-002 |
| IR-003 | existing initiative overwritten | duplicate slug | refusal test | V-003 |
| IR-004 | workflow allows false done | terminal wording | workflow checks + evaluator | V-001/V-006 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | behavior in a real consumer pilot | long-term usability | post-release pilot | no |

## 7. Recommended reviewers and checks

- independent evaluator of contracts and diff;
- Python syntax/structure validation;
- feature, bugfix and overwrite smoke tests;
- manual path/document coherence review.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** no for implementation; yes before destructive publish/tag actions  
**Approval/evidence:** spec and plan  
**Conditions before implementation:** Spec Ready satisfied
