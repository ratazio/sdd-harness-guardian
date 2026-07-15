# Rule: Human Visibility

## Soft rule

Specs are execution contracts, but humans need a concise review surface before
work begins. Non-trivial initiatives must include a stakeholder brief that makes
the intended outcome, scope, impact, risks and validation easy to review in a
meeting.

The stakeholder brief is a derived artifact. It improves visibility and shared
understanding, but it never replaces `spec.md`, `impact-map.md`, `plan.md`,
`validation-plan.md` or `tasks.md` as source of truth.

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

The brief must be concise enough for a stakeholder review and specific enough to
spot misalignment before implementation starts.

## Blocking conditions

Block or request revision when:

- a non-trivial initiative lacks `stakeholder-brief.html`;
- the brief omits outcome, scope, anti-scope, impact, validation or risks;
- the brief contradicts source artifacts;
- the brief invents commitments not present in source artifacts;
- the brief is too vague to support a meeting decision;
- stakeholder-visible uncertainty is hidden in technical language.

When the brief exposes a missing business, product or priority decision, request
human clarification. Do not infer the decision.

## Allowed exception

Formatting-only, comment-only or release-administrative maintenance may record
`not_applicable` with reason in the spec review. Bugfixes may use a shorter
brief when the reproduction, impact and validation are already clear.

## Hard mirror recommendation

Use a brief validator to require the artifact, required section IDs and source
links. Optionally render or screenshot the HTML in CI to catch broken markup.
Flag changed `spec.md`, `impact-map.md`, `plan.md` or `validation-plan.md`
without a matching brief update.

Recommended check: `validate-human-visibility`.
