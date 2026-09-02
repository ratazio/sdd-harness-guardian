# Spec: 015-post-scaffold-planning-completion-assurance

**Status:** draft | outcome_ready | spec_ready | superseded  
**Sequence:** 015  
**Slug:** post-scaffold-planning-completion-assurance  
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

The scaffold intentionally creates an empty safe package, but the mock suite showed that an empty scaffold can be mistaken for a generated SPEC. It must remain cheap to scaffold while being impossible to promote through planning gates before source-backed authorship.

## 2. Objective

Every non-trivial v2 initiative distinguishes `scaffolded` from `authored`; no unresolved template-derived package can reach planning, baseline or Tasks Ready gates.

## 3. Delivery outcome

- Product/user outcome: reviewers can trust that a package declared ready contains authored decision material, not an empty directory.
- Demonstrable increment: structural checks and workflow state distinguish safe blank scaffold from authored source-backed planning.
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
| FR-001 | WHEN a fresh scaffold exists, THE SYSTEM SHALL permit `scaffolded` state but reject planning readiness. | Preserve cheap bootstrap without false completion. |
| FR-002 | WHEN a material source remains placeholder/empty/unprojected, THE SYSTEM SHALL report its artifact and field without leaking document bodies. | Make authorship gaps repairable. |
| FR-003 | WHEN an authored non-trivial package is complete, THE SYSTEM SHALL accept varied domains, stacks, architectures and compositions. | Avoid topic-specific rigidity. |

## 8. Acceptance criteria

Keep one observable claim per row. Validation IDs are finalized in
`validation-plan.md`.

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Empty scaffold cannot reach Plan/Validation/Coverage/Human Visibility/Tasks Ready. | V-001 |
| AC-002 | Diverse mock packages pass after authorship without fixed tabs, stack or section count. | V-002 |
| AC-003 | Historical/pinned sources are not retroactively blocked without material refresh. | V-003 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | | |

## 10. Constraints and non-functional requirements

- Architecture: assurance transition only; it is not an automatic prose generator.
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
