# Tasks: 009-stakeholder-brief-tabbed-decision-surface

**Status:** tasks_drafted — planning only; no task is authorized.  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-26

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | pending | Discover accessible one-document tab behavior and authoring entrypoints | none | high | unassigned | distinct accessibility reviewer | evidence/T-001.md |
| T-002 | pending | Construir a estrutura de abas v2 com fallback progressivo | T-001 | high | unassigned | distinct accessibility reviewer | evidence/T-002.md |
| T-003 | pending | Define tab missions, source-sufficiency questions and proportional detail | T-001 | high | unassigned | distinct Spec Guardian | evidence/T-003.md |
| T-004 | pending | Project rich task and validation contracts into execution views | T-002, T-003 | high | unassigned | distinct planner/reviewer | evidence/T-004.md |
| T-005 | pending | Validate compatibility, fixtures and release evidence independently | T-001–T-004 | medium | unassigned | distinct maintainer | evidence/T-005.md |

## Authorization boundary

`tasks_drafted` is a discussion gate only. D-001 authorizes planning, not changes to a template, script, fixture or consumer brief. A distinct coverage review, rendered-meaning review, meeting decision propagation and refreshed brief must occur before one task can become `ready`.

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

### T-001 — Discover accessible one-document tab behavior and authoring entrypoints

**Status:** pending  
**Objective:** Resolve U-001/U-002 by choosing and documenting the smallest accessible tab interaction/fallback and existing skills/agents that receive the source-sufficiency protocol.  
**Requirement IDs:** FR-001, FR-003, FR-007, FR-009  
**Acceptance criteria IDs:** AC-001, AC-007, AC-008, AC-009  
**Outcome served:** Future implementation focuses a view without hiding content or inventing authoring workflow.  
**Demonstrable increment or reduced uncertainty:** Written decision with prototype evidence states markup, keyboard/focus, no-script/print fallback, guidance surfaces and rejected alternatives.  
**Expected artifact/behavior:** Plan/decision/evidence update only; no irreversible template rollout.  
**Validation method:** V-001, V-007, V-008, M-004, E-003, E-004.  
**Why now:** Later work depends on a safe interaction and a single discovery entrypoint.  
**Max subtasks before validation:** 3  
**Dependencies:** none  
**Risk:** high  
**Builder:** unassigned  
**Evaluator:** distinct accessibility reviewer  
**Human approval:** not_required unless discovery reveals a new dependency or consumer business question  
**Evidence:** evidence/T-001.md

#### Scope

Inventariar a estrutura visual v2, regras sem script/teclado/impressão, validator e skills de autor/planner/reviewer. Comparar padrões nativos com protótipo local mínimo. Registrar fallback e fonte de pergunta material; rejeitar abas só em JS e skill duplicada.

#### Out of scope

No production template, validator, v1, consumer brief, framework/runtime or visual-only proof is completed here.

#### Outcome linkage

- **Requirement/AC/discovery question:** FR-001/003/007/009; U-001/U-002; AC-001/007/008/009.
- **Vertical slice relation:** bounded discovery directly enabling T-002/T-003.
- **Priority source or human decision:** D-001 user request for focused, truthful views.

#### Expected files and contracts

`plan.md` D-002/Q-001/Q-002 resolution and `evidence/T-001.md`; only an existing guidance surface changes if discovery requires it. No sidecar, DOM schema or persistent state.

#### Implementation constraints

One document remains readable in source order without JS; focus is visible; tab/panel relationship is semantic or equivalent accessible; print reveals every panel; remote assets/frameworks are forbidden.

#### Assurance disposition

| Claim/risk | Selected technique and why | Oracle/data/environment | Builder/test executor | Evaluator/specialist | Evidence | Entry/exit/failure or waiver path |
|---|---|---|---|---|---|---|
| Accessibility/fallback | Native prototype/manual behavior proves interaction beyond screenshot. | Desktop, 390px, keyboard, script disabled, print preview. | builder | accessibility reviewer | T-001 evidence | Failure blocks T-002; select another native pattern. |
| Authoring reuse | Inventory avoids duplicate protocol. | Current skills/agents/templates. | builder | Spec Guardian | T-001 evidence | Unresolved entrypoint blocks T-003. |

#### Validation IDs and commands

V-001, V-007, V-008, M-004, E-003, E-004; run existing v2 contract tests if the prototype touches a fixture.

#### Evidence requirements

Options considered, selected behavior, keyboard/no-script/print observations, source entrypoint, unresolved exception and evaluator identity.

#### Exit criteria

- [ ] U-001/U-002 have resolution or bounded blocker.
- [ ] One-document, keyboard, no-script and print fallback are proven or rejected.
- [ ] No template/validator change is claimed complete.
- [ ] Distinct evaluator records approve or revision.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:** planning author only; coverage/meeting gate pending.  
**Blocking conditions:** Tasks Ready has not been granted.

