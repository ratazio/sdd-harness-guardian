# SDD/Harness Audit Report Design Standard

Use this standard when generating a full SDD/Harness audit report. Preserve it
unless a human explicitly asks for a redesign.

## Report Format

- Single static HTML file.
- User-facing copy should follow the consumer project's language.
- Navigation uses a stable tab/subpage structure.
- Each tab must be reachable without JavaScript by using CSS-only controls or
  normal anchors.
- Inline SVG diagrams are preferred for harness graphs, maturity views,
  enforcement ladders and hook status views.
- Raw JSON/Markdown audit artifacts must stay in the human-approved output
  directory beside the HTML report.

## Required Audit Package

```txt
<approved-output>/
  sdd-harness-audit-vN.html
  inventory.json
  graph.json
  findings.json
  hooks.json
  checks.md
  analysis-notes.md
  design.md
  tabs.md
```

## Color Semantics

| Color | Token | Meaning |
|---|---|---|
| Green/teal | `pass` | Present, reachable, operational or validated. |
| White | `neutral` | Present and structurally normal; no special risk signal. It does not mean missing. |
| Blue | `info` | Informational, generated, contextual or report/output artifact. |
| Amber/yellow | `warn` | Present but incomplete, weak, stale, pending or partially enforced. |
| Red | `fail` | Blocking, high risk, inconsistent, absent or release-blocking. |
| Gray | `muted` | Background, inactive rail text, separators or unavailable metadata. |

Every chart, SVG or color-coded visual must include a visible legend close to
the graphic. Do not rely on color alone; pair color with text labels.

## Layout Rules

- Header contains audit title, repository, date, approved output directory and
  metric cards.
- Main body uses the standard tab order from `audit-report-tabs.md`.
- Cards summarize; tables prove; SVGs orient.
- Avoid decorative-only graphics.
- Use border radius of 8px or less.
- Do not use gradient/orb decorations.

## Required Visuals

- Maturity by domain.
- Harness graph with reachability colors and legend.
- Harness layer/coverage view.
- Enforcement ladder.
- Hooks/enforcement status view, even when no hooks exist.
