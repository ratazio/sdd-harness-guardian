# Spec: 014-mandatory-pearson-brief-design

**Status:** spec ready; planning gates pending independent review · **Sequence:** 014 · **Owner:** platform-engineering + Pearson brand owner · **Risk:** high · **Assurance:** A2-elevated

## Problem

The Guardian has a local Pearson guide, an opt-in profile from SPEC 011 and a vendor-neutral v2 shell, but generated mock briefs rebuilt generic CSS instead of retaining a single approved visual system. A design reference that lives outside the bundle can also be forgotten by later agents. The requester has explicitly authorized official Pearson identity and logo use and requires a standardized design in every newly created stakeholder brief.

## Objective and outcome

Make the copied Pearson guide the versioned, local visual authority for all newly scaffolded or materially regenerated v2 stakeholder briefs in this bundle. A brief must begin from the canonical Pearson shell, not ad-hoc CSS; remain local/offline, accessible and decision-oriented; and make deviations fail deterministic checks or independent visual review.

- **User outcome:** every new SPEC opens a recognisably consistent, professional Pearson decision brief rather than a generic page.
- **Increment:** scaffolding produces a Pearson-styled v2 brief with local logo/tokens and tests prove fixture conformance.
- **Scope:** future/new and materially regenerated v2 briefs; guidance, templates, scaffolder, validator, fixtures and migration inventory. Existing historical briefs are not silently mass-rewritten; each gets an explicit migration decision.
- **Priority:** explicit requester directive on 2026-08-27.

## Reference and authority

The immutable local reference is `.harness/references/pearson-design.md`, copied verbatim from the requester-supplied guide on 2026-08-27. Its SHA-256 is `6EEE3DC5D2A058D99F57C5F2D92696C61B8C3BB24AB9CCFE76C524EC53C909AE`. It supplies visual/design direction; the requester explicitly authorizes Pearson identity and official local logo use for this bundle. The official local raster is `.harness/assets/brand/pearson-logo-white.png`, SHA-256 `8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`, PNG 175 × 53. No runtime hotlink or remote font is permitted.

## Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | The canonical source `.harness/templates/plan.md`, copied scaffold, canonical v2 HTML shell, and manual-creation guidance SHALL declare literally `data-client-identity-profile="pearson"` for every new or materially regenerated v2 brief after this SPEC’s cutover. `new_initiative.py` must preserve that declaration. The marker is the post-cutover lineage policy; an absence/`none` profile is valid only for a dated historical/legacy or decision-log exception. | Prevent generic reconstruction or forgotten selection across every supported creation path. |
| FR-002 | The canonical shell SHALL be Pearson by construction: replace the generic green/amber/gradient base with the guide's navy/lavender/white operational-product foundation, Plus Jakarta Sans local-or-system fallback, 8px spacing, consistent radii/borders, restrained shadows and accessible focus. Tokens alone over an unreplaced generic layout are non-conformant. | Standard visual language, not recoloring. |
| FR-003 | The shell SHALL use the official local white logo in a protected navy header/footer link with accessible name, preserved aspect ratio, no `role="img"` on its anchor and no hotlink/filter. | Brand correctness and accessibility. |
| FR-004 | Header, tabs, summaries, cards, diagrams, task/proof/risk/coverage/decision components SHALL follow the guide while preserving existing semantic/provenance/no-script/print contracts. | Design must not lose decision information. |
| FR-005 | A material custom layout or visual deviation SHALL require a decision-log exception with owner, reason, retained decision/accessibility surfaces and visual-review outcome. | Prevent silent generic variants. |
| FR-006 | Validator/fixtures SHALL detect missing or non-Pearson post-cutover profile declaration, external/hotlinked brand assets, absent local design reference, generic selector-only/reconstructed shell, semantic-hook regressions and unsafe logo anchor semantics. The logo oracle verifies the stated path, hash, dimensions/aspect, accessible anchor name, no anchor `role="img"`, and no CSS filter. | Deterministic guardrails for repeated failures. |
| FR-007 | Independent rendered review SHALL compare desktop, 320px, 768px, 1024px and 1440px, keyboard, 200% zoom, no-script, print and reduced motion against the local guide and decision-surface needs. | Visual fidelity remains qualitative. |
| FR-008 | The canonical migration inventory at `.harness/references/pearson-brief-migration-inventory.md` SHALL classify every repository v2 brief outside disposable `testes/mock-runs/` and test fixtures as migrated, scheduled, historical/legacy, or exception. Each row records path, lineage, classification, owner, decision-log identifier, target date, and justification; no state/gate is inferred from style alone. | Safe adoption without rewriting history. |

## Acceptance criteria

| ID | Criterion | Validation |
|---|---|---|
| AC-001 | Fresh scaffold and a manual-creation control use literal `data-client-identity-profile="pearson"`, canonical Pearson shell, local logo path and no remote brand/font request; a dated historical exception is the only negative control. | V-001/V-002 |
| AC-002 | Logo has protected navy context, accessible link/name, local PNG hash `8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`, 175 × 53 preserved aspect, and no prohibited anchor role/hotlink/filter. | V-003/M-001 |
| AC-003 | Core brief components visibly use the guide's product treatment and retain provenance, tabs, no-script and print behavior. | V-004/E-001 |
| AC-004 | 320/768/1024/1440px, keyboard, zoom, reduced motion and print satisfy the guide and existing v2 accessibility contract. | V-005/M-002 |
| AC-005 | Generic reconstructed CSS fixture and undocumented visual override fail with actionable diagnostics. | V-006 |
| AC-006 | Existing briefs have a truthful migration classification and a custom-layout exception cannot bypass review. | V-007/V-008/E-002 |

## Non-goals and constraints

- Do not turn operational briefs into marketing sites, add photography/hero content without source need, or alter canonical decision facts.
- Do not fetch logo/fonts/CSS remotely, use generic CSS fallback as a silent success, or claim legal permission beyond the recorded requester authority.
- Do not automate subjective visual fidelity, accessibility usability or semantic usefulness; retain distinct review.
- Preserve the vendor-neutral lineage only for historical/explicitly excepted documents; this SPEC supersedes SPEC 011's opt-in default for newly scaffolded or materially regenerated v2 briefs in this bundle. It depends on SPEC 013 T-004’s v2 tab contract before the canonical shell changes tabs.

## Risks and open questions

| ID | Risk / unknown | Control / owner |
|---|---|---|
| R-001 | Pearson restyle breaks no-script/print/provenance. | Fixture matrix plus accessibility reviewer. |
| R-002 | Static tests overfit CSS literals or miss visual drift. | Check required contracts/hooks; rendered reviewer evaluates the guide. |
| R-003 | Local Plus Jakarta Sans availability/licensing is unresolved. | Package only authorized local asset or use documented system fallback; brand owner. |
| R-004 | Existing brief is silently restyled and loses reviewed state. | Migration inventory and explicit decision per brief. |
| U-001 | Exact local font packaging authority. | T-001 discovery; blocks release of bundled font, not readable fallback. |

## Spec Guardian decision

**Outcome Ready:** yes. **Spec Ready:** yes — D-004.  
**Next safe step:** independent planning/coverage review of the source package and corrected rendered brief. No task is ready until that review, Human Visibility and post-meeting propagation close their respective gates.
