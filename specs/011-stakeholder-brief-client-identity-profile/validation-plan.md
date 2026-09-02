# Validation Plan: 011-stakeholder-brief-client-identity-profile

**Status:** validation done  
**Spec:** [spec.md](./spec.md)  
**Plan:** [plan.md](./plan.md)  
**Owner:** platform-engineering  
**Last updated:** 2026-08-26

## Strategy

Use a selected Pearson fixture and a negative unselected fixture. Automated
checks inspect selection, local assets, stable markup and no remote dependencies;
manual/accessibility/brand review checks visual hierarchy, contrast, keyboard,
zoom, print, grayscale and fidelity to the supplied guide. Semantic usefulness
remains the existing independent brief review.

## Acceptance traceability

| Validation | AC | Method / fixture | Oracle | Evidence |
|---|---|---|---|---|
| V-001 | AC-001 | Selected/unselected fixture scan. | Profile only changes explicit selected fixture; generic asset-free fixture remains. | evidence/T-001.md |
| V-002 | AC-002 | Asset/header inspection. | Local image, preserved ratio, navy protected surface, accessible link; no filter/hotlink. | evidence/T-002.md |
| V-003 | AC-003 | Token/contrast/type review. | Required tokens/fallback/focus meet documented contrast. | evidence/T-002.md |
| V-004 | AC-004 | Rendered component inventory. | Distinct coherent variants across all semantic views. | evidence/T-003.md |
| V-005 | AC-005 | Impact/coverage browser/manual check. | Risk/source relationships and semantic table/equivalent recoverable. | evidence/T-003.md |
| V-006 | AC-006 | 320/390/tablet/desktop, keyboard, no-script, print, 200% zoom, reduced motion. | No clipped/unreachable information; sensible reflow. | evidence/T-004.md |
| V-007 | AC-007 | Grayscale/screen-reader structure check. | Meaning remains through text/icon/heading/label. | evidence/T-004.md |
| V-008 | AC-008 | Source/state review. | Selection/brand owner recoverable; gates unaffected. | evidence/T-001.md |
| V-009 | AC-009 | Network/source scan and manual review. | No remote font/logo, fake logo, hero bloat or legal claim. | evidence/T-004.md |
| E-001 | AC-004/010 | Independent visual reviewer. | Aligns with supplied guide without generic marketing imitation. | evidence/T-003.md |
| E-002 | AC-008/009 | Brand owner review. | Asset/authority record is explicit; no inferred license. | evidence/T-004.md |
| E-003 | AC-010 | Independent semantic reviewer. | Styling did not hide/proclaim unsupported facts. | evidence/T-004.md |

## Required commands

| Command | Environment | Expected result | Tasks |
|---|---|---|---|
| python scripts/test_brief_v2_contracts.py | bundle root | v2 structure/provenance remains. | T-002–T-004 |
| python scripts/test_tabbed_brief_surface.py | bundle root | tabs/fallback remain. | T-002–T-004 |
| python scripts/validate_bundle.py | bundle root | bundle checks pass. | T-004 |
| selected-profile focused test | bundle root | selected/unselected asset and no-remote rules pass. | T-001–T-004 |

## Manual checks and limits

| ID | Steps | Oracle | Evidence |
|---|---|---|---|
| M-001 | Inspect logo/header offline and at 320px/desktop. | Correct asset/proportion/contrast/link. | T-002 record. |
| M-002 | Inspect contrast/focus/type with supported tools/manual calculation. | WCAG 2.2 AA intent; focus visible. | T-002 record. |
| M-003 | Inspect impact/coverage dense and sparse modes. | Grouping increases scannability but source trace survives. | T-003 record. |
| M-004 | Keyboard/no-script/print/zoom/reduced motion. | Access/fallback remains. | T-004 record. |
| M-005 | Grayscale/structure read. | No colour-only risk/state/disposition. | T-004 record. |
| M-006 | Compare guide and profile surface. | Operational Pearson feel, no hero/marketing excess. | T-003 record. |

## Skipped validation

No live external logo fetch is a success condition; the profile must work
offline. A legal review is not replaced by this plan; brand-owner approval is
a named release condition for a selected profile.

## Validation decision

**Validation Ready:** yes — the mapping is complete and ready for the gated
implementation sequence. No implementation test has been run and this does not
authorize a selected Pearson profile, a brand asset or a release.

## Validation outcome

**Validation Done:** yes — D-018 independently approved the T-004 release
evidence. The focused render, client-profile contract, v2 contract, tabbed
surface and bundle checks passed; the refreshed Human Visibility baseline was
written and rechecked in D-019. Human review remains a required regression gate
for future material brief changes.
