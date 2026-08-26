# Tasks: 008-semantic-brief-review-calibration

**Status:** done — D-010 recorded the passing post-approval baseline and final deterministic validation.  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-25

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Make semantic and post-render review explicit | none | medium | Codex / builder-008 | /root/sandbox_coverage_review | evidence/T-001.md |
| T-002 | done | Add calibration and shallow-negative fixtures | T-001 | medium | Codex / builder-008 | /root/sandbox_coverage_review | evidence/T-002.md |
| T-003 | done | Protect structural-only boundary and v1 compatibility | T-001, T-002 | high | Codex / builder-008 | /root/sandbox_coverage_review | evidence/T-003.md |
| T-004 | done | Independently validate rendered package | T-001–T-003 | medium | Codex / builder-008 | /root/sandbox_coverage_review | evidence/T-004.md |

## Authorization boundary

The task descriptions began as preliminary discussion drafts. `tasks_drafted` did
**not** mean `tasks_ready`; D-006 authorization and D-007 propagation satisfied
the separate readiness boundary before implementation. All four tasks are now
in `needs_evaluation`, so neither their completed diffs nor this text implies a
terminal approval.

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

### T-001 — Make semantic and post-render review explicit

**Status:** done — approved by the distinct evaluator in D-008.  
**Objective:** Add product, architecture/operations and delivery lenses, source → lost fact → recovery action, and the post-render decision-loss question.  
**Requirement IDs:** FR-001–004  
**Acceptance criteria IDs:** AC-001, AC-003  
**Outcome served:** reviewers repair shallow synthesis without a score.  
**Demonstrable increment:** review record distinguishes coverage from rendered meaning.  
**Validation method:** V-001, V-003, E-001.  
**Why now:** establishes vocabulary for examples/tests.  
**Dependencies:** none; **Risk:** medium; **Evidence:** evidence/T-001.md.

**Scope:** existing review skill/agent/workflow/template wording; reuse existing roles and records.  
**Out of scope:** permanent agent, sidecar state, automated semantic approval or v1 change.  
**Expected files/contracts:** review guidance and lifecycle surfaces identified by T-001; decision log stays canonical.  
**Exit criteria:** three lenses/N-A discoverable; findings identify source/fact/action; review moments differ; no role/state/score added.  
**Task Ready:** yes — D-007 reconciled the explicit D-006 execution authorization; implementation is complete and awaits distinct evaluation.

### T-002 — Add calibration and shallow-negative fixtures

**Status:** done — approved by the distinct evaluator in D-008.  
**Objective:** Create one software, one non-software and one shallow-but-formal fixture.  
**Requirement IDs:** FR-005  
**Acceptance criteria IDs:** AC-002, AC-004, AC-007  
**Outcome served:** expectations generalize without rigid rules.  
**Demonstrable increment:** reviewers can compare sufficient and insufficient synthesis.  
**Validation method:** V-002, V-004, M-001–003, E-002.  
**Why now:** turns guidance into observable calibration.  
**Dependencies:** T-001; **Risk:** medium; **Evidence:** evidence/T-002.md.

**Scope:** fictional sources, review records, briefs and focused static checks.  
**Out of scope:** customer data, sample application, or forced diagrams where non-software has no architecture trigger.  
**Exit criteria:** both domains expose outcome, impact/risk/control, validation, state, decision and next step; negative fixture is caught; rendered checks recorded.  
**Task Ready:** yes — D-007 reconciled the explicit D-006 execution authorization; implementation is complete and awaits distinct evaluation.

### T-003 — Protect structural-only boundary and v1 compatibility

**Status:** done — approved by the distinct evaluator in D-008.  
**Objective:** Prevent semantic scoring while preserving v1 lineage.  
**Requirement IDs:** FR-006, FR-007  
**Acceptance criteria IDs:** AC-005, AC-006  
**Outcome served:** quality improves without overfitting or migration harm.  
**Demonstrable increment:** diff review and v1 fixture establish the boundary.  
**Validation method:** V-005, V-006, V-REG-002–003.  
**Why now:** prevents scope expansion during fixture/test work.  
**Dependencies:** T-001, T-002; **Risk:** high; **Evidence:** evidence/T-003.md.

**Scope:** focused validator/test review and a mirror only if fixtures prove a stable invariant.  
**Out of scope:** prose scoring, LLM judge, word thresholds, schema changes or v1 migration.  
**Exit criteria:** no score/parser/gate in diff; v1 fixture passes; any mirror has need/cost/removal record.  
**Task Ready:** yes — D-007 reconciled the explicit D-006 execution authorization; implementation is complete and awaits distinct evaluation.

### T-004 — Independently validate rendered package

**Status:** done — independently approved with release acceptance in D-009.  
**Objective:** Validate source/brief meaning, accessibility/readability and package regressions independently.  
**Requirement IDs:** FR-001–007  
**Acceptance criteria IDs:** AC-001–008  
**Outcome served:** bundle change is useful and bounded before release.  
**Demonstrable increment:** approved evidence resolves whether calibration prevents the observed failure.  
**Validation method:** M-001–003, E-001–003, V-007, `validate_bundle.py`.  
**Why now:** evidence, not author confidence, proves completion.  
**Dependencies:** T-001–T-003; **Risk:** medium; **Evidence:** evidence/T-004.md.

**Scope:** independent evaluation and evidence.  
**Out of scope:** evaluator fixes; it requests revision instead.  
**Exit criteria:** every AC has proof/approved exception; rendered checks cover 60-second/narrow/keyboard/no-script/print; independent decision and maintainer release decision recorded.  
**Task Ready:** yes — D-007 reconciled the explicit D-006 execution authorization; implementation is complete and awaits distinct evaluation.
