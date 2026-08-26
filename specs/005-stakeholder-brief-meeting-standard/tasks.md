# Tasks: 005-stakeholder-brief-meeting-standard

**Status:** validation_done  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-25

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Design standard, template and validator contract | plan | medium | Terra 5.6 implementation agent | Codex acting as Delivery Orchestrator | evidence/T-001.md |
| T-002 | done | Guidance, fixtures and 004 retrofit | T-001 | medium | Terra 5.6 implementation agent | Codex acting as Delivery Orchestrator | evidence/T-002.md |
| T-003 | done | Render/regr​ession validation and evidence | T-001, T-002 | low | Terra 5.6 implementation agent | Codex acting as Delivery Orchestrator | evidence/T-003.md |

## T-001 — Design standard, template and validator contract

**Requirement IDs:** FR-001–005, FR-009  
**Acceptance criteria:** AC-001–004  
**Outcome:** A bare custom page cannot silently satisfy the canonical brief contract.  
**Validation:** V-001–004.  
**Why now:** All later guidance and retrofit depend on this contract.  
**Evidence:** evidence/T-001.md

## T-002 — Guidance, fixtures and 004 retrofit

**Requirement IDs:** FR-006–011  
**Acceptance criteria:** AC-005–008  
**Outcome:** Authors can follow the standard and 004 becomes the concrete regression.  
**Validation:** V-003, V-005, V-007.  
**Evidence:** evidence/T-002.md

## T-003 — Render/regression validation and evidence

**Requirement IDs:** FR-001–011  
**Acceptance criteria:** AC-009  
**Outcome:** Delivered contract is reproducible and reviewable.  
**Validation:** V-006–008.  
**Evidence:** evidence/T-003.md

`done` requires an evidence pack and an independent approval; no task may skip
`needs_evaluation`.
