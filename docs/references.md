# References and source alignment

This bundle follows the internal standards adopted by the project.

## Source documents used

- `harness-engineering 3.html`
- `harness_multiagent_platform 1.html`
- `index.html`
- prior IA Studies documents about skills, agents, harness, Second Brain, MCP, versioning and bundle distribution.

## Adopted concepts

### Spec Driven Development

Used as the source of truth for intent, acceptance criteria and task decomposition.

### Harness Engineering

Used as the environment around the model: rules, workflows, artifacts, validation, memory, evidence and learning.

### Rules, Workflows and Artifacts

Used as first-class primitives:

```txt
Rules = invariants and guardrails
Workflows = repeatable execution sequences
Artifacts = traceable outputs with identity
```

### Soft rules and hard mirrors

Soft rules are markdown instructions. Critical rules must have deterministic mirrors such as schema validators, CI gates, linters, hooks or tests.

### Workflow Engine

The bundle treats orchestration as a workflow problem, not only as an agent prompt. The recommended implementation may use LangGraph or an equivalent stateful workflow engine.

### Memory and state

The bundle separates session context, working state, long-term execution memory and semantic/project knowledge.

Numbered spec directories and `specs/INDEX.md` are adopted as deterministic
memory scaffolding: they preserve order, reduce initial context load and give
retrieval systems stable document identities. Semantic search and embeddings are
recommended as optional harness capabilities for large projects, not as a
replacement for explicit SDD artifacts.

### Builder and Evaluator separation

Implementation and evaluation must be separate roles for medium/high risk work.

### Ratchet principle

Repeated errors must become permanent improvements to the harness.

### Harness audit

Used as the structured review of whether SDD and Harness Engineering are
operationally wired: entrypoints, artifact graph, specs, agents, skills, rules,
workflows, memory, evidence, hard mirrors and report quality. See
`docs/harness-audit-framework.md`.
