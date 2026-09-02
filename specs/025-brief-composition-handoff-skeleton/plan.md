# Plan — SPEC 025

## 1. Strategy

Extend the one v2 composition process selected by SPEC 010 and made
route-aware by SPEC 023. Do not create a prose renderer or post-generation
fixer. The workflow gains a durable, agent-readable handoff and a deliberately
incomplete candidate skeleton; semantic/visual composition remains distinct
agent work.

## 2. Target sequence

| Step | Owner | Input | Output | Gate |
|---|---|---|---|---|
| Editorial composition | `brief-experience-composer` | canonical Markdown | `plan.md` route/block map | every principal material item has target/disposition |
| Coverage review | `executive-brief-reviewer` | sources + map | decision-log review | no unowned material loss; `brief_coverage_ready` only then |
| Skeleton | visual builder | reviewed map + template | `brief-candidates/stakeholder-brief.skeleton.html` | every planned block has visible slot; never renderer input |
| Composition | visual builder | copy of the same skeleton + sources | `brief-candidates/stakeholder-brief.candidate.html` | candidate declares base path/hash; slots filled or justified; root is `composed` / `authored` |
| Exact candidate attestation | distinct reviewer | candidate + source manifest | hash-bound pre-render record | state may become `ready_to_render` / `render_pending` |
| Editorial-exception decision (optional) | distinct reviewer + decision owner | current deterministic projection finding | visible candidate exception + exact-review record | owner, impact, residual risk, `proceed`, expiry and next action; not a gate pass |
| Promotion | renderer/state keeper | exact reviewed candidate | `stakeholder-brief.html` + `rendered` lifecycle | existing guarded promotion; hard integrity gates still refuse |
| Rendered experience review | distinct reviewer | promoted HTML + sources + map | APPROVE / REVISE evidence | only this review can support Human Visibility |
| Meeting propagation | decision owner/state keeper | reviewed rendered brief | canonical decisions + refreshed brief | Tasks Ready remains separate |

## 3. Brief composition plan (canonical intermediate MD)

This section is the required per-initiative handoff. It remains part of
`plan.md`, not a new source of truth. Each row describes a decision-relevant
projection; facts remain in the linked canonical source.

| Route | Block ID | Decision/question | Source locator | Fact or justified absence to recover | Form | Candidate target | Coverage disposition | Handoff state |
|---|---|---|---|---|---|---|---|---|
| scope | `scope.outcome` | What outcome is being bought? | `spec.md#delivery-outcome` | outcome and boundary | narrative + metrics | `#scope-outcome` | synthesized | mapped → skeleton |
| impact | `impact.footprint` | Who/what changes and what controls it? | `impact-map.md#...` | surface, delta, owner/control | footprint/risk chain | `#impact-footprint` | represented | mapped → skeleton |
| execution | `execution.T-XXX` | What safe increment happens next? | `tasks.md#T-XXX` | full non-empty task contract | task card | `#task-T-XXX` | represented | mapped → skeleton |
| validation | `validation.V-XXX` | What proves the claim? | `validation-plan.md#V-XXX` | method/context/oracle/evidence/limit | proof card | `#proof-V-XXX` | represented | mapped → skeleton |
| evolution | `evolution.state` | What is authorized and can change? | `decision-log.md#...` / `run-state.yaml#...` | decision, gate, risk, rollback | decision/state panel | `#evolution-state` | represented | mapped → skeleton |

The real plan enumerates every principal applicable item: outcome/scope,
requirements, ACs, risk, impact, plan/rollback, each material task, each
validation/proof, decision and material progress/state. The only coverage
dispositions are `represented`, `synthesized`, `not_applicable` and
`link_only`; the latter two carry their required reason. `discovery` is not a
coverage disposition: it is a handoff state for an owned material question with
owner, decision impact and resolution path. `a_preencher` is only a visible
skeleton-slot state and blocks promotion.

