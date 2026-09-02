# Spec: 018-derived-brief-completeness-and-delivery-integrity

**Status:** spec_ready  
**Sequence:** 018  
**Slug:** derived-brief-completeness-and-delivery-integrity  
**Owner:** Harness maintainer  
**Created:** 2026-08-27  
**Last updated:** 2026-08-27  
**Risk:** medium
**Assurance profile:** A2-elevated

New initiatives begin `unknown`. Select a profile before Plan Ready: A1 is
local/reversible work; A2 is required for high/unknown risk, public-contract,
data-migration, trust-boundary or material-UI work; A3 escalates to named local
authority and never certifies compliance. Historical/pinned sources may omit it.

## 1. Problem

The Guardian allows a scaffolded `stakeholder-brief.html` to remain generic while Markdown sources are authored. A user who opens the brief therefore sees template instructions rather than the decision package. Mock-lab evidence from `testes/mock-runs/20260827-spec014-final-audit` and drafts 015–017 demonstrates the bypass.

## 2. Objective

A non-trivial SPEC is never presentable, baselineable or reported as delivered unless its stakeholder brief is a source-backed, rendered decision projection with no generic template content.

## 3. Delivery outcome

- Product/user outcome: decision makers can open HTML first and understand change, delta, architecture/operating model, risks, validation, task sequence and next decision.
- Demonstrable increment: the lifecycle proves a derived brief is complete before it can cross Human Visibility/Tasks Ready or be called delivered.
- MVP/slice boundary: lifecycle truth, validation wiring and broad-domain
  regression; it does not build an AI writer or prescribe a visual schema.
- Priority source: human request and demonstrated delivery-integrity failure.

The harness validates that these are declared. It does not decide commercial
value or product priority.

Summarize these fields for human review in `stakeholder-brief.html`.

## 4. Users or actors

- Decision maker opening a SPEC for approval or planning.
- Harness maintainer creating, validating or reporting an initiative.
- Independent evaluator reviewing the rendered package.

## 5. Observable outcomes

- O-001: a fresh scaffold is visibly incomplete and cannot be baselineed or
  reported as delivered.
- O-002: an authored brief projects the decision material from its sources and
  truthfully represents unknowns.
- O-003: a varied-domain brief remains valid without emulating another
  domain's architecture or layout.

## 6. Non-goals

- NG-001: require a standard count of sections, tabs, cards, diagrams or
  technology-specific views.
- NG-002: let a deterministic validator decide whether a strategy is good.
- NG-003: rewrite historical/pinned v1 packages without a material refresh.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN a v2 package contains generic scaffold brief content or unresolved source-to-brief material, THE SYSTEM SHALL reject Human Visibility, baseline and delivery claims with actionable diagnostics. | Prevent HTML-empty SPECs. |
| FR-002 | WHEN a brief is authored, THE SYSTEM SHALL require source-backed coverage of material outcome/delta, scope, architecture or operating model when applicable, risks/unknowns, validation, tasks/state and decision/next step. | Make HTML the decision surface. |
| FR-003 | THE SYSTEM SHALL allow content and presentation to vary by domain; it shall not require a programming architecture, fixed tabs, card count, palette or diagram type. | Preserve generality. |
| FR-004 | WHEN source material is missing, THE SYSTEM SHALL show a truthful owned unknown/block, not generic instructional prose. | Honest planning. |
| FR-005 | The workflow SHALL distinguish `scaffolded`, `authored`, `rendered`, independently reviewed and delivered states. | Close lifecycle ambiguity. |

## 8. Acceptance criteria

Keep one observable claim per row. Validation IDs are finalized in
`validation-plan.md`.

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Fresh scaffold cannot pass readiness/baseline and is visibly labelled scaffolded. | V-001 |
| AC-002 | All eight mock domains can produce a complete brief without a fixed visual/content schema. | V-002 |
| AC-003 | Negative fixtures for generic template prose, source-only changes and incomplete material coverage fail without leaking source bodies. | V-003 |
| AC-004 | Independent rendered review remains required; deterministic checks do not pretend to judge prose or architecture quality. | V-004 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Fresh scaffold is inspected or linked. | It says `scaffolded` and cannot receive delivery/baseline gates. |
| EC-002 | Source changes after a rendered brief. | Freshness/coverage check fails until refresh and review. |
| EC-003 | A category does not apply to the domain. | Source records `not_applicable` with a reason or an owned unknown; no invented technical content. |
| EC-004 | Historical v1 brief is pinned. | Remains compatible; v2 enforcement begins only on material regeneration/migration. |

## 10. Constraints and non-functional requirements

- Architecture: build a reusable source-to-brief completeness contract and workflow state; no application runtime is introduced.
- Security/privacy: diagnostics identify artifact/category/phase without
  printing source bodies or secrets; no network runtime is added.
- Data: source Markdown remains canonical; lifecycle state is additive.
- Performance/reliability: local command execution; an invalid state fails
  closed at the named v2 transition.
- Compatibility/accessibility: preserve existing local-asset, no-script,
  responsive, print and semantic brief requirements; historic v1 is protected.
- Operational: HTML is the primary delivery link; evidence retains commands,
  evaluator and residual limits.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| Existing composition contract can be connected to the validator without a new runtime service. | T-001 code trace; owner harness maintainer. |
| Independent reviewers are available for each task. | If unavailable, task remains `needs_evaluation`. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Fix accepts one mock pattern only. | medium | high | T-004 fresh varied suite and evaluator. |
| R-002 | Gate blocks legitimate non-software brief. | medium | high | category/unknown semantics and negative anti-rigidity fixture. |
| R-003 | Legacy package unexpectedly fails. | medium | medium | lineage/material-refresh fixture. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Existing scaffold/template/validator workflow | available | harness maintainer | yes |
| Independent evaluator | available per task | delivery orchestrator | yes |

## 14. Validation notes

Initial expectations only; `validation-plan.md` is authoritative for execution.

## 15. Spec Guardian decision

**Outcome Ready:** approved.  
**Spec Ready:** approved.  
**Reviewer:** audit_018_root_cause (independent).  
**Reviewed at:** 2026-08-27  
**Blocking issues:** none for T-001; task evidence/evaluation gates remain.  
**Required revisions:** none.  
**Decision evidence/link:** D-018-03 accepted.
