# SDD/Harness Audit Action Backlog

Audit ID: `sdd-harness-guardian-2026-07-25`  
Source report: `auditoria/sdd-harness-audit-v3.html`  
Purpose: convert audit findings into candidate SDD initiatives/specs.

This file is intentionally not a final spec set. It is a prioritized backlog of
spec candidates to feed into the SDD Harness Guardian flow. Each epic should
become its own numbered initiative under `specs/NNN-slug/` before implementation.

## Recommended Sequence

| Order | Candidate Spec | Priority | Main Findings | Why First |
|---|---|---:|---|---|
| 1 | Close Audit Capability Evaluation And Release State | P0 | F-001, F-002, F-006 | Removes contradictory source-of-truth state before building on top of it. |
| 2 | Add Spec State Consistency Validator | P0 | F-002, F-003 | Prevents future divergence between `specs/INDEX.md`, `run-state.yaml` and `tasks.md`. |
| 3 | Add Harness Enforcement Hooks And CI Examples | P1 | F-003, F-008 | Turns manual checks into lifecycle enforcement. |
| 4 | Add Harness Graph Reachability Validator | P1 | F-003 | Converts the audit graph from analytical artifact into deterministic protection. |
| 5 | Normalize Agent Contracts | P1 | F-005 | Makes subagent delegation more predictable and evaluable. |
| 6 | Normalize Skill Contracts | P1 | F-004 | Makes skill activation, inputs, tools and outputs consistent. |
| 7 | Add Audit Package Completeness Validator | P1 | F-003, F-008 | Ensures future audit reports keep tabs, hooks, legends and raw artifacts. |
| 8 | Refresh Release Evidence And Versioning Workflow | P2 | F-001, F-006 | Makes release metadata match the actual validation surface. |
| 9 | Improve UTF-8/CLI Readability | P2 | F-007 | Reduces audit noise and improves Windows terminal readability. |

## Epic 1: Close Audit Capability Evaluation And Release State

Suggested slug: `close-audit-capability-release-state`

### Outcome

The recently added SDD/Harness audit capability is independently evaluated,
state is synchronized, evidence is approved, and release metadata no longer
advertises a misleading readiness state.

### Why This Exists

The audit found that spec 002 is implemented but still needs independent
evaluation, while `manifest.yaml` currently says `status: ready`. It also found
stale release evidence.

### Suggested Prompt

```txt
Crie uma spec para fechar a avaliação independente da iniciativa 002,
sincronizar run-state/tasks/specs index e atualizar a postura de release do
sdd-harness-guardian sem pular os gates de evidence e evaluator.
```

### Suggested Tasks

- Review `specs/002-sdd-harness-audit-process/` as evaluator, not builder.
- Decide whether T-001 is `approved`, `needs_revision` or still
  `needs_evaluation`.
- Synchronize `run-state.yaml`, `tasks.md`, `progress.md` and `specs/INDEX.md`.
- Refresh evidence references with the current `validate_bundle.py` count.
- Decide whether `manifest.yaml` should stay `ready` or move to
  `release_candidate`.
- Update `CHANGELOG.md`, `VERSION` and release docs only after evaluation is
  resolved.
- Produce an evidence pack proving all terminal gates are satisfied.

### Acceptance Signals

- No contradictory status between index, tasks and run-state.
- Independent evaluator decision is recorded.
- Release metadata matches current capability status.
- `python scripts\validate_bundle.py` passes.

## Epic 2: Add Spec State Consistency Validator

Suggested slug: `spec-state-consistency-validator`

### Outcome

A deterministic validator detects divergence between `specs/INDEX.md`,
initiative `run-state.yaml`, `tasks.md`, evidence files and terminal gate
requirements.

### Why This Exists

The audit found a concrete mismatch in spec 002: `run-state.yaml` says draft
while the current phase and task ledger indicate `needs_evaluation`.

### Suggested Prompt

```txt
Crie uma spec para implementar um validator determinístico que confira
consistência entre specs/INDEX.md, run-state.yaml, tasks.md, evidence e gates
terminais de cada iniciativa numerada.
```

### Suggested Tasks

- Define the consistency rules for index status, run-state status/current phase
  and task ledger states.
- Parse every `specs/NNN-slug/` initiative.
- Validate required artifacts for feature and bugfix initiatives.
- Validate that terminal `done` requires approved evidence.
- Detect active initiatives whose task state and run-state diverge.
- Add clear machine-readable error messages.
- Integrate the check into `scripts/validate_bundle.py` or create a dedicated
  script invoked by it.
- Add smoke fixtures for pass/fail cases.

### Acceptance Signals

- The current F-002 class of mismatch is detected automatically.
- Error output names exact file paths and fields.
- Existing valid specs still pass.