## 3.1 Deep visual construction contract

The preceding register answers **what source fact reaches which target**. It
is not enough on its own to construct a decision brief. For every route, the
composer must add the following construction record before a skeleton is
instantiated. This is a generic grammar for any SPEC: it does not presume a
software system, a fixed organisation, a task count or a diagram type.

| Construction field | Required answer | Why the skeleton needs it |
|---|---|---|
| Executive question | What decision or understanding must this route enable? | Gives the route a purpose beyond a heading. |
| Narrative arc | Orientation → significance → evidence/structure → trade-off or limit → action. | Prevents a page from becoming a bucket of cards. |
| Reader and time horizon | Who reads it, what they need now, and whether it is a decision, operating or assurance view. | Controls depth and vocabulary. |
| Material evidence | Source locator, fact/absence, owner and decision impact for every claim. | Keeps narrative source-backed. |
| Relationship model | What connects to what: flow, dependency, ownership, risk/control, task/proof or decision/gate. | Determines a meaningful visual rather than decorative geometry. |
| Visual form and reason | Chosen form — narrative plate, topology, footprint, task dossier, proof dossier, timeline, matrix, or justified alternative — and why it makes this relationship legible. | Lets a builder create the right component without guessing. |
| Repetition rule | The source-driven collection to repeat and the complete fields each repetition exposes. | A task/proof/domain cannot collapse into a title-only card. |
| Absence / uncertainty | `not_applicable` reason or owned discovery with owner, decision impact and resolution path. | A missing architecture or validation is visible, not silently erased. |
| Acceptance of the route | What a reviewer must recover from the rendered route without opening Markdown. | Creates a human review question without a prose score. |

### Route grammar

Every route is a real internal subpage in the one offline HTML. At runtime it
shows only its own content, with the shared header and route navigation; it is
not an anchor on a long document. Every route starts with a visible view title,
an executive question and a short source-backed orientation. It then contains
the selected evidence components and ends in a limit, action or next decision.

The default route grammar is deliberately complete but conditional. A route
must show either its applicable component model **or** a visible, source-backed
absence/discovery state. It must never show a generic empty paragraph because
the composer did not decide what belongs there.

| Route | Required story the reader must receive | Component model selected from sources |
|---|---|---|
| Value and scope | Why now; beneficiary/outcome; what is and is not being bought; current authority. | Decision snapshot, outcome narrative, 3–5 value pillars when material, scope/anti-scope and measures. |
| Architecture | How the relevant system or operating model is organised; where change occurs; what remains outside; how responsibility, information and controls flow. | Architecture thesis; 3–5 pillars; one global relationship model with legend; one zoom dossier per affected domain; deterministic-versus-human assurance boundary; explicit absence only if architecture is immaterial. |
| Impact | Whose work, data, interfaces, obligations or risks change; how each is controlled; how recovery works. | Footprint dossier per affected surface; risk-control chain; rollback/recovery card; protected-boundary card. |
| Execution | How delivery reaches the outcome through safe increments, dependencies and gates. | Source-backed epic/phase arc when grouping exists; one complete task dossier per material task; dependency relation; authority/status. |
| Validation | Why the proposed evidence is credible, which assurance modes apply, and what each proof cannot prove. | Validation thesis; applicable assurance pillars; validation flow; one complete proof dossier per validation/AC; acceptance/evidence matrix; retained guarantees and limits. |
| Evolution | What changed, which decisions caused it, what is true now and how the plan recovers. | Decision timeline, truthful gateboard, open risks and rollback references. |
| Decision | What is requested, from whom, with which alternatives, consequences and next safe step. | Recommendation callout, alternatives/trade-offs, authority boundary and audience decision matrix. |
| Coverage | Why the reader can trust the projection and where every material source went. | Coverage dispositions, source → fact → component register, justified absence/discovery. |

### Component dossiers

