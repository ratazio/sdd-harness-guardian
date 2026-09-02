# Handoff: 012-stakeholder-brief-evidence-projection-enforcement

**From:** spec012_t005_release_builder  
**Intended role/recipient:** independent T-005 semantic evaluator  
**Created at:** 2026-08-27  
**Current phase/status:** needs_evaluation; T-001–T-004 done, T-005 needs_evaluation  
**Current task/status:** T-005 needs_evaluation; release builder recorded validation and static brief evidence without self-approval  
**Last safe checkpoint:** evaluator-requested canonical tab contract was repaired in the new local-only fixture; inline script syntax, release suite and baseline checks pass; a fresh distinct T-005 semantic evaluation is required.  
**Repository revision/working-tree summary:** inspect before change; repository has unrelated pre-existing work.

## 1. Completed and approved work

- Reproduced the audit gap from `testes/specs/001-news-blog-auth`.
- Declared ACs for evidence, risks, routes, compatibility and reviewer boundary.
- Mapped impact, A2 validation and preliminary tasks.

## 2. Partial or unverified work

- T-004 uses the canonical block-form task ledger in `001-news-blog-auth`, so its pending task evidence references defer truthfully.
- T-004 adds explicit template/rule guidance and a complete normal-and-baseline regression matrix: four future states defer, while evaluation and terminal states fail without the same pack.

## 3. Files changed

| File | State | Reason |
|---|---|---|
| spec.md, reproduction.md, impact-map.md, plan.md, validation-plan.md, tasks.md | planning complete | actionable corrective scope and evidence design. |
| `.harness/templates/README.md`, `run-state.yaml.md`, `.harness/rules/human-visibility.md` | synchronized | Lifecycle-scoped deterministic boundary and retained independent-review guidance. |
| `testes/specs/001-news-blog-auth/run-state.yaml`, `scripts/test_validate_human_visibility.py` | synchronized | Canonical fixture ledger and future-versus-evaluation regression. |
| run-state.yaml, progress.md, decision-log.md, tasks.md, stakeholder-brief.html | synchronized | T-004 handoff state and derived decision surface. |

## 4. Validations and evidence

| Task/check | Result | Evidence |
|---|---|---|
| audited fixture repair | independently approved | `testes/specs/001-news-blog-auth/evidence/planning-review.md` |
| T-001 grammar inventory | independently approved | `evidence/T-001.md` |
| T-002 safe evidence resolver | repair checks pass; fresh security evaluation pending | `evidence/T-002.md` |
| T-003 risk/API projection | independently approved | `evidence/T-003.md` |
| T-004 guidance/fixture/baseline | implementation checks pass; distinct evaluator pending | `evidence/T-004.md` |

## 5. Decisions and approvals

D-001–D-014 accept the narrow validator extension, safe containment, source-derived hard mirrors, retained independent review, T-001–T-003 approvals and T-004's lifecycle-scoped evaluator gate.

## 6. Blockers, unknowns and risks

T-004 needs a distinct evaluation of its lifecycle boundary, guidance and baseline proof. T-005 remains pending.

## 7. Exact next safe step

Obtain a distinct evaluation of T-004 before releasing T-005.

## 8. Resume reading order

1. `run-state.yaml`
2. `progress.md`
3. this handoff
4. `reproduction.md`
5. repository status
6. `validation-plan.md` and `decision-log.md`

## 9. Do not do

Do not implement validator code before T-001 is ready; do not treat deterministic PASS as semantic approval; do not read evidence paths outside the selected initiative; do not overwrite unrelated root work.
