# Spec: 006-stakeholder-brief-complete-decision-surface

**Status:** spec_ready  
**Sequence:** 006  
**Slug:** stakeholder-brief-complete-decision-surface  
**Owner:** platform-engineering  
**Created:** 2026-08-19  
**Last updated:** 2026-08-19  
**Risk:** high

## 1. Problem

The current `stakeholder-brief.html` is a strong, attractive executive decision
summary, but the method now expects it to be the primary surface from which
product, architecture and delivery participants understand, challenge and
decide an initiative. That role is broader than the contract implemented by
initiatives 003–005.

The existing rule intentionally optimizes for a concise, selective synthesis:
it recommends one compact view per concern, a five-minute read and roughly
600–900 visible words for M/L work. The deterministic validator follows only
`spec.md`, `impact-map.md`, `plan.md` and `validation-plan.md`. The lifecycle
also builds the brief before task breakdown. Consequently the current process
cannot guarantee that tasks, decision history, superseded choices, complete
architecture concerns or every principal source heading are represented in the
meeting surface.

This creates four risks as the methodology becomes spec-driven in practice:

- stakeholders may decide from an attractive but incomplete projection;
- architects may receive diagrams too shallow for contract, data, security,
  failure-mode or rollback discussions;
- task sequence and validation coverage may remain outside the document used in
  the meeting;
- meeting decisions may update source artifacts without an explicit account of
  what changed in the next brief.

The gap is a product-policy evolution, not a defect in the existing visual
design. The enriched opening, visual language, derived-artifact boundary and
deterministic/agentic split remain valuable and must be preserved.

## 2. Objective

Evolve the Stakeholder Brief into a progressively disclosed, coverage-verified
and independently reviewed projection of the complete initiative, so it is the
single meeting and decision-reading surface without becoming a competing source
of truth.

## 3. Delivery outcome

- **Product/user outcome:** meeting participants can begin with the existing
  executive narrative and progressively inspect every material business,
  architecture, impact, execution, validation and decision-history concern from
  one offline HTML page.
- **Demonstrable increment:** a versioned Stakeholder Brief v2 contract,
  coverage model, lifecycle, architecture-readiness profile, independent
  pre-render review, validator updates, tests, guidance and at least one
  complete rendered regression example are delivered together.
- **MVP/slice boundary:** static, portable HTML with inline assets; Markdown and
  state artifacts remain canonical; deterministic checks validate provenance,
  coverage, freshness and structure while agents/humans judge synthesis,
  diagram meaning and meeting usefulness.
- **Priority source:** explicit human approval on 2026-08-19 to create this
  initiative after reviewing the complete-decision-surface proposal. Execution
  remains subject to a second explicit human approval of this planned package.

## 4. Users or actors

- Product/business stakeholder deciding value, scope, priority and outcomes.
- Architect reviewing system boundaries, responsibilities, contracts, data,
  trust boundaries, failure behavior, trade-offs and reversibility.
- Engineering, QA, security and operations participants reviewing execution,
  validation, rollout and evidence.
- Brief author/assembler producing the coverage plan and final HTML.
- Independent coverage reviewer comparing the proposed brief against every
  source heading before final rendering.
- Spec Guardian and Delivery Orchestrator enforcing readiness and freshness.
- Meeting recorder/agent extracting decisions and updating canonical artifacts
  after discussion.

## 5. Observable outcomes

- **O-001:** the executive opening and visual identity established by v1 remain
  recognizable and useful for a 60-second orientation.
- **O-002:** the same page exposes deeper value/scope, solution/architecture,
  impact/risk, execution, validation/evidence, decisions/evolution and
  source-coverage views without requiring another artifact for normal meeting
  discussion.
- **O-003:** every principal heading in the applicable source set has an
  explicit disposition: represented, synthesized, not applicable with reason,
  or link-only with a stakeholder-relevance reason. Core decision sources may
  not silently use link-only coverage.
- **O-004:** tasks and their dependencies, demonstrable increments, risks,
  validation IDs and readiness state are visible before implementation is
  authorized.
- **O-005:** architects receive diagram depth proportional to affected
  boundaries and risk, including current/target context, components/contracts,
  data/trust boundaries and success/failure/rollback flows when triggered.
- **O-006:** a distinct reviewer performs a source-to-brief coverage pass before
  the final HTML is rendered and records gaps, contradictions and required
  revisions.
- **O-007:** the brief shows material changes since its previous approved or
  reviewed version, including superseded decisions and changed scope, ACs,
  architecture, tasks, risks and validation.
- **O-008:** meeting decisions are appended to `decision-log.md`, propagated to
  affected canonical artifacts, revalidated and then reflected in a regenerated
  brief; the HTML is never edited as the only record of a decision.
