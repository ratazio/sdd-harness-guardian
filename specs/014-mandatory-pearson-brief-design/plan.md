# Technical Plan: 014-mandatory-pearson-brief-design

**Status:** source-complete; awaiting distinct planning/coverage review · **Owner:** platform-engineering · **Risk:** high · **Assurance:** A2-elevated

## Intent and cutover boundary

This plan makes the Pearson guide a **default-by-construction** for a v2 stakeholder brief created or materially regenerated after the approved cutover. It does not silently restyle historical artifacts. The literal root marker is `data-client-identity-profile="pearson"`; missing or another value is allowed only when the specific historical/legacy or custom-layout exception is recorded in that brief's decision log and migration inventory.

The local authority is `.harness/references/pearson-design.md` (SHA-256 `6EEE3DC5D2A058D99F57C5F2D92696C61B8C3BB24AB9CCFE76C524EC53C909AE`). The only logo source is `.harness/assets/brand/pearson-logo-white.png` (SHA-256 `8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`, PNG 175 × 53). Neither runtime network access nor a remote font/CDN is permitted.

## Delivery strategy

1. **Provenance and adoption inventory (T-001).** Verify guide/logo bytes and dimensions; publish a repository-wide inventory of v2 briefs, deliberately excluding disposable `testes/mock-runs/` output and validator/test fixtures. Decide whether any local font asset is authorized; until then use the documented system fallback.
2. **Canonical source and generation (T-002, blocked by SPEC 013 T-004).** Replace the generic green/amber/gradient base in the canonical HTML source with a Pearson operational layout, then ensure the plan template, `new_initiative.py`, manual authoring guidance and fresh-scaffold control emit the literal marker. Keep semantic component hooks, provenance attributes, native anchor/no-script fallback, print behavior and the finalized SPEC 013 tab contract.
3. **Objective enforcement (T-003).** Add deterministic checks and focused controls for lineage, local asset/hash/ratio, no hotlinks/filters, accessible logo-link semantics, required Pearson structural hooks and an explicit failure for selector-only/reconstructed generic CSS. Diagnostics identify the broken source contract and repair location without leaking full document content.
4. **Rendered decision review and migration decisions (T-004).** Independently inspect 320, 768, 1024 and 1440px; keyboard navigation, 200% zoom, reduced motion, no-script and print. Reconcile the inventory; only a decision-log exception with owner, reason, retained decision/accessibility surfaces and review outcome may retain a material deviation.

## Architecture and interfaces

```text
local guide + local logo
          │
          ▼
canonical plan/template + scaffolder + manual-authoring guidance
          │ emits literal Pearson lineage marker
          ▼
new/materially regenerated v2 stakeholder brief
          ├── deterministic validator + negative/control fixtures
          └── independent rendered/accessibility review
                     │
                     ▼
          migration inventory and explicit legacy/exception decisions
```

There is no application API, data-store or remote service change. The stable interfaces are the template root marker, semantic/provenance hooks, the local asset path and validator diagnostics. SPEC 013 T-004 is a hard predecessor for changing the canonical tab shell; it establishes the v2 DOM/tab regression contract that this design work must retain.

## Architecture-readiness profile and coverage composition

**Profile:** high, because this changes the canonical source bundle across template, scaffolder, authoring guidance, deterministic validation, identity asset and migration controls. The proportionate decision surface is the local source pipeline above; there is no consumer runtime, API, datastore, secret or deployment topology to invent. The controlled unknown is font packaging authority (U-001); T-001 can verify provenance and decide the safe fallback boundary only after it is formally authorized.

The following is the v2 composition plan for the derived brief. Every core source is rendered or accurately synthesized. The brief synthesizes the migration-inventory corpus size, exclusions and classification distribution while preserving the row-by-row inventory as the canonical source of record.

| Applicable source / principal headings | Disposition | Rendered target / reason |
|---|---|---|
| `spec.md` — Problem; Objective and outcome; Reference and authority; FR-001–FR-008; AC-001–AC-006; constraints; risks; Guardian decision | synthesized | `#scope`, `#architecture`, `#validation`, `#evolution`, `#decision`; outcome, boundaries, literal profile, asset facts and acceptance mapping are recoverable. |
| `impact-map.md` — surface table; dependency flow; IR-001–IR-005 | synthesized | `#impact`; risks and blast radius are condensed without asserting a consumer runtime. |
| `plan.md` — intent; strategy; architecture; readiness/coverage; safety; font; completion | synthesized | `#architecture`; pipeline, interfaces, high-profile rationale, rollback and U-001 are represented. |
| `tasks.md` — ledger; T-001–T-004 | synthesized | `#execution`; every task remains visibly pre-gate, with dependencies, limits and proof expectations. |
| `validation-plan.md` — V-001–V-008; commands | synthesized | `#validation`; deterministic and rendered-review limits are separate. |
| `decision-log.md` — D-001–D-007; exception contract | synthesized | `#decision` and `#evolution`; authority, pre-gate correction and gate boundaries are recoverable. |
| `progress.md` — phase; gates; risks; next safe step | synthesized | `#evolution`; no implementation/baseline/evaluator claim is hidden. |
| `run-state.yaml` — status; gates; ledger; review; approvals; next step | synthesized | `#evolution` (`#state-current`); source state rather than visual inference is displayed. |
| `.harness/references/pearson-brief-migration-inventory.md` — corpus, exclusions and classifications | synthesized | `#evolution` states the 9-brief corpus, explicit exclusions and truthful distribution (8 historical/legacy, 1 scheduled); the linked inventory retains row-level ownership and decision detail. |

**Review record boundary:** the independent pre-gate rendered-brief review recorded PASS for source-to-rendered recoverability; it does not approve a task, establish a fresh-fixture baseline, or act as an evaluator decision. The next reviewer must decide Plan Ready, Validation Ready, Brief Coverage Ready and Human Visibility Ready from these source artifacts, then the meeting/propagation gate may decide Tasks Ready.

## Safety, accessibility and rollback

| Concern | Control | Proof / rollback |
|---|---|---|
| Brand provenance | Versioned guide and exact local asset oracle. | T-001 evidence; reject remote URL, filter or wrong bytes. |
| Accessible identity | A named anchor contains a real logo image with preserved ratio; anchor has no `role="img"`; visible focus survives. | Focused fixture + rendered keyboard review. |
| Information/access regression | Retain provenance, semantic regions, tabs, native anchors, no-script, print and reduced motion. | Existing and focused suites plus T-004 review. |
| Historical truth | Inventory precedes migration; exception is decision-backed. | No bulk overwrite; inventory record is evidence. |
| Bad release | Restore prior versioned source files and rerun bundle/fresh-scaffold controls; record generated briefs affected by the reverted version. | Existing briefs are never rolled back by overwriting them. |

## Font decision

`Plus Jakarta Sans` may be named before the local/system fallback, but no font file may be bundled until its source and authorization are recorded in T-001. The safe initial path is `"Plus Jakarta Sans", "Segoe UI", Arial, sans-serif`; absence of the first family must remain readable and must not trigger a network request.

## Completion boundary

Implementation is complete only when T-001 through T-004 have distinct builder/evaluator evidence, the dependency is satisfied, deterministic checks and fresh-scaffold baseline pass, human visibility is refreshed, and each in-scope pre-existing v2 brief has a truthful inventory classification. A visually attractive selector overlay on the old generic shell is explicitly not completion.
