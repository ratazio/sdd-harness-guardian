# Impact Map: 003-stakeholder-brief-enrichment

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex using the impact-analysis skill  
**Reviewed at:** 2026-08-12  
**Overall risk:** medium

## 1. Change boundary

Change the reusable authoring, visual and review contract for the existing
`stakeholder-brief.html`. Preserve the passive bundle architecture, canonical
initiative layout, scaffold command, source-of-truth boundaries, lifecycle
states and evidence protocol.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| HTML template | `.harness/templates/stakeholder-brief.html` | direct | Decision-first layout, sizing, conditional visual patterns and embedded checklist guidance. | medium | FR-001–FR-007 |
| Author guidance | `.harness/rules/human-visibility.md`, existing `spec-review`/`impact-analysis` skills and agent prompts | direct | One concise synthesis procedure and conditional checklist; no new skill or agent. | medium | FR-002–FR-008 |
| Human visibility rule | `.harness/rules/human-visibility.md` | direct | Define proportionality, visual triggers, filler rejection and minimal hard mirror. | medium | FR-003–FR-011 |
| Agent contracts | `.harness/agents/spec-guardian.md`, `.harness/agents/delivery-orchestrator.md` | direct | Assign refresh and short semantic/visual review explicitly. | low | FR-008, FR-010 |
| Lifecycle | `.harness/workflows/sdd-lifecycle.md`, possibly specialized workflows | direct | Clarify author/refresh/review within the existing gate; no new transition. | low | FR-008 |
| Planning source | `.harness/templates/plan.md` | direct | Add a compact size/proportionality decision as source for the brief. | low | FR-003 |
| Structural validation | `scripts/validate_bundle.py`, `scripts/smoke_test_scaffolder.py` | direct | Check stable IDs, sources and placeholders in template/scaffold output. | medium | FR-009 |
| Architecture/docs | `docs/architecture.md`, `docs/operating-model.md`, template guide, README/INSTALL if needed | indirect | Explain brief as primary meeting surface but derived view. | low | AC-007 |
| Consumer initiatives | future `specs/NNN-slug/stakeholder-brief.html` | indirect | Richer default on new scaffold; existing briefs change only when intentionally refreshed. | medium | AC-001 |
| Runtime/product code | none | untouched | No application, service, database or infrastructure behavior changes. | low | NG-002 |

## 3. Dependency and control flow

```txt
spec.md + impact-map.md + plan.md + validation-plan.md
                         |
                         v
       existing author guidance + conditional checklist
                         |
                         v
              stakeholder-brief.html
                         |
             +-----------+-----------+
             |                       |
      Spec Guardian review     Orchestrator gate
             |                       |
             +---- Human Visibility Ready ----> task breakdown
```

The current author synthesizes a derived view using existing guidance. The Spec
Guardian judges coherence and visual meaning. The Orchestrator controls the existing transition. None becomes a new
runtime engine or source of product intent.

## 4. Compatibility and migration

- **Backward compatibility:** preserve existing core section IDs where useful;
  existing consumer briefs remain valid until an initiative is refreshed.
- **Data migration:** none.
- **Rollout/feature flag:** release in a new bundle version; consumers receive it
  when they update their pinned submodule.
- **Rollback implications:** revert the template/guidance commit or pin the prior
  bundle tag. Initiative source Markdown is unaffected.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | Scaffold stops creating a usable brief. | template/scaffolder | Existing smoke plus enriched content assertions. | V-001, V-007 |
| IR-002 | Validator becomes a semantic bureaucracy engine. | validation script | Limit checks to IDs, links, metadata and placeholders. | V-006 |
| IR-003 | New guidance contradicts the derived-artifact boundary. | rule/skill/docs | Cross-file phrase and semantic review. | V-003, V-005 |
| IR-004 | Responsive layout or SVG clips content. | HTML/CSS | One desktop and one narrow visual inspection. | V-004 |
| IR-005 | Conditional visuals become universally mandatory. | rule/skill/template | Test both non-trivial and localized examples in guidance. | V-003 |
| IR-006 | Existing initiative work is forced into a migration. | consumer compatibility | Explicit prospective adoption; no bulk rewrite. | V-005 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Whether 600–900 visible words is the right normal range across consumers. | Too low can hide risk; too high can waste review time. | Treat as guidance and revisit from adoption feedback; maintainer. | no |
| U-002 | Whether existing guidance is discoverable enough across agent environments. | Poor discovery could reduce consistency, but a new skill would add maintenance before evidence exists. | Start with existing rule/skills/agents; reconsider only after adoption evidence. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** Spec Guardian plus one stakeholder for the first adoption.
- **Automated:** bundle validator, scaffolder smoke, placeholder/section/source assertions.
- **Manual/operational:** render the template at desktop and narrow viewport; run
  the 60-second decision test. No screenshot evidence is required by default.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** no additional approval beyond the user's explicit
direction and the existing Human Visibility review  
**Approval/evidence:** this map plus rendered `stakeholder-brief.html`  
**Conditions before implementation:** keep changes within the listed bundle
surfaces; any new state file, gate, external renderer or mandatory semantic
scoring requires returning to spec review.
