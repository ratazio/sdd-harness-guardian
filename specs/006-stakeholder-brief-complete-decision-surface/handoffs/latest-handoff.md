# Handoff: 006-stakeholder-brief-complete-decision-surface

**From:** Codex / State Keeper  
**Intended role/recipient:** human sponsor / adopting maintainer  
**Created at:** 2026-08-19  
**Current phase/status:** validation_done  
**Current task/status:** none  
**Last safe checkpoint:** T-005 and all validation gates are done; D-020
authorizes release 0.3.0 through main and immutable tag v0.3.0.  
**Repository revision/working-tree summary:** base recorded in run-state;
uncommitted initiative-006 planning artifacts plus T-001 rules/workflows/
templates/role/skill/operating-model changes and one focused test.
T-004 adds only scaffolder rendering, consumer guidance, Factory compatibility
and a minimal post-meeting propagation fixture; no release or service work.

## 1. Completed and approved work

- Implemented the T-001 semantic contract only.
- D-010 is represented as block-level `data-source`, `data-source-section` and
  `data-coverage` plus a human coverage table, with no JSON index/sidecar.
- D-011 is represented by extending existing Spec Guardian/spec-review and
  runtime identities, with no new permanent agent or skill.
- Lifecycle now requires preliminary task draft, composition, distinct review,
  final render, meeting propagation and only then Tasks Ready.
- Plan template and guidance define the full architecture-readiness dimensions,
  proportional S/M/L/high/unknown profiles and block-or-discovery behavior.
- The v2 lifecycle is explicitly conditional on v2 lineage. Historical/pinned
  v1 retains legacy brief-before-task ordering until material refresh/migration.
- The existing 006 v1 brief was refreshed only for the material T-001 planning
  facts and its local freshness baseline was renewed; marker/design remain v1.

## 2. Partial or unverified work

- T-003 is independently approved and done: stdlib v1/v2 validation,
  schema-v2 baseline migration and precise v1/v2/privacy fixtures passed.
  D-015 records Q-003; deterministic PASS still does not claim visual approval.
- T-003 is independently approved/done; its validator and migration fixtures
  remain green. The former smoke/Factory integration debts are resolved by T-004.
- Canonical v2 design/behavior and the populated 006 example are independently
  approved; D-014 records coverage/Human Visibility/Tasks Ready v2 readiness.
- The evaluator revision removed stale v1/T-001 text, propagated D-013/Q-002,
  made provenance single-source per block, aligned the v2 design standard and
  added `evidence/rendered/T-002/` artifacts. The legacy v1-only validator now
  honestly fails against v2; T-003 owns that compatibility work.
- Second revision: coverage dispositions are restricted to `represented`,
  `synthesized`, `not_applicable` and `link_only`; a gap is a blocker. Evidence
  no longer claims legacy-validator green status. T-002 is again
  `needs_evaluation`.
- The production v2 validator and freshness/migration fixtures are approved;
  consumer scaffolding and propagation guidance are implemented in T-004.
- Rendered, accessibility and cross-role reviews are T-005 work.
- T-001/T-002/T-003/T-004 are done. T-005 is the only active task.
- T-004 is independently approved. It renders v2 scaffold
  placeholders, updates consumer/install/prompt guidance, proves pinned v1 plus
  v2 Factory compatibility and proves decision-log -> source -> regeneration
  ordering before Tasks Ready.

## 3. Files changed

| File group | State | Reason |
|---|---|---|
| `.harness/rules`, workflows, templates | changed | v2 coverage, lifecycle, architecture and state contracts. |
| Existing agents and skills | changed | Discoverable responsibility without creating a role/skill. |
| `.harness/AGENTS.md`, `manifest.yaml`, `docs/operating-model.md` | changed | Gate/operating model alignment. |
| `scripts/test_brief_v2_contracts.py` | added | Focused behavioral T-001 fixtures; not a production HTML validator. |
| `specs/006/.../{plan,decision-log,run-state,tasks,progress,evidence}` | changed | D-010/D-011 resolution, honest v1 lineage/state, revision evidence and `needs_evaluation`. |
| `scripts/{new_initiative,smoke_test_scaffolder,test_factory_guardian_fixture,test_post_meeting_workflow}.py` | changed/added | T-004 rendered v2 scaffold, dual-lineage Factory and post-meeting integration proof. |
| Consumer docs/prompt/manifest/Factory bridge | changed | v2 lifecycle, migration and consumer-owned propagation guidance. |

