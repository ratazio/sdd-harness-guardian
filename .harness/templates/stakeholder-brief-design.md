# Stakeholder Brief Design Standard

## Purpose and lineage

`stakeholder-brief.html` is a derived, offline meeting surface. Populate the
canonical template; do not rebuild it as a bare page. Every standard instance
uses `data-harness-brief-design="v1"` and the shell hooks `brief-shell`,
`brief-header`, `decision-register`, `impact-evidence`, and
`decision-actions`. These are a deterministic lineage contract, not a claim
that a machine has approved visual quality.

A material custom layout is permitted only when its reviewed exception is
recorded in the initiative `decision-log.md`. The row must name the layout or
design exception, rationale, owner/reviewer, retained decision surfaces, and
accepted/reviewed status. Do not create an exception sidecar for layout.

## Visual foundation

Use the following template tokens; they are intentionally restrained so the
brief reads like a decision document, not a product dashboard.

| Role | Token | Value | Use |
|---|---|---|---|
| Canvas | `--canvas` | `#f4f1ea` | Warm, low-contrast page background. |
| Paper | `--paper` | `#fffdf8` | Cards and sections; preserve high reading contrast. |
| Ink | `--ink` | `#17211f` | Headings and primary body text. |
| Muted | `--muted` | `#5f6b68` | Metadata, helper text and table labels only. |
| Primary | `--brand` | `#0e665d` | Positive scope, active navigation and key emphasis. |
| Primary dark | `--brand-dark` | `#084b45` | Requested-decision panel and high-emphasis links. |
| Positive soft | `--soft` | `#dff0ec` | Positive/confirmed background, never status by color alone. |
| Attention | `--amber` / `--amber-soft` | `#9a5b07` / `#fff0ce` | Pending decision, uncertainty and next-safe-step callouts. |
| Risk | `--red` | `#8b3535` | Anti-scope, material risk and blocked path; pair with visible text. |
| Divider | `--line` | `#d9d5ca` | Quiet section/card/table separation. |

Typography uses the system UI stack: `Inter, ui-sans-serif, system-ui,
-apple-system, "Segoe UI", sans-serif`. Keep the editorial hierarchy from the
template: large, compact `h1` for the meeting decision; uppercase, tracked
micro-labels for metadata; 16px body text with about 1.55 line-height; and
small muted labels rather than small muted paragraphs. Do not introduce remote
fonts, more than one display treatment, gradients beyond the existing subtle
header wash, or decorative shadows that compete with the decision ask.

Use whitespace as hierarchy: the header is the strongest region, cards group
snapshot facts, sections separate decision topics, and tables carry dense
traceability. Keep one accent purpose per block—green for confirmed/scope,
amber for attention or pending choice, red for risk/anti-scope—and always print
the corresponding state label. Inline SVGs use the same palette, a nearby
legend when color encodes several states, and a text equivalent.

## Required meeting shell

Keep the template's paper/canvas visual tokens, strong header, decision ask,
source/freshness metadata, responsive card grid, semantic tables, and source
footer. Use system fonts and inline CSS/SVG only. Preserve visible text labels
for every status; color is supportive, never its sole meaning. At narrow
widths cards stack and tables scroll locally without page-wide overflow.

The shell always contains:

- decision header and snapshot: request, owner/audience, status, review
  trigger, outcome, benefit, size/rationale, smaller option, evidence and
  source freshness state;
- focused scope and anti-scope;
- decision/trade-off register: status, recommendation and alternative,
  rationale, consequence, reversibility, confidence and source;
- impact/evidence table: actor or surface, change/blast radius,
  owner/mitigation, validation and honest evidence state;
- acceptance/risk/validation, then open questions, decision actions and next
  safe step.

## Conditional views

Add only the smallest useful architecture, impact, or flow view. Each included
view names the stakeholder concern, audience and purpose, exposes a concrete
relationship, and supplies a text equivalent. Architecture is C4-light at the
context/container boundary; impact explains propagation; flow explains a
journey, handoff, failure or rollback. If omitted, state why the localized
table/text is sufficient. Never retain generic example nodes as if they were
evidence.

## Author and reviewer guidance

Use canonical sources as truth and label claims `planned`, `observed`,
`proved`, `accepted risk`, or `uncertain`. A planned check is never proof.
Before Human Visibility Ready, run the deterministic validator, then conduct an
independent desktop and narrow rendered review. Confirm a reviewer can locate
the request, owner/status, outcome, scope, impact, evidence state, trade-offs,
risks and next safe step in five minutes. The validator can reject missing
lineage/shell/freshness; it cannot approve prose, accessibility in practice, or
visual decision usefulness.