These are field contracts, not a demand for a fixed number of cards. The
skeleton contains the component shapes before any factual writing. The
composer duplicates a shape only for source material that the construction
record marks as material.

| Component | It must make recoverable | Never reduce it to |
|---|---|---|
| Global architecture model | Nodes/responsibilities, flows/relationships, change boundary, preserved boundary, legend, relevant data/contract/control and the task links. | A sequence of technology names or unlabeled boxes. |
| Solution landscape | The actual solution/operating environment appropriate to the source — application, services, teams, policy domains, devices or other material context — with change surfaces, preserved surfaces and out-of-scope boundary visually distinguished. | Three generic boxes labelled origin, domain and destination. |
| Relationship flow | The contextual sequence that makes the change credible: data, navigation, user action, decision, contract, handoff or control; trigger, transition, owner and outcome are visible where material. | A duplicate of the landscape or an arbitrary left-to-right arrow. |
| Architecture zoom dossier | Role, owner, what changes, what does not, inputs/outputs or operating contract, dependencies, linked tasks, failure control and recovery. | A repeated paragraph that says only “frontend”, “API” or “database”. |
| Impact dossier | Affected surface/person, delta, owner, exposure, control and escalation or next action. | A red/yellow/green label without consequence. |
| Epic or phase | Outcome, sequencing reason, dependencies, tasks included and the gate it is intended to reach. | A calendar label or arbitrary group of tasks. |
| Task dossier | ID, outcome/increment, scope and anti-scope, dependency, risk/control, validation/acceptance links, evidence, exit criterion, status/authority and why now. | A task title with a status badge. |
| Validation pillar | Assurance purpose, applicable method class, owner and limitation. | A generic claim that “tests will be done”. |
| Proof dossier | Element/objective, method, context/fixture/audience, acceptance criterion, oracle, evidence destination, reviewer/owner, result or future gate, and limitation. | A command without an oracle or a manual-review label without a decision question. |
| Decision / state element | Decision/gate ID, context, owner, authority, consequence, expiry or next action, and the risk of delay. | “Approved” or “pending” without meaning. |

### Selection and absence rules

1. The construction record selects the relationship model; the renderer never
   chooses it from keywords or invents a domain diagram.
2. A visual component may be compact for a small operational or policy change,
   but it must retain every applicable field of its dossier. Proportionality
   changes density, not recoverability.
3. If architecture, an epic grouping, a proof type or another component is not
   applicable, the skeleton renders an explicit absence card with source,
   reason, decision impact and owner. A missing fact becomes `discovery` and
   blocks or bounds the next action.
4. The visual builder may choose a table, narrative, topology, process lane or
   another accessible form when the construction record explains why. A
   reviewer judges whether the chosen form works; deterministic checks only
   verify route, target, IDs, slot state and provenance.
5. A candidate moves from skeleton to composed only after every selected
   component has source-backed content or its explicit absence/discovery state.

### Candidate derivation and architectural representations

1. The candidate starts as a byte copy of that initiative's approved skeleton.
   It declares the base path and SHA-256 in its root metadata before the
   composer fills it.  The composer edits that copy in place; it does not build
   a second HTML from a visual recollection of the skeleton.
2. The first architectural representation is a **solution landscape** whenever
   the sources describe a material context.  It may be an application
   architecture, operational ecosystem, policy boundary, research workflow or
   another domain-true model.  Changed surfaces receive a distinct visual
   treatment; preserved and out-of-scope surfaces remain explicit.  The plan
   names the legend, relationship types and source locators.
3. The second representation is a **relationship flow** only when it makes a
   separate question legible.  Depending on the SPEC it may be a sequence,
   data flow, user-navigation flow, decision flow, integration/contract flow
   or control/recovery flow.  It must not repeat the landscape with arrows.
4. A small, non-software or policy-only SPEC may select one representation or
   an explicit absence.  The selection is a source-backed editorial decision,
   never a keyword rule in a renderer.

### Agent authorship boundary

