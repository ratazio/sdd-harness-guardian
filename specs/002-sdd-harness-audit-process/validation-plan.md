# Validation Plan: 002-sdd-harness-audit-process

**Status:** validation_ready  
**Spec:** ./spec.md  
**Owner:** platform-engineering  
**Last updated:** 2026-07-25

## Validation matrix

| ID | Covers | Type | Method | Success condition | Evidence |
|---|---|---|---|---|---|
| V-001 | AC-001 | structural | inspect `manifest.yaml` and run bundle validator | audit agents, skill, workflow, rule and template registered | evidence/T-001.md |
| V-002 | AC-002/003/005 | semantic | inspect skill, workflow and framework docs | audit process covers SDD, graph, agents/skills, memory and enforcement | evidence/T-001.md |
| V-003 | AC-004 | semantic | inspect HTML template | required report sections are present | evidence/T-001.md |
| V-004 | AC-006 | command | `python scripts/validate_bundle.py`; `python scripts/smoke_test_scaffolder.py` | both commands pass | evidence/T-001.md |

## Evidence requirements

- command output summary;
- files changed summary;
- known limitation that independent evaluator approval is still required before
  terminal `done`.
