# Spec: 011-stakeholder-brief-client-identity-profile

**Status:** draft — awaiting Outcome/Spec Guardian review  
**Sequence:** 011  
**Owner:** platform-engineering with client brand owner  
**Created / updated:** 2026-08-26  
**Risk:** medium  
**Assurance profile:** A2-elevated

## 1. Problem

The current stakeholder brief is structurally useful but visually uniform:
impact and coverage can read as long tables, cards have little hierarchy, and
the generic palette does not express the customer's identity. The supplied
Pearson digital identity guide provides a clear, accessible visual system and a
white logo asset, but the SDD Harness Guardian is a reusable bundle. Hard-coding
one customer's trademark, font or palette into every consumer would be unsafe
and would make vendor-neutral briefs misleading.

## 2. Objective

Add an explicit, opt-in client visual identity profile mechanism for stakeholder
briefs, delivering a first Pearson profile from the supplied design guide. The
profile styles the already source-backed semantic composition from 010; it does
not determine facts, change gates, or substitute visual polish for review.

## 3. Delivery outcome

- **Usuário:** stakeholders see a brief with a coherent Pearson-like hierarchy:
  navy/lavender/white foundation, readable type, protected white logo,
  differentiated panels and richer impact/coverage treatments.
- **Incremento demonstrável:** a consumer explicitly selecting the Pearson
  profile renders an offline/local branded brief with consistent header,
  tabs/cards, impact/risk and provenance patterns at 320/390px, desktop and
  print; an unselected consumer remains vendor-neutral.
- **MVP:** profile-selection contract, local brand asset workflow, design
  tokens, component variants, responsive/accessibility guidance, fixture and
  visual regression/manual review.
- **Prioridade:** explicit client identity request on 2026-08-26, using the
  attached Pearson guide as visual reference.

## 4. Reference boundary

The supplied visual reference at D:/Projetos/virtual-architect/projects/afas/design.md
is a **visual reference supplied by the requester**, not repository operating
instructions. Its applicable guidance is: Pearson white logo use on protected
navy, the documented tokens and typography, responsive/accessible components,
and an operational (not marketing-hero) treatment for dense brief content.
Trademark permission, client approval and the final asset source must be
recorded by the executing consumer before a branded release.

## 5. Actors

- **Consumer/project owner:** explicitly selects a profile and confirms
  brand/trademark authority.
- **Brief author:** uses semantic component roles from 010; never uses brand
  colour/logo to imply a decision state.
- **Stakeholder:** receives a recognisable, legible decision document.
- **Accessibility reviewer:** checks contrast, focus, motion, responsive
  reflow and non-colour status semantics.
- **Brand owner:** approves client-specific logo/asset use and updates.
- **Vendor-neutral consumer:** can retain the existing default without Pearson
  asset, remote request or visual contamination.

## 6. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | The bundle SHALL define a deliberate opt-in visual-profile selection contract; default briefs SHALL remain vendor-neutral. | Protects reusable consumers from accidental client branding. |
| FR-002 | The first profile SHALL encode the supplied Pearson system as local design tokens: navy, violet, lavender, canvas, surface, accessible semantic colours, Plus Jakarta Sans fallback and spacing/radius rules. | Gives agents a coherent rather than ad hoc visual language. |
| FR-003 | A selected Pearson profile SHALL use the official white logo only from a locally served asset, at preserved aspect ratio, inside a navy/protected dark header and accessible homepage link. | Prevents hotlinking, distortion and unsafe contrast. |
| FR-004 | The profile SHALL provide component variants for header, tabs, summary metrics, diagrams, task cards, impact footprint/risk chain, validation proof cards, decision calls and coverage/provenance groups. | The requested improvement is information design, not a recolour. |
| FR-005 | Impact and coverage SHALL have a visually differentiated, scannable treatment while preserving semantic table/equivalent, provenance and text labels. | Avoids monotonous matrices without losing auditability. |
| FR-006 | The profile SHALL use colour as reinforcement only: risk/state/coverage must retain text, icon/shape or structural meaning. | Meets accessibility and preserves decision truth. |
| FR-007 | It SHALL support 320px, 390px, tablet, desktop, keyboard, no-script, 200% zoom, print and prefers-reduced-motion. Complex rows may become cards on narrow screens. | Branded aesthetics cannot regress v2 access guarantees. |
| FR-008 | The profile SHALL not use remote CSS, remote font, hotlinked logo, generated imitation logo, image-only diagrams or marketing photography that interferes with an operational decision surface. | Preserves offline/reliable brief operation and correct client asset use. |
| FR-009 | Profile metadata/selection SHALL be visible in canonical source and brief provenance but SHALL not become a new initiative state store or alter gate authority. | Keeps brand choice explicit and source-backed. |
| FR-010 | The implementation SHALL not claim legal/trademark approval from this design guide alone; the owner/approval path shall be recorded. | Visual reference is not legal authority. |
| FR-011 | If 010 is implemented, this profile SHALL consume its semantic component roles; if not, it SHALL enhance the current v2 shell without changing the source model. | Allows safe sequencing without coupling facts to CSS. |

