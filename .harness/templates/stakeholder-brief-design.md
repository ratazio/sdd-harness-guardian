# Stakeholder Brief Design Standard

## Lineage and authority

`stakeholder-brief.html` is an offline, derived meeting projection; Markdown,
state, decisions and evidence remain canonical. New complete-decision briefs
use `data-harness-brief-design="v2"` and are vendor-neutral by default.
Pearson is an explicit opt-in: only a source-backed rendered brief that
literally declares `data-client-identity-profile="pearson"` may use its identity
assets. Historical or pinned `v1` and pre-cutover v2 briefs retain their
recorded contract until a material refresh follows the explicit migration path;
do not silently rewrite them.

The vendor-neutral v2 shell provides proportionate spacing, visible focus and
restrained borders/shadows. A selected Pearson profile adds its local
navy/lavender/white treatment, 8px spacing rhythm and readable Plus Jakarta
Sans system fallback. It adds eight anchored
decision views in one HTML: value/scope, architecture, impact, execution,
validation, evolution, decision and coverage. A custom layout requires a
reviewed exception in `decision-log.md`; no layout sidecar is allowed.

When Pearson is selected, the official local white logo is an actual image
inside a named native link. Its relative URL resolves only when the consumer
contains `.harness/assets/brand/pearson-logo-white.png`; the renderer provisions
it and verifies the release hash. A vendor-neutral brief does not load, copy or
reference that asset. Never replace it with a hotlink, data URI or a path into
the installed bundle.

The canonical base is `<style data-harness-brief-shell>` for neutral briefs or
the single `<style data-harness-pearson-shell>` only for the explicit opt-in;
do not inject a second unmarked base. When a material visual override is
declared with `<style data-harness-visual-override>`, place one
`<meta name="harness-pearson-layout-exception">` in the same document. Its
semicolon-delimited `content` records `decision`, `owner`, `reason`,
`retained`, `review` and an ISO `re-review` date. This is a narrow, auditable
exception contract—not permission to remove semantic/provenance, no-script,
print, focus or tab behavior. A dated historical/legacy control instead uses
`<meta name="harness-pearson-exception">` with its classification, decision,
owner, reason, retained surfaces, review and re-review date.

The brief helps a person select a decision surface; it is not a second spec,
task system, architecture framework or semantic-quality score. It can describe
software, operations, research, policy or a localized change. Technical words
such as component, API or data boundary appear only when their source fact is
material to the initiative.

When an editorial finding is explicitly promoted under a reviewed editorial
exception, render the exception as a visible callout in the Evolution or
Decision view. It must reproduce the decision-log record's ID, finding,
source → rendered target, decision impact, residual risk, accountable owner,
decision to proceed, expiry and next action, plus the exact candidate and
composition-manifest SHA-256 bindings. This narrow projection cannot waive
integrity, provenance, lifecycle or security controls, and it must visibly say
that Human Visibility and Tasks Ready remain false until normal correction,
rerender and re-review complete. Do not use a hidden meta tag, a sidecar or an
HTML-only exception record.

## Provenance and progressive disclosure

Every material rendered section or child block has exactly one canonical
`data-source`, its heading/ID in `data-source-section`, and a
`data-coverage` disposition plus `data-source-digest` for that local source.
It also carries a literal source-supported `data-source-fragment` and its
`data-source-fragment-sha256`: the fragment must occur in both the local source
and the visible block. This makes the locator reproducible and prevents a
foreign fact from being cosmetically relabelled as a local one. It does not
score, count or prescribe the surrounding prose; semantic sufficiency remains
the distinct human review.
For `decision-log.md`, use the exact named decision-record digest rather than
the whole self-referential file. Use `synthesized`, `represented`,
`not_applicable`, or `link_only`; `not_applicable` and `link_only` must state
their reason. A gap is a blocking finding, never a coverage disposition. Do not
put CSV source lists in one block. Core material must be synthesized or
represented, never `link_only`.

A composed candidate changes the scaffold's generic source/locator/coverage
topology to its reviewed mapping. The renderer may verify that lineage identity,
but it does not rate the prose, count visual components or replace the human
review of semantic sufficiency.

