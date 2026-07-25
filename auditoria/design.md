# SDD/Harness Audit Report Design Standard

This file freezes the visual and structural standard for audit reports generated
in this directory. Future audit reports should preserve this design unless a
human explicitly asks for a redesign.

Canonical bundle source: `.harness/templates/audit-report-design.md`.

## Report Format

- Single static HTML file.
- Language: Portuguese for user-facing copy in this repository.
- Navigation: left-side tab rail on desktop, stacked on mobile.
- Each tab behaves like a subpage and must be reachable without JavaScript using
  radio-button CSS or regular anchors.
- Visuals: SVG diagrams embedded inline in the HTML.
- Raw artifacts: keep JSON/Markdown audit inputs in the same directory.

## Required Files In Audit Package

```txt
auditoria/
  sdd-harness-audit-vN.html
  inventory.json
  graph.json
  findings.json
  hooks.json
  checks.md
  analysis-notes.md
  design.md
  tabs.md
  spec-suggestions.md
```

## Color Semantics

Use the same colors in badges, cards, SVG nodes and legends.

| Color | Token | Meaning |
|---|---|---|
| Green/teal | `pass` | Present, reachable, operational or validated. |
| White | `neutral` | Present and structurally normal; no special risk signal. It does not mean missing. |
| Blue | `info` | Informational, generated, contextual or report/output artifact. |
| Amber/yellow | `warn` | Present but incomplete, weak, stale, pending or partially enforced. |
| Red | `fail` | Blocking, high risk, inconsistent or release-blocking. |
| Gray | `muted` | Background, inactive rail text, separators or unavailable metadata. |

Every chart, SVG or visual encoding must include a visible legend close to the
graphic. Do not rely on color alone; pair color with text labels.

## Layout Rules

- Header contains audit title, repository, date, approved output directory and
  4 metric cards.
- Main body uses tab navigation.
- Tables are dense but readable.
- Cards summarize; tables prove; SVGs orient.
- Avoid purely decorative graphics. Every visual must encode graph, maturity,
  coverage, risk, hooks, roadmap or raw artifact structure.
- Do not use rounded UI above 8px radius.
- Do not use gradient/orb decorations.

## Required Visuals

- Maturity by domain.
- Harness graph with reachability colors and legend.
- Harness layer/coverage view.
- Enforcement ladder.
- Hooks/enforcement status view, even when no hooks exist.

## Action Backlog Link

When `spec-suggestions.md` exists, the Brutos tab must link to it. The HTML
roadmap may summarize actions, but `spec-suggestions.md` is the canonical place
for candidate epics/specs, suggested prompts and seed tasks.

## Output Naming

Use monotonic report names when regenerating:

```txt
sdd-harness-audit.html
sdd-harness-audit-v2.html
sdd-harness-audit-v3.html
```

Do not delete prior reports unless the user asks.
