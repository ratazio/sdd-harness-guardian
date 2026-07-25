# Workflow: SDD Harness Audit

## Purpose

Audit a repository for Spec Driven Development and Harness Engineering
readiness, including whether its agentic files form a usable operating graph or
only a decorative methodology layer.

## Entry condition

A repository root is available and the auditor has read project-local
instructions, this bundle entrypoint and `.harness/skills/sdd-harness-audit/SKILL.md`.
The HTML report output path is explicit. If the request does not specify where
to place the report, ask the user before report generation.

## Roles

| Phase | Primary role | Specialist support |
|---|---|---|
| Scope | Harness Auditor | State Keeper |
| Inventory | Harness Graph Mapper | Delivery Orchestrator |
| SDD review | Harness Auditor | Spec Guardian, Harness Planner |
| Agentic review | Harness Auditor | Agent/Skill Reviewer when available |
| Enforcement review | Harness Auditor | Evaluator Agent |
| Memory review | Harness Auditor | State Keeper |
| Report synthesis | Harness Auditor | Evaluator Agent |

## Flow

1. **Scope and authority** - identify consumer root, bundle root, active specs,
   local entrypoints, source hierarchy and user-approved report output path.
2. **Output package** - create the user-approved audit directory and keep raw
   artifacts there: inventory, graph, findings, command outputs, notes and
   action backlog.
3. **Inventory** - list `.harness/`, root agent files, specs, docs, scripts,
   schemas, hooks, CI, memory, ratchet, evidence and templates.
4. **Graph map** - build nodes and edges: entrypoint loads, manifest registers,
   workflow invokes, skill requires, agent delegates, template scaffolds, state
   points to, evidence validates, rule recommends hard mirror and script
   validates.
5. **Reachability review** - mark each harness artifact as reachable,
   weakly-reachable, orphaned or stale. Missing references and wrong names are
   findings.
6. **SDD contract review** - check numbered specs, `specs/INDEX.md`, spec
   schema, outcome, non-goals, EARS-style acceptance criteria, impact map, plan,
   tasks, validation plan, evidence and decision log.
7. **Harness contract review** - check bootstrap, state, handoff, progress,
   memory, ratchet, human visibility, destructive-operation approvals, builder
   vs evaluator separation and interruption recovery.
8. **Agentic contract review** - check agent roles, skill frontmatter, skill
   body structure, progressive disclosure, external knowledge policy, MCP
   boundary, subagent output contracts and tool permissions.
9. **Enforcement review** - check whether critical soft rules have hard mirrors:
   hooks, schemas, CI, validators, evals, agent-readable failures and release
   gates.
10. **Hooks review** - list implemented hooks and what they enforce. If no
    hooks are found, record that explicitly and recommend hooks.
11. **Platform harness review** - when present, check workflow engine, registry,
    memory layers, tracing, cost controls, audit log, identity, approvals and
    least privilege.
12. **Finding classification** - classify issues as critical, high, medium or
    low. Each finding must name evidence, impact and remediation.
13. **HTML report** - produce a rich tabbed report at the user-approved output
    path using `.harness/templates/audit-report.html`,
    `.harness/templates/audit-report-design.md` and
    `.harness/templates/audit-report-tabs.md` as the stable structure. Include
    SVG diagrams for graph, coverage and risk where useful. Include a visible
    legend for every graphic.
14. **Action backlog** - produce `spec-suggestions.md` using
    `.harness/templates/audit-spec-suggestions.md` when the user wants the audit
    converted into remediation action. Each candidate epic should include
    priority, linked findings, suggested slug, suggested prompt, seed tasks,
    acceptance signals and dependencies.
15. **Independent review** - a distinct evaluator reviews the report for
    unsupported claims, missed critical gaps and vague remediation.

## Severity guide

| Severity | Meaning |
|---|---|
| Critical | Can cause unsafe action, false `done`, missing evaluation, lost state or unusable bootstrap. |
| High | Breaks SDD/harness operation for non-trivial work or leaves required artifacts unreachable. |
| Medium | Creates ambiguity, weak validation, stale references or avoidable context waste. |
| Low | Naming, documentation or polish issue that does not block safe operation. |

## Output

The workflow produces:

```txt
audit-report.html
user-approved output path
inventory.json
graph.json
findings.json
hooks.json
checks.md
analysis-notes.md
design.md
tabs.md
spec-suggestions.md
graph summary
finding list
remediation roadmap
open questions
```

The HTML is authored by the auditor from evidence and specialist findings. A
script may assist graph extraction, but may not be the sole author of the
judgment.
