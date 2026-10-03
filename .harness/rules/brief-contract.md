# Brief Contract — Normative Source

## Status and dispatch

Single normative source for stakeholder-brief doctrine. BC-001 through BC-025
are defined exactly once here; other files cite IDs instead of competing
doctrine. Unqualified rules apply to every lineage. Explicit **v2** clauses
preserve the historical model/review contract; **v3** clauses govern new
generation and explicitly authorized refreshes. They are alternatives, never
cumulative gates. Legacy utilities remain available, not mandatory for v3.

## BC-001 — Brief authority and lineage

`stakeholder-brief.html` is a derived meeting projection. `spec.md`,
`impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md`,
`decision-log.md`, `progress.md` and `run-state.yaml` remain canonical.
Historical/pinned bytes are preserved. Before rendering, `brief_phase:
not_rendered` means no HTML delivery; scaffolding creates sources only.
For v3 composition/repair, existing consumer Markdown is correct by premise
and read-only. Source gaps are reported in HTML under BC-015, never repaired
as part of these operations.

## BC-002 — Version axis

New HTML uses exactly one axis, `data-brief-contract="3"`, resolved as `v3`.
Readers try the unified axis first, then recognized historical markers:

| Unified axis | Historical marker | Lineage |
|---|---|---|
| `"1"` | `data-harness-brief-design="v1"` | `v1` |
| `"2"` | `data-harness-brief-design="v2"` | `v2` |
| `"3"` | none | `v3` |

Historical `data-harness-brief-structure="executive-brief-v3"` and
`data-brief-shell-contract="v1"` are shell metadata, not lineage 3.
Absent/unknown lineage is a structural failure. Upgrade alone never migrates
HTML/state. v1 retains ready sources → concise brief → Human Visibility
review → task breakdown → Tasks Ready, without v2 coverage gates. v2 retains
BC-009's historical chain. Material refresh receives an explicit migration
diagnostic: choose v3 or record a reviewed legacy exception; continuing pinned
v2 is explicit, never a hidden prerequisite for v3.

## BC-003 — Applicable source set and principal heading

Read the canonical set in BC-001. Include `reproduction.md`, `ratchet.md`,
task evidence and handoffs when they contain stakeholder-material facts.
A principal item is a decision heading or named requirement, AC, task,
decision, risk or validation entry needed to understand the initiative.
Empty headings are source gaps, not permission to hide existing facts.

## BC-004 — Coverage disposition vocabulary

Applicable items use `represented`, `synthesized`, `not_applicable` (with
source-backed reason), or `link_only` (with relevance/reason). Core material
facts cannot be `link_only`. In v2 unresolved coverage gaps block review;
in v3 missing HTML facts are repaired, while facts absent from sources are
exposed as limitations, never claimed covered or invented (BC-015).

## BC-005 — Provenance attribute contract

Rendered blocks carry `data-source`, `data-source-section` (heading/optional
ID) and `data-coverage`; multiple locators use children or separate blocks.
**v2:** also requires `data-source-digest`, visible verbatim
`data-source-fragment` and `data-source-fragment-sha256`; decision-log digest
binds the exact named decision record. **v3:** traces file/heading → material
fact → tab/block inside HTML, with source snapshot/digests in existing
evidence/state when recorded. No hand-authored verbatim fragments, mandatory
JSON model, duplicate index or editorial sidecar is required. A valid locator
alone never proves factual completeness.

## BC-006 — Human coverage table

One human-readable register lives in `coverage`, mapping source locator,
material fact, disposition, target and reason/omission. v2 pairs its register
with BC-005's historical tuple. v3 starts from what should be present in all
applicable sources, compares it to HTML and exposes omissions/limitations;
listing only emitted blocks is not coverage. No permanently visible duplicate
register beside the tab.

## BC-007 — Canonical routes

Eight stable IDs, in order: `scope`, `architecture`, `impact`, `execution`,
`validation`, `evolution`, `decision`, `coverage`. Architecture is
`architecture`, never `architecture.global`. **v3:** all eight tabs remain,
including minimal cases, with honest conditional limits under BC-022.
**v2:** this is the closed `routes[]` vocabulary; BC-022 selects presence.
Pinned SPEC025 eight-route fixtures and SPEC024's unrelated vocabulary remain
historical regression/reference artifacts, not live v3 requirements.

## BC-008 — Construction record location

**v2:** construction lives in `brief-model.yaml`
(`schemas/brief-model.schema.json`), projected by `scripts/project_brief.py`;
no separate editorial map. **v3:** A reads sources and fills
`.harness/templates/stakeholder-brief.html` directly, preserving identity,
structure and components. HTML holds derived facts/provenance; neither model,
reviewed construction plan nor parallel narrative is mandatory.

## BC-009 — Two-pass brief protocol

