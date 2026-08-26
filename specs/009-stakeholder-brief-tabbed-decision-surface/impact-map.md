# Impact Map: 009-stakeholder-brief-tabbed-decision-surface

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex / Impact Mapper  
**Reviewed at:** 2026-08-26  
**Overall risk:** medium

## 1. Change boundary

The change reorganizes the v2 stakeholder-brief presentation and the planning
guidance that feeds it. It adds an accessible tabbed view to one offline HTML
document and a proportional source-sufficiency/discovery protocol. It does not
change consumer application behavior, create a runtime web application, add a
data store, make prose scoring deterministic or migrate v1 briefs.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Estrutura visual do brief v2 | `.harness/templates/stakeholder-brief-design.md` e HTML v2 renderizado | direct | Interação de abas no mesmo documento, estados visuais e fallback sem script/impressão. | high | FR-001, FR-007, AC-001, AC-008 |
| Composition guidance | spec-author/planner/review guidance, Human Visibility rule and relevant agent instructions found in T-001 | direct | Per-tab mission, material-detail eligibility and clarification/unknown contract. | high | FR-002, FR-003, FR-006 |
| Task projection | `tasks.md` template and brief execution view | direct | Rich task cards derived from the existing task contract. | high | FR-004, AC-005 |
| Validation projection | `validation-plan.md` template and brief validation view | direct | AC/proof matrix with command/environment/oracle/evidence and skip rationale. | high | FR-005, AC-006 |
| Lifecycle/state/decision | `.harness/workflows/sdd-lifecycle.md`, decision/state presentation | indirect | Preserve existing gates while evolution/decision views make authority visible. | medium | FR-008, FR-009 |
| Deterministic validator | `scripts/validate_human_visibility.py` and focused tests | direct | Verify stable structural/tab/fallback invariants only. | high | FR-007, FR-009, FR-010 |
| Public/API contract | none | not_applicable | No runtime API, client endpoint or externally hosted UI exists. | low | change boundary |
| Auth/security/privacy | static artifacts and fixtures | indirect | Prevent sensitive facts from being exposed through richer projections. | medium | spec §10; IR-006 |
| Build/deploy/infra | none | not_applicable | No service, deployment, database or infrastructure changes. | low | change boundary |
| Observability/support | decision log, progress, handoff and discovery unknowns | direct | Questions and state become visible/recoverable in a bounded form. | medium | FR-003, FR-008 |
| Tests/docs/fixtures | templates, fixtures, tests, consumer-enforcement documentation when warranted | direct | Cross-context examples and independent rendered review demonstrate proportionality. | medium | validation plan §1–6 |

## 3. Dependency and information flow

```txt
canonical Markdown + run state
  -> per-tab source sufficiency check
  -> question / owned unknown when a material fact is absent
  -> single derived HTML document
  -> tab enhancement and no-script reading order
  -> independent rendered-meaning review
  -> canonical correction, refresh and existing lifecycle gates
```

Text equivalent: the tab never owns facts. Before an author composes a tab,
they decide whether a source fact is represented, summarized, not applicable
with reason, or absent and therefore a question/unknown. The rendered page is
then an easier way to select a decision surface; without script it remains a
complete ordered document.

## 4. Compatibility and migration

- **Backward compatibility:** v1 mantém seu formato visual histórico e lifecycle.
  The tabbed design applies to new v2 briefs or a material v2 refresh only.
- **Data migration:** none. Markdown, decision log and YAML state retain their
  current ownership; no content is transformed in place.
- **Rollout/feature flag:** versioned bundle update, exercised first in static
  fixtures and the ignored news/blog sandbox; no feature flag because there is
  no running service. A consumer can keep a pinned bundle version.
- **Rollback implications:** revert the bounded template/guidance/fixture/test
  changes as one release. Existing source artifacts and decision histories are
  unaffected; a rendered brief can fall back to its linear reading order.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-001 | Uma aba esconde decisão ou faz parecer que painéis omitidos não existem. | Só o painel ativo fica acessível após desativar script ou imprimir. | medium / high | Fallback progressivo, estado textual e checks de teclado/sem script/impressão. | Retornar à leitura linear; responsável pelo template. | V-008, M-004 |