- **O-009:** small/local initiatives retain full topic disposition but use
  materially less depth; proportionality controls depth, not silent omission.

## 6. Non-goals

- **NG-001:** make HTML an authoring source or allow it to override Markdown,
  run-state, evidence or decision history.
- **NG-002:** copy every sentence or table cell verbatim into HTML; the contract
  requires loss-aware coverage of principal elements, not transcription.
- **NG-003:** force the same number or depth of diagrams for every initiative.
- **NG-004:** allow an agent to invent missing architecture, impact, evidence or
  decisions to make the brief appear complete.
- **NG-005:** introduce a hosted service, remote diagram dependency, external
  font, product dashboard or database.
- **NG-006:** require automatic semantic scoring, screenshot CI or an LLM judge
  to approve prose and visuals.
- **NG-007:** rewrite all historical briefs immediately; v1 remains valid for
  pinned/historical initiatives until a material refresh or explicit migration.
- **NG-008:** expose secrets, sensitive production topology or unnecessary PII
  in the expanded architecture and evidence views.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | THE v2 brief SHALL retain the v1 executive opening, decision ask, visual foundation, responsive behavior, offline operation, evidence-state honesty and canonical-source warning. | The current strengths are the foundation, not work to replace. |
| FR-002 | THE v2 brief SHALL provide progressive views for executive summary, value/scope, solution/architecture, impact/risk, execution/tasks, validation/evidence, decisions/evolution and sources/coverage. | One page must serve several audiences and depths. |
| FR-003 | THE method SHALL define an applicable source set containing `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `decision-log.md`, `progress.md` and `run-state.yaml`, plus conditional `reproduction.md`, `ratchet.md`, evidence and handoff information when stakeholder-material. | Current validation omits execution and evolution sources. |
| FR-004 | FOR every principal heading in the applicable source set, THE assembly plan and final HTML SHALL record a source locator and coverage state of `represented`, `synthesized`, `not_applicable`, or `link_only`; `not_applicable` and `link_only` require reasons. | Completeness must be inspectable without demanding verbatim duplication. |
| FR-005 | CORE decision sources (`spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `decision-log.md`) SHALL NOT use `link_only` for a material heading. | Links alone do not make the HTML a usable meeting surface. |
| FR-006 | EACH rendered content block SHALL expose stable provenance metadata such as source file, source section/IDs and coverage mode; the page SHALL include a human-readable coverage register. | Supports deterministic enforcement and reviewer trust. |
| FR-007 | THE lifecycle SHALL create a preliminary task breakdown before the final brief, perform coverage planning and independent coverage review, render the final brief, hold the decision meeting, propagate decisions, and only then declare Tasks Ready. | Tasks must be discussable before authorization. |
| FR-008 | THE coverage reviewer SHALL be a distinct identity from the brief author and SHALL report missing headings, weak synthesis, contradictions, unsupported claims, stale decisions, hidden unknowns and insufficient diagram depth before final render. | A separate reading catches omissions the author normalizes. |
| FR-009 | WHEN an independent reviewer is unavailable, THE initiative SHALL remain not Human Visibility Ready unless a named human performs and records the coverage review. | Independence is a gate, not optional polish. |
| FR-010 | THE plan template and Plan Ready review SHALL evaluate proportional architecture dimensions: current/target context, components/responsibilities, interfaces/events/contracts, data ownership/lifecycle, security/trust boundaries, critical runtime flows, failure behavior, NFRs, compatibility/migration, observability, rollout/rollback, alternatives and unknowns. | Architecture completeness must exist in sources before visualization. |
| FR-011 | THE diagram profile SHALL be proportional: localized/S may use text or one boundary view; M normally exposes context plus changed components/contracts and critical flow; L/high/unknown SHALL expose the applicable context, responsibility, data/trust and success/failure/rollback views. Omission requires a source-backed reason. | Architects need depth matched to risk, not a universal one-diagram cap. |
| FR-012 | WHEN architecture information required by the profile is missing, THE agent SHALL record an unknown with owner/resolution path and block Plan Ready or create a bounded discovery task; it SHALL NOT fabricate the visual. | Completeness pressure must improve sources, not hallucinations. |
| FR-013 | THE final brief SHALL show task sequence, dependencies, outcome linkage, demonstrable increment, risk, validation IDs, evidence destination and readiness without presenting draft tasks as authorized. | Execution is a first-class meeting decision. |
| FR-014 | THE final brief SHALL show validation traceability, regression/NFR checks, manual checks/evals, skipped or unavailable validation and current proof state. | Planned validation and evidence must remain distinguishable. |
| FR-015 | THE final brief SHALL include a material-change view derived from the prior reviewed baseline and append-only decision history, showing accepted, pending and superseded decisions. | Repeated meetings need an explicit delta, not memory. |
| FR-016 | AFTER a meeting, THE workflow SHALL extract decisions, append them to `decision-log.md`, update every affected canonical artifact, rerun readiness/coverage checks and regenerate the brief before execution. | Keeps spec-driven decision-making coherent. |
| FR-017 | THE deterministic validator SHALL check v2 lineage, required views, applicable source links, provenance/coverage metadata, unresolved headings/placeholders, source freshness and recorded independent review while explicitly disclaiming semantic or aesthetic approval. | Hard mirrors cover stable facts only. |
| FR-018 | THE v2 migration SHALL preserve historical/pinned v1 briefs, provide a clear upgrade diagnostic and require v2 for newly scaffolded non-trivial initiatives after the versioned bundle release. | Avoids silently breaking consumers. |
| FR-019 | THE implementation SHALL include author/reviewer guidance, consumer prompt updates, workflow/role changes, fixtures, negative tests and at least one desktop/narrow rendered v2 example. | The contract must be adoptable and regression-tested. |
| FR-020 | THE brief SHALL remain printable, searchable, keyboard accessible and understandable without color; progressive disclosure SHALL not hide content from print or source coverage inspection. | Increased depth must not reduce accessibility. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A v2 design and content contract preserves the v1 executive/visual strengths while defining all eight progressive information views. | V-001 |
| AC-002 | A machine-readable and human-readable coverage register maps every principal applicable source heading to a rendered location and coverage state, with reasons for allowed omissions. | V-002 |
| AC-003 | Fixtures prove that missing `tasks.md`, `decision-log.md`, a principal source heading, provenance metadata or an independent review record blocks the v2 gate. | V-003 |
| AC-004 | The common lifecycle orders task draft, composition plan, independent coverage review, final render, meeting decision propagation and Tasks Ready as specified, without weakening existing implementation/evidence gates. | V-004 |
| AC-005 | The plan template and reviewer guidance enforce the architecture dimensions and proportional S/M/L/high/unknown diagram profiles, including block/discovery behavior for missing information. | V-005 |
| AC-006 | A populated M/L v2 example lets product, architecture and delivery reviewers recover the complete decision packet from one page while distinguishing draft, planned, proved, uncertain, accepted and superseded states. | V-006 |
| AC-007 | The example exposes preliminary task sequence/dependencies/outcomes/validation and does not mark Tasks Ready before the human decision is incorporated. | V-007 |
| AC-008 | A material-change/evolution view identifies source changes and superseded decisions since the prior reviewed baseline. | V-008 |
| AC-009 | Post-meeting guidance and tests demonstrate decision extraction → append-only log → source propagation → revalidation → regeneration, with no HTML-only decision. | V-009 |
| AC-010 | Historical v1 fixtures remain accepted under their pinned/legacy contract while new scaffold output uses v2 after release. | V-010 |
| AC-011 | Desktop, narrow and print reviews confirm progressive navigation, keyboard access, readable dense tables/diagrams, no page-wide overflow and no color-only status meaning. | V-011 |
| AC-012 | Existing bundle, scaffolder and consumer validator suites pass, and new negative coverage/freshness/order cases fail precisely. | V-012 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | A local/S initiative has no material architecture or operational detail. | Cover every topic disposition, use concise text/`not_applicable` reasons and keep the executive path short. |
| EC-002 | A core source heading is empty. | Show the gap/unknown in the coverage review and block final Human Visibility rather than hiding it. |
| EC-003 | Two source artifacts contradict one another. | Surface the contradiction, name affected IDs and return to the owning gate before rendering a decision-ready brief. |
| EC-004 | Tasks change after the brief review. | Invalidate freshness, update the delta view and repeat coverage review for material changes. |
| EC-005 | Meeting decisions change scope or architecture. | Append decisions, update spec/impact/plan/tasks/validation as affected and regenerate; do not patch only the HTML. |
| EC-006 | Git comparison is unavailable. | Use an inspectable local source-hash baseline and disclose the limitation; never silently claim a change history. |
| EC-007 | An initiative has hundreds of tasks or ACs. | Show decision-relevant rollups plus complete expandable/indexed ledgers; retain per-ID provenance and local searchability. |
| EC-008 | Architecture contains sensitive topology or data. | Use the minimum safe abstraction, record the redaction and keep protected details in the authorized source. |
| EC-009 | A historical v1 brief is opened without material refresh. | Preserve it under the v1 contract and offer migration guidance; do not auto-rewrite history. |
| EC-010 | Independent agent review cannot be created. | Require a named human reviewer and record the limitation; self-review alone cannot pass the v2 coverage gate. |

