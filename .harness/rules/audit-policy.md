# Rule: Harness Audit Policy

## Soft rule

A harness audit must judge operational use, not file existence. Every claimed
capability needs evidence that an agent can discover it, understand when to use
it, execute the expected workflow and produce verifiable output.

An audit must include at least:

- explicit user-provided or user-confirmed HTML output path;
- raw/intermediate audit artifacts stored in the same approved audit directory;
- SDD contract review: spec numbering/index, spec quality, plan, tasks,
  validation mapping, evidence, decision log and stakeholder brief;
- harness graph review: entrypoints, agents, skills, rules, workflows,
  templates, scripts, hooks, schemas, memory, ratchet and references;
- agentic contract review: role boundaries, skill anatomy, subagent contracts,
  tool policy, MCP/Second Brain boundaries and output contracts;
- enforcement review: soft rules, hard mirrors, CI/hooks/schemas/evals and
  agent-readable failure messages;
- hooks review: implemented hooks, hookless state, enforcement point and
  recommended hooks;
- state and memory review: run-state, progress, handoff, memory index,
  retrieval policy, context economy and restart safety;
- report review: findings have severity, evidence, affected artifacts and
  concrete remediation.

## Blocking conditions

Block an `audit_pass` conclusion when:

- the root entrypoint cannot lead an agent to the active harness;
- required SDD artifacts are missing for non-trivial work;
- implementation can reach `done` without evidence or independent evaluation;
- critical safety, destructive-operation or privacy rules are only textual;
- a required artifact is orphaned from the bootstrap/workflow graph;
- skills or agents lack role boundaries, output contracts or validation;
- memory/retrieval guidance would require loading the whole repository by
  default;
- the requested report output path is missing and the auditor did not ask the
  user where to place it;
- raw inventory, graph, findings or command-output artifacts are missing from
  the approved audit directory;
- the HTML report lacks evidence-backed findings.
- any color-coded graph lacks a visible legend;
- the report lacks a hooks section/tab.

## Hard mirror recommendation

Add deterministic checks that parse the harness graph, validate required
artifact names and schemas, detect missing references, detect orphaned harness
files, and fail the audit when critical rules lack hard mirrors.

Recommended check: `validate-harness-audit-readiness`.