## 7. Pearson visual profile contract

| Area | Required profile behavior | Explicit limit |
|---|---|---|
| Foundation | Canvas #EDECF5; surface white; dominant navy #0B004A; lavender borders #C1BFFA; violet #4C30A5 for action/focus. | No generic purple-dominant page, neon/glass, heavy gray shadows. |
| Typography | Plus Jakarta Sans when locally available; 400/500/600/700; readable fallbacks; sentence case. | No remote font requirement or ultra-heavy display. |
| Brand header | Navy surface, local white logo, protected contrast, 44px targets, accessible home link. | No white logo on light/unprotected image, no CSS recolour or distortion. |
| Cards/panels | White surfaces, lavender border, 16–24px radius, 24–32px padding, sparse shadow. | Do not make every control a capsule or floating card. |
| Impact | Surface footprint cards plus risk-chain/control cards; information/success/warning/danger treatment with text labels. | Do not rely on colour or turn risk into decorative dashboard. |
| Coverage | Grouped provenance cards/sections with semantic table/equivalent, source→view→disposition visible. | Do not hide source traceability behind visual treatment. |
| Motion/interaction | 160–240ms subtle transitions; focus violet; reduced motion honored. | No panel motion required to understand state. |
| Responsive/print | Reflow cards; dense table converts/scrolls locally with equivalent reading order; print keeps all content. | No global horizontal page scroll or clipped print. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A consumer can select Pearson explicitly while a fixture without selection stays vendor-neutral and does not request/contain Pearson assets. | V-001, V-REG-001 |
| AC-002 | Selected brief uses local white logo with correct dimensions/aspect and protected navy header; no hotlink, filter or altered logo exists. | V-002, M-001 |
| AC-003 | Tokens and typography match the supplied design guide's accessible foundation; body text/focus contrast is verified. | V-003, M-002 |
| AC-004 | Header, tabs, summary, diagram, task, impact, validation, decision and coverage components show a coherent profile rather than a single recoloured background. | V-004, E-001 |
| AC-005 | Impact has a readable surface/risk/control composition; coverage has grouped provenance plus semantic table/equivalent. | V-005, M-003 |
| AC-006 | Narrow 320/390px, keyboard, no-script, print, 200% zoom and reduced-motion behavior preserve access and information order. | V-006, M-004 |
| AC-007 | State/risk/disposition survive grayscale/colour-independent reading through text/icon/structure. | V-007, M-005 |
| AC-008 | Canonical profile selection/brand approval owner is recoverable and does not modify lifecycle/gate truth. | V-008, E-002 |
| AC-009 | No remote asset/font dependency, generic marketing hero or legal approval claim is added. | V-009, V-REG-002 |
| AC-010 | Visual regression/reference review confirms alignment with the supplied guide while independent semantic review still verifies the actual brief content. | E-003, M-006 |

## 9. Non-goals

- Rebrand every SDD Harness Guardian consumer as Pearson by default.
- Copy the customer guide as a universal design system or claim trademark
  licence/legal approval.
- Add an image generator, remote CDN, runtime theme switcher, framework or
  multiple brief pages.
