# Impact Map: 005-stakeholder-brief-meeting-standard

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex acting as Impact Mapper  
**Reviewed at:** 2026-08-18  
**Overall risk:** medium

## Change boundary

Evolve the canonical stakeholder-brief design contract, authoring path and
consumer validator. Retrofit only 004. Preserve source Markdown as canonical,
static HTML and the existing Human Visibility gate.

| Surface | Change | Risk | Evidence |
|---|---|---|---|
| Brief template | Visual shell, design marker, decision/evidence panels | medium | AC-002, AC-004 |
| Design guidance | New brief-specific design standard | medium | AC-001 |
| Validator/tests | Lineage/shell and decision-log exception checks | medium | AC-003, AC-009 |
| Agent/workflow guidance | Populate, do not reconstruct; render review | medium | AC-008 |
| 004 regression | Rebuild into canonical design | medium | AC-006, AC-007 |

```txt
canonical sources -> populated canonical brief -> lineage check + rendered review -> meeting decision
```

## Regression risks

| Risk | Mitigation |
|---|---|
| Marker pass is mistaken for visual quality | Explicit HUMAN REVIEW output and rendered review. |
| Optional views become ritual | Require named concern/audience/purpose or omission reason. |
| Brief duplicates or stales | Source links and existing freshness validation. |

**Impact mapped:** yes  
**Human review required:** yes  
**Condition:** Plan/validation ready before implementation.
