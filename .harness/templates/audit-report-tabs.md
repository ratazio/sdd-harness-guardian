# SDD/Harness Audit Report Tab Anatomy

Future SDD/Harness audit reports should keep these tabs in this order.

## 1. Resumo

Executive decision, maturity, metrics, domain score visual and top blockers.

## 2. Harness Graph

Reachability graph for harness components. Include SVG, legend, node classes,
edge meaning and links to `graph.json` and `inventory.json`.

## 3. SDD

Spec-driven structure: spec index, numbered initiatives, artifact coverage,
state consistency, validation and evidence posture.

## 4. Harness

Harness primitives and lifecycle: rules, workflows, artifacts, state, proof,
memory, ratchet, bootstrap and portability.

## 5. Agentes & Skills

Agentic contracts: role coverage, skill anatomy, delegation boundaries, output
contracts and weak/missing sections.

## 6. Enforcement

Hard mirrors: validators, schemas, hooks, CI, evals, release gates and
agent-readable failure modes.

## 7. Hooks

Implemented hooks, missing hooks, lifecycle interception point and recommended
hooks. If none exist, say so plainly and explain impact.

## 8. Memoria

Context economy and resumability: indexes, run-state, progress, handoff,
decision log, ratchet and retrieval policy.

## 9. Achados

Severity-ranked findings with ID, severity, domain, evidence, impact and
remediation.

## 10. Roadmap

Implementation sequence with P0/P1/P2 actions, owner role, validation method and
expected evidence.

## 11. Brutos

Links to raw/transient artifacts: `inventory.json`, `graph.json`,
`findings.json`, `hooks.json`, `checks.md`, `analysis-notes.md`, `design.md`
and `tabs.md`.