## 4. Validations and evidence

| Task/check | Result | Evidence |
|---|---|---|
| `python scripts/test_brief_v2_contracts.py` | PASS | `evidence/T-001.md` |
| `python scripts/validate_bundle.py` | PASS, 267 checks | `evidence/T-001.md` |
| `git diff --check` | PASS | `evidence/T-001.md` |
| v1 source-to-brief + Human Visibility refresh | PASS; baseline renewed, structural/gate/freshness failures none | `evidence/T-001.md` |
| T-004 focused integration suite | PASS: smoke, Factory v1/v2, post-meeting workflow, v1/v2 validator, v2 contracts, bundle and diff check | `evidence/T-004.md` |

## 5. Decisions and approvals

- D-009 authorizes execution but not release.
- D-010 and D-011 are implemented in the bounded T-001 surface.
- D-012 records the planning coverage-review locator and explicitly does not
  stand in for final v2 coverage, rendered or evaluator approval.
- D-016 records the T-004 integration increment; `evidence/T-004.md` records
  its later independent approval.

## 6. Blockers, unknowns and risks

- T-001 has independent `approve` and an approved evidence pack; it is done.
- T-002/T-003/T-004/T-005 are done, and residual risks are recorded in
  `progress.md` and `evidence/T-001.md`.
- The Factory fixture baseline debt is resolved by real v1/v2 installed-validator
  paths; independent evaluation is complete.

## 7. Exact next safe step

No implementation task remains. Publish the validated bundle as version
`0.3.0` on `main` and immutable tag `v0.3.0`, as authorized by D-020.

## 8. Resume reading order

1. `run-state.yaml`
2. `progress.md`
3. this handoff
4. repository status/diff
5. `tasks.md` and `evidence/T-001.md`
6. `validation-plan.md` and `decision-log.md`

## 9. Do not do

- Do not reopen or alter the approved T-001 contract without a new finding.
- Do not edit Factory, scaffolder, consumer docs/prompts or release metadata in
  T-003.
- Do not add a permanent agent, sidecar, embedded JSON index or duplicate
  provenance state.

## T-005 render finding / T-002 CSS correction

V-011/M-001 found unreadable compressed columns in the 390px decision and
coverage tables. T-002 supplied only a local-scroll/minimum-cell CSS correction
to the template and example; new renders are in `evidence/rendered/T-002/`.
The HTML baseline is stale and needs a distinct rendered recheck before renewal.
- Do not mask F-005-01 in terminal evidence or advance T-005 to
  `needs_evaluation` before the owning T-002 return loop is complete.

## Superseding T-005 evaluator checkpoint

D-018's distinct T-002 approval resolved F-005-01. The current T-005 rerun
passes bundle (267), visibility unit, scaffold smoke, Factory v1/v2,
post-meeting, v2-contract, diff, desktop/narrow/no-script/keyboard/print
mechanical checks. Final artifacts are `evidence/rendered/T-005/*-final.*`;
the earlier non-suffixed T-005 renders are historical pre-correction evidence.

Because final brief/state/evidence alignment changed source hashes, the current
baseline is deliberately stale. Do not write it yet. The distinct `t5_evaluator`
must first judge E-001–E-003 and M-004–M-006 from the final content and renders,
then authorize baseline renewal and the final independent validator run. T-005
is `needs_evaluation`, not approved or done; release/tag/publish remains
unauthorized.

## Terminal approval

The distinct `t5_evaluator` approved V-001–V-012, E-001–E-003 and M-001–M-006
after authorizing and verifying the final baseline renewal. Source/brief hashes
match; validator, bundle (267), smoke, Factory v1/v2, post-meeting, lifecycle
and final rendered checks pass with no blocker/high finding. State Keeper
recorded T-005 `approved -> done` and initiative `validation_done`. D-019 and
`evidence/T-005.md` supersede the pending checkpoint above; release/tag/publish
remains separately unauthorized.

## Release authorization

D-020 supersedes only the prior release hold: the human sponsor authorized
commit, main push, version `0.3.0` and immutable tag `v0.3.0`. Implementation
and validation remain closed; consumers may pin the tag after publication.
