# Tasks: 006-stakeholder-brief-complete-decision-surface

**Status:** validation_done  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-19

The task package was approved by D-009. T-001/T-002/T-003 are done after
independent approval. T-004 and terminal T-005 are also done after independent
approval; all tasks are complete. D-020 grants the separately required release
authorization, limited to commit/push on `main` and immutable tag `v0.3.0`.

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Define v2 semantic, coverage, architecture and lifecycle contracts | human approval granted | high | Terra 5.6 high / t1_builder | Terra 5.6 high / t1_evaluator | evidence/T-001.md |
| T-002 | done | Build the progressive v2 template and populated decision example | T-001 | high | Terra 5.6 high / t2_builder | Terra 5.6 high / t2_evaluator | evidence/T-002.md |
| T-003 | done | Implement version-aware coverage, freshness and evolution validation | T-001, T-002 | high | Terra 5.6 high / t3_builder | Terra 5.6 high / t3_evaluator | evidence/T-003.md |
| T-004 | done | Integrate scaffolding, consumer guidance and post-meeting workflow | T-001, T-003 | medium | Terra 5.6 high / t4_builder | Terra 5.6 high / t4_evaluator | evidence/T-004.md |
| T-005 | done | Perform independent rendered/eval/regression validation and release handoff | T-002, T-003, T-004 | medium | Terra 5.6 high / t5_builder | Terra 5.6 high / t5_evaluator | evidence/T-005.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires approved evidence, distinct identities and synchronized state.

## T-001 — Define v2 semantic, coverage, architecture and lifecycle contracts

**Status:** done  
**Revision note:** two evaluator `request_revision` rounds (lineage/fixtures,
then v1 planning-brief freshness) were each applied through
`needs_revision -> in_progress -> needs_evaluation`; final re-evaluation
returned `approve` and State Keeper recorded `approved -> done`.  
**Objective:** make the complete-decision-surface rules unambiguous before HTML
or validator implementation.  
**Requirement IDs:** FR-003–012, FR-016–018  
**Acceptance criteria IDs:** AC-002–005, AC-009–010  
**Outcome served:** authors and reviewers share one enforceable definition of
source completeness, architecture depth, independence and safe task ordering.  
**Demonstrable increment:** updated rules/workflows/state/roles/skills/templates
describe v2 and focused fixtures prove the intended order/coverage model.  
**Expected artifact/behavior:** versioned source inventory; heading disposition
and provenance schema; distinct review contract; architecture profiles;
`tasks_drafted`/`brief_coverage_ready` transitions; v1 compatibility policy.  
**Validation method:** V-002, V-004, V-005, V-009, V-010; V-REG-002/004.  
**Why now:** every visual and validator choice depends on these semantics.  
**Max subtasks before validation:** 3  
**Dependencies:** explicit human execution approval.  
**Risk:** high  
**Builder:** Terra 5.6 high / t1_builder  
**Evaluator:** Terra 5.6 high / t1_evaluator  
**Human approval:** approved  
**Evidence:** evidence/T-001.md

### Scope

- Update Human Visibility, lifecycle, state contract and gate matrix.
- Update Spec Guardian, Orchestrator, Harness Planner/Impact Mapper/State Keeper
  responsibilities and relevant skills; add focused assembly/review skills if
  that is the smallest discoverable design.
- Resolve Q-001/Q-004 and define heading inventory/applicability semantics.
- Strengthen Plan Ready architecture dimensions and proportional profiles.

### Out of scope

- Final HTML styling/behavior, production validator and consumer rollout.

### Outcome linkage

- Requirement/AC/discovery question: FR-003–012, FR-016–018; AC-002–005.
- Vertical slice relation: directly enables.
- Priority source or human decision: 2026-08-19 direction; execution pending.

### Expected files and contracts

Rules, common/specialized workflows, agent/skill guidance, plan/run-state
templates, manifest state/gate docs and focused contract fixtures.

### Implementation constraints

Do not weaken existing evidence/terminal gates. Do not create a permanent agent
unless skills plus distinct runtime identities cannot make the review contract
discoverable and enforceable.

### Validation IDs and commands

V-002, V-004, V-005, V-009, V-010; run focused tests plus
`python scripts/validate_bundle.py`.

### Evidence requirements

Contract diff, transition table, source/heading schema examples, S/M/L/high
architecture fixtures, compatibility reasoning and evaluator decision.

