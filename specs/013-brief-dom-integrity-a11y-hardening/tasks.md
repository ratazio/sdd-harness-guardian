# Tasks: 013-brief-dom-integrity-a11y-hardening

**Status:** T-001–T-003 complete and independently approved; T-004 is in progress.  
**Authority:** D-009 approves T-001, D-011 approves T-002, and D-013 approves T-003. D-014 authorizes the release-only T-004; it remains non-terminal until its own distinct evaluation.

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Define rendered parser and static-tab fixture contract | D-006/D-007 | medium | Codex / implementation builder | evaluate_t001_013 | evidence/T-001.md |
| T-002 | done | Enforce rendered duplicate-ID and post-document integrity | T-001 done / D-010 | medium | Codex / implementation builder | evaluate_t002_013 | evidence/T-002.md |
| T-003 | done | Enforce conditional accessible tab mechanics | T-001 done / D-012 | medium | Codex / implementation builder | evaluate_t003_013 | evidence/T-003.md |
| T-004 | done | Release diagnostics and regression matrix | T-002,T-003 done | medium | Codex / implementation builder | evaluate_t004_013 | evidence/T-004.md |

Allowed transition: `pending → ready → in_progress → needs_evaluation → approved → done`; a distinct evaluator alone may approve. Every task updates evidence, decision-log, ledger, run-state, progress and brief before `done`.

### T-001 — Define rendered parser and static-tab fixture contract

**Objective:** resolve U-001/U-002 with a minimal parser boundary and static-contract oracle before production validation changes.  
**Requirement / acceptance:** FR-001–FR-004; AC-001–AC-004.  
**Outcome and increment:** reviewed fixture matrix identifies rendered versus inert input, permitted tails, v1/non-tab controls, reciprocal tab state and canonical handler tokens; it reduces uncertainty without an implementation claim.  
**Why now:** T-002/T-003 would otherwise encode brittle or over-broad heuristics. **Dependencies:** planning/brief gates and D-004 task-selection decision. **Risk:** medium.

**Scope:** inspect current parser/canonical script; add or stage only focused probes/fixtures needed to prove the boundary; document accepted controls and negatives.  
**Out of scope:** changing production validator/templates, profiles, browser automation, scoring or broad a11y certification.

**Expected files/contracts:** `plan.md` §§6/10, fixture/test records and `evidence/T-001.md`. The contract states `script`, `style`, `template` are inert; non-comment/non-whitespace rendered tail is forbidden; static evidence is not runtime proof.

**Validation:** V-001–V-004 fixture probe; existing focused suite only if touched. **Evidence:** grammar, rejected alternatives, matrix, command result if run, limitation and distinct evaluator decision.

**Exit criteria:**

- [ ] U-001/U-002 resolved with a bounded decision.
- [ ] Every AC has a negative and applicable control fixture.
- [ ] v1, tabless v2, inert and permitted trailing content are explicit.
- [ ] No production validator/template change claimed complete.
- [ ] Distinct evaluator approves evidence.

**Readiness:** in progress — D-006/D-007 authorize discovery only.

### T-002 — Enforce rendered duplicate-ID and post-document integrity

**Objective:** implement FR-001/FR-002 using T-001’s approved parser contract.  
**Requirement / acceptance:** FR-001, FR-002, FR-005; AC-001, AC-002, AC-005.  
**Outcome and increment:** malformed rendered duplicate IDs or tail content cannot pass locally; inert/permitted controls remain valid.  
**Why now:** T-001 removes false-positive risk. **Dependencies:** T-001 done. **Risk:** medium.

**Scope:** update parser/checker and focused tests; keep reports rule/ID-only.  
**Out of scope:** tab semantics, browser execution, source-location claims, template/profile change.

**Expected files/contracts:** validator, focused test/fixture only as needed, `evidence/T-002.md`.  
**Validation:** V-001, V-002, V-005 and focused suite. **Evidence:** negative/control outputs, redaction observation, evaluator decision, residual risk.

**Exit criteria:**

- [ ] Known/arbitrary rendered duplicate IDs fail and name only ID/rule.
- [ ] Rendered material after final close fails.
- [ ] Inert literals and permitted whitespace/comments pass.
- [ ] Focused suite passes; distinct evaluator approves.

**Readiness:** pending T-001 done.

### T-003 — Enforce conditional accessible tab mechanics

**Objective:** implement FR-003/FR-004 only for v2 briefs declaring a tablist, retaining native anchors, no-script/source-order and print semantics.  
**Requirement / acceptance:** FR-003, FR-004; AC-003, AC-004.  
**Outcome and increment:** click-only/miswired/multi-selected/missing-handler tabs fail; v1, tabless v2 and canonical tabs pass.  
**Why now:** closes the mock-suite keyboard blind spot. **Dependencies:** T-001 done. **Risk:** medium.

**Scope:** conditional static check/fixtures for reciprocal references, selection, roving `tabindex` and handler evidence.  
**Out of scope:** JS execution, browser/AT conformance claims, forcing tabs or visual-template work.

**Expected files/contracts:** validator, focused tests/fixtures, `evidence/T-003.md`; static evidence retains Arrow keys, Home/End, Enter/Space, focus, selection, active panel and hash mutation.  
**Validation:** V-003/V-004 and focused suite. **Evidence:** result matrix, preserved fallback/print statement, evaluator decision and runtime limitation.

**Exit criteria:**

- [ ] Invalid declared-tab controls fail with bounded diagnostics.
- [ ] Canonical tabbed v2 passes.
- [ ] v1 and v2 without tablist remain outside tab check.
- [ ] Focused suite passes; distinct evaluator approves.

**Readiness:** pending T-001 done.

### T-004 — Release diagnostics and regression matrix

**Objective:** prove combined checks are releasable and leave recoverable evidence/state.  
**Requirement / acceptance:** FR-005; AC-005 plus all regression controls.  
**Outcome and increment:** focused, bundle and brief-visibility proof prevent silent recurrence of M-006–M-008.  
**Why now:** only both increments support release. **Dependencies:** T-002/T-003 done. **Risk:** medium.

**Scope:** diagnostic/redaction tests, full commands, independent review, state/brief synchronization and reviewer-approved baseline refresh.  
**Out of scope:** new runtime, deploy, semantic score or self-approval.

**Expected files/contracts:** only justified test/guidance changes; evidence, decision/progress/state/brief, baseline and handoff.  
**Validation:** V-001–V-005; `python scripts/test_validate_human_visibility.py`; `python scripts/validate_bundle.py`; initiative baseline write/recheck.

**Exit criteria:**

- [ ] Combined focused and bundle checks pass.
- [ ] Independent evaluator verifies fixture realism and redaction.
- [ ] Baseline/recheck succeeds after approval.
- [ ] Evidence, decisions, ledger, state, progress and brief agree.
- [ ] Distinct evaluator approves before `done`.

**Readiness:** in progress — D-014 follows the completed, independently approved T-002/T-003 increments. T-004 must not move to `done` before its own distinct evaluator approves the combined release evidence.
