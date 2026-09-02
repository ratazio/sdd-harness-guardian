# Technical Plan: 011-stakeholder-brief-client-identity-profile

**Status:** draft — planning source, not implementation approval  
**Spec:** [spec.md](./spec.md)  
**Impact map:** [impact-map.md](./impact-map.md)  
**Validation plan:** [validation-plan.md](./validation-plan.md)  
**Owner:** platform-engineering with client brand owner  
**Last updated:** 2026-08-26

## Technical approach

Create a small, explicit profile-selection contract and a local Pearson profile
layer above the vendor-neutral v2 shell. The profile consumes semantic component
roles from 010 when available; otherwise it targets current v2 hooks. A
selected consumer packages its logo/font assets locally, records source and
brand owner, and renders a single offline HTML. A non-selected consumer imports
none of these assets or branding.

## Architecture decisions

| ID | Decision | Rationale | Rejected alternative | Consequence |
|---|---|---|---|---|
| D-001 | Make visual identity opt-in by explicit consumer selection. | Reusable bundle cannot assume one client. | Global Pearson rebrand. | Negative fixture is required. |
| D-002 | Keep logo/font assets local and versioned with source/owner record. | Brief must work offline and avoid hotlink/trademark ambiguity. | Remote logo/font CDN. | Asset/package review is required. |
| D-003 | Use Pearson navy/lavender/white tokens and operational component variants. | Matches supplied guide without marketing-page excess. | Single recoloured generic template or hero photography. | Visual hierarchy follows semantic roles. |
| D-004 | Preserve semantic table/equivalent and text/icon state alongside visual cards. | Brand styling cannot hide provenance/accessibility. | Image-only charts or colour-only matrix. | More responsive markup/CSS discipline. |
| D-005 | Brand approval is a release condition, not an inferred property of design.md. | User-provided guide is a visual reference only. | Treat attached guide as legal permission. | Q-001 gates selected release. |
| D-006 | 011 can follow 010 but must tolerate its absence. | Avoids blocking safe shell improvements. | Couple profile to unimplemented component framework. | Two supported integration modes. |

## Size and proportionality

**Initiative size:** M.  
**Why:** cross-cutting template/assets/accessibility/brand boundary but no
business-runtime/data mutation.  
**Smaller option considered:** recolour the current CSS. It is insufficient
because it would not provide selection, local asset safety, semantic impact/
coverage variants or responsive proof.  
**Complexity deliberately excluded:** theme runtime, remote asset service,
multi-brand admin UI, image generation and consumer application rebrand.

### Client visual profile selection (conditional)

| Field | Record for this initiative |
|---|---|
| Profile | `pearson` is a named prospective profile; it is not the default. |
| Selection owner | Requester, for gated contract/fixture work only under D-006. |
| Brand owner | Requester, acting officially for Pearson (D-010). |
| Authority path | D-010 authorizes the official asset and release. Local source is `https://plc.pearson.com/sites/pearson-corp/files/logo_w.png`; SHA-256 `8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`. |
| Release state | `authorized_for_profile_implementation`; generic default remains unbranded. |

The section itself is the canonical selection source. Its absence in any other
consumer means `none`, so that consumer remains vendor-neutral and cannot load
Pearson identity by accident.

## Architecture readiness

**Profile:** A2-elevated.  
**Rationale:** an asset or style defect applies to every selected brief and can
break brand/accessibility/offline behavior.  
**Reapproval trigger:** new remote dependency, another brand, runtime switching,
embedded third-party asset, legal exception or failure of contrast/access checks.

| Dimension | Current | Target | Proof / N/A |
|---|---|---|---|
| Context | Generic v2 one-file brief. | Opt-in profile over same derived HTML. | D-001/D-006. |
| Components | Generic header/cards/tables. | Profile token and variants for semantic roles. | D-003/D-004. |
| Interfaces | Canonical sources to brief. | Explicit selection and brand record; no new runtime API. | FR-001/FR-009. |
| Assets | No client asset contract. | Local logo/font or fallback. | D-002, U-002/U-004. |
| Trust | Brief authority/provenance. | Unchanged; profile cannot alter gates. | FR-009. |
| Failures | Brand/access failure can spread. | Generic fallback and release block. | IR-001–IR-005. |
| NFRs | Tabs/no-script/print exist. | Add WCAG/responsive/motion checks. | FR-006–FR-008. |

## Change sequence

| Step | Surface | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Profile selection/approval metadata and design-reference extraction. | T-001 ready. | Explicit profile boundary; U-003 resolved. | yes |
| 2 | Local asset/tokens/header/base components. | T-001 evidence and U-001/U-004 record for selected fixture. | Safe Pearson foundation/fallback. | yes |
| 3 | Semantic component variants for impact, coverage and decision views. | T-002 evidence. | Differentiated operational information design. | yes |
| 4 | Responsive/accessibility/negative fixtures and independent review. | T-001–T-003 evidence. | Release evidence and rollback criteria. | yes |

## Contracts and compatibility

- **Selection:** a canonical consumer configuration/design source names selected
  profile and brand owner; exact home is T-001 discovery, not a new state store.
- **Assets:** local white logo preserves 175 by 53 proportion; font is local
  only when available, otherwise documented system fallback.
- **Output:** unchanged one HTML/offline/provenance/tabs; selected CSS/header
  variants only.
- **Compatibility:** no selected profile means generic output; v1 legacy route
  stays untouched.

## Security, privacy and brand permissions

No authentication/PII change. Do not include sensitive customer data in
branding. U-001/U-004 require explicit owner/source/version before selected
profile release. The guide itself is not license evidence.

## Rollout, observability and rollback

- Use selected and unselected fixtures, local-network/offline observation,
  contrast/access review and print/no-script checks.
- Failure signal: remote request, wrong/logo-modified file, profile leakage,
  inaccessible focus/contrast/reflow or provenance loss.
- Rollback: remove selection/profile assets and restore generic shell; preserve
  canonical content and decision state.

## Brief coverage composition

The eventual 011 brief must disclose profile purpose, client boundary, selected
tokens/asset constraints, impact/brand risks, task/proof plan, U-001 approval
state and explicit non-global authority. It is not rendered/approved at draft
phase.

## Open questions

| ID | Question | Owner | Resolution | Blocks? |
|---|---|---|---|---|
| Q-001 | Which existing canonical surface holds profile selection? | T-001 / bundle owner | Resolved: conditional `plan.md` profile-selection section; no new state store. | no |
| Q-002 | Where is approved local logo/font package and version recorded? | T-002 / brand owner | Record local path/checksum/source. | yes for selected release |
| Q-003 | How do cards represent dense coverage at narrow widths? | T-003 / accessibility owner | Prototype cards plus semantic table/equivalent. | no |

## Plan decision

**Plan Ready:** yes for gated bundle implementation under D-006.  
**Selected-profile release:** authorized for this execution by D-010; the local
asset source and checksum are recorded above. The generic fallback remains the
default for every unselected consumer.