### Exit criteria

- [x] human approval is recorded;
- [x] Q-001 and Q-004 are resolved in `decision-log.md`;
- [x] source/coverage/provenance and review identity are unambiguous;
- [x] lifecycle preserves every pre-existing protected invariant;
- [x] architecture profiles and missing-information behavior are testable;
- [x] focused and bundle validation passes;
- [x] distinct evaluator approves the evidence pack and state is synchronized.

### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex acting as Orchestrator  
**Blocking conditions:** none; implement only T-001 and stop at
`needs_evaluation` with evidence draft.

## T-002 — Build the progressive v2 template and populated decision example

**Status:** done  
**Revision note:** evaluator requested removal of stale v1/T-001/prototype text,
single-source provenance, D-013 propagation, honest validator compatibility,
v2 design-standard alignment and retained render artifacts. Builder applied the
revision through `needs_revision -> in_progress -> needs_evaluation`; distinct
evaluation remains required.
**Second revision note:** `gap` is a blocking finding rather than a coverage
disposition; allowed dispositions are `represented`, `synthesized`,
`not_applicable` and `link_only`. Builder corrected the template/evidence and
again returned through `needs_revision -> in_progress -> needs_evaluation`.
**Objective:** extend the proven v1 visual shell into a complete, progressively
disclosed decision surface.  
**Requirement IDs:** FR-001–006, FR-011, FR-013–015, FR-020  
**Acceptance criteria IDs:** AC-001–002, AC-006–008, AC-011  
**Outcome served:** meeting participants can move from executive value to full
business, architecture, execution, validation and history depth on one page.  
**Demonstrable increment:** canonical v2 template and a populated M/L example
with task draft, deep architecture, coverage and evolution views.  
**Expected artifact/behavior:** `v2` lineage; eight views; semantic progressive
navigation; source-backed diagrams; task/validation/decision ledgers; coverage
register; desktop/narrow/print behavior.  
**Validation method:** V-001, V-002, V-005–008, V-011; V-REG-003/005.  
**Why now:** it is the human-visible implementation of T-001 contracts.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001.  
**Risk:** high  
**Builder:** Terra 5.6 high / t2_builder  
**Evaluator:** Terra 5.6 high / t2_evaluator  
**Human approval:** approved  
**Evidence:** evidence/T-002.md

### Scope

- Extend, do not replace, v1 visual tokens/header/decision ask.
- Implement executive plus seven deep progressive views.
- Add proportional architecture diagrams and text equivalents from sources.
- Add task draft, validation, decision evolution and coverage/provenance states.
- Resolve Q-002 through an accessibility prototype.

### Out of scope

- Hosted editing, remote assets, semantic auto-approval and fixed universal
  diagram count.

### Outcome linkage

- Requirement/AC/discovery question: FR-001–006, FR-011, FR-013–015, FR-020.
- Vertical slice relation: delivers.
- Priority source or human decision: pending execution approval.

### Expected files and contracts

Canonical HTML/design standard, populated v2 example/006 brief and any static
render helper already compatible with the repository.

### Implementation constraints

All content remains in semantic HTML without script; any inline interaction is
progressive enhancement. Print must reveal deep content. No unsupported source
claim or sensitive detail.

### Validation IDs and commands

V-001, V-002, V-005–008, V-011; `python scripts/validate_bundle.py` plus
rendered manual checks.

### Evidence requirements

Source-to-view coverage matrix, rendered desktop/narrow/print artifacts,
keyboard/no-script notes, architecture provenance and evaluator findings.

### Exit criteria

- [x] human approval and T-001 approval are recorded;
- [x] v1 strengths and all eight v2 views are present;
- [x] every applicable principal heading is dispositioned;
- [x] tasks remain visibly draft and pre-approval gates were not fabricated;
- [x] architecture depth matches L/high profile without invented claims;
- [x] desktop/narrow/keyboard/no-script/print checks pass or gaps are recorded;
- [x] distinct evaluator approves the evidence pack and state is synchronized.

### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex acting as Orchestrator  
**Blocking conditions:** none; T-001 and human approval are recorded, and
distinct T-002 identities are assigned. Stop at `needs_evaluation`.

## T-003 — Implement version-aware coverage, freshness and evolution validation