The coverage view contains the human register with source, principal heading,
stable target ID, disposition and rationale. This table complements DOM-local
provenance; it is not JSON or a sidecar.

Native anchors, source order and open `details` are the baseline. The accepted
v2 template progressively enhances that one document with tabs only after load:
without script, every panel remains in source order; keyboard focus stays
visible; print reveals all content. No framework, route, remote asset or
JS-only content is needed.

## Content sufficiency before composition

For each tab, first identify its material decision and then recover the
supporting fact from a canonical source. A fact is eligible when it helps a
stakeholder decide scope, value, risk/control, execution, proof, authority or
next safe step. State it faithfully, summarize it with provenance, or make a
concise source-backed N/A disposition. Do not turn a blank optional field into
generic prose, a fictional technical layer, a decorative diagram or a vague
“to be confirmed”.

Ask for clarification only when the missing fact would block or materially
change one of: a requested decision, acceptance criterion, risk control,
authority, or next safe step. Record the question in the existing plan,
decision log or progress source—not in an HTML sidecar—with these four compact
parts:

1. **Exact needed fact:** what is absent, without a generic questionnaire.
2. **Accountable owner:** the person, role or discovery task able to resolve it.
3. **Decision impact:** which decision, AC, risk or next step cannot safely
   proceed, and why.
4. **Resolution path:** answer source, bounded discovery, or explicit
   source-backed N/A/deferral and its checkpoint.

If the absence does not have that material effect, do not ask merely to make a
tab look complete. Use a concise N/A with a reason when the reader needs to
know why the topic is absent; otherwise leave the optional child detail out.
An unknown is owned and recoverable, never a blocker disguised as a filler
sentence. Sensitive facts are redacted to the minimum useful abstraction with
the access constraint recorded.

## Eight decision-view contracts

Every view opens with a short **mission** and, where useful, a **vision** that
orients the reader before evidence. The following are content contracts, not
mandatory field quotas. Include only facts supported by the source profile and
make a justified absence visible when it changes the decision.

| View | Mission and eligible source-backed depth | Source posture when detail is absent |
|---|---|---|
| **Value and scope** | Explain the initiative’s mission; affected people or operating outcome; main pillars of delivered value; high-level technical/operating pillars only when they influence the decision; outcome level, limits/anti-scope, main risk and current authority/requested decision. | Do not invent a technical pillar for a non-technical change. Ask only when the missing value, limit, risk or authority blocks scope/priority/approval. |
| **Architecture** | Introduce the architecture mission and vision, then show the source-backed context, responsibilities, boundaries, contracts, data/trust, failure/rollback or operating flow warranted by the profile. A diagram has a textual equivalent. | A localized/simple initiative may use one boundary sentence or a justified N/A rather than decorative boxes. Missing material architecture is an owned unknown or Plan Ready block. |
| **Impact** | State the impact objective and change footprint: people, work surfaces, interfaces, information, compatibility, risks, controls, contingencies and owners as applicable. “Surface” is a neutral affected area, not a command shell or a programming layer. | Never manufacture a deployment/API impact. Record a concise reason when a normally relevant blast-radius dimension does not apply. |
| **Execution** | Explain how work reaches a safe increment. For every material task, project the existing non-empty task contract: objective/outcome/increment, FR/AC or discovery question, scope/anti-scope, files/contracts when present, dependencies, risk/assurance, validation/evidence, exit criteria, status/authority and why it is next. Tasks may be research, operation or delivery work. | A title/status alone is insufficient when the canonical task contains detail. Do not invent files, implementation or priority; absent material fields become a source question/N/A under the rule above. |
| **Validation** | Explain what claim is proved, how, in what context, with which oracle, evidence destination and limitation. Project the canonical AC trace and its method, command **or** manual steps/environment, fixture/data when relevant, expected result/oracle, owner and legitimate skip/risk rationale. | A command is not universal. A non-software or no-command check remains truthful when its method, context, oracle, evidence and limitation are recoverable; ask only when lack of proof blocks a decision or AC. |
| **Evolution** | Make decisions, supersessions, current gates, checkpoint, open risks/unknowns and changes of state recoverable. | Do not infer authority from prose or a visual state. Missing authority/gate that changes what is allowed is a material question. |
| **Decision** | State the decision owner, current authorization, consequence, boundary and one exact next safe step. Distinguish proposal, ready, evidence review and approved/done. | HTML never grants approval. If owner, trigger or consequence is unknown and action depends on it, ask/record it in canonical state. |
| **Coverage** | Show why the source set supports the view: human coverage register, local provenance, dispositions and reasons, plus any material gap. | Coverage cannot convert missing facts into proof. `link_only` cannot hide core material and an absence must retain its rationale. |