### T-002 — Construir a estrutura de abas v2 com fallback progressivo

**Status:** pending  
**Objective:** Implementar a estrutura selecionada de abas/painéis no template v2 e fixture focada, preservando hierarquia, ordem de fonte, foco de teclado e impressão.  
**Requirement IDs:** FR-001, FR-002, FR-007, FR-009  
**Acceptance criteria IDs:** AC-001, AC-002, AC-008, AC-009  
**Outcome served:** Stakeholders isolate a decision surface while every reader retains full access.  
**Demonstrable increment or reduced uncertainty:** Fixture shows eight selectable views in one HTML and complete no-script/print fallback.  
**Expected artifact/behavior:** Template HTML/CSS/minimal inline behavior and fixture only.  
**Validation method:** V-001, V-008, V-009, M-004, E-004.  
**Why now:** T-001 establishes interaction contract before content guidance depends on it.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001 approved  
**Risk:** high  
**Builder:** unassigned  
**Evaluator:** distinct accessibility reviewer  
**Human approval:** not_required  
**Evidence:** evidence/T-002.md

#### Scope

Add controls, panel states, responsive layout, visible selection, no-script/read-order fallback and print behavior. Retain visual lineage, header, snapshot and provenance conventions.

#### Out of scope

No domain enrichment, v1 change, router/framework, anchor removal without compatible recovery, or JS-only hidden content.

#### Outcome linkage

- **Requirement/AC/discovery question:** FR-001/002/007/009; AC-001/002/008/009.
- **Vertical slice relation:** directly enables rich content projections.
- **Priority source or human decision:** D-001 focused reading without multiple pages.

#### Expected files and contracts

`stakeholder-brief-design.md`, selected template HTML/CSS surface, focused fixture and only the minimum structural test justified by T-005. DOM retains `data-source`, `data-source-section` and `data-coverage` on material blocks.

#### Implementation constraints

No remote assets, app state, route, build step or semantic validator. A panel cannot leave accessibility tree/read order unless T-001 fallback proves recovery.

#### Assurance disposition

| Claim/risk | Selected technique and why | Oracle/data/environment | Builder/test executor | Evaluator/specialist | Evidence | Entry/exit/failure or waiver path |
|---|---|---|---|---|---|---|
| Abas em um documento | Fixture/assertion estático captura DOM/wiring estáveis. | Fixture local e inventário de arquivos. | builder | evaluator | T-002 evidence | Falha retorna à revisão da estrutura visual. |
| Accessible fallback | Manual behavior observes interaction modes. | Desktop/390px/keyboard/no-script/print. | builder | accessibility reviewer | T-002 evidence | Any unreachable panel blocks approval. |

#### Validation IDs and commands

V-001, V-008, V-009, M-004, E-004; `python scripts/test_brief_v2_contracts.py`; focused test when justified.

#### Evidence requirements

Tab/panel mapping, fallback observations, screenshots only as visual supplement, command results and evaluator decision.

#### Exit criteria

- [ ] Eight views exist in one offline document.
- [ ] Every panel is recoverable without script and in print.
- [ ] Keyboard/focus behavior matches T-001 decision.
- [ ] Existing v1/v2 checks pass.
- [ ] Distinct evaluator approves evidence.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:** planning author only.  
**Blocking conditions:** T-001 and global Tasks Ready gate.

### T-003 — Define tab missions, source-sufficiency questions and proportional detail

**Status:** pending  
**Objective:** Make existing authoring/review guidance specify mission, eligible facts, N/A/unknown behavior and clarification protocol for every tab; resolve U-003.  
**Requirement IDs:** FR-002, FR-003, FR-004, FR-006, FR-008, FR-009  
**Acceptance criteria IDs:** AC-002, AC-003, AC-004, AC-005, AC-007, AC-009  
**Outcome served:** Rich briefs derive depth from canonical sources instead of generic filler.  
**Demonstrable increment or reduced uncertainty:** Source inventory can decide content, N/A or owned question for all eight views.  
**Expected artifact/behavior:** Compact guidance/template contracts plus rich/non-software/sparse source records.  
**Validation method:** V-002–V-005, V-007, M-001, M-005, E-001–E-003.  
**Why now:** A estrutura visual é inútil se autores não distinguem profundidade material de detalhe ausente.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001 approved  
**Risk:** high  
**Builder:** unassigned  
**Evaluator:** distinct Spec Guardian  
**Human approval:** only for an actual unresolved consumer business question  
**Evidence:** evidence/T-003.md

#### Scope

