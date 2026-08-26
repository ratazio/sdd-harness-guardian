# Stakeholder Brief Design Standard

## Lineage and authority

`stakeholder-brief.html` is an offline, derived meeting projection; Markdown,
state, decisions and evidence remain canonical. New complete-decision briefs
use `data-harness-brief-design="v2"`. Historical or pinned `v1` briefs retain
their v1 contract until a material refresh follows the explicit migration path;
do not silently rewrite them.

V2 preserves the v1 paper/canvas palette, strong executive header, requested
decision ask, snapshot cards, responsive local table overflow and source footer.
It adds eight anchored views: value/scope, architecture, impact, execution,
validation, evolution, decision and coverage. A custom layout requires a
reviewed exception in `decision-log.md`; no layout sidecar is allowed.

## Provenance and progressive disclosure

Every material rendered section or child block has exactly one canonical
`data-source`, its heading/ID in `data-source-section`, and a
`data-coverage` disposition. Use `synthesized`, `represented`,
`not_applicable`, or `link_only`; `not_applicable` and `link_only` must state
their reason. A gap is a blocking finding, never a coverage disposition. Do not
put CSV source lists in one block. Core material must be synthesized or
represented, never `link_only`.

The coverage view contains the human register with source, principal heading,
stable target ID, disposition and rationale. This table complements DOM-local
provenance; it is not JSON or a sidecar.

Use native anchors and `details` as the baseline. Mark deep `details` open in
HTML so no-script reading is complete; a small inline script may collapse them
after load. Keyboard behavior must remain native and visible, and print CSS
must reveal collapsed content. No framework, remote asset or JS-only tab is
needed.

## Architecture and states

Choose depth from the source-backed S/M/L/high profile. Every included diagram
node, edge and text equivalent must map to one source block; unknown material
detail is a discovery or block, never an invented claim. A localized change may
use a concise justified N/A instead of a diagram.

Show task drafts, dependency, outcome linkage, validation and evidence, but
label drafts as non-authorizing. Do not claim coverage review, Human Visibility
or Tasks Ready from the HTML. Record decisions append-only and propagate a
meeting decision to canonical sources before regenerating the brief.

After rendering, a reviewer separately checks product,
architecture/operations and delivery for `recoverable`, `superficial`,
`absent` or justified `N/A`. A synthesis loss is recorded as source → lost fact
→ source correction, plus the material decision that cannot be made from the
brief alone. This is human/agent judgment; no score, prose parser or automated
semantic approval belongs in the HTML contract.

## Visual/accessibility baseline

Keep system UI typography, the existing muted green/amber/red palette and
visible text alongside every color-coded state. At narrow widths cards stack,
wide tables/diagrams scroll locally, and the page never gets global horizontal
overflow. Validate desktop, 390px narrow, keyboard, no-script and print
behavior separately; structural validation never proves semantic usefulness.