## Architecture, impact and states

Choose architecture depth from the source-backed S/M/L/high profile. Every
included diagram node, edge and text equivalent maps to one source block;
unknown material detail is a discovery or block, never an invented claim. A
localized change may use a concise justified N/A instead of a diagram. The
impact view uses the same proportional rule for a change footprint, regardless
of whether the work is software.

### Material architecture visual contract

When an authored v2 architecture route declares
`data-architecture-visual="material"`, it makes a narrow, testable claim:
the route contains a source-backed structural projection, rather than a
paragraph dressed as a diagram. The topology wrapper uses
`data-architecture-projection="topology"` and declares `svg` or
`semantic-html` as its renderer. It names at least two
`data-architecture-node` entries with distinct `data-architecture-node-id`
values; every `data-architecture-relation` has a visible
`data-architecture-relation-label` plus `data-architecture-relation-from` and
`data-architecture-relation-to` values that link two declared node IDs. Every
declared relation is validated, so one valid edge cannot mask an invalid or
self-referential edge. This prevents a
loose arrow from posing as a connected topology. The accessible legend exposes
the four textual states `proposed`, `preserved`, `out-of-scope` and
`discovery`, each with non-empty visible text. An SVG topology uses an
accessible `role="img"` SVG with non-empty `aria-label` or `title`/`desc`,
plus a non-empty `data-architecture-text-equivalent`. Semantic HTML has the
same non-empty text-equivalent requirement.

The same route then carries a `surface-map` projection with a source-backed,
non-empty `data-architecture-unit` and named
`data-architecture-surface` entries. This unit may be “declared integration
surfaces”, for example; it must never silently become a count of files,
screens, people or effort. A `zoom` projection is also required. It is either
`supported` with a named source-backed target, or explicitly
`not_applicable`/`discovery` with its reason. Every projection declares
`data-architecture-source-backed="true"` and the normal local provenance
tuple (`data-source`, `data-source-section`, `data-coverage`).

Do not mark the route material merely because it has a technical heading. A
localized or immaterial route omits this declaration altogether, or declares
`not-material`, `not_applicable` or `discovery` with
`data-architecture-visual-reason`. That path deliberately requires no SVG.
The deterministic check proves only this structural promise; a distinct
rendered review remains responsible for factual completeness, accessibility,
legibility and executive usefulness.

Show task drafts, dependency, outcome linkage, validation and evidence, but
label drafts as non-authorizing. Do not claim coverage review, Human Visibility
or Tasks Ready from the HTML. Record decisions append-only and propagate a
meeting decision to canonical sources before regenerating the brief.

## Review and rendered usefulness

After rendering, a reviewer separately checks product,
architecture/operations and delivery for `recoverable`, `superficial`, `absent`
or justified `N/A`. A synthesis loss is recorded as source → lost fact → source
correction, plus the material decision that cannot be made from the brief
alone. The reviewer also checks that each question meets the four-part
clarification contract and that a non-software/localized view did not acquire
fictional technical detail. This is human/agent judgment; no score, prose
parser or automated semantic approval belongs in the HTML contract.

## Visual/accessibility baseline

