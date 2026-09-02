# Pearson stakeholder-brief migration inventory

**Authority:** SPEC 014 FR-008 · D-003/D-004 · updated 2026-08-27  
**Corpus rule:** every repository `stakeholder-brief.html` whose root declares `data-harness-brief-design="v2"`, excluding all paths beneath `testes/mock-runs/` and `scripts/fixtures/`. This inventory is a migration decision record; style inspection alone never establishes a state or gate.

## Schema

| Field | Meaning |
|---|---|
| Path | Repository-relative v2 brief path. |
| Lineage | Root v2 lineage and relevant pre-cutover profile fact. |
| Classification | Exactly one of `migrated`, `scheduled`, `historical/legacy`, `exception`. |
| Owner | Accountable migration/exception owner. |
| Decision-log ID | Decision authorizing the classification; an exception needs its own complete record. |
| Target date | Date to decide/migrate, or `not applicable — retained historical` for a true historical record. |
| Justification | Why the classification is truthful; never inferred from CSS alone. |

## Included v2 corpus

| Path | Lineage | Classification | Owner | Decision-log ID | Target date | Justification |
|---|---|---|---|---|---|---|
| `specs/006-stakeholder-brief-complete-decision-surface/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Completed pre-cutover decision artifact; no migration authorization has been granted. |
| `specs/007-risk-based-assurance-contracts/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Historical assurance artifact; preserve reviewed representation until a dedicated change decision. |
| `specs/008-semantic-brief-review-calibration/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Calibration record; style change would alter an evaluated historical sample. |
| `specs/009-stakeholder-brief-tabbed-decision-surface/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Historical tab-surface artifact; preserve while SPEC 013 owns the tab contract. |
| `specs/010-stakeholder-brief-composition-kit/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Completed composition artifact; no visual migration has been approved. |
| `specs/011-stakeholder-brief-client-identity-profile/stakeholder-brief.html` | v2, pre-cutover, explicit opt-in `pearson` | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | It proves the prior opt-in contract; it is not evidence that the new default/migration is complete. |
| `specs/012-stakeholder-brief-evidence-projection-enforcement/stakeholder-brief.html` | v2, pre-cutover, no Pearson marker | historical/legacy | platform-engineering | D-003 | not applicable — retained historical | Historical evidence-projection artifact; retain provenance/review state. |
| `specs/013-brief-dom-integrity-a11y-hardening/stakeholder-brief.html` | v2, pre-cutover corrective planning artifact | scheduled | platform-engineering | D-004 | after SPEC 013 T-004, before any material regeneration | It must first close the DOM/tab contract; its later material regeneration is intentionally sequenced behind that work. |
| `specs/014-mandatory-pearson-brief-design/stakeholder-brief.html` | v2, post-cutover planning projection | scheduled | platform-engineering | D-004 | before SPEC 014 T-004 closeout | This derived brief will be regenerated from the canonical Pearson shell during T-002 and independently reviewed in T-004. |

## Exclusions

| Excluded path class | Reason |
|---|---|
| `testes/mock-runs/**` | Disposable generated evaluation output, not a repository brief to migrate. |
| `scripts/fixtures/**` | Positive/negative validator fixtures; they must retain controlled states and are covered by fixture tests, not migration decisions. |
| v1 or unmarked historical briefs | Outside the v2-only FR-008 corpus; they are not silently changed by this policy. |

## Reconciliation rule

Before a row changes classification, the builder records the proposed change and evidence; a distinct evaluator verifies the path, lineage, decision reference and target date. `migrated` additionally requires T-004's rendered/accessibility review. A custom layout can be `exception` only with owner, reason, retained decision/accessibility surfaces, visual-review outcome and a dated re-review target in the cited decision log.

## T-001 verification record

**Verified:** 2026-08-27 · **Builder:** `build_t001_014` · **Evidence:** `specs/014-mandatory-pearson-brief-design/evidence/T-001.md`

The corpus discovery enumerated every repository `stakeholder-brief.html`, then selected only roots that declare the literal v2 marker and applied the two stated path exclusions with either Windows or POSIX separators. It produced exactly the nine rows above (SPECs 006–014); each has all seven schema fields and one permitted classification. This is a structural inventory check, not evidence that any historical brief already uses the Pearson shell.