**Status:** done  
**Revision note:** the evaluator requested precise coverage-row parsing,
baseline review/change metadata, an explicit v1 migration route and
record-specific propagation. After correction and freshness synchronization,
the distinct evaluator returned `approve`; State Keeper recorded
`approved -> done`.  
**Objective:** enforce the deterministic v2 contract while preserving v1
history and disclaiming semantic approval.  
**Requirement IDs:** FR-003–006, FR-008–009, FR-015, FR-017–019  
**Acceptance criteria IDs:** AC-002–003, AC-008, AC-010, AC-012  
**Outcome served:** incomplete or stale decision projections cannot silently
pass; existing consumers are not broken.  
**Demonstrable increment:** version-aware validator/baseline with precise
positive/negative fixtures for sources, headings, provenance, identity,
freshness, delta and migration.  
**Expected artifact/behavior:** v1 branch remains stable; v2 requires expanded
sources/coverage/reviewer metadata; baseline/delta schema is explicit.  
**Validation method:** V-002–003, V-008, V-010, V-012; V-REG-001/006.  
**Why now:** hard mirrors must match the final v2 DOM and lifecycle before
consumer rollout.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001, T-002.  
**Risk:** high  
**Builder:** Terra 5.6 high / t3_builder  
**Evaluator:** Terra 5.6 high / t3_evaluator  
**Human approval:** approved  
**Evidence:** evidence/T-003.md

### Scope

- Extend bundle and consumer validators with lineage-aware contracts.
- Expand freshness sources and baseline/change metadata.
- Check coverage/provenance, distinct review identity and new state gates.
- Resolve Q-003 and implement migration diagnostics.
- Add precise positive/negative/privacy fixtures.

### Out of scope

- Automatic semantic scoring, visual approval or external services.

### Outcome linkage

- Requirement/AC/discovery question: FR-003–006, FR-008–009, FR-015, FR-017–019.
- Vertical slice relation: directly enables.
- Priority source or human decision: pending execution approval.

### Expected files and contracts

`validate_human_visibility.py`, `validate_bundle.py`, baseline/schema handling,
unit fixtures and scaffold/consumer regression inputs.

### Implementation constraints

Prefer Python standard library; emit source/section-specific failures without
secret content; no structural success message may imply semantic approval.

### Validation IDs and commands

V-002, V-003, V-008, V-010, V-012; run validator, scaffolder and bundle suites.

### Evidence requirements

Fixture matrix with expected diagnostics, v1/v2/baseline migration results,
privacy sentinel result, commands/output and evaluator decision.

### Exit criteria

- [x] T-001/T-002 contracts are stable and human approval is recorded;
- [x] Q-003 is recorded;
- [x] all required negative cases fail precisely;
- [x] v1 historical fixture and v2 positive fixture pass;
- [x] freshness/delta and privacy behavior are verified;
- [x] T-003-focused and bundle regressions pass; known integration failures are assigned to T-004;
- [x] distinct evaluator approves the evidence pack and state is synchronized.

### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex acting as Orchestrator  
**Blocking conditions:** none; T-001/T-002, D-009 and D-014 are recorded with
distinct T-003 identities. Stop at `needs_evaluation`.

## T-004 — Integrate scaffolding, consumer guidance and post-meeting workflow

**Status:** done  
**Revision note:** Evaluator requested only state/brief freshness synchronization.
Builder applied it through `needs_evaluation -> needs_revision -> in_progress ->
needs_evaluation`: D-016, T-004 status/readiness history, handoff, brief and
v2 baseline now agree. No evaluator approval is claimed.
**Objective:** make v2 adoption and repeated decision meetings reproducible in
consumer repositories.  
**Requirement IDs:** FR-007–009, FR-015–019  
**Acceptance criteria IDs:** AC-004, AC-008–010, AC-012  
**Outcome served:** consumers scaffold the right contract and reliably turn
meeting decisions back into canonical spec changes before execution.  
**Demonstrable increment:** scaffolder, manifest, docs, prompts and Factory
fixture express the v2 order, approval boundary, migration and regeneration.  
**Expected artifact/behavior:** new initiative output uses v2; post-meeting
fixture propagates a decision; existing pinned v1 path remains supported.  
**Validation method:** V-004, V-008–010, V-012.  
**Why now:** validator/template changes are incomplete if consumers cannot invoke
the workflow safely.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001, T-003.  
**Risk:** medium  
**Builder:** Terra 5.6 high / t4_builder  
**Evaluator:** Terra 5.6 high / t4_evaluator  
**Human approval:** approved  
**Evidence:** evidence/T-004.md

