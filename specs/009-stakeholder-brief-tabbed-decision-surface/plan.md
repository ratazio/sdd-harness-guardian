# Technical Plan: 009-stakeholder-brief-tabbed-decision-surface

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-26

## 1. Technical approach

Evoluir a estrutura visual existente do brief v2, sem criar páginas ou aplicação. Um HTML contém todos os painéis; uma melhoria de abas, nativa quando possível, seleciona uma visão por vez, enquanto ordem normal, teclado e impressão preservam a leitura completa sem script.

Each view has a fixed purpose but conditional content. Source-backed facts are represented or synthesized. A material absence becomes a precise question or owned unknown; irrelevant detail receives concise N/A with reason. The renderer never starts by making a prettier blank panel.

T-001 inventaria a estrutura visual atual, validator, entrypoints de autoria/review e fixtures, então resolve os unknowns de interação/suficiência de fonte. As tasks seguintes evoluem template e guidance existentes, projetam contratos ricos de task/validação e testam fontes software, não-software e esparsas. Checks determinísticos provam somente markup/fallback/provenance estáveis; review independente julga utilidade.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| AD-001 | Keep one offline v2 HTML document; tabs are in-document views. | Focused reading without fragmented artifacts. | One file/route per section; SPA/router. | Fallback must recover every panel. |
| AD-002 | Use a native-first progressive enhancement selected by T-001. | No-script, keyboard and print are existing constraints. | Framework or JS-only tabs. | Accessibility behavior is a gate. |
| AD-003 | Define eight tab missions and conditional content contracts. | Different projects require different depth. | Word/field quotas and mandatory diagrams. | N/A/unknown must be concise and visible. |
| AD-004 | Missing material source detail becomes question/owned unknown before composition. | Renderer cannot enrich absent Markdown truthfully. | Invented facts; generic “a confirmar”; universal questionnaire. | A material business question pauses only its affected gate. |
| AD-005 | Project existing full task/validation contracts when present. | Titles and commands alone do not support delivery decisions. | Parallel schemas or source-file copy. | Cards need fine-grained provenance/responsive layout. |
| AD-006 | Preserve v1 and keep validator structural. | This is v2 usability, not semantic enforcement. | Forced migration; score/parser/LLM judge. | Independent review remains required. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** reusable template, authoring/review workflow, task/validation projection, fixtures and focused checks change; there is no runtime service, migration or external integration.  
**Smaller option considered:** style current anchors as chips. Rejected because it hides the same shallow long page and does not solve depth/discovery.  
**Complexity deliberately excluded:** routes, framework, remote assets, telemetry, persistent UI state, per-domain templates, mandatory diagrams, semantic score/parser, external question tracker and v1 migration.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** A2-elevated.  
**Rationale and trigger evidence:** this is cross-consumer UI and governance behavior; an accessibility or source-fidelity regression can impair future decisions, while rollback is static and bounded.  
**A2/A3 source links/headings:** spec §7 FR-001–010; impact IR-001–IR-007; validation §1–6.  
**Reapproval trigger:** JS-only reading, more than one HTML document, external dependency/storage, v1 migration, semantic gate or failed accessibility proof.

### Architecture scope/size profile