Specify the eight contracts. Value/scope includes mission, value pillars, high-level technical pillars when material, outcome, limits, main risk and authority. Architecture/impact open with mission/vision. Evolution, decision and coverage expose state/authority. Source sufficiency is needed fact → owner → decision impact → resolution path.

#### Out of scope

No quota, mandatory diagram, universal clarification form, domain ontology or interaction change beyond T-002 contract annotations.

#### Outcome linkage

- **Requirement/AC/discovery question:** FR-002/003/004/006/008/009; U-003; AC-002–005/007/009.
- **Vertical slice relation:** directly enables truthful rich panels and bounded discovery.
- **Priority source or human decision:** D-001 asks system to ask rather than invent.

#### Expected files and contracts

Existing authoring/planning/review/design guidance selected in T-001, relevant templates and fixtures. Unknowns stay in plan/decision/progress; no composition sidecar.

#### Implementation constraints

Ask only if absent fact blocks a decision, AC, risk control or next safe step. Each question states exact need, owner, impact and resolution. Simple initiatives use concise source-backed N/A.

#### Assurance disposition

| Claim/risk | Selected technique and why | Oracle/data/environment | Builder/test executor | Evaluator/specialist | Evidence | Entry/exit/failure or waiver path |
|---|---|---|---|---|---|---|
| Proportional depth | Paired/sparse fixtures expose overfitting. | Software, non-software and missing-detail sources. | builder | Spec Guardian | T-003 evidence | Fake/mandatory detail returns to source guidance. |
| Discovery specificity | Qualitative review checks question completeness. | Source gaps and decision log/progress. | builder | reviewer | T-003 evidence | Generic question blocks approval. |

#### Validation IDs and commands

V-002–V-005, V-007, M-001, M-005, E-001–E-003; `python scripts/test_semantic_brief_review_calibration.py`.

#### Evidence requirements

Per-tab contract, three fixture comparisons, each unknown/question and source → fact → correction/resolution path.

#### Exit criteria

- [ ] All eight missions are concrete and source-backed.
- [ ] Rich task/validation fields are identified without new schema.
- [ ] Sparse/non-software examples avoid fake detail.
- [ ] Material gaps produce owned questions; non-material gaps do not.
- [ ] Distinct Spec Guardian approves evidence.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:** planning author only.  
**Blocking conditions:** T-001 and global Tasks Ready gate.

### T-004 — Project rich task and validation contracts into execution views

**Status:** pending  
**Objective:** Implement detailed Execution and Validation panels from canonical task/validation sources, including compact variants for legitimate N/A/skips.  
**Requirement IDs:** FR-004, FR-005, FR-006, FR-008, FR-009  
**Acceptance criteria IDs:** AC-005, AC-006, AC-007, AC-009  
**Outcome served:** Builder, evaluator and stakeholder distinguish deliverable, proof and limitation without reopening several Markdown files.  
**Demonstrable increment or reduced uncertainty:** Rich fixture and sandbox expose complete task cards and AC/proof matrix; sparse fixture explains absence of command/detail.  
**Expected artifact/behavior:** Template/content guidance/fixtures and source-provenance mappings.  
**Validation method:** V-005–V-007, M-002, M-003, E-001–E-003.  
**Why now:** T-002 gives panels and T-003 defines eligible content.  
**Max subtasks before validation:** 3  
**Dependencies:** T-002 and T-003 approved  
**Risk:** high  
**Builder:** unassigned  
**Evaluator:** distinct planner/reviewer  
**Human approval:** not_required  
**Evidence:** evidence/T-004.md

#### Scope

Create execution cards for each material task and validation rows for each AC/proof. Project objective, FR/AC, outcome, scope/anti-scope, artifacts, dependencies, risk/assurance, validation, evidence, exit and next-safe-step; project AC/method/environment/fixture/oracle/evidence/skip reason.

#### Out of scope

No task/validation source of truth in HTML, no claim every task is implementation work, no fabricated command/oracle and no inferred product priority.

#### Outcome linkage

- **Requirement/AC/discovery question:** FR-004–006/008/009; AC-005–007/009.
- **Vertical slice relation:** delivers depth needed for execution/proof decisions.
- **Priority source or human decision:** D-001 rejects generic task titles.

#### Expected files and contracts

Selected v2 template/design and task/validation templates, rich/sparse fixtures and news/blog candidate. Provenance identifies source heading/ID for every substantive child block.

#### Implementation constraints

Use responsive cards/local table overflow; distinguish planned, observed, proved and unavailable evidence; preserve draft status; no duplicate JSON/sidecar or semantic score.

#### Assurance disposition

