# Spec: 010-stakeholder-brief-composition-kit

**Status:** approved for gated execution — 2026-08-26 user authorization recorded in D-006  
**Sequence:** 010  
**Owner:** platform-engineering  
**Created / updated:** 2026-08-26  
**Risk:** medium  
**Assurance profile:** A2-elevated

## 1. Problem

A aba v2 já separa os domínios de decisão, mas o brief ainda pode parar no
primeiro nível de descrição: uma arquitetura macro de caixas não explica, por
exemplo, a responsabilidade interna de um componente relevante; uma matriz de
impacto ou cobertura pode voltar a ser uma tabela uniforme e cansativa; e uma
task pode regredir para título/estado quando o autor não lembra do contrato
completo que deve projetar.

Criar um segundo agente que “conserta” HTML depois de gerado aumentaria a
cadeia, perderia contexto das fontes e criaria risco de divergência. Ao mesmo
tempo, impor detalhes, diagramas ou campos em qualquer iniciativa faria o
harness inventar software em uma mudança simples, operacional ou não técnica.

## 2. Objective

Integrar ao processo normal de composição do stakeholder brief um kit de
raciocínio visual e mini-templates proporcionais. O autor constrói profundidade
a partir da mesma leitura das fontes canônicas; o reviewer independente avalia
a projeção resultante. Não há agente corretor posterior nem score automático de
qualidade.

## 3. Delivery outcome

- **Usuário:** decisor entende a relação macro e, onde suportado, os poucos
  pontos internos que realmente orientam uma escolha; builder/evaluator
  recuperam a definição completa de cada task sem abrir uma caça a contexto.
- **Incremento demonstrável:** guidance, template e fixtures distinguem
  corretamente uma arquitetura rica com corte interno, uma mudança simples e
  um caso não-software; o brief rico passa a apresentar cards de task e
  superfícies de impacto/cobertura com hierarquia visual útil.
- **MVP:** uma etapa de composição integrada, um catálogo compacto de padrões,
  uma régua de profundidade e exemplos/validações de regressão. O HTML continua
  único, local e derivado.
- **Prioridade:** feedback explícito do mantenedor após avaliar o sandbox
  news/blog em 2026-08-26.

## 4. Actors

- **Spec author / planner:** decide qual padrão visual serve ao fato de fonte e
  explicita uma lacuna material em vez de preenchê-la.
- **Stakeholder decisor:** percorre macrovisão e cortes internos sem receber
  detalhe ornamental.
- **Builder / evaluator:** lê um card de task suficiente para executar ou
  revisar a unidade seguinte com segurança.
- **Independent brief reviewer:** julga suficiência, proporcionalidade e
  legibilidade depois do render, sem reescrever fontes durante a revisão.
- **Leitor não-software:** vê processos, responsabilidades e controles sem
  receber uma arquitetura de APIs fictícia.

## 5. Decision: where the intelligence lives

The selected design is **one integrated composition process**:

1. author/planner inventories canonical headings and applies the existing
   source-sufficiency/discovery rule;
2. the selected mini-template turns supported facts into a visual relationship;
3. the v2 reviewer evaluates the source-to-render projection under the
   existing independent gate;
4. correction happens in Markdown/decision/state and the brief is regenerated.

There is no mandatory downstream HTML-polish sub-agent. A later visual review
may identify a source/render mismatch, but cannot become a parallel author or
silently fabricate content.