**Profile:** M.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Canonical Markdown/YAML feed one offline v2 brief. | Same ownership; selected view plus complete fallback. | spec §10; AD-001; T-001. |
| Components/responsibilities | Template renderiza; autor/reviewer compõem e avaliam. | Estrutura visual de abas, missões, protocolo de discovery e projeções ricas reutilizam papéis. | AD-002–005; T-001–T-004. |
| Interfaces/events/contracts | File/template/DOM/provenance; no network. | Stable tab/panel/fallback markup and existing `data-*`. | FR-001, FR-009; T-002. |
| Data ownership/lifecycle | Markdown/state/log canonical; HTML derived. | Question/unknown is recorded in existing source/log, never tab-local. | AD-004; FR-003. |
| Security/trust boundaries | Static source detail may be sensitive. | Redact sensitive facts; no remote assets. | impact IR-006; T-005. |
| Critical runtime flows | No application runtime; reader interaction is operational flow. | Tab selection → decision view → source recovery; fallback works. | Flow below; T-002. |
| Failure behavior | Linear brief works without JS; detail can be unsupported. | Script failure/unknown fact becomes readable panel or explicit question/N/A. | EC-003–006; T-001/T-003. |
| NFRs | Responsive/no-script/print requirements exist. | Keyboard/focus/390px/print remain valid. | FR-007; V-008. |
| Compatibility/migration | v1 retained; v2 provenance/coverage gates exist. | v1 untouched; v2 mapping remains DOM-local/table-based. | AD-006; V-009. |
| Observability | Decision log, progress and state describe gates. | Evolution/decision view makes facts recoverable; no telemetry. | FR-008; T-004. |
| Rollout/rollback | Arquivos versionados/fixtures estáticas. | Atualização limitada do bundle; leitura linear anterior permanece fallback. | §8; impact §4. |
| Alternatives/trade-offs | Long scroll minimizes interaction but diffuses focus. | Tabs focus one decision surface while retaining full fallback. | AD-001–003. |
| Unknowns | Interaction, authoring entrypoint, task/validation field set unverified. | Resolve U-001–U-004 through discovery. | impact §6; T-001/T-003/T-004. |

### Critical reader and discovery flow

```txt
source inventory -> material fact present? -> tab content
                          | no
                          v
                 question / owned unknown -> source resolution

tab selection -> active decision view -> source recovery
      | script unavailable
      v
ordered full document / details / print
```

Text equivalent: the author determines whether a fact exists and matters first. A reader can focus a decision view; a failure of enhancement reveals the same content in normal document order.

### Current → target → delta and complexity envelope

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Architecture/method | Eight anchored sections in one long flow. | Eight focused tab views with fallback. | Template/CSS/small inline behavior only. | Router/framework/remote asset. |
| Modules/classes/APIs/data/contracts | Templates, rules, skills, static validators. | Per-tab composition and stable DOM checks; no API/data. | Extend existing contracts only. | Schema or semantic parser. |
| Process/tooling | Coverage composition/rendered review exist. | Bounded source-sufficiency question/unknown before composition. | Existing sources/log/state only. | External ticket system. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Inventory template, validator, skills/agents, 008 fixtures and sandbox; prototype interaction. | Spec/plan ready | U-001/U-002 resolved; fallback behavior documented. | yes |
| 2 | Estrutura visual v2 e fixture focada. | Step 1 | Esqueleto de abas/painéis em um documento, com contrato visual/fallback. | yes |
| 3 | Authoring/planning/review guidance and source templates. | Step 1 | Tab missions, detail eligibility and question/unknown protocol discoverable. | yes |
| 4 | Task/validation projections and rich/sparse fixtures. | Steps 2–3 | Execution/validation views recover source contracts proportionally. | yes |
| 5 | Focused checks, independent rendered review and bundle validation. | Steps 1–4 | Stable behavior checked; independent release decision. | yes |

## 6. Contracts, data and compatibility

- **API/events:** no runtime API, event or router; tab selection is local presentation state, not persistent consumer state.
- **Database/storage:** none; `spec.md`, plan, tasks, validation, decision log and YAML state remain canonical.
- **External systems:** none; no remote assets/analytics. A stakeholder question uses existing decision/unknown workflow.
- **Compatibility/migration:** v1 has no implicit layout migration. v2 retains provenance, coverage table, lifecycle gates and material-refresh behavior.

## 7. Security, privacy and permissions

- **Authentication/authorization:** not applicable; static/offline artifact.
- **Secrets/PII:** do not turn a detail request into disclosure; use redacted source-backed abstraction and record access constraints.
- **Required permission:** ordinary versioned-file changes; business context is requested from the accountable consumer stakeholder only when material.
- **Destructive operations and approvals:** none. New dependency, semantic gate or v1 migration needs explicit human reapproval.