- Turn operational stakeholder briefs into marketing pages with hero photos.
- Replace semantic/provenance markup, existing gates, coverage review or 008
  judgment with visual tests.
- Enforce one client profile on a consumer that has not selected it.

## 10. Edge cases

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Consumer does not select a profile. | Existing vendor-neutral v2 shell remains; no Pearson logo/font request. |
| EC-002 | Logo license/brand owner cannot be recorded. | Profile stays unavailable for release; generic shell remains usable. |
| EC-003 | Local font asset is unavailable. | Use documented system fallback with stable readable layout; do not fetch remote font. |
| EC-004 | Impact has no risks or coverage has few sources. | Use compact source-backed panel; do not manufacture colorful metrics/cards. |
| EC-005 | Long provenance/risk content at 320px. | Preserve ordered labels/values as cards or local scroll; never clip or rely only on colour. |
| EC-006 | Printed/offline brief cannot resolve an image. | Local asset packaged with consumer; meaningful text/brand label and document remain legible if image fails. |
| EC-007 | 010's richer component catalog is delayed. | Apply profile to current semantic v2 hooks; do not block layout/accessibility improvements. |

## 11. Constraints and NFRs

- **Offline:** selected assets reside locally in the consumer/bundle package
  according to the chosen packaging contract; no remote runtime fetch.
- **Brand safety:** logo only as supplied, unmodified and on safe dark
  contrast; brand owner approval is a release condition.
- **Accessibility:** WCAG 2.2 AA intent; contrast verified; semantic structure,
  focus, keyboard, zoom, reduced motion and text equivalents retained.
- **Information integrity:** visual hierarchy may prioritise, never hide or
  alter canonical facts/gates/provenance.
- **Performance:** CSS/SVG/local raster budget stays proportionate; no
  excessive photographic or font payload for an operational brief.
- **Compatibility:** v1 stays legacy; v2 stays one HTML/no-script/print;
  unselected consumers remain stable.

## 12. Risks and controls

| ID | Risk | Signal | Control / owner | Validation |
|---|---|---|---|---|
| R-001 | Pearson profile contaminates generic consumers. | Unselected fixture has logo/tokens/assets. | Explicit selection boundary and negative fixture; bundle owner. | V-001 |
| R-002 | Logo is hotlinked, altered or used on unsafe background. | URL/image/filter/contrast inspection fails. | Local asset workflow and brand review; brand owner. | V-002, M-001 |
| R-003 | Colourful redesign obscures status/provenance. | Grayscale or screen-reader inspection loses meaning. | Text/icon/semantic equivalents; accessibility reviewer. | V-005–V-007 |
| R-004 | Editorial identity makes decision brief too decorative/dense. | Hero/photo/heavy motion reduces task reading. | Operational component constraints and visual review. | V-004, M-006 |
| R-005 | Fonts/assets hurt offline/mobile/print. | Network dependency, shift or print failure. | Local/fallback/print checks; template owner. | V-006, V-009 |
| R-006 | Guide is treated as legal permission. | No brand owner/approval record. | FR-010 release gate; product/brand owner. | V-008, E-002 |

## 13. Dependencies and open questions

| Item | Status | Owner / resolution |
|---|---|---|
| Supplied Pearson guide | available as requester-provided visual reference | T-001 extracts only applicable local profile material and preserves reference attribution. |
| Official white logo URL | reference only | T-002 defines approved local download/package flow; no hotlink in runtime. |
| 009 tab shell | completed; required base | Preserve one-document, tab/fallback/provenance contract. |
| 010 composition kit | planned | Preferred semantic component catalog; profile may be sequenced after or adapted to current hooks. |
| Q-001: actual brand/trademark approval | resolved for this execution | D-010 records the requester's explicit authority for the official asset, profile implementation and selected-profile release. |
| Q-002: local Plus Jakarta Sans distribution | open, non-blocking | T-002 confirms package/right/fallback; no runtime remote fetch. |

## 14. Decision needed

Approve planning for an **opt-in Pearson visual identity profile**, not a global
rebrand. Execution must retain vendor-neutral fallback, local asset handling,
brand-owner approval and accessibility validation.
