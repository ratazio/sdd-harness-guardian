# Spec: 005-stakeholder-brief-meeting-standard

**Status:** spec_ready  
**Sequence:** 005  
**Slug:** stakeholder-brief-meeting-standard  
**Owner:** platform-engineering  
**Created:** 2026-08-18  
**Last updated:** 2026-08-18  
**Risk:** medium

## 1. Problem

`stakeholder-brief.html` is intended to be the primary meeting and decision
surface for non-trivial initiatives. The canonical template is a rich,
responsive HTML page with a decision snapshot, conditional architecture/impact/
flow views, visual hierarchy, source links and a 60-second decision test.

Initiative 004 violated that contract: its brief was manually rebuilt as a
minimal 4 KB page instead of being a populated instance of the 17 KB canonical
template. It retained the stable section IDs and source links, so the structural
validator passed, but it lost the template's visual language, decision cards,
conditional diagram patterns, responsive layout and reviewer guidance. Its
appearance is visibly inferior to the 25 KB brief in initiative 003, the very
initiative that established the enriched standard.

The root cause is a governance gap, not a missing HTML template. The bundle
already has `.harness/templates/stakeholder-brief.html`, but lacks a dedicated
stakeholder-brief design standard, a design-lineage contract, content model for
meeting decisions, and a validator/review gate that rejects a custom bare page
which mimics only required IDs. The only comparable design reference is
`.harness/templates/audit-report-design.md`, which applies to audit reports,
not stakeholder briefs.

External practice supports strengthening the brief as a selective decision
packet rather than a longer generic document: C4 recommends only the diagrams
that add value for the audience; SEI recommends stakeholder- and view-based
documentation; and ADR guidance requires clear context, rationale,
consequences, status and confidence. Links are recorded in §13.

## 2. Objective

Make every non-trivial `stakeholder-brief.html` a recognizable, accessible and
information-rich instance of one canonical meeting standard, so stakeholders,
architects and delivery teams can decide scope, trade-offs, evidence and next
steps from it without turning it into a second source of truth or mandatory
diagram ceremony.

## 3. Delivery outcome

- **Product/user outcome:** meeting participants can quickly distinguish what
  is proposed, proved, uncertain, accepted, rejected or awaiting their
  decision, and can see the relevant impact, architecture and trade-offs at the
  appropriate level of detail.
- **Demonstrable increment:** a dedicated brief design standard, enriched
  canonical template, authoring/review guidance and deterministic design-lineage
  checks exist; initiative 004 is retrofitted to the standard as the regression
  example.
- **MVP/slice boundary:** static, offline HTML/CSS/inline-SVG only; retain the
  existing source artifacts as canonical. Add only machine checks for stable
  lineage/structure and a short rendered semantic review for actual quality.
- **Priority source:** human request on 2026-08-18 after observing the 004
  regression.

The harness validates declared contracts; it does not decide product priority
or substitute for the stakeholder decision requested by a brief.

## 4. Users or actors

- Product/business stakeholder deciding value, scope and priority.
- Architect deciding whether the design and trade-offs are acceptable.
- Developer, QA or operations representative checking implementation impact,
validation and operability.
- Agent authoring or refreshing the derived brief.
- Spec Guardian and independent reviewer deciding Human Visibility Ready.

## 5. Observable outcomes

- **O-001:** a rendered non-trivial brief visibly follows the canonical visual
  shell and cannot be mistaken for an arbitrary plain HTML summary.
- **O-002:** in a five-minute review, each audience can locate the requested
  decision, decision owner/status, outcome, scope/anti-scope, affected
  surfaces, material risks, evidence state and next safe step.
- **O-003:** each architecture/impact/flow view is selected for a named
  stakeholder concern, exposes a concrete relationship, and includes a text
  equivalent; irrelevant views are omitted with a reason.
- **O-004:** the brief makes uncertainty and evidence legible through explicit
  states such as planned, observed, proved, accepted risk and decision pending;
  it never presents planned validation as proof.
- **O-005:** an architect can identify significant decisions, alternatives,
  rationale, consequences, reversibility and confidence without opening the
  full decision log.
- **O-006:** initiative 004's brief is upgraded to the canonical standard and
  serves as a rendered regression/example alongside 003.

## 6. Non-goals

- **NG-001:** make the HTML a canonical source or duplicate all details from
  `spec.md`, `plan.md`, `impact-map.md`, `validation-plan.md` or evidence packs.
- **NG-002:** require every possible C4 level, diagram type, KPI or status
  field for every initiative.
- **NG-003:** introduce an LLM judge, prose score, screenshot CI, JavaScript
  framework, external diagram service or design-system dependency.
- **NG-004:** prescribe a specific product-management process, estimation
  method, delivery date or CI provider.
