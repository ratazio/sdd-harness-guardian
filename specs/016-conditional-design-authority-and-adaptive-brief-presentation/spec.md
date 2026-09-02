# Spec: 016-conditional-design-authority-and-adaptive-brief-presentation

**Status:** draft | outcome_ready | spec_ready | superseded  
**Sequence:** 016  
**Slug:** conditional-design-authority-and-adaptive-brief-presentation  
**Owner:** <name-or-team>  
**Created:** 2026-08-27  
**Last updated:** 2026-08-27  
**Risk:** low | medium | high | unknown
**Assurance profile:** unknown | A1-local | A2-elevated | A3-critical-local-policy

New initiatives begin `unknown`. Select a profile before Plan Ready: A1 is
local/reversible work; A2 is required for high/unknown risk, public-contract,
data-migration, trust-boundary or material-UI work; A3 escalates to named local
authority and never certifies compliance. Historical/pinned sources may omit it.

## 1. Problem

Fresh-consumer testing proved that identity assets can be absent while structural validation still accepts generic/older briefs. The remedy must enforce declared local design authority when applicable without forcing all briefs into one visual composition.

## 2. Objective

Fresh/materially regenerated briefs prove the applicable local design authority and asset provenance while retaining adaptive, decision-useful presentation.

## 3. Delivery outcome

- Product/user outcome:
- Demonstrable increment:
- MVP/slice boundary:
- Priority source: human request | roadmap | incident | risk reduction | human_decision_required

The harness validates that these are declared. It does not decide commercial
value or product priority.

Summarize these fields for human review in `stakeholder-brief.html`.

## 4. Users or actors

- Actor:

## 5. Observable outcomes

- O-001:

## 6. Non-goals

- NG-001:

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN consumer policy declares Pearson/current authority, THE SYSTEM SHALL verify root profile, local resolved asset/hash, named logo link, no hotlink/filter and canonical shell provenance. | Trustworthy identity. |
| FR-002 | WHEN a brief is historical or has documented alternative authority, THE SYSTEM SHALL preserve it without silent restyle. | Historical truth. |
| FR-003 | THE SYSTEM SHALL validate provenance/accessibility hooks, not fixed palette, technology, cards, tabs, sections or diagrams. | Flexible composition. |
| FR-004 | WHEN navigation is useful, THE SYSTEM SHALL preserve progressive keyboard/no-JS/print/linear reading. | Communication over format. |

## 8. Acceptance criteria

Keep one observable claim per row. Validation IDs are finalized in
`validation-plan.md`.

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Missing, remote, filtered, divergent or unresolved applicable assets fail; current fresh consumer passes. | V-001 |
| AC-002 | Valid non-software and unusual-composition briefs pass without synthetic tabs/cards. | V-002 |
| AC-003 | Rendered review proves responsive/no-JS/keyboard/print recoverability. | V-003 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | | |

## 10. Constraints and non-functional requirements

- Architecture: small provenance/a11y contracts plus rendered review, never screenshot/palette snapshots.
- Security/privacy:
- Data:
- Performance/reliability:
- Compatibility/accessibility:
- Operational:

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| | |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | | | | |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| | | | |

## 14. Validation notes

Initial expectations only; `validation-plan.md` is authoritative for execution.

## 15. Spec Guardian decision

**Outcome Ready:** draft — review required.  
**Spec Ready:** draft — review required.  
**Reviewer:**  
**Reviewed at:**  
**Blocking issues:**  
**Required revisions:**  
**Decision evidence/link:**