The final candidate is authored in HTML/CSS/JS by the visual-builder agent,
which reads the reviewed construction record and the canonical sources. It
chooses the concrete diagram, card density, hierarchy, narrative wording and
route-level composition for the actual situation. One or more specialist
agents may contribute to the map, architecture representation or validation
presentation, but a distinct reviewer still judges the integrated candidate.

Scripts may only instantiate/copy the already designed blank shell, check
identity/route/slot/ID/provenance contracts, render the exact reviewed bytes
and capture verification evidence. They MUST NOT parse Markdown to summarize a
SPEC, select components from keywords, choose a topology, write a task/proof
dossier, or generate the final HTML blocks. In particular, a Python brief
generator is not part of this path.

### Review prompt before composition

The independent coverage reviewer must answer, route by route: **Can a
stakeholder recover the decision, the relationships that make it credible, the
owner/control, the applicable task/proof and the next action from the planned
component model?** A REVISE finding records source → lost relationship or
field → decision impaired → required plan/skeleton correction. It never asks a
script to rate prose, diagram beauty or executive taste.

## 4. Minimal deterministic contract

Implementation may parse stable IDs, targets and states, create structural
slots and reject unfinished/absent links. It must not infer facts, select a
diagram, rate prose or declare a brief executive-ready.

Required checks:

1. every material map row has unique target/slot;
2. skeleton uses the explicit `brief-candidates/` identity, exposes every slot
   and remains non-promotable;
3. composed candidate has no `a_preencher` material slot, unless a v3 reviewed editorial exception names that current slot finding visibly and binds it to the candidate SHA-256 and composition-manifest record;
4. each populated `T-XXX` maps to Execution and each populated AC/V maps to
   Validation or reviewed source-backed omission;
5. candidate attestation, promotion and post-render review retain the existing
   lifecycle order and provenance checks.

6. Before qualitative review, a candidate is checked against the exact
   initiative-local skeleton by `validate_brief_candidate_inheritance.py`.
   The check validates only base hash, v3 route/component surface and visible
   slot completion. It rejects a small parallel HTML that merely declares
   `data-composition-base`; it never writes prose, chooses a diagram or rates
   the executive quality of the result.

`--allow-reviewed-editorial-exceptions` is an explicit promotion mode, never a
global relaxation. It admits only the mechanical projection findings the v3
contract can reproduce from current `tasks.md`, `validation-plan.md` or an
explicit skeleton slot. Each finding has a visible `#composition-exceptions`
entry and a matching nested record in the exact review decision: finding,
source, rendered target, decision impact, residual risk, owner, exact
`Decision: proceed`, non-expired date and next action. SHA-256, manifest,
reviewer distinction, provenance, lifecycle, skeleton identity, security and
brand checks remain hard refusals. An open exception is visible decision debt:
it keeps Human Visibility and Tasks Ready false.

## 5. Pilot and rollback

Pilot on a fresh disposable M-003 root. Compare source docs, map, skeleton,
composed candidate and render. If a tool causes source invention, abandon the
candidate and retain sources/lab histories unchanged. Rollback reverts only
new workflow/template/script surfaces; consumer/history migration is excluded.

## 6. Plan decision

**Plan Ready:** yes  
**Reviewer:** `/root/spec025_independent_review`  
**Reviewed at:** 2026-09-01  
**Conditions/links:** preserve the integrated composition process; do not
repurpose the SPEC 024 reference generator.

## 7. Editorial composition map — SPEC 025

This is the concrete handoff for this brief. Every fact below remains owned by
the linked Markdown; the HTML only projects it.

