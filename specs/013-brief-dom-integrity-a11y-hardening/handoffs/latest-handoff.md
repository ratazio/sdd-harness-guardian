# Handoff: 013-brief-dom-integrity-a11y-hardening

**From:** Codex / implementation builder  
**Intended role/recipient:** distinct T-004 evaluator  
**Created at:** 2026-08-27  
**Current phase/status:** execute / release evidence pending independent evaluation  
**Current task/status:** T-004 / in_progress  
**Last safe checkpoint:** D-015 records a clean focused/bundle/baseline matrix; no T-004 approval exists.  
**Repository revision/working-tree summary:** repository has unrelated in-progress work; this handoff concerns only SPEC 013 artifacts and the validator/template changes already covered by T-002/T-003 evidence.

## 1. Completed and approved work

- T-001 is done under D-009, T-002 under D-011, and T-003 under D-013.
- The tab contract is conditional on declared v2 tablists and has no fixed tab/view/content-layout count.

## 2. Partial or unverified work

- T-004 evidence exists at `evidence/T-004.md`, but requires a distinct evaluation.

## 3. Files changed

| File | State | Reason |
|---|---|---|
| `tasks.md`, `decision-log.md`, `progress.md`, `run-state.yaml`, `stakeholder-brief.html` | synchronized | Align T-001–T-003 approvals, T-004 gate and the non-fixed per-tablist initializer. |
| `human-visibility-baseline.json` | refreshed | Source/brief hashes after the synchronized release projection. |
| `evidence/T-004.md` | draft evidence | Matrix, boundary and evaluator request. |

## 4. Validations and evidence

| Task/check | Result | Evidence |
|---|---|---|
| focused Human Visibility suite | PASS | `evidence/T-004.md` |
| bundle validation | PASS — 267 checks | `evidence/T-004.md` |
| SPEC 013 baseline write/recheck | PASS | `evidence/T-004.md` |

## 5. Decisions and approvals

D-009, D-011 and D-013 are the distinct approvals for T-001–T-003. D-014 authorizes T-004 evidence only; D-015 is a builder checkpoint, not an approval.

## 6. Blockers, unknowns and risks

The remaining blocker is the mandatory evaluator decision for T-004. Deterministic checks do not replace its semantic/rendered review.

## 7. Exact next safe step

Independently inspect `evidence/T-004.md`, `stakeholder-brief.html` and the release commands. If accepted, record an evaluator decision, transition T-004 through `approved` to `done`, then synchronize state; otherwise return only the affected task to revision.

## 8. Resume reading order

1. `run-state.yaml`
2. `progress.md`
3. this handoff
4. repository status
5. current task and evidence
6. `validation-plan.md` and `decision-log.md`

## 9. Do not do

Do not use a fixed tab count, require a standard architecture layout, treat a structural PASS as accessibility certification, or mark T-004 done without a distinct evaluator.
