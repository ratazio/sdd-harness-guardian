# Spec: 003-stakeholder-brief-enrichment

**Status:** spec_ready  
**Sequence:** 003  
**Slug:** stakeholder-brief-enrichment  
**Owner:** platform-engineering  
**Created:** 2026-08-12  
**Last updated:** 2026-08-12  
**Risk:** medium

## 1. Problem

The bundle already scaffolds and gates `stakeholder-brief.html`, but the current
brief is mostly textual. It does not consistently expose architecture, execution
flow, blast radius, initiative size, trade-offs or signs that the proposed
solution is disproportionate to the outcome. Stakeholders therefore need to
read several source files to make a sound decision, while agents can satisfy the
brief contract with generic text that adds little understanding.

The opposite failure is also material: making every brief exhaustive would turn
spec creation into a documentation project whose token and review cost can
exceed the implementation it governs.

## 2. Objective

Make `stakeholder-brief.html` the default, concise and visual meeting surface for
understanding and deciding non-trivial specs, while keeping it derived from the
canonical source artifacts and proportional to the initiative.

## 3. Delivery outcome

- **Product/user outcome:** stakeholders can understand the value, boundary,
  impact, high-level implementation shape, risk and requested decision of a spec
  from one short rendered page.
- **Demonstrable increment:** newly scaffolded initiatives receive an enriched
  brief; existing author/reviewer guidance carries one conditional checklist; the Spec Guardian can
  perform a short semantic and visual review before the existing Human
  Visibility gate.
- **MVP/slice boundary:** update the template and existing governance surfaces,
  reuse existing skills/roles for authorship and review, and add only cheap
  structural regression checks.
- **Priority source:** explicit human request on 2026-08-12.

## 4. Users or actors

- Stakeholder or product/engineering leader making a spec decision in a meeting.
- Agent authoring or updating the spec and its derived brief.
- Spec Guardian reviewing meaning, consistency and rendered usability.
- Delivery Orchestrator enforcing the existing Human Visibility gate.
- Bundle maintainer evolving and releasing the reusable templates.

## 5. Observable outcomes

- **O-001:** a reviewer can state the outcome, affected boundary, size and
  requested decision after a 60-second scan of the rendered brief.
- **O-002:** architecture, impact and flow visuals appear only when their
  relevance triggers apply and communicate concrete relationships.
- **O-003:** a small/local initiative can produce a materially shorter brief and
  explicitly omit unnecessary diagrams.
- **O-004:** no new per-initiative data file, workflow state or mandatory gate is
  introduced.
- **O-005:** the brief remains traceable to `spec.md`, `impact-map.md`, `plan.md`
  and `validation-plan.md` rather than becoming a parallel source of truth.

## 6. Non-goals

- **NG-001:** replicate the complete spec, plan or impact map in HTML.
- **NG-002:** create YAML/JSON schemas, a database, workflow engine or hosted UI.
- **NG-003:** require Mermaid, JavaScript, a CDN or an external diagram service.
- **NG-004:** create a permanent Stakeholder Brief agent or a separate checklist
  artifact for every initiative.
- **NG-005:** use an LLM judge, screenshot CI or subjective design scoring as a
  mandatory hard gate.
