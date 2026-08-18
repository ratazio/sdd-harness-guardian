# Rule: Human Visibility

## Soft rule

Specs are execution contracts, but humans need a concise review surface before
work begins. Non-trivial initiatives must include a stakeholder brief that makes
the intended outcome, scope, impact, risks and validation easy to review in a
meeting.

The stakeholder brief is a derived artifact. It improves visibility and shared
understanding, but it never replaces `spec.md`, `impact-map.md`, `plan.md`,
`validation-plan.md` or `tasks.md` as source of truth. Create or refresh it in
one synthesis pass after those sources are ready; refresh again only when
outcome, scope, architecture, impact, risk or validation changes materially.

## Required contract

Each non-trivial feature, epic or behavior-changing initiative includes
`stakeholder-brief.html` alongside the spec. The brief declares:

- what will be done;
- why it matters, using the declared outcome;
- who is affected;
- what surfaces, files, systems or contracts may change;
- what is explicitly out of scope;
- the demonstrable increment or uncertainty reduction;
- the most important acceptance criteria;
- validation approach;
- risks, decisions and open questions;
- the next safe step.

It also makes proportionality visible: declare qualitative size `S`, `M` or
`L`, give a one-sentence rationale, and state whether a smaller approach was
considered. This is not a delivery estimate.

## Conditional author/reviewer checklist

Use this one checklist while authoring and reviewing; do not create a separate
per-initiative checklist artifact.

- [ ] outcome/benefit, scope/anti-scope, affected actors/surfaces, validation,
  material risks and requested decision are specific;
- [ ] size, rationale and smaller-option decision are visible;
- [ ] show one compact architecture view only when two or more components, a
  contract, data boundary or material architecture decision changes; otherwise
  state why the change is localized;
- [ ] show one compact impact map only when three or more surfaces, indirect
  effects or medium/high/unknown risk apply; otherwise use a short surfaces table;
- [ ] show one compact flow only when a journey, multi-step execution, handoff,
  failure path or rollback needs explanation; otherwise state why it is omitted;
- [ ] each included visual exposes a concrete boundary, dependency or trade-off,
  includes a text equivalent, and does not rely on color alone;
- [ ] the rendered page passes a 60-second scan: a reviewer can state outcome,
  impact, size and requested decision without opening another artifact.

For local/S work, keep the brief materially shorter and omit visuals that do not
improve a decision. For M/L work, a five-minute read and 600–900 visible words
are reference points, never a minimum or automated gate.

The brief must be concise enough for a stakeholder review and specific enough to
spot misalignment before implementation starts.

## Design standard and exception

Populate the canonical template and retain its versioned design lineage and
meeting shell. The deterministic contract detects missing lineage/shell, not
rendered quality. A materially custom layout is allowed only with a reviewed
exception in the initiative `decision-log.md` containing rationale, owner and
retained decision surfaces. Do not add a separate layout-exception sidecar.

## Blocking conditions

Block or request revision when:

- a non-trivial initiative lacks `stakeholder-brief.html`;
- the brief omits outcome, scope, anti-scope, impact, validation or risks;
- the brief contradicts source artifacts;
- the brief invents commitments not present in source artifacts;
- the brief is too vague to support a meeting decision;
- the brief hides a disproportionate approach, or uses generic/decorative
  visuals that reveal no concrete relationship;
- a required conditional visual is absent without a localized/omission reason,
  or a visual is unreadable in a rendered review;
- stakeholder-visible uncertainty is hidden in technical language.

When the brief exposes a missing business, product or priority decision, request
human clarification. Do not infer the decision.

## Allowed exception

Formatting-only, comment-only or release-administrative maintenance may record
`not_applicable` with reason in the spec review. Bugfixes may use a shorter
brief when the reproduction, impact and validation are already clear.

## Hard mirror recommendation

Use a brief validator to require the artifact, stable base section IDs,
versioned design-lineage marker, canonical shell hooks, source links, update
metadata and absence of canonical placeholders. Keep semantic
meaning and visual legibility in the short reviewer pass; do not use word-count
blocking, automated prose scoring or screenshot CI as a default. Flag changed
`spec.md`, `impact-map.md`, `plan.md` or `validation-plan.md` without a matching
brief update when the change is material.

Recommended check: `validate-human-visibility`.
