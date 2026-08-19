# Rule: Human Visibility

## Soft rule

Specs are execution contracts, but humans need one readable meeting surface
before work begins. For a non-trivial v2 initiative, `stakeholder-brief.html`
is the derived, progressively disclosed projection of the complete initiative;
Markdown, state, evidence and the append-only decision log remain canonical.

## Lineage applicability

Apply this v2 coverage, provenance and lifecycle contract only when the brief
declares `data-harness-brief-design="v2"`. Historical or pinned v1 briefs keep
their legacy lifecycle: ready source artifacts → concise v1 brief → Human
Visibility review → task breakdown → Tasks Ready. They do not require
`tasks_drafted`, `brief_coverage_ready`, v2 provenance attributes or a coverage
register merely because the bundle is upgraded.

A material v1 refresh (outcome, scope, architecture, impact, risk, validation,
tasks or decision-history change) must receive the version-aware migration
diagnostic and either migrate to v2 or record a reviewed legacy exception. The
diagnostic/enforcement is T-003 work; this rule does not rewrite historical
HTML. Once migrated, the v2 lifecycle is mandatory from the next affected gate.

The applicable source set is `spec.md`, `impact-map.md`, `plan.md`,
`tasks.md`, `validation-plan.md`, `decision-log.md`, `progress.md` and
`run-state.yaml`. Include `reproduction.md`, `ratchet.md`, task evidence and
handoff information only when they contain stakeholder-material facts. A
principal heading is a source's top-level decision heading, plus a named
requirement, acceptance, task, decision, risk or validation entry that a
meeting participant must be able to inspect. Empty headings are gaps, not
license to omit them.

Before final rendering, the author records a coverage composition plan in the
existing technical plan or decision log; do not create a sidecar or duplicate
JSON index. Every principal applicable item has exactly one disposition:

| Coverage | Meaning |
|---|---|
| `represented` | A rendered block presents the material source fact directly. |
| `synthesized` | A rendered block accurately condenses one or more source facts. |
| `not_applicable` | The item does not affect this initiative; record the source-backed reason. |
| `link_only` | The source is linked but not rendered; record stakeholder relevance and reason. |

For each rendered v2 block, use stable `data-source`, `data-source-section`
and `data-coverage` attributes. `data-source` is one canonical relative source
path; `data-source-section` is its stable Markdown heading locator and optional
ID (for example `7-functional-requirements#FR-003`); `data-coverage` is one of
the four values above. Repeat a block or use a child block for each distinct
source locator rather than encoding a second machine index. The page also has
a human-readable coverage table with source locator, disposition, rendered
target and required reason. This attributes-plus-table model is the complete
provenance contract; embedded JSON and a separate coverage sidecar are not
allowed by default.

