# Technical Plan: <initiative>

**Status:** draft | plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:**  
**Last updated:**

## 1. Technical approach

Describe sequence, boundaries and why this is the smallest safe approach.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | | | | |

## 3. Size and proportionality

**Initiative size:** S | M | L.  
**Why:** one sentence on the affected boundaries and risk; this is not an effort estimate.  
**Smaller option considered:** state the smaller approach and why it is sufficient or insufficient.  
**Complexity deliberately excluded:** state infrastructure, process or scope not justified by the outcome.

### Client visual profile selection (conditional)

Every new v2 brief is vendor-neutral unless the canonical sources select a
client profile. This `plan.md` remains the canonical record for that selection
or a dated historical/legacy or material custom-layout exception; do not create
a second initiative-state file for branding.

| Field | Required record |
|---|---|
| Default profile | `vendor-neutral`; it carries no client logo or client asset reference. |
| Pearson selection | Only when the rendered HTML explicitly selects `pearson` with `data-client-identity-profile="pearson"`. |
| Brand authority | `.harness/references/pearson-design.md` when Pearson is selected. |
| Asset | Local `.harness/assets/brand/pearson-logo-white.png` only when Pearson is selected; no hotlink or CSS filter. |
| Asset distribution | The renderer provisions that exact file only for a selected Pearson brief; a divergent pre-existing file is a clear failure, never an overwrite. |
| Font boundary | Pearson's system fallback applies only to the selected profile; no packaged font or network request until separately authorized. |
| Exception | Dated historical/legacy or reviewed custom-layout decision with owner, retained decision/accessibility surfaces and review outcome. |

Do not use the Pearson root marker, logo or asset without a source-backed
selection. A visual reference alone does not authorize a custom layout or a
different asset.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** unknown | A1-local | A2-elevated | A3-critical-local-policy  
**Rationale and trigger evidence:**  
**A2/A3 source links/headings (or A1 N/A reason):**  
**Reapproval trigger:** profile change, envelope breach, new trust/data/public
boundary, or an assurance failure/waiver.

### Architecture scope/size profile (separate from assurance profile)

State the architecture scope/size profile (`localized/S`, `M`, `L`, `high` or `unknown`) and
complete every applicable row before Plan Ready. An omission needs a source-backed
reason. Missing material information becomes a named unknown with owner and
resolution path; block Plan Ready or create a bounded discovery task rather
than inventing a diagram or contract.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | | | |
| Components/responsibilities | | | |
| Interfaces/events/contracts | | | |
| Data ownership/lifecycle | | | |
| Security/trust boundaries | | | |
| Critical runtime flows | | | |
| Failure behavior | | | |
| NFRs | | | |
| Compatibility/migration | | | |
| Observability | | | |
| Rollout/rollback | | | |
| Alternatives/trade-offs | | | |
| Unknowns | | | |

### Current → target → delta and complexity envelope

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Architecture/method | | | | |
| Modules/classes/APIs/data/contracts | | | | |
| Process/tooling | | | | |

Use bounded counts or `not_applicable` with reason when meaningful. This is a
decision envelope, not a speculative implementation inventory.

| Architecture scope/size profile | Minimum architecture decision surface |
|---|---|
| localized/S | Concise text or one boundary view only when it improves a decision. |
| M | Context, changed components/contracts and applicable critical flow. |
| L, high or unknown | Applicable context, responsibilities, data/trust and success/failure/rollback views; source-backed omissions only. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | | | | |

## 6. Contracts, data and compatibility

- API/events:
- Database/storage:
- External systems:
- Compatibility/migration:

## 7. Security, privacy and permissions

- Authentication/authorization:
- Secrets/PII:
- Required permission:
- Destructive operations and approvals:

## 8. Rollout, observability and rollback

- Rollout:
- Success/failure signals:
- Rollback trigger:
- Exact rollback/checkpoint:

## 9. Brief coverage composition (v2 when applicable)

Before final rendering, inventory the applicable sources and principal headings
in this existing plan. For each, record source locator, coverage disposition,
rendered target and any required reason. Do not create an embedded JSON index
or coverage sidecar. Core material headings may not be `link_only`.

| Source locator | Coverage (`represented`/`synthesized`/`not_applicable`/`link_only`) | Rendered target | Reason when required |
|---|---|---|---|
| | | | |

Record the author, distinct coverage reviewer, review date, findings status and
the `decision-log.md` row that records the review. The review must precede
`brief_coverage_ready`; a named human reviewer is required if an independent
agent is unavailable.

### 9.1 Brief construction record — required before skeleton instantiation

Coverage says that a source reaches a target. The construction record says how
the resulting subpage will make a decision intelligible. Add one row for every
route and one additional row for every material repeated component (affected
architecture domain, impact surface, task, validation/AC, decision or other
source-defined collection). This stays in `plan.md`; it is not a second source
of truth.

