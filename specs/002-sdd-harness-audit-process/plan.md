# Technical Plan: 002-sdd-harness-audit-process

**Status:** plan_ready  
**Spec:** ./spec.md  
**Owner:** platform-engineering  
**Last updated:** 2026-07-25

## 1. Approach

Add audit capability as passive bundle artifacts:

- agents for audit synthesis and graph mapping;
- rule defining audit blocking conditions and hard mirror recommendation;
- workflow for audit phases and specialist roles;
- skill containing the procedural audit method;
- HTML report template with stable sections;
- docs framework distilling supplied source knowledge;
- manifest and entrypoint wiring.

## 2. Decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | Use an agent-authored HTML template, not a script-only report. | User requested complex agentic judgment with stable structure. | Deterministic simplistic Python generator. | Audits require evaluator review. |
| D-002 | Store source knowledge as framework docs, not inside the skill body. | Skills should carry method; knowledge remains separate. | Copy large HTML-derived content into SKILL.md. | Auditor must read docs when needed. |
| D-003 | Make graph reachability mandatory. | File existence alone hides unused methodology. | Checklist-only audit. | Findings can include orphan/weak artifacts. |

## 3. Change sequence

| Step | Area | Output | Validation |
|---|---|---|---|
| 1 | Agents/rule/workflow/skill | audit capability registered | manifest + structural review |
| 2 | Template/docs/memory | report contract and knowledge baseline | file review |
| 3 | Entry docs | discoverability | README/AGENTS review |
| 4 | Validation | bundle validator and smoke test | commands |

## 4. Rollback

Revert the added audit artifacts and manifest registrations. Existing SDD
workflow remains unaffected.