**v3 default:** A (`executive-brief-composition`) authors HTML → B
(`rendered-brief-decision-review`) compares applicable source facts and
required slots, locates omissions/contradictions/inventions and repairs the
same HTML → same B (`executive-brief-experience-review`) opens every tab and
repairs explanation, SVG, hierarchy, cards, titles, concision and navigation →
report. Inspection needed to finish a repair belongs to that skill. No
pre-render review, routine return to A, reapproval, mandatory repeat of content
skill or third validation follows the two repairs.

**v2 historical only:** Executive Brief Reviewer performs independent pass
(a), model/construction before projection, comparing applicable headings and
selected routes, returning `APPROVE`/`REVISE` and setting
`brief_coverage_ready`; pass (b), rendered HTML over loopback, judges product,
architecture/operations and delivery as `recoverable`, `superficial`,
`absent` or justified `N/A`, setting `human_visibility_ready`. Recoverable
findings return to composition and relevant re-review. No third pass and no
Spec Guardian rendered review. Judgment is qualitative, not a semantic score.

## BC-010 — Actor identity and authority

**v3:** `A_id != B_content_id` and `B_content_id == B_visual_id`.
B is a reparador, not an independent evaluator of bytes B edited. Completion
is not `approve`, evidence approval, owner authorization or task `done`;
implementation builder/evaluator separation remains protected.
**v2:** reviewers are distinct from author/builder and do not edit while
evaluating. A named human substitutes if no independent agent is available;
otherwise the review gate stays blocked.

## BC-011 — Visual profile default

Vendor-neutral is default; client profile/brand selection must be source-backed
and explicit, e.g. `data-client-identity-profile="pearson"`. Preserve selected
identity without requiring a new brand. v2 retains local-logo/hash/no-hotlink
mechanics and reviewed material-layout exception in `decision-log.md`.
For v3 selected assets are embedded in the single HTML (BC-024); selection
never permits network or auxiliary-file display dependencies.

## BC-012 — Architecture visual contract

Material architecture (`data-architecture-visual="material"`) has distinct
named `data-architecture-node` IDs and visible labeled
`data-architecture-relation` connections between declared nodes. States
`proposed`, `preserved`, `out-of-scope`, `discovery` have visible meanings;
color alone is insufficient. **v3:** connected inline SVG, accessible name
(`role="img"`) and text equivalent explain supported relationships,
contracts/data, preserved/change boundaries and declared failures/limits.
Cards or textual arrows alone do not fulfill material architecture.
**v2:** supported semantic HTML forms remain valid with text equivalent.
Non-material/unknown architecture has a reason under BC-015, no invented graph.

## BC-013 — Decision-view content contracts

Each present tab opens with a clear purpose; richness follows material facts,
not quotas. v3 keeps all tabs; v2 applies this table to selected routes.

| Tab | Recoverable source content |
|---|---|
| `scope` | Identity, problem, business objective, beneficiaries, transformation, concrete benefit and measurable success criterion, scope/anti-scope, main risk, authority/requested decision. |
| `architecture` | Context, responsibilities, boundaries, relations, contracts/data/trust, operating and failure/rollback flows where declared (BC-012/014). |
| `impact` | People, surfaces, interfaces, information, compatibility, risks, controls, contingencies and source-backed owners. |
| `execution` | Material task objective/outcome/increment, FR/AC/discovery, scope/anti-scope, dependencies, risk/assurance, validation/evidence, exit criteria, status/authority and why-now. |
| `validation` | Each AC's claim, method, context, oracle, evidence destination and limitations. |
| `evolution` | Decisions/supersessions, gates, checkpoints, open risks/unknowns. |
| `decision` | Owner, current authorization, consequences/boundary and exact next safe step; HTML grants no approval. |
| `coverage` | BC-006 register, BC-005 provenance and honest omissions/limits. |

## BC-014 — Architecture proportionality profile

Source-backed depth: `localized/S` concise boundary; `M` context,
components/contracts and applicable critical flow; `L`/`high`/`unknown`
applicable responsibilities, data/trust, success/failure/rollback or explicit
omission reasons. Source-authoring Plan Ready rules remain protected. v3
composition never reopens Plan Ready or repairs MD for missing information;
it reports the supplied profile/limits under BC-015.

## BC-015 — Missing-fact / clarification contract

No generic filler, fabricated metric/relation/owner/approval/decision or vague
"to be confirmed". **v3:** HTML states exact source absence, locator, decision
impact and any owner/resolution path actually supplied; if absent, say so.
Use justified N/A only where inapplicability is supported. Existing facts
elsewhere must still be recovered. Finish with source limitations, without
changing/recreating MD or requiring routine clarification/reapproval.
**v1/v2 source workflow:** when absence materially blocks decision/AC/risk/
authority/next step, record fact, owner, impact and resolution in an existing
canonical source; absent owner/path is explicit, never attributed by inference.

## BC-016 — Rendered inspection method