#### Brief thesis and global choices

| Field | Record |
|---|---|
| Decision and audience | |
| Brief thesis | |
| Global relationship(s) to make visible, if material | |
| Visual profile / boundary | vendor-neutral unless a canonical source selects another profile |
| Repeated component treatment | Which source-defined collections need one record per item, and why |

#### Route and repeated-component record

| Route / component ID | Executive question and reader | Narrative arc | Source facts and relationships to recover | Chosen visual form and reason | Repetition / required fields | Absence, uncertainty or discovery | Rendered target | Closing action |
|---|---|---|---|---|---|---|---|---|
| `scope` | | orientation → value → boundary → decision | outcome, actors, scope and anti-scope | prose, comparison, table or other with reason | applicable actors / boundaries | | | |
| `architecture.global` | | orientation → significance → structure → trade-off → action | responsibilities, flows, boundaries, controls | topology, lane, table, prose or other with reason | affected domain zooms: role, change, unchanged boundary, contract, dependencies, linked task, recovery | | | |
| `impact.<id>` | | delta → exposure → control → action | surface, owner, risk and control | footprint, chain, dossier, table or other with reason | delta, owner, exposure, control, rollback | | | |
| `execution.task.<id>` | | orientation → increment → dependency → assurance → next gate | task outcome, scope, anti-scope, risk/control, validation/evidence | task dossier, sequence, table or other with reason | ID, outcome, scope, anti-scope, dependency, risk/control, AC/proof, evidence, exit, authority, why now | | | |
| `validation.proof.<id>` | | claim → method → oracle → limit → gate | objective, method, context, AC, oracle, evidence, owner, limitation | proof dossier, matrix, flow or other with reason | all applicable fields named in previous column | | | |
| `evolution` | | state → consequence → next step | milestones, changes or pending discoveries | timeline, register, prose or other with reason | source-backed events only | | | |
| `decision` | | context → authority → consequence → action | decision, owner, authority, trade-off and next action | decision record, comparison, prose or other with reason | source-backed decisions only | | | |
| `coverage` | | source → disposition → confidence → action | source locator, fact, target and disposition | coverage table, register or other with reason | every applicable source heading | | | |

For every route, record a source-backed entry or an explicit N/A/discovery
explaining the decision impact. The skeleton renders one route at a time; it is
not a long page of anchored sections. Add a row for every material repeated
item; do not turn a source-defined collection into title-only cards.

Use these component dossiers when applicable:

- Architecture global view: nodes/responsibilities, flows, change and preserved
  boundaries, legend, relevant contract/control, and links to task dossiers.
  Each affected domain gets a zoom dossier with role, owner, change, unchanged
  boundary, contract, dependencies, linked task and recovery.
- Impact: one dossier per material surface with delta, owner, exposure,
  control and next action; show rollback and protected boundaries.
- Execution: source-backed epic/phase arc only when a grouping exists, then a
  full dossier for every material task. Never show title-only tasks.
- Validation: applicable assurance pillars and flow, then one full proof dossier
  for every validation/acceptance criterion: element/objective, method,
  context, acceptance criterion, oracle, evidence, owner and limitation.
- Evolution and decision: decision/gate ID, context, owner, authority,
  consequence and next action. Coverage: source → fact → visual target →
  disposition/reason.

An inapplicable component requires a visible, source-backed absence card with
reason and decision impact. A missing material fact becomes an owned discovery;
it is never silently omitted. The reviewer judges clarity, proportionality and
form choice. Deterministic checks verify only routes, targets, IDs, slots,
provenance and lifecycle.

#### Independent construction review — before skeleton instantiation

A reviewer distinct from the plan author compares requester intent and
canonical sources with this construction record before a skeleton is copied.
The review returns only `APPROVE` or `REVISE`; it is qualitative evidence, not
a score, quota, diagram requirement or deterministic HTML instruction.

| Author | Reviewer | Date | Verdict | Review record / decision-log locator | Blocking recovery |
|---|---|---|---|---|---|
| | | | `APPROVE` / `REVISE` | | |

For a `REVISE`, record each finding as: **source → loss or ambiguity → decision
prejudiced → canonical correction**. `APPROVE` means every material route and
repeated component has a recoverable planned treatment or a source-backed
N/A/discovery; it does not approve final HTML. Do not instantiate the skeleton
while a blocking `REVISE` remains.

The composed candidate is authored in HTML/CSS/JS by an agent that reads this
reviewed construction record and the canonical sources. Scripts may copy the
blank shell, verify contracts, promote exact reviewed bytes and capture
evidence; they must not parse Markdown to summarize a SPEC, choose a visual
form, write narrative, construct a topology or generate final route blocks.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | | | | yes/no |

## 11. Plan decision

**Plan Ready:** no  
**Reviewer:**  
**Reviewed at:**  
**Conditions/links:**