## 6. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | The authoring guidance SHALL add a small composition stage before HTML render, using existing canonical sources and the existing coverage review. | Preserves context and source of truth. |
| FR-002 | Architecture SHALL use a depth ladder: orientation; macro relationship; and, only when source-backed and decision-material, one focused internal cut. | Enables useful decomposition without recursive diagrams. |
| FR-003 | A focused architecture cut SHALL name the selected boundary, responsibilities, information/contract in and out, data/trust/failure implication and decision it helps; it SHALL not invent modules. | A second diagram must answer a decision, not decorate. |
| FR-004 | The composition SHALL select no more than the supported depth: a simple/localized/non-software initiative may use text, one boundary or a justified compact omission. | Keeps the bundle general-purpose. |
| FR-005 | Execution SHALL use a reusable task card projection whenever source task fields exist: objective/outcome; demonstrable increment; scope/anti-scope; contracts/artifacts; dependencies/risk/assurance; validation/evidence; exit; status/authority; and why-now/next-safe-step. | The complete task contract must be consistently recoverable. |
| FR-006 | Optional task details absent from source SHALL be omitted from the visible card or shown as a concise source-backed limitation; a material absence SHALL follow the owned-question path. | Avoids empty rows and invented detail. |
| FR-007 | Impact SHALL offer source-appropriate compositions beyond a flat table, such as a surface footprint, risk chain, owner/control cards or compatibility path. | Impact needs relationships, not only rows. |
| FR-008 | Coverage SHALL offer a scannable provenance composition that groups source/heading, rendered decision view and disposition while preserving a semantic table/equivalent for accessibility. | Coverage needs trust and traceability without monotony. |
| FR-009 | Validation, evolution and decision patterns SHALL make proof, limitation, state and authority visually distinguishable without colour-only meaning. | Applies the same information-design reasoning across tabs. |
| FR-010 | All patterns SHALL retain one offline HTML, local provenance, keyboard/no-script/390px/print recovery and v1 compatibility. | A richer composition cannot regress 009. |
| FR-011 | Deterministic tests SHALL cover only stable wiring/presence/fallback/fixture behavior; semantic usefulness and visual proportionality remain independent review. | Avoids a brittle prose or aesthetics gate. |
| FR-012 | The kit SHALL be vendor-neutral; client visual identity is introduced only by the separate profile initiative 011 and must not be hard-coded here. | The source bundle serves many consumers. |
| FR-013 | Before a brief is opened, linked or represented as the generated stakeholder brief, the composer SHALL synchronize its Execution and Validation projections with populated canonical sources. Every source task ID in a non-empty task ledger SHALL have a corresponding Execution projection; every source AC in a populated validation trace SHALL have a corresponding validation projection or an explicit source-backed omission. | A scaffold must never masquerade as the derived artifact. |
| FR-014 | A pre-render scaffold MAY exist only as an explicitly labelled draft with Human Visibility false; it SHALL not be presented as the initiative brief or pass coverage/readiness checks while its task/proof projections are generic. | Makes lifecycle truth visible even before a derived brief exists. |

## 7. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Guidance identifies the integrated composition stage and explicitly rejects a required post-generation fixer agent. | V-001, E-001 |
| AC-002 | A rich fixture shows macro architecture plus one source-backed focused cut with boundary, responsibility, interface/data/trust/failure and decision context. | V-002, M-001, E-002 |
| AC-003 | A localized and a non-software fixture do not receive fabricated component diagrams or forced technical fields. | V-003, E-003 |
| AC-004 | Each task in a rich fixture projects the full non-empty task contract; a sparse task does not render empty generic labels. | V-004, M-002 |
| AC-005 | Impact offers at least one relationship-oriented composition and coverage is scannable while a semantic table/equivalent remains available. | V-005, M-003 |
| AC-006 | Validation/evolution/decision distinguish proof, limitation, state and authority with text/icon/structure, not colour alone. | V-006, M-004 |
| AC-007 | Existing eight tabs, provenance, fallback, keyboard, 390px and print tests retain their guarantees. | V-007, V-REG-001 |
| AC-008 | A reviewer can trace every deeper visual block to source sections or a justified absence and returns source corrections rather than HTML-only facts. | E-004 |
| AC-009 | No semantic scoring, word quota, mandatory diagram count, LLM quality judge or fixed development-domain ontology is introduced. | V-008, V-REG-002 |
| AC-010 | The composition kit has no Pearson or other client identity hard-coded; visual profile selection is a separate concern. | V-009 |
| AC-011 | A rich fixture with four canonical tasks and a populated AC trace renders all four task IDs as detailed Execution cards and every AC as a recoverable Validation entry; a generic scaffold fails the parity check. | V-011, M-005 |
| AC-012 | An intentionally unrendered draft is visibly identified as a scaffold and cannot satisfy Brief Coverage, Human Visibility or Tasks Ready; it is never linked as the generated stakeholder brief. | V-012, E-005 |

## 8. Detail ladder and selection rules

| Level | Use when | Required source support | Visible output | Do not use when |
|---|---|---|---|---|
| 0 — orientation | A decision view is material. | Mission, current/target or limit. | Short framed introduction. | A source-backed concise N/A is clearer. |
| 1 — macro relation | Two or more decision-relevant actors, surfaces or stages relate. | Responsibility/flow/contract in plan or impact map. | Diagram, sequence, map or structured card group with textual equivalent. | Relationship is merely decorative. |
| 2 — focused cut | One macro component/boundary carries a material decision or risk. | Internal responsibility plus at least one interface, data/trust/failure fact and decision relevance. | One subordinate cut/card group, maximum one level below macro. | Internal facts are absent, generic, non-material or would create a fake implementation plan. |