### Scope

- Update scaffolder output, manifest, templates README and run-state docs.
- Update install/consumer enforcement and use-in-consumer prompt.
- Add the transcript/decision propagation/regeneration workflow example.
- Update Factory fixture/invocation and compatibility guidance.

### Out of scope

- Automatic transcription service or direct integration with meeting platforms.

### Outcome linkage

- Requirement/AC/discovery question: FR-007–009, FR-015–019.
- Vertical slice relation: delivers.
- Priority source or human decision: pending execution approval.

### Expected files and contracts

Scaffolder/manifest, consumer docs/prompts/fixtures, post-meeting workflow and
version/migration notes.

### Implementation constraints

Do not grant publish/release authorization. Consumer remains owner of invocation
and canonical initiative data.

### Validation IDs and commands

V-004, V-008–010, V-012; run scaffold and Factory regression suites.

### Evidence requirements

Scaffold tree/content diff, post-meeting propagation fixture, compatibility
result, consumer command output and evaluator decision.

### Exit criteria

- [x] upstream tasks and human approval are recorded;
- [x] new scaffold is coherent v2 and old pinned fixture is supported;
- [x] meeting decision flows through log and affected sources before refresh;
- [x] consumer/Factory instructions invoke the correct gates in order;
- [x] all integration regressions pass;
- [ ] distinct evaluator approves the evidence pack and state is synchronized.

### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex acting as Orchestrator  
**Blocking conditions:** none at release; transition recorded as `pending -> ready -> in_progress -> needs_evaluation`. Independent evaluator approval remains required before `done`.

## T-005 — Perform independent rendered/eval/regression validation and release handoff

**Status:** done  
**Objective:** prove the complete v2 outcome across deterministic, visual,
semantic and compatibility dimensions without self-approval.  
**Requirement IDs:** FR-001–020  
**Acceptance criteria IDs:** AC-001–012  
**Outcome served:** maintainers receive decision-grade evidence that v2 is
complete, usable, safe to adopt and reversible.  
**Demonstrable increment:** approved cross-role evals, render artifacts, full
regression output, residual risks, migration/release handoff and initiative
validation decision.  
**Expected artifact/behavior:** independent reviewers can decide release/adoption
from evidence; no task or initiative closes on author assertion.  
**Validation method:** V-001–012, E-001–003, M-001–006.  
**Why now:** it is the terminal proof after all implementation slices converge.  
**Max subtasks before validation:** 3  
**Dependencies:** T-002, T-003, T-004.  
**Risk:** medium  
**Builder:** Terra 5.6 high / t5_builder  
**Evaluator:** Terra 5.6 high / t5_evaluator  
**Human approval:** approved  
**Evidence:** evidence/T-005.md

### Scope

- Run every required command and collect outputs.
- Perform independent coverage, architecture and three-audience evals.
- Render desktop/narrow/keyboard/no-script/print artifacts.
- Reconcile sources/state/evidence, residual risks and release handoff.

### Out of scope

- Publishing/tagging/releasing without separate explicit authorization.

### Outcome linkage

- Requirement/AC/discovery question: all.
- Vertical slice relation: delivers.
- Priority source or human decision: pending execution approval; release separate.

### Expected files and contracts

Evidence pack, rendered artifacts, eval rubrics/results, regression logs,
progress/run-state/handoff and release recommendation.

### Implementation constraints

The Evaluator may not repair implementation while judging. Findings return to
the owning Builder/task. Release remains outside this task's authority.

### Validation IDs and commands

All entries in `validation-plan.md`.

### Evidence requirements

Complete AC/FR coverage, reviewer identities, working tree/revision, commands,
render/eval artifacts, findings, decisions, gaps and residual risk.

### Exit criteria

- [x] upstream tasks are done with approved evidence;
- [x] all V/M/E validations pass or have explicit approved exceptions;
- [x] three reviewer perspectives and v1 compatibility are evidenced;
- [x] no blocker/high finding remains;
- [x] residual risk and rollback are recorded;
- [x] distinct evaluator approves the pack;
- [x] run-state/progress/handoff are synchronized; release remains pending because it is not authorized.

### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex acting as Orchestrator  
**Blocking conditions:** none at release; T-002/T-003/T-004 are done, human
approval and distinct identities are recorded. Stop at `needs_evaluation` and
do not release/publish/tag.