- **NG-005:** retrofit every historic brief; only 004 is required as a
  regression case and future refreshes follow the standard.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | THE BUNDLE SHALL add a canonical `stakeholder-brief-design.md` next to the HTML template. It SHALL define visual tokens, hierarchy, spacing, accessible color/legend rules, responsive behavior, source/lineage rules and content-to-view mapping. | The brief currently lacks the counterpart that `audit-report-design.md` provides for audit reports. |
| FR-002 | THE canonical brief template SHALL expose an explicit design-lineage/version marker and a stable visual shell. A customized brief SHALL preserve this marker and shell or record an approved, reasoned design exception. | Prevents a bare page from satisfying only IDs and links. |
| FR-003 | THE template SHALL provide a decision header and snapshot with decision request, decision owner/audience, status, decision deadline or review trigger, outcome/benefit, S/M/L, smaller option and freshness/source status. | Makes the meeting purpose and responsibility immediately visible. |
| FR-004 | THE template SHALL provide a compact decision/trade-off register for architecturally or product-significant choices: status, recommendation/alternative, rationale, consequence, reversibility, confidence and source link. It SHALL show only decisions relevant to the meeting. | Applies ADR-quality information without replacing `decision-log.md`. |
| FR-005 | THE template SHALL provide an impact/evidence view that maps affected actor or surface, change, blast-radius/risk, owner/mitigation, validation method and current evidence state. | Lets technical and business participants discuss what is known versus merely planned. |
| FR-006 | WHEN a view is required by a named concern, THE template SHALL use a compact C4-light context/container, impact relationship or execution/failure flow at the smallest informative level; each view SHALL declare purpose, audience and text equivalent. | Selective views are more useful than universal diagram ceremony. |
| FR-007 | THE template SHALL provide a visible open-questions and decision-actions panel with owner, decision needed, consequence of deferral and next safe step. | Converts the brief from a status page into a meeting decision surface. |
| FR-008 | THE Spec Guardian review SHALL check meeting-readiness: source consistency, evidence-state honesty, decision clarity, visual purpose, stakeholder/view coverage, accessibility and rendered desktop/narrow layout. | Stable checks alone cannot evaluate decision usefulness. |
| FR-009 | THE consumer-facing Human Visibility validator SHALL check the stable design-lineage marker, required canonical shell hooks and source freshness in addition to existing structural checks. It SHALL label this as design-contract validation, not visual-quality approval. | Creates a proportionate hard mirror for the failure observed in 004. |
| FR-010 | THE scaffold, authoring guide and consumer prompt SHALL direct agents to populate the canonical template, not reconstruct the page. A material custom layout requires an explicit reviewed exception. | Makes the desired default path easy and the bypass visible. |
| FR-011 | THE bundle SHALL retrofit `specs/004-consumer-enforcement-contract/stakeholder-brief.html` as a concrete regression example and validate it against the updated contract. | Repairs the bundle's own violation and guards against recurrence. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A dedicated stakeholder-brief design standard exists, is linked from template guidance, and distinguishes required visual shell from conditional information views. | V-001 |
| AC-002 | A newly scaffolded brief carries the design-lineage marker, canonical shell hooks and all base decision surfaces with resolved scaffold placeholders. | V-002 |
| AC-003 | The validator rejects a non-exempt brief missing design lineage or required shell hooks, while reporting that a pass does not judge rendered quality. | V-003 |
| AC-004 | The canonical template makes decision ownership/status, alternatives/trade-offs, confidence/reversibility, impact/evidence state, risks, open decisions and next safe step visible without requiring all optional diagrams. | V-004 |
| AC-005 | Conditional architecture, impact and flow views declare concern/audience/purpose/text equivalent and use the smallest appropriate C4-light or flow representation; omission reasons remain available. | V-005 |
| AC-006 | The 004 brief visibly uses the canonical visual standard and contains concrete decision, impact/evidence and next-action content derived from its sources. | V-006 |
| AC-007 | A desktop and narrow rendered review confirms readability, semantic hierarchy, no global overflow, non-color-only status meaning, and recovery of outcome, proof state, trade-offs and requested decisions within five minutes. | V-007 |
| AC-008 | Author/reviewer/workflow guidance prevents manual bare-page reconstruction and gives a reviewed-exception path for justified custom layout. | V-008 |
| AC-009 | Existing bundle, consumer visibility and scaffolder regression suites pass, including negative cases for missing design lineage/shell and a 004 regression fixture. | V-009 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Local/S change has no architecture, impact or flow trigger. | Retain decision/evidence shell; state why each optional view is omitted. |
| EC-002 | A stakeholder concern requires a view unavailable from source artifacts. | State the uncertainty and requested owner/decision; do not invent nodes, impacts or proof. |
| EC-003 | Brief needs a materially different layout for accessibility or a special audience. | Record a reviewed design exception with rationale, owner and retained decision surfaces. |
| EC-004 | Planned test or assertion has not run. | Display `planned`, not `proved`; link the planned validation source. |
| EC-005 | Evidence contradicts a prior decision or confidence claim. | Surface the conflict, downgrade confidence and request a decision/review. |
| EC-006 | Historical brief does not have the new marker. | Existing history is not rewritten automatically; validator offers a migration diagnostic and 004 is the required regression migration. |

