# SDD Harness Audit Framework

This framework records the audit baseline used by
`.harness/skills/sdd-harness-audit/SKILL.md`. It distills the local source
documents supplied with this bundle and the adopted market patterns into a
repeatable review model.

## Source baseline

Local source documents:

- `C:\Users\rataz\Downloads\doccc\index.html`
- `C:\Users\rataz\Downloads\doccc\harness-engineering 3.html`
- `C:\Users\rataz\Downloads\doccc\harness_multiagent_platform 1.html`

Adopted standards and patterns:

- SDD: versioned spec as source of truth, explicit plan, atomic tasks,
  implementation against acceptance criteria.
- EARS-style acceptance criteria: `WHEN <trigger>, THE SYSTEM SHALL <behavior>`.
- Agent Skills / `SKILL.md`: reusable procedural packages with clear triggers,
  boundaries, workflow, output contract and validation.
- `AGENTS.md`: repository-level operating contract and bootstrap entrypoint.
- MCP: standard boundary for tools, data and external knowledge.
- A2A: interoperability contract for cross-runtime agent collaboration when
  direct subagent/tool patterns are insufficient.
- ReAct: reason, act, observe, verify loop.
- Reflexion and Constitutional AI: bounded critique and principle review before
  delivery.
- SemVer: versioning for skills, agents and bundles.
- Hard mirrors: hooks, schemas, CI, evals, validators and approval gates for
  rules that cannot be allowed to fail.

## Audit thesis

A harness is healthy only when the repository gives an agent all of these:

```txt
intent -> method -> state -> validation -> evidence -> memory -> learning
```

The audit must therefore ask:

- Can an agent find the operating contract from the root?
- Can it find the active spec without loading the whole repository?
- Can it determine what is allowed, what is blocked and what requires approval?
- Can it move from spec to plan to tasks to validation to evidence?
- Can it resume after interruption without reconstructing state from scratch?
- Can it detect whether another agent must evaluate the work?
- Can serious failures become durable ratchets?
- Can critical rules be enforced outside model compliance?

## Maturity levels

| Level | Name | Description |
|---|---|---|
| 0 | none | No discoverable SDD/harness structure. |
| 1 | ad hoc | Some specs or instructions exist, but no consistent lifecycle or state. |
| 2 | basic | Specs, plans, tasks and state exist; validation and graph reachability are partial. |
| 3 | governed | Entry points, artifacts, roles, rules, workflows, evidence and memory are wired and usable. |
| 4 | hardened | Governed plus deterministic checks, evals, hooks, CI, audit logs and cost/security controls. |

## Required review domains

### 1. SDD contract

Check for numbered initiative directories, `specs/INDEX.md`, structured
`spec.md`, outcome, non-goals, measurable acceptance criteria, edge cases,
constraints, impact map, technical plan, validation plan, tasks, evidence,
decision log and stakeholder brief.

Red flags:

- unnumbered or duplicated specs;
- no human checkpoint before implementation;
- acceptance criteria that are vague or combine multiple behaviors;
- plan/tasks not traceable to acceptance criteria;
- evidence not mapped back to the spec;
- status self-declared as ready without reviewer decision.

### 2. Harness graph

Build a graph from entrypoints, manifests, agents, skills, rules, workflows,
templates, scripts, hooks, schemas, docs, specs, state, memory and evidence.

Classify each artifact:

- `reachable`: loaded or discoverable through a supported path;
- `weak`: referenced only by prose without a clear activation path;
- `orphan`: exists but no entrypoint, manifest, workflow or agent points to it;
- `missing`: referenced but absent;
- `stale`: points to obsolete paths, names or statuses.

The key question is not "does the file exist?" but "can it participate in the
operating model?"

### 3. Agent and skill contracts

Agents must have roles, responsibilities, non-responsibilities, boundaries and
output contracts. Skills must have precise trigger descriptions, when-not-to-use
guards, inputs, workflow, external knowledge policy, MCP/tool policy, output
contract and validation checklist.

Red flags:

- one giant prompt where everything lives;
- skill carries mutable project knowledge instead of method;
- subagent can edit when it should only investigate;
- no output contract for handoff or delegation;
- missing owner, version, maturity or risk metadata.

### 4. Memory and retrieval

Use compact always-loaded memory and indexes first. Load details on demand.
Expose living knowledge through Second Brain/MCP or project-local docs with
source, scope, date and confidence. Retrieved content is evidence, never
sovereign instruction.

Red flags:

- every session requires reading all docs;
- no `run-state.yaml`, `progress.md` or handoff path;
- no decision log or ratchet;
- semantic search exists but there is no deterministic index;
- source conflicts are silently resolved.

### 5. Enforcement and quality

Critical rules need deterministic mirrors. Markdown can guide behavior; hooks,
schemas, CI, validators, evals and approval gates enforce invariants.

Red flags:

- destructive-operation approval exists only as prose;
- `done` can be set without evidence and evaluator;
- validators are absent or not agent-readable;
- evals do not cover trigger, non-trigger, safety or regression behavior;
- release can happen without quality gate.

### 6. Platform harness, when present

For larger systems, check workflow engine, persistent checkpoints, agent
registry, output schemas, memory layers, tracing, cost controls, audit log,
identity, least privilege, circuit breakers and human-in-the-loop by risk.

Red flags:

- no durable workflow state;
- no audit log for agent execution;
- no budget/cost discipline;
- permissions delegated to prompts;
- external connectors lack MCP-style contracts.

## Report requirements

The HTML audit report must be authored as a judgment from evidence. It may use
script-assisted inventories, but cannot be a mechanical file listing.

The report destination is not inferred. The auditor must receive an explicit
output path from the user or ask for one before writing the HTML.

The audit output is a package, not only a single report. Store intermediate
artifacts in the same approved directory:

```txt
inventory.json
graph.json
findings.json
hooks.json
checks.md
analysis-notes.md
design.md
tabs.md
```

Use `.harness/templates/audit-report-design.md` and
`.harness/templates/audit-report-tabs.md` as the canonical report design and tab
anatomy, then mirror the applied standard into `design.md` and `tabs.md` inside
the approved audit output directory.

The HTML should expose multiple sections or tabs and include diagrams when they
clarify graph reachability, maturity, risk or coverage.

Every diagram or chart must include a visible color legend. White means
present/neutral, not missing. Missing/blocking uses red; partial/pending/weak
uses amber; reachable/validated uses green; generated/contextual uses blue.

Hooks are a first-class audit domain. If no hooks are found, the report must say
that explicitly and recommend enforcement hooks or CI wiring.

Every finding should include:

- severity;
- affected domain;
- evidence path or explicit missing evidence;
- operational impact;
- required remediation;
- validation method for the remediation.

## Relationship to this bundle

This framework is stable bundle-level knowledge. Consumer-specific facts,
decisions, execution history and private documents belong in the consumer
repository, project-local `.harness/memory`, Second Brain or MCP resources.