**v3:** B's visual skill opens all eight tabs in a browser and records URL or
file/preview context, viewport and supported JS/no-JS behavior. Loopback is
available, not an exclusive gate. Unsupported file/preview/no-JS context is
a stated limit; lack of a browser to open all tabs makes the visual pass
`incomplete`, never completed merely by recording that limitation.
Inspection occurs during repair, not after it as
a third validation. **v2:** pass (b) is served on `127.0.0.1`; APPROVE
evidence names each opened selected-route HTTP URL. File/screenshot-only
reading does not fulfill that historical pass.

## BC-017 — Editorial exception

**v2:** only editorial findings use a reviewed decision-log exception:
ID, finding, source/target, decision impact, residual risk, owner, proceed
decision, expiry, next action, exact candidate/manifest SHA-256. It waives no
integrity/provenance/lifecycle/security gate and grants no readiness.
**v3:** repair available content/presentation and report genuine source or
environment limitations; no exception/reapproval gate is introduced.

## BC-018 — Meeting decision propagation

HTML never becomes the only decision record. Source-authoring owners append
meeting decisions to `decision-log.md` and propagate affected canonical
artifacts before authorizing tasks. v2 rechecks coverage/freshness and
regenerates the brief. v3 repair keeps sources read-only; subsequently
authorized source change/refresh uses BC-009 anew as a separate operation,
not a repeat gate after concluded repair. No HTML completion grants Tasks Ready.

## BC-019 — Source sufficiency pre-check

**v2:** deterministic source checks require AC validation paths, risk owners,
architecture profile, task exit criteria/evidence; failure blocks composition.
**v3:** supplied MD are authoritative/read-only by premise. Source gaps
become BC-015 limitations, not a precomposition gate or instruction to refactor
MD. Proportional technical checks never substitute qualitative repair.

## BC-020 — Blocking conditions

Never conclude false lineage, invented/contradictory facts, hidden material
omissions, author/reparador conflation, fabricated effort or task authority.
v3 repairs HTML defects; unavailable qualified actor, required effort or
browser inspection is `incomplete`, not success. Specific unsupported
preview contexts may be reported as limits under BC-016. v2 retains missing
coverage/provenance/reviewer/source-readiness gates. Structural PASS is not
semantic approval. Task/evidence/owner authorization gates remain separate.

## BC-021 — Accessibility and visual baseline

Keyboard/focus, reduced motion, responsive cards and local table/diagram
scroll preserve reading without global horizontal overflow. **v3:** only one
main panel visible at a time on screen, including no JS; native navigation
works offline. Print may show all tabs. Visual repair improves explanation
without cutting recovered material facts. v2 preserves no-script source order
and historical layout behavior.

## BC-022 — Profile × domain selection

**v3:** domain/profile chooses depth and representation within eight stable
tabs, never removes a tab. Conditional absence is supported limit/N/A under
BC-015. **v2:** profile/domain selects `routes[]` from BC-007; unselected
routes are absent without dispositions, coverage always present. Reasons for
deviations live in model/thesis/plan; no rigid domain hierarchy. Source-backed
non-software relations are as material as software.

## BC-023 — Reduced-depth exception

Formatting, comments or release administration may use justified N/A;
bugfix depth may be concise when reproduction, impact and validation are clear.
v2 still dispositions applicable topics. v3 preserves all eight tabs and
source-backed material facts; small size is not permission to omit them.

## BC-024 — Single-file template delivery

v3 delivers one self-contained `stakeholder-brief.html` with inline CSS,
navigation and SVG, system fonts and no network/auxiliary-file dependency for
display. Slots instruct source, decision question, material fields and useful
representation. Scaffold/placeholders do not count as delivery. Facts use
concise cards/tables/details without empty cards or loss of contracts.

## BC-025 — Effective effort and completion record

For both v3 B skills require effective `high` or `xhigh`, or explicitly
supported higher effort, confirmed from executor configuration. No mandatory
model/provider or invented universal API; prompt wording alone is not proof.
`medium`/unavailable effort cannot conclude a qualified pass. Record A/B
identities, effective effort per pass, source snapshot, repaired facts/visuals
and limits in existing evidence/state or final report, without permanent
agent file. Final disposition: `completed`,
`completed_with_source_limitations` or `incomplete`, never own `approve`.
No report invents implementation/evidence approval or a third review.

## Soft rule

Apply the version branch before composing/repairing. Doctrine stays compact:
role reads this contract plus operating files/skill; historical budget
measurements remain in SPEC029 evidence/T-008.md.

## Hard mirror recommendation

Mechanical readers
dispatch lineage and check containment, IDs/navigation and source integrity
proportionally; preserve legacy validators/projector/schema for v1/v2.
Such checks cannot certify meaning or create a third semantic gate in v3.

Recommended check: `validate-human-visibility` (version-aware mechanics).