Use `"Plus Jakarta Sans", "Segoe UI", Arial, sans-serif` without packaging or
fetching a font until separately authorized. Keep Pearson navy/lavender/white
as the canonical base and visible text alongside every color-coded state. The
official local white logo is an actual image inside a named native link—never a
hotlink, CSS filter or `role="img"` anchor. At narrow widths cards stack, wide
tables/diagrams scroll locally, and the page never gets global horizontal
overflow. Preserve keyboard focus, no-script source order, reduced motion and
print; validate desktop, 320px/768px/1024px/1440px, keyboard and print
behavior separately; structural validation never proves semantic usefulness.

## Composition kit: source-aware mini-templates

This catalogue is an integrated authoring aid, not a second renderer, a
component runtime or a post-generation repair agent. Choose the smallest
pattern that makes a supported decision recoverable. Each child block retains
its own provenance tuple; source facts remain canonical.

### Depth selection

1. **Orientation (0):** one short mission/vision sentence when a view affects
   a decision. It may be the complete architecture output for a local policy,
   research or document change.
2. **Macro relation (1):** show two or more source-backed actors, work areas,
   responsibilities or stages when their relation changes scope, risk or
   validation. Use structured HTML/SVG and a textual equivalent.
3. **Focused cut (2):** add at most one subordinate view only when the source
   names the selected boundary, responsibility, one interface/data/trust/failure
   implication, and the decision it explains. Do not recurse or infer modules.

If any required level-2 fact is absent, omit the cut. If that absence changes
scope, acceptance, control, authority or the next safe step, record the owned
four-part question in canonical sources instead. A non-software boundary may
be a handoff, approval, operational control or research workstream.

### Reusable projections

| Semantic role | Render only when source supplies it | Omit / escalate rule |
|---|---|---|
| `brief-architecture-cut` | Boundary, responsibility, information/contract, trust/data/failure implication and decision. | Omit an unsupported cut; own a material architecture gap. |
| `brief-task-card` | Objective/outcome, increment, scope/anti-scope, contracts/artifacts, dependency, risk/assurance, validation/evidence, exit/status/authority and why-now. | Do not print a generic label for an empty optional field; own a missing material execution fact. |
| `brief-proof-card` | Claim/AC, method, command **or** manual context, fixture/data when relevant, oracle, evidence, owner and limitation. | A command is optional; method/context/oracle/evidence are not optional when an AC needs proof. |
| `brief-absence-note` | Concise source-backed N/A or limitation and why the topic does not alter a decision. | Never use it to hide a material unknown or placeholder. |

Rich input may use every populated role. Sparse input renders only the
recoverable subset. A card is a source projection—not a new required task
schema—and it may describe delivery, operations or discovery rather than code.

### Reviewer trace

For a deeper block, review source locator → fact → rendered block → decision.
Return a loss to the canonical source with the decision it prevents; never
repair a fact only in HTML. Confirm that rich fixtures expose full task/proof
contracts, while sparse and non-software fixtures have no invented technical
fields. These are qualitative judgments, not automated prose scoring.

### Impact and coverage compositions

Do not reduce impact to one uniform matrix when the source contains a useful
relationship. Select among: a **surface footprint** (affected actor/work area/
information/interface and delta), a **risk chain** (event → signal → control →
contingency → owner), or a **compatibility path**. Keep the source table or an
equivalent structured reading order when a dense comparison remains material.
For a local/non-software change, one concise source-backed card can be more
truthful than a decorative multi-surface map.

Coverage first groups the source/heading → rendered decision view →
disposition/rationale relationship for scanning, then retains the mandatory
human-readable coverage table. At narrow widths, a wide matrix may become
labelled cards or scroll locally; neither transformation may remove provenance,
text state or the source order. Use `brief-impact-footprint`,
`brief-risk-chain` and `brief-coverage-group` as semantic hooks, not a fixed
visual quota.

Before linking or presenting a derived brief, compare every task ID in a
populated ledger with the Execution panel and every AC ID in a populated trace
with Validation. The comparison checks identifiers only; it cannot score prose
or approve usefulness. A scaffold with populated sources must declare
`data-brief-phase="scaffold"`, remain outside Human Visibility/Tasks Ready and
never be presented as the generated brief.