## 10. Constraints and non-functional requirements

- **Architecture:** static offline HTML/CSS/inline SVG; canonical Markdown
  artifacts remain source of truth; no runtime service.
- **Accessibility:** semantic headings/tables, text equivalents, legible
  responsive layout, visible status labels and no color-only semantics.
- **Performance/cost:** target a five-minute stakeholder read; use progressive
  disclosure rather than repeated prose; no automatic visual scoring.
- **Security/privacy:** no secrets or sensitive production details in views;
  safe diagnostics expose paths/IDs only.
- **Compatibility:** desktop and narrow viewport review; no external fonts,
  CDN, images or diagram runtime.
- **Operational:** template, design standard, rules, prompt, validator and
  fixtures evolve together under a versioned bundle release.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| The existing enriched template is a suitable visual foundation rather than a design to discard. | Compare 003, template and 004 during V-006/V-007; Spec Guardian. |
| A stable marker/shell check prevents the observed regression without claiming aesthetic judgment. | Negative fixture and independent rendered review; bundle maintainer. |
| Selective stakeholder/view mapping can be concise enough for a meeting artifact. | Five-minute review with product, architecture and engineering perspectives; reviewers. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | More blocks become visual bureaucracy. | medium | high | Conditional triggers, named concern/audience and five-minute review; Spec Guardian. |
| R-002 | Marker check creates false confidence in visual quality. | medium | high | Explicit validator limitation plus rendered independent review; evaluator. |
| R-003 | Brief duplicates sources and becomes stale. | medium | high | Derived links, freshness check, compact summaries and evidence states; Orchestrator. |
| R-004 | Dense meeting content becomes unreadable. | medium | medium | Information hierarchy, progressive disclosure and narrow-layout review; design reviewer. |
| R-005 | Existing consumers cannot adopt a changed contract cleanly. | low | medium | Versioned migration diagnostics and 004 regression; bundle maintainer. |

## 13. Dependencies and research basis

| Dependency/source | Status | Owner | Blocking? |
|---|---|---|---|
| Canonical `stakeholder-brief.html` and Human Visibility rule | available | bundle | no |
| Consumer visibility validator from initiative 004 | delivered | bundle | no |
| [C4 model: selective diagram levels and supporting views](https://c4model.com/diagrams) | reviewed | architecture guidance | no |
| [CMU SEI: stakeholder- and view-based architecture documentation](https://www.sei.cmu.edu/library/a-structured-approach-for-reviewing-architecture-documentation/) | reviewed | documentation guidance | no |
| [Microsoft ADR guidance: status, context, rationale, consequence and confidence](https://learn.microsoft.com/nb-no/azure/well-architected/architect-role/architecture-decision-record) | reviewed | architecture guidance | no |
| [Microsoft architect checklist: evidence, trade-offs and accepted risk](https://learn.microsoft.com/da-dk/azure/well-architected/architect-role/checklist) | reviewed | architecture guidance | no |
| Design marker and migration exception syntax | approved: `data-harness-brief-design="v1"`; reviewed decision-log exception | platform-engineering | no |

**Market note:** no credible, established external product or standard named
“Spec Guardian” was found in the research. The closest comparable public SDD
tooling is GitHub Spec Kit, whose Spec → Plan → Tasks → Implement flow and
cross-artifact analysis support the Guardian's broad lifecycle but do not supply
this stakeholder-brief meeting surface.

## 14. Validation notes

Use deterministic tests for design lineage, shell hooks, source links,
placeholders, freshness and scaffold output. Use rendered review for layout,
accessible meaning and whether each view enables a concrete decision. Compare
template, 003 and migrated 004 at desktop and narrow widths. The detailed plan
must specify the marker, exception syntax and migration behavior before tasks.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex acting as Spec Guardian  
**Reviewed at:** 2026-08-18  
**Blocking issues:** none. The user approved the marker and exception contract
on 2026-08-18.  
**Required revisions:** complete the impact map, technical plan and validation
plan before task execution; refresh the derived brief with approval status.  
**Decision evidence/link:** comparison of template/003/004; current bundle
rules; external sources in §13.