Material headings from `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
`validation-plan.md` and `decision-log.md` cannot be `link_only`. A
`not_applicable` or `link_only` row always identifies the reason. The brief
does not copy every sentence: loss-aware synthesis is allowed, invented claims
are not.

## Required contract

Each non-trivial feature, epic or behavior-changing initiative includes
`stakeholder-brief.html` alongside the spec. A v2 brief retains the concise v1
executive orientation while making value/scope, solution/architecture,
impact/risk, execution/tasks, validation/evidence, decisions/evolution and
sources/coverage progressively inspectable. It declares the requested decision,
outcome, scope/anti-scope, affected actors/surfaces, demonstrable increment,
acceptance and validation, risks, decisions/open questions and next safe step.

The author creates preliminary tasks before the final brief, clearly labels
them as drafts, and records `tasks_drafted`; this never authorizes
implementation. The author then prepares the composition plan. A distinct
coverage reviewer compares it with every applicable source heading before final
rendering and records missing headings, weak synthesis, contradictions,
unsupported claims, stale decisions, hidden unknowns and insufficient
architecture depth. Record reviewer identity, author identity, date, finding
status and the review record locator in the existing `decision-log.md` and
`run-state.yaml`. Self-review cannot set `brief_coverage_ready` or Human
Visibility Ready. If a distinct agent is unavailable, a named human reviewer
performs and records the same review; otherwise the gate remains blocked.

After the final render and Human Visibility review, the meeting may decide.
Meeting decisions are appended to `decision-log.md`, propagated to every
affected canonical source, rechecked for coverage/freshness and reflected by a
regenerated brief before `tasks_ready` can become true. Never edit the HTML as
the only record of a decision.

## Architecture proportionality

Plan Ready must establish source-backed current/target context,
components/responsibilities, interfaces/events/contracts, data ownership and
lifecycle, security/trust boundaries, critical runtime flows, failure behavior,
NFRs, compatibility/migration, observability, rollout/rollback, alternatives
and unknowns. The profile controls depth, never whether a material topic gets a
disposition:

| Profile | Minimum decision surface |
|---|---|
| localized/S | Text or one boundary view when it adds a decision; record concise N/A reasons. |
| M | Context, changed components/contracts and a critical flow when applicable. |
| L, high or unknown | Applicable context, responsibilities, data/trust and success/failure/rollback views, or a source-backed omission reason. |

If required source information is missing, record the unknown, owner and
resolution path. Block Plan Ready or create a bounded discovery task; neither
the author nor reviewer may fabricate a diagram, data flow or failure claim.
Use minimum-safe abstraction and record required redaction rather than exposing
secrets, PII or sensitive topology.

## Conditional author/reviewer checklist

- [ ] the applicable source inventory and every principal-heading disposition
  are explicit; core material headings are not link-only;
- [ ] every rendered v2 content block has the three provenance attributes and
  the coverage table can be checked without another machine-readable copy;
- [ ] outcome/benefit, scope/anti-scope, actors/surfaces, validation, risks and
  requested decision are specific; size, rationale and smaller option are visible;
- [ ] preliminary tasks visibly remain drafts until post-meeting propagation;
- [ ] architecture depth follows the S/M/L/high/unknown profile; each included
  visual has a source, text equivalent and non-colour explanation;
- [ ] author and independent reviewer identities and the review record are
  present; unresolved gaps block the gate;
- [ ] the rendered page supports a 60-second executive scan and deeper source
  recovery without replacing the canonical artifacts.

## Design standard and exception

Populate the canonical template and retain its versioned design lineage and
meeting shell. Historical v1 briefs retain their v1 contract until a material
refresh or explicit migration. A v2 brief uses the v2 lineage defined by the
versioned template; detailed DOM and validator enforcement ship with that
template, not as a reason to mutate historical HTML.

A materially custom layout is allowed only with a reviewed exception in the
initiative `decision-log.md` containing rationale, owner and retained decision
surfaces. Do not add a separate layout-exception sidecar.

## Blocking conditions

Block or request revision when:

- an applicable source, principal heading, coverage disposition, required
  reason or provenance tuple is absent;
- a material core heading uses `link_only`, a brief contradicts sources, or a
  claim/visual invents an unsupported commitment;
- `tasks_drafted`, `brief_coverage_ready`, Human Visibility and Tasks Ready are
  conflated, or draft work appears authorized;
- coverage reviewer and author are the same identity, the review record is
  absent, or a named human has not substituted for an unavailable reviewer;
- required architecture information/profile is missing without a bounded
  unknown/discovery path;
- a meeting decision exists only in HTML or has not refreshed affected sources;
- stakeholder-visible uncertainty is hidden in technical language.

When the brief exposes a missing business, product or priority decision,
request human clarification. Do not infer it.

## Allowed exception

Formatting-only, comment-only or release-administrative maintenance may record
`not_applicable` with reason in the coverage plan. Bugfixes may use concise
depth when reproduction, impact and validation are clear, but still disposition
every applicable topic.

## Hard mirror recommendation

Use a version-aware brief validator to enumerate applicable sources/headings,
check provenance/coverage attributes and table, required views, freshness and
distinct review metadata. Keep semantic synthesis, diagram fitness,
accessibility and meeting usefulness in the independent review; no structural
pass may claim semantic or aesthetic approval. Validate lifecycle order and
Plan Ready architecture profiles with focused fixtures.

Recommended check: `validate-human-visibility` plus
`test-brief-v2-contracts`.