## 8. Rollout, observability and rollback

- **Rollout:** versioned bundle update for new/materally refreshed v2 briefs; exercise reference fixtures and ignored news/blog sandbox first.
- **Success/failure signals:** all views recover without script; rich task and validation facts are recoverable; sparse fixture asks only material questions; no score/parser; independent reviewer accepts rendered package.
- **Rollback trigger:** hidden content, keyboard/print failure, fabricated detail, v1 regression or mandatory discovery burden.
- **Exact rollback/checkpoint:** reverter conjunto limitado de template/guidance/fixture; preservar histórico de decisão e leitura linear v2 anterior. Sem migração de dados/tasks.
- **Gate authority:** distinct reviewer controls coverage/Human Visibility; existing maintainer accepts final evidence. A human answers only an actual material business/context question.

## 9. Brief coverage composition (v2)

Author: **Codex / brief author**. This is planning composition, not a self-approved review. A distinct reviewer is required before `brief_coverage_ready` or Human Visibility.

| Source locator | Coverage | Rendered target | Reason when required |
|---|---|---|---|
| spec.md §1–3 | synthesized | `#scope`, `#decision-snapshot` | Mission, outcome and delivery boundary. |
| spec.md §4–6 | represented | `#scope` | Actors/outcomes/non-goals must remain recoverable. |
| spec.md §7–8 | synthesized | `#architecture`, `#execution`, `#validation` | Requirements split by decision view. |
| spec.md §9–14 | represented | `#impact`, `#validation`, `#decision` | Controls and unknowns are material. |
| spec.md §15 | represented | `#evolution`, `#decision` | Planning authority is visible. |
| impact-map.md §1–4 | synthesized | `#architecture`, `#impact` | Boundary, flow and compatibility. |
| impact-map.md §5–8 | represented | `#impact`, `#decision` | Risk/control/owner and conditions. |
| plan.md §1–4 | synthesized | `#architecture`, `#scope` | Architecture mission/vision and envelope. |
| plan.md §5–8 | represented | `#execution`, `#architecture`, `#impact` | Delivery and trust/rollback facts. |
| plan.md §9–11 | represented | `#coverage`, `#evolution`, `#decision` | Coverage and discovery state. |
| tasks.md ledger/T-001–T-005 | represented | `#execution` | Draft task contracts are material/non-authorizing. |
| validation-plan.md §1–8 | represented | `#validation` | Proof matrix and skipped checks. |
| decision-log.md D-001 onward | represented | `#evolution`, `#decision` | Append-only authority/rationale. |
| progress.md checkpoint/risks/next step | synthesized | `#evolution` | Compact resumable state. |
| run-state.yaml gates/ledger/risks | represented | `#decision-snapshot`, `#evolution` | Truthful authorization state. |

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Which native-first markup/behavior selects a tab while retaining no-script, keyboard and print access? | T-001 planner + accessibility reviewer | Prototype and record fallback in D-002. | yes |
| Q-002 | Which existing authoring skill/agent receives source-sufficiency protocol? | T-001 planner | Inventory entrypoints; select minimal existing surfaces. | yes |
| Q-003 | Which full task fields are stable to project and how do absent optional fields appear? | T-003 planner | Compare template, 008 and sandbox. | yes |
| Q-004 | How does no-command/non-software validation appear without looking like failure? | T-004 planner | Validate a justified skip/N/A fixture. | no |
| Q-005 | Is a new structural test needed or can current tests cover tab/fallback invariants? | T-005 maintainer | Compare fixture failure modes; add minimum check. | no |

## 11. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex / Harness Planner  
**Reviewed at:** 2026-08-26  
**Conditions/links:** U-001–U-003 are bounded discovery work; no template or validator change begins before their resolution. Tasks remain non-authorizing until independent review and meeting propagation.