| Claim/risk | Selected technique and why | Oracle/data/environment | Builder/test executor | Evaluator/specialist | Evidence | Entry/exit/failure or waiver path |
|---|---|---|---|---|---|---|
| Task fidelity | Source-to-card trace detects drift. | Rich `tasks.md` + rendered panel. | builder | planner/reviewer | T-004 evidence | Invented/missing fact returns to source. |
| Validation fidelity | AC-to-proof matrix detects vague proof. | Rich and no-command fixtures. | builder | planner/reviewer | T-004 evidence | Missing oracle/skip rationale returns to source/question. |

#### Validation IDs and commands

V-005–V-007, M-002, M-003, E-001–E-003; sandbox Human Visibility command after refresh.

#### Evidence requirements

For each fixture: task/validation locator mapping, recovered decision, skip/N/A reasoning, command result and independent review record.

#### Exit criteria

- [ ] Rich tasks are more than titles/status and match canonical sources.
- [ ] Validation matrix recovers AC, method, context, oracle and evidence.
- [ ] Missing data uses appropriate question/N/A and owner/risk.
- [ ] Draft status remains non-authorizing.
- [ ] Distinct evaluator approves evidence.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:** planning author only.  
**Blocking conditions:** T-002/T-003 and global Tasks Ready gate.

### T-005 — Validate compatibility, fixtures and release evidence independently

**Status:** pending  
**Objective:** Run proportionate regression checks, choose minimum focused structural test, obtain independent accessibility/meaning review and prepare release evidence.  
**Requirement IDs:** FR-007, FR-009, FR-010  
**Acceptance criteria IDs:** AC-001, AC-002, AC-004, AC-008, AC-009, AC-010  
**Outcome served:** Bundle change is proven bounded, accessible and reusable before adoption.  
**Demonstrable increment or reduced uncertainty:** Commands, fixture reviews, no-score diff review and independent release decision show safety.  
**Expected artifact/behavior:** Focused test only if failure analysis warrants it, evidence pack, decision and baseline where applicable.  
**Validation method:** V-001–V-011, V-REG-001–004, M-004, E-001–E-004.  
**Why now:** All surfaces must exist before compatibility/rendered meaning can be assessed.  
**Max subtasks before validation:** 3  
**Dependencies:** T-001–T-004 approved  
**Risk:** medium  
**Builder:** unassigned  
**Evaluator:** distinct maintainer  
**Human approval:** pending only if new dependency, v1 migration or semantic mirror is proposed  
**Evidence:** evidence/T-005.md

#### Scope

Choose minimum structural test, run command matrix, inspect diff, exercise all fixture classes and obtain independent rendered/accessibility/release review. Refresh baselines only after review per existing policy.

#### Out of scope

No self-approval, accessibility waiver for polish, score conversion, consumer application code or v2 scope expansion without approval.

#### Outcome linkage

- **Requirement/AC/discovery question:** FR-007/009/010; AC-001/002/004/008–010; Q-005.
- **Vertical slice relation:** proves and contains the complete delivery slice.
- **Priority source or human decision:** reusable bundle must remain safe across consumers.

#### Expected files and contracts

Focused test if justified, fixture records, `evidence/T-005.md`, decision log, state/progress/handoff and refreshed affected brief/baseline. No external CI/service.

#### Implementation constraints

Evaluator is not builder. Structural pass does not replace meaning/accessibility review. Any non-pass returns to revision; no release without clean synchronized state/evidence.

#### Assurance disposition

| Claim/risk | Selected technique and why | Oracle/data/environment | Builder/test executor | Evaluator/specialist | Evidence | Entry/exit/failure or waiver path |
|---|---|---|---|---|---|---|
| Compatibility/no semantic gate | Commands plus diff review. | Bundle root, v1/v2 fixtures. | builder | maintainer | T-005 evidence | Failure blocks release. |
| Rendered usefulness/accessibility | Independent review catches contextual loss. | Rich/non-software/sparse HTML at required modes. | builder prepares | distinct reviewer | T-005 evidence | Revise canonical/template source. |

#### Validation IDs and commands

V-001–V-011, V-REG-001–004, M-004, E-001–E-004; all validation-plan §4 commands.

#### Evidence requirements

Command output, fixture matrix, no-score diff assertion, independent reviewer identity/findings, residual risk, baseline action and release decision.

#### Exit criteria

- [ ] Required commands pass or approved exception is explicit.
- [ ] v1/v2 contracts remain valid.
- [ ] Independent review covers meaning, fallback and accessibility.
- [ ] No score/parser/sidecar/new runtime appears.
- [ ] Evidence, state, progress and handoff synchronize.
- [ ] Distinct maintainer approves or requests revision.

#### Readiness decision

**Task Ready:** no  
**Reviewed by:** planning author only.  
**Blocking conditions:** all preceding tasks, coverage review, meeting decision and global Tasks Ready gate.
