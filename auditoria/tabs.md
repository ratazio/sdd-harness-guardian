# Audit Report Tab Anatomy

Future reports should keep these tabs in this order.

Canonical bundle source: `.harness/templates/audit-report-tabs.md`.

## 1. Resumo

Purpose: executive decision, maturity, strongest patterns, release blockers and
domain score overview.

Must include:

- decision: `pass`, `pass_with_gaps`, `fail` or `blocked`;
- maturity level;
- key metrics;
- domain score visual;
- top blockers.

## 2. Harness Graph

Purpose: show whether the harness is actually wired.

Must include:

- SVG graph;
- color legend;
- node/edge explanation;
- reachable, weak, orphan, missing and stale classification;
- links to `graph.json` and `inventory.json`.

## 3. SDD

Purpose: review spec-driven structure.

Must include:

- spec index status;
- numbered initiative status;
- per-initiative artifact coverage;
- spec/plan/tasks/validation/evidence consistency;
- current active spec risks.

## 4. Harness

Purpose: review harness primitives and lifecycle.

Must include:

- rules/workflows/artifacts/state/proof/memory/ratchet;
- lifecycle enforcement;
- bootstrap and portability review;
- harness layer visual.

## 5. Agentes & Skills

Purpose: review agentic contracts.

Must include:

- agent role coverage;
- skill anatomy coverage;
- subagent/delegation boundaries;
- output contracts;
- missing or weak sections.

## 6. Enforcement

Purpose: review hard mirrors and deterministic enforcement.

Must include:

- soft rule versus hard mirror coverage;
- validators/scripts/CI/schemas/evals;
- release gate evidence;
- enforcement ladder visual.

## 7. Hooks

Purpose: make hooks explicit.

Must include:

- hooks found;
- hooks not found;
- what each hook enforces;
- lifecycle interception point;
- recommended hooks when absent.

If no hooks exist, say so plainly and explain the impact.

## 8. Memoria

Purpose: review context economy and resumability.

Must include:

- indexes;
- run-state;
- progress;
- handoff;
- decision log;
- ratchet;
- MCP/Second Brain/retrieval policy.

## 9. Achados

Purpose: severity-ranked findings.

Must include:

- ID;
- severity;
- domain;
- evidence;
- impact;
- remediation.

## 10. Roadmap

Purpose: convert findings into an implementation sequence.

Must include:

- P0/P1/P2 actions;
- owner role;
- validation method;
- expected evidence.

## 11. Brutos

Purpose: expose raw/transient artifacts.

Must include links to:

- `inventory.json`;
- `graph.json`;
- `findings.json`;
- `hooks.json`;
- `checks.md`;
- `analysis-notes.md`;
- `design.md`;
- `tabs.md`.
