# Spec: 019-rendered-brief-decision-quality-gate

**Status:** draft  
**Sequence:** 019  
**Owner:** platform engineering  
**Created:** 2026-08-27  
**Risk:** high  
**Assurance profile:** A2-elevated

## Problem

The mock run `20260827-spec018-t004` passed structural and freshness checks
while independent architect, system-design, CEO, stakeholder and delivery
reviews rejected all eight briefs. HTML pages were compressed, hid material
decisions in Markdown, reduced tasks to titles, and represented architecture
as prose or typographic arrows. `represented` provenance can overstate what a
reader actually sees.

## Objective

Before a v2 brief is presented as decision-ready, require a distinct,
evidence-backed qualitative comparison of original request, canonical sources
and rendered HTML from five decision perspectives. A material `REVISE` blocks
qualitative approval; deterministic PASS remains useful but insufficient.

## Outcomes

- Decision makers recover change/delta, material architecture or operating
  model, risks/authority, execution and proof without opening Markdown.
- Material relationships use an accessible connected model or a justified
  alternative; text with arrows alone is not a relation model.
- Material tasks expose workfront, dependency, increment, risk/authority,
  validation/evidence and next-safe-step, not title-only summaries.
- The gate is adaptive: no required technology, number of tabs/cards, diagram
  library or fixed information architecture.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-001 | Require an operationally independent review with digest/locator of original request, canonical sources and locally served rendered HTML. |
| FR-002 | Record architect, system-design, executive, stakeholder and delivery perspectives, identity/role/environment and materiality rationale; `insufficient` or material `revise` blocks approval. |
| FR-003 | Assess source-to-HTML decision sufficiency, not only provenance/word count. |
| FR-004 | When relations are material, require connected accessible representation or justified alternative. |
| FR-005 | When execution is material, make workfront/dependency/increment/risk/proof/authority recoverable. |
| FR-006 | Deterministic checks verify gate evidence/state only; they never score architecture or prose. |
| FR-007 | Each finding identifies request/source/HTML locator, decision impact, canonical recovery action and required re-review. |
| FR-008 | A material dissent only ceases to block through a finding-specific, accountable disposition with authority, residual risk, corrected-render evidence and re-review by the originating role. |

## Non-goals

- Mandate tabs, card counts, SVG, a stack or diagram syntax.
- Replace judgment with word counts or an opaque LLM score.
- Require diagrams for simple work with no material relation.

## Acceptance criteria

| ID | Criterion |
|---|---|
| AC-001 | Structurally valid but decision-poor fixture fails with role-specific findings. |
| AC-002 | A rich varied fixture passes only after all five perspectives approve, or every material dissent has a finding-specific accountable disposition, corrected render and originating-role re-review. |
| AC-003 | Gate records request/source/rendered inputs without leaking source bodies. |
| AC-004 | Adaptive representation permits concise justified prose for low-relation work while requiring legible material flows. |
| AC-005 | M001–M008 are regenerated/reviewed in an 8×5 role matrix, with correction/re-review dispositions, and never summarized as deterministic PASS alone. |

## Risks and validation

Primary risk is replacing shallow validation with rigid bureaucracy. Mitigation
is a role rubric based on material decision capabilities, explicit N/A rationale
and independent evidence, then complete mock-suite review.

## Spec Guardian decision

**Outcome Ready:** pending independent review.  
**Spec Ready:** pending independent review.  
**Evidence:** five-role audit of `20260827-spec018-t004`; M001–M008 REVISE.
