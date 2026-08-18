# Technical Plan: 005-stakeholder-brief-meeting-standard

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-18

## Approach

Add `stakeholder-brief-design.md` beside the template. Extend the canonical
HTML—not a replacement—with `data-harness-brief-design="v1"`, stable shell
hooks and concise decision/trade-off, impact/evidence and open-action panels.
Extend the consumer validator to require that contract or a reviewed entry in
the existing decision log. Update authoring guidance, fixture tests and 004.

| Decision | Choice | Consequence |
|---|---|---|
| Lineage | `data-harness-brief-design="v1"` | Stable, inspectable, not a visual-score proxy. |
| Exception | Reviewed decision-log entry | No new sidecar; parser convention must be documented/tested. |
| Views | C4-light/impact/flow only for named concern | Information-rich without diagram ritual. |

**Size:** M — template, validator, guidance, tests and retrofit move together.  
**Smaller option rejected:** instruction-only; 004 already bypassed it.  
**Excluded:** JavaScript, external assets, LLM judge, screenshot CI, Factory changes.

## Sequence

1. Design standard and enriched template.
2. Validator/fixtures for lineage and reviewed exception.
3. Guidance and 004 retrofit.
4. Rendered desktop/narrow review plus regression suite.

**Plan Ready:** yes  
**Reviewer:** Codex acting as Harness Planner