## Epic 3: Add Harness Enforcement Hooks And CI Examples

Suggested slug: `harness-enforcement-hooks-ci`

### Outcome

The repository ships optional hooks and CI examples that run core validation
commands before risky lifecycle events.

### Why This Exists

The audit found no implemented Git hooks or CI workflows. Existing scripts are
good enforcement candidates but are manual today.

### Suggested Prompt

```txt
Crie uma spec para adicionar hooks e exemplos de CI opcionais para executar os
validadores do sdd-harness-guardian sem tornar o bundle dependente de uma única
plataforma.
```

### Suggested Tasks

- Define portability constraints for GitHub Actions, local Git hooks and
  consumer projects.
- Add sample `pre-commit` hook for `python scripts\validate_bundle.py`.
- Add sample `pre-push` or CI job for `python scripts\smoke_test_scaffolder.py`.
- Add documentation explaining installation and opt-in behavior.
- Ensure hooks do not assume this repo is a consumer project.
- Add validation that hook templates reference existing scripts.
- Record hook behavior in `.harness/rules/soft-hard-rules.md` or related docs.

### Acceptance Signals

- Hook templates exist and are documented.
- CI example is optional and vendor-neutral where feasible.
- The audit Hooks tab would report implemented examples or explicit opt-in
  surfaces instead of `none_found`.

## Epic 4: Add Harness Graph Reachability Validator

Suggested slug: `harness-graph-reachability-validator`

### Outcome

The harness can deterministically map entrypoints, manifest registrations,
agents, skills, rules, workflows, templates, scripts and docs, then report
missing, orphaned, stale or weakly wired components.

### Why This Exists

The audit graph is useful but currently analytical. A validator would make
orphaned or unreachable harness elements fail fast.

### Suggested Prompt

```txt
Crie uma spec para transformar o Harness Graph em um validator determinístico
que detecte arquivos órfãos, registros quebrados, referências ausentes e
componentes criados mas não utilizados.
```

### Suggested Tasks

- Define node types and edge evidence rules.
- Parse `manifest.yaml`, `.harness/AGENTS.md`, workflows, rules, agents, skills
  and templates.
- Detect manifest entries that point to missing files.
- Detect files in harness directories not referenced by manifest or entrypoint.
- Emit `graph.json` with stable schema.
- Add CLI output summarizing reachable, orphaned, missing, stale and weak nodes.
- Add tests/fixtures for orphan and missing-reference cases.
- Decide whether this validator runs inside `validate_bundle.py`.

### Acceptance Signals

- A created-but-unreferenced harness artifact is flagged.
- A referenced-but-missing file is flagged.
- `graph.json` schema is documented.

## Epic 5: Normalize Agent Contracts

Suggested slug: `normalize-agent-contracts`

### Outcome

Every `.harness/agents/*.md` file follows a consistent, reviewable contract for
mission, responsibilities, non-responsibilities, inputs, outputs, blocking
conditions and escalation behavior.

### Why This Exists

The audit found that newer audit agents are more explicit than older role
files. That makes delegation quality uneven.

### Suggested Prompt

```txt
Crie uma spec para normalizar todos os agent docs do SDD Harness Guardian,
preservando o comportamento atual mas tornando contratos de entrada, saída e
bloqueio consistentes.
```

### Suggested Tasks

- Define canonical agent document anatomy.
- Inventory every current agent file.
- Identify missing sections per agent.
- Update one low-risk agent first as pattern proof.
- Normalize high-leverage agents: `delivery-orchestrator`,
  `harness-planner`, `state-keeper`.
- Normalize remaining agents.
- Add validation for required agent headings if appropriate.

### Acceptance Signals

- Every agent has the same minimum contract sections.
- No responsibilities are silently changed.
- Validator or audit checklist can detect contract drift.

## Epic 6: Normalize Skill Contracts

Suggested slug: `normalize-skill-contracts`

### Outcome

Every `.harness/skills/*/SKILL.md` has production-ready sections for purpose,
use cases, inputs, workflow, external knowledge, MCP/tool policy, output
contract, validation checklist and gotchas.

### Why This Exists

The audit found older skills useful but compact compared to the stronger
`sdd-harness-audit` skill.

### Suggested Prompt

```txt
Crie uma spec para normalizar os SKILL.md do bundle com uma anatomia consistente
de uso, inputs, tool policy, output contract, validação e gotchas.
```

### Suggested Tasks

- Define minimum skill anatomy by risk level.
- Inventory every skill and classify missing sections.
- Normalize `interruption-recovery` first because it is high impact.
- Normalize `spec-review`, `impact-analysis`, `validation-planning`,
  `task-breakdown`, `evidence-pack-generation` and `ratchet-learning`.
