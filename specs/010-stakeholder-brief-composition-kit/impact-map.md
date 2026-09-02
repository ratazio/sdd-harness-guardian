# Impact Map: 010-stakeholder-brief-composition-kit

**Status:** draft, mapped for review  
**Spec:** [spec.md](./spec.md)  
**Mapped by:** platform-engineering  
**Reviewed at:** not yet independently reviewed  
**Overall risk:** medium

## Change boundary

This changes reusable authoring guidance, the v2 stakeholder-brief template,
fixtures and non-semantic checks so a source-backed brief can choose a richer
visual composition. It must preserve canonical Markdown/state authority, v1
legacy behavior, offline single-document output and the existing independent
semantic review. It does not implement a customer brand, an application UI,
remote renderer or post-processing agent.

## Affected surfaces

| Surface | Expected change | Risk | Source / control |
|---|---|---|---|
| Authoring workflow | One composition/depth-selection step before render. | medium | FR-001–FR-006; no separate agent state. |
| Architecture/impact views | Macro relation and optional one-level focus cut; visual impact patterns. | high | FR-002–FR-004, FR-007; provenance + reviewer trace. |
| Execution/validation views | Reusable rich task/proof projections, sparse variants and source-to-render parity guard. | high | FR-005–FR-006, FR-009, FR-013–FR-014; task source remains canonical. |
| Coverage/accessibility | Grouped provenance with semantic equivalent; responsive/print/no-script recovery. | high | FR-008, FR-010; manual accessibility review. |
| Tests/docs | Rich/sparse/non-software fixtures and structural regression checks. | medium | FR-011; no semantic score. |
| Brand/client identity | not_applicable — profile styling is owned by 011. | low | FR-012. |

## Dependency and information flow

    canonical Markdown -> source-sufficiency decision -> selected mini-template
    -> single derived HTML + provenance -> independent reviewer -> source correction/regeneration

## Compatibility, rollout and rollback

- **Compatibility:** v1 is unchanged; v2 tabs/provenance/fallback remain.
- **Migration:** additive guidance/template/component catalogue only; no
  consumer initiative data migration.
- **Rollout:** validate fixtures and release as a versioned bundle change.
- **Rollback:** restore the prior template/guidance/fixture set together if a
  regression hides content, fabricates depth or breaks access.

## Risks and controls

| ID | Risk event | Signal | Control | Contingency / owner | Validation |
|---|---|---|---|---|---|
| IR-001 | Focus cut invents internal architecture. | No source section or decision connection. | Depth ladder and source trace. | Remove/correct source and rerender; template owner. | V-002, E-004 |
| IR-002 | Task card becomes a parallel contract. | Card conflicts with tasks.md. | Project only non-empty source fields. | Correct Markdown, not HTML alone; planner. | V-004, E-004 |
| IR-003 | Sparse/non-software case receives forced software visuals. | Fixture shows empty technical rows or decorative graph. | Paired sparse/non-software fixtures. | Simplify pattern; Spec Guardian. | V-003, E-003 |
| IR-004 | Rich composition hides content on narrow/print/no-script. | Unreachable/overflowing content. | Semantic equivalents, progressive fallback, manual inspection. | Revert affected pattern; accessibility owner. | V-005–V-007 |
| IR-005 | Deterministic tests become semantic score. | Parser/threshold judges prose or aesthetics. | FR-011 code review and negative test. | Remove the check; bundle maintainer. | V-008 |
| IR-006 | A generated/linkable brief is still a generic scaffold after tasks/ACs exist. | Execution/Validation lack populated source identifiers. | Parity guard and visible draft lifecycle label. | Regenerate before sharing; release owner. | V-011, V-012 |

## Unknowns

| ID | Unknown | Impact | Owner / resolution | Blocks? |
|---|---|---|---|---|
| U-001 | Smallest existing file/skill surface for component catalogue. | A duplicate guidance location would fragment authoring. | T-001 inventories and selects one home. | no |
| U-002 | Whether current fixtures exercise both sparse and non-software selection. | Missing calibration allows rigid pattern. | T-001/T-004 add only necessary fixture. | no |
| U-003 | Exact mobile card/table switch threshold. | May affect readability but not semantic selection. | T-003 validates at 320/390 and chooses content-led breakpoint. | no |

## Impact decision

**Impact mapped:** yes  
**Human review required:** yes — reviewer must reject unsupported visual detail.  
**Conditions before implementation:** resolve U-001/U-002 through bounded
discovery; no template change before a preliminary task becomes ready.