A level-2 architecture cut can describe a service, a policy approval path, an
operational handoff, a research workstream or another source-backed boundary.
Internal architecture does not mean programming classes.

## 9. Non-goals

- Multiple HTML pages, routes, JavaScript framework, remote service or
  persistent composition state.
- A mandated extra agent that mutates the HTML after its sources are forgotten.
- Unlimited drill-down, UML formalism, data model or diagram in every spec.
- Empty cards, generic filler or invented unknowns.
- Mandatory technical architecture for policy, research, documentation or
  local changes.
- Client logo, palette, font or photography; those belong to 011.
- Automatic semantic/aesthetic approval.

## 10. Edge cases

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Architecture source has one boundary and no internal contract. | Render level 0/1 concise explanation; do not create a child diagram. |
| EC-002 | One component has many internal details but only one affects the requested decision. | Render a single focused cut around that boundary; link the rest to canonical source if needed. |
| EC-003 | Task is discovery/operations with no files or API contract. | Card retains objective, uncertainty, owner, method/evidence and why-now; technical rows are omitted or source-backed N/A. |
| EC-004 | Impact has no risk register but has affected stakeholders/process. | Use footprint/relationship composition and disclose the source's risk limitation. |
| EC-005 | Coverage has many headings on mobile. | Semantic table remains reachable; cards/grouping avoid whole-page horizontal table dependence. |
| EC-006 | Reviewer finds a deeper diagram unsupported. | Correct/remove at canonical source/composition level and regenerate; never patch only pixels. |
| EC-007 | Canonical tasks/validation are populated after a scaffold was created. | Regenerate the derived HTML before sharing; parity failure blocks all v2 visibility/readiness gates. |
| EC-008 | Initiative genuinely has no tasks or no validation trace. | Project a concise source-backed absence; parity compares only populated source identifiers and does not invent a task/proof. |

## 11. Constraints and NFRs

- **Provenance:** every material visual block carries existing v2 provenance
  attributes; no coverage sidecar.
- **Accessibility:** real headings, text equivalents for diagrams, visible
  focus, semantic table/equivalent, non-colour state cues, 320/390px,
  no-script and print support.
- **Performance:** inline/local HTML/CSS/SVG only; no remote dependency caused
  by the composition kit.
- **Maintainability:** a small component catalog with selection guidance, not a
  general-purpose UI framework.
- **Compatibility:** preserve v1 historical flow; integrate with 008 reviewer
  calibration and 009 tabs without changing their authority model.

## 12. Risks and controls

| ID | Risk | Signal | Control / owner | Validation |
|---|---|---|---|---|
| R-001 | Detail becomes ornamental or hallucinates implementation. | Child diagram lacks source locator/decision. | Depth ladder and reviewer trace; template owner. | V-002, E-004 |
| R-002 | Guidance becomes a rigid checklist. | Sparse/non-software fixture gets empty/technical card. | Omit optional rows; use owned-question only when material; Spec Guardian. | V-003, E-003 |
| R-003 | A visual component becomes a parallel source. | HTML differs from source task/plan. | Correct canonical source and regenerate; reviewer. | V-004, E-004 |
| R-004 | Richness hurts mobile/print/accessibility. | Overflow, hidden detail or colour-only cue. | Semantic equivalent, responsive composition and manual review. | V-005–V-007, M-003/M-004 |
| R-005 | New patterns mix client branding into reusable reasoning. | Palette/logo appears in generic kit. | Explicit dependency boundary with 011. | V-009 |
| R-006 | A scaffold is linked as a completed brief while task/proof sources are populated. | Execution/Validation show generic copy or no source IDs. | FR-013/014 parity guard, visible lifecycle label and reviewer check; release owner. | V-011, V-012, E-005 |

## 13. Dependencies and open questions

| Item | Status | Owner / resolution |
|---|---|---|
| 009 tabbed decision surface | completed; required base | Reuse existing tabs/provenance/fallback; no redesign of tab authority. |
| 008 semantic reviewer calibration | completed; required review model | Extend rubric examples, not deterministic scoring. |
| 011 identity profile | planned, separate | May style components after 010 establishes semantic roles; does not block vendor-neutral composition guidance. |
| Q-001: exact catalog file location | open, non-blocking | T-001 inventories existing template/skill surfaces and selects the smallest coherent home. |
| Q-002: whether current fixtures are enough | open, non-blocking | T-001 identifies minimal rich/sparse/non-software additions; avoid fixture explosion. |

## 14. Decision needed

Approve implementation planning for this vendor-neutral composition kit. The
decision does not authorize template changes until impact, plan, validation,
preliminary tasks and independent coverage review are complete.