- **NG-006:** estimate dates or detailed effort from qualitative initiative size.
- **NG-007:** require architecture, impact and flow diagrams for trivial changes.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN a non-trivial initiative is scaffolded, THE BUNDLE SHALL provide an enriched `stakeholder-brief.html` without an extra creation step. | Keeps visual decision support in the default path. |
| FR-002 | WHEN an author builds or refreshes the brief, existing rule/skill/agent guidance SHALL provide one short conditional checklist covering outcome/benefit, scope/anti-scope, affected actors/surfaces, size/proportionality, validation, risks and the requested decision. | Prevents omissions without creating another artifact or capability. |
| FR-003 | THE BRIEF SHALL declare qualitative size `S`, `M` or `L`, a one-sentence rationale and whether a smaller approach was considered. | Makes likely overengineering visible without pretending to estimate delivery. |
| FR-004 | WHEN two or more components, a contract, data boundary or material architecture decision changes, THE BRIEF SHALL show a compact architecture view; otherwise it SHALL state that the change is localized. | Makes architecture conditional on decision value. |
| FR-005 | WHEN three or more surfaces, indirect effects or medium/high/unknown risk exist, THE BRIEF SHALL show a compact impact map; otherwise a short affected-surfaces table is sufficient. | Matches visual depth to blast radius. |
| FR-006 | WHEN a new journey, multi-step execution, handoff, failure path or rollback must be understood, THE BRIEF SHALL show a compact flow; otherwise the block may be omitted with a reason. | Avoids decorative diagrams. |
| FR-007 | Visuals SHALL use responsive HTML/CSS or inline SVG, include an accessible text equivalent, remain understandable without color alone and have no external runtime dependency. | Keeps the bundle portable and reviewable. |
| FR-008 | THE Delivery Orchestrator SHALL trigger brief creation/refresh after the source artifacts are ready and before task breakdown; THE Spec Guardian SHALL review source consistency and rendered meaning at the existing Human Visibility gate. | Makes authorship and review explicit without a new role or state. |
| FR-009 | THE structural validator SHALL check only stable facts: required base section IDs, source links, update metadata and absence of canonical placeholders. | Adds a cheap hard mirror without pretending to automate judgment. |
| FR-010 | THE qualitative review SHALL reject contradiction, generic filler, an unreadable or misleading visual, and a page that does not make the requested decision clear. | Addresses “filled in but meaningless” briefs. |
| FR-011 | THE brief SHOULD target a five-minute read and no more than one architecture view, one impact view and one flow. For an M/L initiative, 600–900 visible words is a reference range, never a minimum; local/S briefs should be materially shorter. | Bounds token, authoring and meeting cost without rewarding filler. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A feature scaffold still creates `stakeholder-brief.html`, and the created file contains the enriched base sections and no initiative-name/date placeholders. | V-001 |
| AC-002 | The template exposes outcome/benefit, requested decision, scope/anti-scope, affected people/surfaces, size/proportionality, validation, risks and next step. | V-002 |
| AC-003 | Existing author/reviewer guidance contains one conditional checklist and does not require a new skill, per-initiative checklist, YAML or JSON file. | V-003 |
| AC-004 | Architecture, impact and flow use explicit relevance triggers and allow a concise `not applicable` reason instead of empty visual ceremony. | V-003 |
| AC-005 | Inline visuals have a text equivalent and the rendered template remains readable without external assets at desktop and narrow viewport widths. | V-004 |
| AC-006 | Spec Guardian guidance explicitly checks source consistency, proportionality, meaningful content, requested decision and visual legibility before Human Visibility Ready. | V-005 |
| AC-007 | Delivery Orchestrator/lifecycle guidance assigns authoring/refresh before the existing gate without adding a gate or state. | V-005 |
| AC-008 | The lightweight validator rejects a missing base section, a canonical placeholder or missing source reference, without semantic scoring or screenshot CI. | V-006 |
| AC-009 | Existing bundle validation and scaffolder smoke tests pass after the change. | V-007 |
| AC-010 | This initiative's rendered brief passes the 60-second test: a reviewer can identify outcome, impact, architecture, size, excluded complexity and requested decision without opening another file. | V-008 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Formatting-only or truly local change. | Use a short brief or the existing allowed exception; do not generate decorative diagrams. |
| EC-002 | A relevance trigger applies but source artifacts lack enough information. | Show the uncertainty and block Human Visibility Ready; do not invent nodes or flows. |
| EC-003 | Brief and source artifact conflict. | Source artifact wins; refresh the brief before tasks. |
| EC-004 | A diagram looks polished but repeats generic labels. | Qualitative review requests revision because it reveals no concrete boundary, dependency or trade-off. |
| EC-005 | The brief grows beyond the normal size target for a high-risk initiative. | Allow with a short reason; the word target is a proportionality guide, not a brittle failure threshold. |
| EC-006 | Source changes after Human Visibility Ready. | Refresh only when outcome, scope, architecture, impact, risk or validation changes materially. |

## 10. Constraints and non-functional requirements

- **Architecture:** passive, file-based bundle; brief stays a derived view.
- **Security/privacy:** visuals must not expose secrets or production-sensitive data.
- **Data:** no new structured state or per-initiative artifact.
- **Performance/cost:** one synthesis pass after sources are ready; one short
  review pass; deterministic checks remain local and cheap.
- **Compatibility/accessibility:** static offline HTML, responsive at desktop and
  narrow widths, semantic headings/tables, text equivalents for diagrams.
- **Operational:** existing scaffold command, states and gates remain intact.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| Existing agents can edit static HTML from a template and source Markdown. | Demonstrated by current bundle/specs; bundle maintainer. |
| Qualitative `S/M/L` is sufficient to expose proportionality without effort estimation. | Review during first consumer adoption; product/engineering stakeholders. |
| Visual meaning cannot be safely reduced to a deterministic linter. | Keep semantic review agentual; Spec Guardian. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | The brief becomes a second, stale spec. | medium | high | Explicit source links, derived warning and material-change refresh rule; Orchestrator. |
| R-002 | Visual requirements add bureaucracy and tokens. | medium | high | Conditional triggers, size target, single checklist and no new gate/artifact; bundle maintainer. |
| R-003 | Agents create decorative filler to satisfy the template. | medium | medium | 60-second decision test and semantic review of concrete boundaries; Spec Guardian. |
| R-004 | A rigid validator blocks valid variations. | low | medium | Validate only stable structure/placeholders; never score prose or aesthetics. |
| R-005 | Inline SVG becomes hard to maintain. | low | medium | Limit node counts, reuse simple patterns and always include a text equivalent. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Existing human-visibility rule and gate | available | bundle | no |
| Existing scaffolder and template registry | available | bundle | no |
| Browser-capable visual review by author or Spec Guardian | available in supported agent environments; manual browser is acceptable | consumer | no |

## 14. Validation notes

Prefer static structure checks and the existing smoke test. Use a rendered visual
review for meaning and layout; do not add mandatory screenshot artifacts. The
full mapping is in `validation-plan.md`.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex acting as Spec Guardian  
**Reviewed at:** 2026-08-12  
**Blocking issues:** none  
**Required revisions:** none before planning; implementation must preserve the
anti-bureaucracy constraints and conditional visual triggers.  
**Decision evidence/link:** `stakeholder-brief.html`, `impact-map.md`,
`validation-plan.md`