- Update `validate_bundle.py` to check required headings if this is acceptable.
- Keep existing maturity/frontmatter behavior stable.

### Acceptance Signals

- Every skill has explicit input and output contracts.
- Tool/MCP behavior is defined where relevant.
- Validation catches missing required sections.

## Epic 7: Add Audit Package Completeness Validator

Suggested slug: `audit-package-completeness-validator`

### Outcome

A deterministic check ensures generated audit packages include the expected raw
artifacts, stable tabs, hooks tab, graph legends and color semantics.

### Why This Exists

The user explicitly wants future audit reports to keep the same structure and
not randomly degrade or omit hooks/legends.

### Suggested Prompt

```txt
Crie uma spec para validar automaticamente a completude do pacote de auditoria:
HTML, abas obrigatórias, hooks, legendas, design.md, tabs.md e artefatos brutos.
```

### Suggested Tasks

- Define required files in an audit output directory.
- Validate `inventory.json`, `graph.json`, `findings.json` and `hooks.json`.
- Validate that HTML includes all required tab labels.
- Validate that color-coded SVG/chart sections have nearby legends.
- Validate that `design.md` and `tabs.md` exist and match canonical template
  requirements.
- Add a CLI command such as `validate_audit_package.py <path>`.
- Add fixtures for missing hooks tab, missing legend and missing raw artifact.

### Acceptance Signals

- A report without Hooks tab fails validation.
- A graph without legend fails validation.
- A report with missing raw artifacts fails validation.

## Epic 8: Refresh Release Evidence And Versioning Workflow

Suggested slug: `release-evidence-versioning-workflow`

### Outcome

Release metadata, changelog, acceptance criteria and validation evidence are
kept aligned when the harness capability surface changes.

### Why This Exists

The audit found stale acceptance criteria and release metadata that can mislead
maintainers.

### Suggested Prompt

```txt
Crie uma spec para reforçar o workflow de release do bundle, garantindo que
VERSION, manifest, CHANGELOG, acceptance criteria e evidências reflitam a mesma
realidade antes de status ready.
```

### Suggested Tasks

- Define release readiness rules for `draft`, `release_candidate`, `ready` and
  `deprecated`.
- Validate `VERSION` against `manifest.yaml` and `CHANGELOG.md`.
- Validate acceptance criteria check counts or remove brittle counts from docs.
- Require evidence refresh after adding validators/templates/agents/skills.
- Document when to mark the bundle `release_candidate` instead of `ready`.
- Consider a release checklist template.

### Acceptance Signals

- Stale validation counts are detected or avoided.
- `ready` cannot coexist with unresolved evaluation gates.
- Release docs name the exact validation commands and latest results.

## Epic 9: Improve UTF-8/CLI Readability

Suggested slug: `utf8-cli-readability`

### Outcome

Portuguese documentation remains readable in common Windows and CI terminal
contexts, reducing noise during audits and reviews.

### Why This Exists

The audit observed mojibake in terminal reads of Portuguese text. This is low
risk but annoying enough to hide useful signal.

### Suggested Prompt

```txt
Crie uma spec para melhorar a legibilidade UTF-8/CLI dos documentos em português
do bundle, especialmente em Windows PowerShell e logs de auditoria.
```

### Suggested Tasks

- Identify whether mojibake comes from file encoding, terminal code page or tool
  output rendering.
- Confirm repository files are UTF-8.
- Add documentation for expected terminal encoding on Windows.
- Prefer ASCII-safe anchors and machine-parsed tokens.
- Add a lightweight encoding check if useful.

### Acceptance Signals

- Files remain valid UTF-8.
- CLI audit output is readable or documented.
- Machine-parsed headings/tokens are ASCII-safe where needed.

## Cross-Epic Dependencies

```txt
Epic 1 -> should happen before release metadata work.
Epic 2 -> supports Epic 1 and Epic 8.
Epic 3 -> should run Epic 2/4/7 validators once they exist.
Epic 4 -> supports future audits and audit package generation.
Epic 5 + Epic 6 -> can run in parallel after Epic 1.
Epic 7 -> depends on the current audit report standard.
Epic 8 -> should close after Epic 1 and after any validators chosen for release.
Epic 9 -> independent low-risk polish.
```

## Suggested First Command

Start with the highest-risk state inconsistency:

```powershell
python scripts\new_initiative.py spec-state-consistency-validator
```

Then ask the harness to create the spec from Epic 2 in this file.

## Notes For The Spec Creator

- Do not implement multiple epics in a single initiative unless the human
  explicitly asks for a larger release train.
- Preserve the bundle/consumer distinction: this repository is the source
  bundle, not a downstream project.
- Prefer deterministic validators for protected invariants.
- Keep every new initiative numbered and indexed.
- For each epic, make acceptance criteria testable and evidence-oriented.
