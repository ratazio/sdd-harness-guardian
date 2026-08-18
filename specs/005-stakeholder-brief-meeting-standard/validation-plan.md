# Validation Plan: 005-stakeholder-brief-meeting-standard

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-18

## Strategy

Use deterministic template/scaffold/consumer fixtures for stable contracts;
render 004 and the template at desktop/narrow sizes for human meaning and
accessibility review. A green machine check never approves visual quality.

| ID | AC | Method | Expected result |
|---|---|---|---|
| V-001 | AC-001 | design-guide inspection | Dedicated standard and linked authoring path. |
| V-002 | AC-002 | scaffolder/template test | Marker, shell and resolved placeholders. |
| V-003 | AC-003 | negative validator fixtures | Missing marker/shell fails; valid reviewed exception passes. |
| V-004 | AC-004–005 | template review | Decision/evidence panels and conditional view contract. |
| V-005 | AC-006 | 004 validation + rendered review | Canonical visual standard and concrete content. |
| V-006 | AC-007 | desktop/narrow review | No clipping; proof/trade-off/decision recovered in five minutes. |
| V-007 | AC-008 | prompt/rule review | Explicit populate-not-rebuild and exception path. |
| V-008 | AC-009 | full suite | Bundle, consumer validator, scaffolder and new tests pass. |

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex acting as Harness Planner
