# Impact Map: 011-stakeholder-brief-client-identity-profile

**Status:** draft, mapped for review  
**Spec:** [spec.md](./spec.md)  
**Mapped by:** platform-engineering  
**Reviewed at:** not yet independently reviewed  
**Overall risk:** medium

## Change boundary

This introduces an opt-in Pearson visual profile for the existing stakeholder
brief. It may add local assets, CSS tokens, component variants, profile
selection guidance, fixtures and accessible visual checks. It must not hard-code
Pearson into unselected consumers, change canonical facts/gates, hotlink the
logo/font, claim trademark permission or turn an operational brief into a
marketing site.

## Affected surfaces

| Surface | Expected change | Risk | Source / control |
|---|---|---|---|
| Consumer selection | Explicit profile and brand-owner approval record. | high | FR-001, FR-009–FR-010. |
| Local assets | White logo and optional local font package workflow. | high | FR-003, FR-008; no remote runtime fetch. |
| Brief shell | Navy header, tokens, typography, card/radius/spacing variants. | medium | FR-002–FR-004. |
| Impact/coverage | Footprint/risk/provenance components with semantic equivalents. | high | FR-004–FR-006. |
| Accessibility/print | Contrast/focus/reflow/motion/no-script/print verification. | high | FR-006–FR-007. |
| Vendor-neutral default | No asset/token/profile leakage when not selected. | high | FR-001, AC-001. |
| Legal/brand process | Owner confirmation rather than an inferred license. | high | FR-010. |

## Dependency and asset flow

    consumer profile selection + brand owner record -> local approved asset/tokens
    -> semantic v2 component variants -> offline derived brief -> accessibility/brand review

## Compatibility, rollout and rollback

- **Compatibility:** unselected/v1 consumers retain current behavior; selected
  v2 briefs retain provenance/tabs/fallback.
- **Migration:** additive profile metadata and local asset packaging, with no
  initiative-data conversion.
- **Rollout:** publish profile only with negative unselected fixture, local
  asset verification and explicit brand-owner record.
- **Rollback:** deselect/remove profile CSS/local assets as a versioned bundle
  change; generic shell remains the safe fallback.

## Risks and controls

| ID | Risk event | Signal | Control | Contingency / owner | Validation |
|---|---|---|---|---|---|
| IR-001 | Pearson styling leaks to generic consumer. | Unselected fixture contains asset/tokens/header. | Explicit profile boundary and negative test. | Disable profile; bundle owner. | V-001 |
| IR-002 | Logo is hotlinked/altered/low contrast. | Remote URL, CSS filter or light background. | Local asset contract and brand review. | Remove asset/profile; brand owner. | V-002, M-001 |
| IR-003 | Colour hides status/provenance. | Grayscale/screen reader loses distinction. | Text/icon/structural cues. | Rework components; accessibility owner. | V-005–V-007 |
| IR-004 | Visual layer breaks small/print/offline use. | Overflow, network fetch, clipped print. | Responsive/fallback/local checks. | Revert component variant; template owner. | V-006, V-009 |
| IR-005 | Guide is treated as legal permission. | No approval owner record. | Release blocker Q-001. | Keep profile unshipped; client owner. | V-008 |

## Unknowns

| ID | Unknown | Impact | Owner / resolution | Blocks? |
|---|---|---|---|---|
| U-001 | Client trademark/asset authority. | Cannot release selected profile safely. | Resolved by requester authorization in D-010 for this execution. | no — recorded authority |
| U-002 | Local Plus Jakarta Sans package/distribution path. | Font fallback/layout must be sound. | T-002 selects legal local path/fallback. | no |
| U-003 | Selected consumer profile metadata location. | Needs one recoverable source without state duplication. | T-001 chooses smallest existing config/design surface. | no |
| U-004 | Actual local logo checksum/version. | Brand asset needs traceability. | Resolved in T-002: local source/version and SHA-256 are recorded in evidence/T-002.md and approved in D-011. | no — verified local package |

## Impact decision

**Impact mapped:** yes  
**Human review required:** yes — brand and accessibility reviews are distinct.  
**Conditions before implementation:** U-003 was resolved by T-001. D-010 and
D-011 resolve U-001/U-004 for this execution; preserve those records and the
negative fixture before selected-profile release.
