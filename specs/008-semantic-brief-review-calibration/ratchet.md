# Ratchet Log: 008-semantic-brief-review-calibration

Serious first-time or recurring preventable failures are appended here using
`ratchet-entry.md`. An entry is `implemented` only after its prevention and
regression check are verified.

## Index

| ID | Failure type | Severity | Status | Owner | Regression check |
|---|---|---|---|---|---|
| R-001 | state_loss | medium | verified | Codex / State Keeper | D-007 reconciliation + D-008/D-009 evaluator review |

## Entries

## Ratchet Entry: R-001

**Date/detected by:** 2026-08-25 / `/root/sandbox_coverage_review`  
**Failure type:** state_loss  
**Severity:** medium  
**Occurrence:** first_serious  
**Status:** verified  
**Owner:** Codex / State Keeper  
**Related task/evidence:** T-001–T-004; `decision-log.md#D-007`; `evidence/T-004.md`

### Failure and impact

The bundle and sandbox implementation diffs existed while the initiative still
presented the pre-authorization planning state. A false close would have hidden
the missing independent task evaluation and would have made the derived brief
contradict its canonical sources.

### Root cause

The existing resume rule required reconciliation, but it did not name the
moment when a direct stakeholder execution authorization must become a
checkpoint before any implementation artifact changes.

### Prevention

At that authorization boundary, record the decision and synchronize state,
progress and handoff first; refresh the brief if decision-relevant. If the
boundary is discovered late, stop and send affected tasks to
`needs_evaluation`, without self-approving the completed work.

### Artifact change

- [x] soft rule
- [ ] hard mirror
- [x] test/eval
- [ ] template
- [x] skill/workflow
- [ ] documentation

**Exact change/link:** `.harness/rules/state-and-memory.md` —
“Execution-authorization checkpoint”; D-007; evaluator review of all evidence
packs.

### Regression check

**Check/command:** distinct evaluator compares `run-state.yaml`, `progress.md`,
handoff, decision log, evidence and brief before terminal approval.  
**Expected failure before prevention:** authorization or implementation can
appear only in diffs/evidence while planning state stays pending.  
**Expected pass after prevention:** D-007 and the three state artifacts agree;
the brief is regenerated and no task becomes `done` before independent
approval.  
**Verification evidence:** D-008 returned the divergence instead of accepting
release; D-009 accepted the corrected state only after the brief/validator
reconciliation; D-010 passed the final baseline and checks.