| IR-002 | A rich execution card drifts from `tasks.md`. | Brief promises an artifact, contract or evidence absent from the task source. | medium / high | DOM-local provenance, task-card fixture and independent recovery review. | Correct source first, refresh brief; planner. | V-005, M-002 |
| IR-003 | Generic depth requirements force fake architecture or validation in a simple/non-software initiative. | N/A contains filler, fake APIs or ornamental diagrams. | medium / high | Detail eligibility and question/unknown protocol; paired fixtures. | Remove unsupported block and record reason; Spec Guardian. | V-004, V-007, E-002 |
| IR-004 | Discovery asks every possible question and stalls a small change. | Clarification list lacks material decision/impact. | medium / medium | Ask only when the absent fact blocks a decision, AC, risk control or next safe step. | Downgrade to source-backed N/A; Orchestrator. | V-007, E-003 |
| IR-005 | Tabs break keyboard, focus, narrow layout or print. | Focus is lost, ARIA/visible state disagrees, or hidden panels are absent in print. | medium / high | Native-first prototype, manual accessibility checks and fixture contract. | Revert enhancement, retain full reading order; accessibility reviewer. | V-008, M-004 |
| IR-006 | Richer projection leaks sensitive topology or personal data. | Source recovery exposes secrets/PII in a broad tab. | low / high | Redaction rule and source-backed abstraction; no remote assets. | Redact source/brief and review exposure; security owner. | V-011 |
| IR-007 | A structural check becomes an automated prose-quality gate. | Diff introduces score, threshold, parser or pass/fail semantic claim. | low / high | Explicit scope guard and negative diff check. | Reject change; maintainer. | V-010, V-REG-002 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Which native-first tab pattern meets current no-script, keyboard and print contract without a framework? | Interaction choice can otherwise regress accessibility. | T-001 / planner + accessibility reviewer; prototype and inspect browser behavior. | yes |
| U-002 | Which existing skill/agent is the authoritative authoring entrypoint for a source-sufficiency question? | Adding duplicate guidance would create inconsistent discovery behavior. | T-001 / planner; inventory guidance and select reuse points. | yes |
| U-003 | Which task fields are stable enough for a detailed card across current consumer templates? | The card must project canonical fields, not invent a new task schema. | T-003 / planner; compare template, 008 and news/blog sandbox. | yes |
| U-004 | Which validation fields can be consistently recovered when a project has no command? | A mandatory command table would punish legitimate non-software work. | T-004 / planner; use non-software fixture and skip rationale. | no; blocks only contract finalization |
| U-005 | Whether the current v2 validator can express tab/fallback structure without coupling to prose. | Determines smallest safe test boundary. | T-005 / maintainer; fixture failure-mode comparison. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** distinct accessibility reviewer for interaction/fallback;
  distinct Spec Guardian for coverage and post-render meaning; human only when
  a consumer question is a business/priority decision.
- **Unit/integration/contract/E2E:** teste focado da estrutura visual de abas e fixtures,
  `test_brief_v2_contracts.py`, `test_validate_human_visibility.py`, semantic
  calibration test and `validate_bundle.py`.
- **Manual/operational:** desktop and 390px tab scan, keyboard tab/arrow/panel
  navigation as selected by T-001, no-script read, print preview and a
  60-second decision recovery review of software, non-software and sparse
  source fixtures.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes — for independent accessibility/rendered-meaning
review; consumer business questions require their stakeholder owner.  
**Approval/evidence:** user request in this conversation; planning sources
complete enough for discovery tasks, not implementation.  
**Conditions before implementation:** resolve U-001–U-003, keep v1 untouched,
retain one HTML/fallback, preserve canonical provenance, and keep checks out
of semantic judgment.