| Route | Block ID | Decision/question | Source locator | Fact to recover | Form | Candidate target | Coverage | Handoff state |
|---|---|---|---|---|---|---|---|---|
| scope | `scope.outcome` | What is being authorized? | `spec.md#3` | One canonical path from source to decision brief; no second renderer. | outcome plate + boundary cards | `#scope-outcome` | represented | mapped |
| scope | `scope.boundary` | What stays out? | `spec.md#6` | No semantic auto-authoring, sidecar, quota or history rewrite. | inclusion/exclusion split | `#scope-boundary` | represented | mapped |
| architecture | `architecture.flow` | Where does each responsibility live? | `plan.md#2` | Composer, reviewer, skeleton, composed candidate, renderer, post-render reviewer and state keeper. | connected topology + responsibility cards | `#architecture-flow` | represented | mapped |
| architecture | `architecture.state` | What cannot be confused? | `spec.md#FR-025-03`; `spec.md#FR-025-04`; `spec.md#FR-025-05`; `decision-log.md#D-025-002` | Skeleton is external/non-promotable; candidate is composed/authored; promoted brief is rendered. | lifecycle lane | `#architecture-state` | synthesized | mapped |
| architecture | `architecture.assurance-boundary` | Which work is deterministic and which remains human judgment? | `spec.md#FR-025-06`; `plan.md#4` | Scripts bind slots, IDs, provenance, placeholders, lifecycle and regressions; agents/reviewer decide narrative, diagram form, hierarchy, materiality and usefulness. | two-lane assurance boundary | `#architecture-assurance` | represented | mapped |
| impact | `impact.footprint` | What changes and what is protected? | `impact-map.md#Outcome-and-boundary`; `impact-map.md#Dependency-and-data-flow` | Seven surfaces, controls and negative boundary. | impact footprint | `#impact-footprint` | represented | mapped |
| impact | `impact.risks` | What can fail? | `spec.md#11`; `ratchet.md#R-025-001` | Four risks, trigger/check/consequence and owners. | risk-control chain | `#impact-risks` | synthesized | mapped |
| impact | `impact.rollback` | How is an unsafe change reversed? | `plan.md#5`; `spec.md#EC-025-04` | Abandon an inventive candidate; revert only workflow/template/script; preserve canonical Markdown, laboratory and history. | rollback card | `#impact-rollback` | represented | mapped |
| impact | `impact.lab-boundary` | What is deliberately untouched? | `impact-map.md#Negative-boundary`; `spec.md#AC-025-07`; `validation-plan.md#V-025-07` | SPEC 024 generator remains evidence-only; mock runs/history are not bulk refreshed; HTML is never canonical. | protected-boundary panel | `#impact-lab-boundary` | represented | mapped |
| execution | `execution.T-001` | What first makes the handoff usable? | `tasks.md#T-001` | Route/block editorial map and review; no promotion. | task card | `#task-T-001` | represented | mapped |
| execution | `execution.T-002` | What makes the commitment visible? | `tasks.md#T-002` | Skeleton identity, slots, lifecycle refusal. | task card | `#task-T-002` | represented | mapped |
| execution | `execution.T-003` | What prevents a polished omission? | `tasks.md#T-003` | Slot, task/proof parity, placeholder and provenance checks; no prose scoring. | task card | `#task-T-003` | represented | mapped |
| execution | `execution.T-004` | What proves the process in a real rich case? | `tasks.md#T-004` | Fresh M-003 pilot, source-to-render review and history preservation. | task card | `#task-T-004` | represented | mapped |
| execution | `execution.T-005` | What makes the visual commitment durable and generic? | `tasks.md#T-005` | Deep construction record, canonical component contract, profile-aware skeleton and independent desktop review. | task card | `#task-T-005` | represented | mapped |
| execution | `execution.T-006` | Is the skeleton now a working base rather than an example? | `tasks.md#T-006`; `decision-log.md#D-025-012` | Candidate copied from the skeleton, source-backed composition, declared base/hash and no promotion. | task card | `#task-T-006` | represented | composing |
| validation | `validation.V-025-01` | Is the map materially complete? | `validation-plan.md#V-025-01` | M-003 source-to-map comparison. | proof card | `#proof-V-025-01` | represented | mapped |
| validation | `validation.V-025-02` | Does the skeleton refuse promotion? | `validation-plan.md#V-025-02` | Identity, source-only state and renderer refusal. | proof card | `#proof-V-025-02` | represented | mapped |
| validation | `validation.V-025-03` | Does the final candidate expose tasks/proofs? | `validation-plan.md#V-025-03` | Positive/negative DOM/map parity. | proof card | `#proof-V-025-03` | represented | mapped |
| validation | `validation.V-025-04` | Are controls and authority recoverable? | `validation-plan.md#V-025-04` | Source → block → decision review. | proof card | `#proof-V-025-04` | represented | mapped |
| validation | `validation.V-025-05` | Is the rendered brief usable? | `validation-plan.md#V-025-05` | Independent desktop source/render review. | proof card | `#proof-V-025-05` | represented | mapped |
| validation | `validation.V-025-06` | Did existing guarantees regress? | `validation-plan.md#V-025-06` | Renderer, composition parity, bundle and relevant contracts. | proof card | `#proof-V-025-06` | represented | mapped |
| validation | `validation.V-025-07` | Did history remain preserved? | `validation-plan.md#V-025-07` | Before/after hashes and path inventory. | proof card | `#proof-V-025-07` | represented | mapped |
| validation | `validation.V-025-08` | Is a reviewed editorial exception transparent rather than a bypass? | `validation-plan.md#V-025-08` | Visible, exact-review-bound and expiring exception; hard checks unchanged. | proof card | `#proof-V-025-08` | represented | mapped |
| validation | `validation.V-025-09` | Is the visual construction contract real before composition? | `validation-plan.md#V-025-09` | Routed components, plan depth and independent desktop review recover the promised structure without factual invention. | proof card | `#proof-V-025-09` | represented | mapped |
| validation | `validation.V-025-10` | Does the composed candidate remain grounded in its skeleton and the actual architectural context? | `validation-plan.md#V-025-10`; `brief-candidates/stakeholder-brief.candidate.html` | Declared base/hash, no material placeholder, solution landscape and distinct relationship flow are source-recoverable before promotion. | proof card | `#proof-V-025-10` | represented | composing |
| validation | `validation.preserved-guarantees` | What must remain compatible while the flow changes? | `spec.md#FR-025-07`; `spec.md#FR-025-08`; `spec.md#AC-025-06` | One workflow/role sequence; offline HTML, Pearson when selected, accessibility, no-script, print, v1/v2 and existing promotion guarantees. | preservation checklist | `#validation-guarantees` | synthesized | mapped |
| evolution | `evolution.decisions` | What changed in the design? | `decision-log.md#D-025-001`; `decision-log.md#D-025-002`; `decision-log.md#D-025-003` | Canonical-path choice, lifecycle repair and independent approval. | decision timeline | `#evolution-decisions` | represented | mapped |
| evolution | `evolution.state` | What is truthful now? | `run-state.yaml#quality_gates`; `run-state.yaml#next_safe_step` | Spec/plan ready; brief and task gates remain false. | gate board | `#evolution-state` | represented | mapped |
| decision | `decision.call` | What approval is being requested? | `spec.md#2`; `spec.md#12` | Approve the controlled implementation path, not any generated conclusion. | decision callout | `#decision-call` | synthesized | mapped |
| decision | `decision.audience` | Who receives what decision support? | `spec.md#4` | Composer, independent reviewer, executive decision maker and Guardian maintainer each receive a distinct answer. | audience decision matrix | `#decision-audience` | represented | mapped |
| coverage | `coverage.register` | Why trust this brief? | `plan.md#7` | Source/target/disposition register and honest boundary. | coverage table | `#coverage-register` | represented | mapped |

**Coverage review request:** Verify that the map represents every material
outcome, requirement, acceptance/validation entry, risk, task, decision and
current authority. Return source → lost fact → decision impact for any gap.