## 10. Constraints and non-functional requirements

- **Architecture:** passive versioned bundle; static offline HTML/CSS/inline SVG
  and at most minimal inline behavior that degrades to readable content without
  JavaScript. No hosted runtime.
- **Security/privacy:** provenance and diagrams must not expose secrets, tokens,
  personal data or sensitive topology beyond the meeting audience's need.
- **Data:** Markdown/state/evidence remain canonical. Coverage metadata and
  source hashes are derived and must be reproducible.
- **Performance/reliability:** executive orientation remains fast; deep content
  is progressively disclosed. Validation remains Python standard-library where
  practical and emits precise failures.
- **Compatibility/accessibility:** v1 historical compatibility, v2 versioned
  rollout, responsive/print layouts, semantic headings/tables, keyboard
  navigation and non-color-only states.
- **Operational:** changes to templates, rules, skills/roles, workflows,
  validator, tests, prompts, docs, manifest and version metadata move together.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| The v1 opening and visual language should be extended rather than redesigned. | Side-by-side rendered review; product/design reviewer. |
| Principal-heading coverage plus semantic review is a better completeness contract than word count or verbatim duplication. | Coverage fixtures and M/L meeting eval; Spec Guardian. |
| Native anchors/details or a minimal accessible tab controller can provide progressive disclosure offline. | Keyboard, no-script, narrow and print review; implementer/evaluator. |
| Task drafts can be discussed before Tasks Ready without being mistaken for authorization when state labels are explicit. | Lifecycle fixture and stakeholder review; Orchestrator. |
| Git diff plus append-only decisions can produce a useful material-change view with a local-hash fallback. | Change-history fixtures; State Keeper. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Complete coverage turns the brief into unreadable duplication. | medium | high | Progressive disclosure, synthesis modes, executive path and no verbatim requirement; brief author/reviewer. |
| R-002 | Coverage metadata creates false confidence in semantic completeness. | medium | high | Distinct coverage reviewer and explicit validator limitation; Spec Guardian. |
| R-003 | More lifecycle stages add ceremony to small work. | medium | medium | Same topic contract with depth profiles and concise N/A reasons; Orchestrator. |
| R-004 | Reordering brief/tasks weakens an existing readiness invariant. | medium | high | Distinguish Tasks Drafted from Tasks Ready; keep implementation blocked until meeting decisions are propagated; Delivery Orchestrator. |
| R-005 | Expanded diagrams encourage invented architecture. | medium | high | Source-backed provenance, Plan Ready architecture gate and discovery/block behavior; Harness Planner. |
| R-006 | Tracking more sources creates frequent stale-brief failures. | high | medium | Material-change exception path, precise delta and fast regeneration guidance; State Keeper. |
| R-007 | v2 breaks pinned consumers or historical initiatives. | low | high | Versioned lineage, legacy acceptance and migration fixtures; bundle maintainer. |
| R-008 | Dense task/evidence information degrades accessibility. | medium | medium | Expandable ledgers, semantic tables, print/no-script/narrow tests; accessibility reviewer. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Initiative 003 enriched brief and conditional-view policy | delivered; partially superseded by this initiative | bundle | no |
| Initiative 004 consumer validator/freshness contract | delivered; extension required | bundle | no |
| Initiative 005 v1 meeting design, lineage and independent rendered review | delivered; visual foundation retained | bundle | no |
| Current canonical templates, lifecycle, roles, prompts and fixtures | available | platform-engineering | no |
| Human approval of this spec/plan/brief before implementation | pending | human sponsor | yes |
| Independent evaluator capacity during implementation | required by existing harness | Delivery Orchestrator | yes for task completion |

## 14. Validation notes

Use deterministic tests for source enumeration, heading coverage, provenance,
review identity, lifecycle order, freshness, v1/v2 compatibility and scaffold
output. Use rendered/eval review for information hierarchy, diagram adequacy,
accessibility in practice and whether product/architecture/delivery audiences
can make the requested decision without opening normal source artifacts.

Do not use a maximum word count as a gate. Measure executive-path readability
separately from deep-source coverage.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex acting as Spec Guardian  
**Reviewed at:** 2026-08-19  
**Blocking issues:** implementation authorization is intentionally pending; it
does not block planning or the approval meeting.  
**Required revisions:** incorporate independent brief-coverage findings before
Human Visibility Ready; record explicit human approval before setting any task
to `ready`.  
**Decision evidence/link:** human direction in the 2026-08-19 conversation;
initiatives 003–005; current rule, workflow, templates and validator comparison;
independent pre-render source-to-brief coverage PASS after two revision rounds.
