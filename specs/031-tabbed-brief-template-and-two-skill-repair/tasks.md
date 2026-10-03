# Tasks — 031

**Status:** complete — cinco tasks done e evidências aprovadas em D-016
**Last updated:** 2026-10-02
**Spec:** spec.md
**Plan:** plan.md
**Validation plan:** validation-plan.md

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Contrato 3 e mandatos operacionais | OK do owner | high | /root/contract031 | /root | evidence/T-001.md |
| T-002 | done | Template único instruído e compositor | T-001 | high | /root/presentation031 | /root | evidence/T-002.md |
| T-003 | done | Duas skills corretivas high/xhigh | T-002 | high | /root/presentation031; B /root/contract031 | /root | evidence/T-003.md |
| T-004 | done | Integração/estado e compatibilidade dos leitores | T-001/002; aceite após T-003 | high | /root/integration031 | /root | evidence/T-004.md |
| T-005 | done | Aceitação do bundle nos oito casos congelados | T-001..004 | high | A /root/presentation031; B /root/contract031 e /root/repair_offline031 | /root | evidence/T-005.md |

Não implementar produtos mockados, alterar fontes, criar HTML031 ou remover
fisicamente legado. Tarefas do bundle mantêm evidence/evaluator distinto;
isso não cria terceira validação na operação de cada brief.

### T-001 — Contrato 3 e mandatos operacionais

**Objective:** substituir o protocolo do brief para nova geração sem mudar
evidência/autoridade da implementação.
**Requirement IDs:** FR-011, FR-012, FR-015, FR-016, FR-017
**Acceptance criteria IDs:** AC-011, AC-012, AC-014, AC-015, AC-017
**Outcome served:** O-003/O-004
**Increment:** regra única de A→B/conteúdo→B/visual e dispatch por contrato.
**Expected files:** brief-contract.md, AGENTS/agents/workflows, manifest,
.harness/skills/spec-review/SKILL.md e instruções de templates/estado afetadas.
**Scope:** mandatos disjuntos, encerramento/limites, dispensa do modelo no
caminho 3, preservação dos gates de produto.
**Out of scope:** mudança de autoria dos MD, códigos de UI ou remoção física.
**Dependencies:** OK do owner e Spec/Plan/Validation Ready.
**Risk:** high. **Assurance:** A2, V-012/014/015/017.
**Builder/Evaluator:** atribuir identidades distintas antes de ready.
**Evidence:** evidence/T-001.md
**Why now:** evita adicionar novas skills sobre protocolos incompatíveis.

#### Exit criteria

- [x] Contrato 3 tem caminho/autoridade/limites inequívocos.
- [x] Entry points normativos não exigem a cadeia 2 para 3.
- [x] Histórico 1/2 e aprovação de tasks de implementação permanecem separados.
- [x] Evidência e decisão de evaluator distinto registradas.

### T-002 — Template único instruído e compositor

**Objective:** obter HTML inicial rico com casca padrão e abas portáteis.
**Requirement IDs:** FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008
**Acceptance criteria IDs:** AC-002, AC-003, AC-004, AC-005, AC-007, AC-008, AC-016
**Outcome served:** O-001/O-002/O-005
**Increment:** template com oito abas, instruções de slot e autoria direta.
**Expected files:** stakeholder-brief.html/design.md,
executive-brief-composition/SKILL.md e testes comportamentais de casca.
**Scope:** identidade/títulos/header, CSS tabs/teclado, SVG/cards/tabelas,
HTML autossuficiente, preenchimento das fontes e N/A.
**Out of scope:** renderer Markdown, alteração de marca/source, implementações
dos produtos e HTML031.
**Dependencies:** T-001 done.
**Risk:** high. **Assurance:** A2, V-002..008/016; browser/DOM e leitura.
**Builder/Evaluator:** atribuir identidades distintas.
**Evidence:** evidence/T-002.md
**Why now:** as duas skills precisam de estrutura estável para corrigir.

#### Exit criteria

- [x] Um HTML com oito abas/IDs únicos e um painel por vez, também sem JS.
- [x] Slots descrevem fonte, fato e representação; nenhum scaffold na entrega.
- [x] Identidade, SVG e leitura desktop/mobile demonstrados.
- [x] Compositor entrega diretamente a B sem modelo/review obrigatório.
- [x] Evidence pack com evaluator distinto.

### T-003 — Duas skills corretivas high/xhigh

**Objective:** corrigir conteúdo e experiência no próprio HTML, sem loop
de aprovação.
**Requirement IDs:** FR-001, FR-009, FR-010, FR-011, FR-012, FR-013, FR-014
**Acceptance criteria IDs:** AC-001, AC-009, AC-010, AC-011, AC-012, AC-013
**Outcome served:** O-001/O-003/O-004
**Increment:** duas skills ajustadas completam ensaios de omissão e visual.
**Expected files:** rendered-brief-decision-review/SKILL.md,
executive-brief-experience-review/SKILL.md; invocação/metadata existentes
quando efetivamente necessários para confirmar esforço.
**Scope:** comparação/materialidade/reparo, visual/explicação, esforço efetivo,
mesmo B distinto de A, limites finais sem re-review.
**Out of scope:** instalação global, source repair, reescrita de aprovação.
**Dependencies:** T-002 done.
**Risk:** high. **Assurance:** A2, V-001/009..013; ensaios comportamentais.
**Builder/Evaluator:** atribuir identidades distintas; avaliar a mudança da
skill, não fingir que B é evaluator das próprias edições.
**Evidence:** evidence/T-003.md
**Why now:** concretiza a simplificação que resolve o retrabalho observado.

#### Exit criteria

- [x] Primeira skill detecta/corrige fato disponível retirado do HTML.
- [x] Segunda corrige apresentação sem cortar fatos.
- [x] Ambas executam com high/xhigh efetivo; caso medium é tratado honestamente.
- [x] Fontes intactas, sem aprovação/intermediário/terceira validação.
- [x] Evidence pack com evaluator distinto.

### T-004 — Integração/estado e compatibilidade dos leitores

**Objective:** permitir uso real do novo fluxo sem exigências residuais 2.
**Requirement IDs:** FR-003, FR-012, FR-014, FR-015, FR-016, FR-017
**Acceptance criteria IDs:** AC-002, AC-012, AC-013, AC-014, AC-015, AC-017
**Outcome served:** O-003/O-004
**Increment:** entrypoint documentado despacha por versão e termina com relato
verdadeiro; promotor/leitores não exigem reviews que deixaram de existir.
**Expected files:** render_stakeholder_brief.py,
validate_human_visibility.py, validate_bundle.py, manifest.yaml,
templates/README.md e estado/compatibility docs afetados.
**Scope:** integrar mandatos novos; preservar checks mecânicos proporcionais,
históricos 1/2, estado e relato, sem novo agente semântico.
**Out of scope:** remover schema/projetor antigo, limpar working tree,
regenerar históricos ou mexer em sources.
**Dependencies:** implementação após T-001/T-002 done e interfaces estáveis;
aceite após T-003 done (D-013). Paralelismo não dispensa integração/regressão.
**Risk:** high. **Assurance:** A2, V-012..015/017 e regressão afetada.
**Builder/Evaluator:** atribuir identidades distintas.
**Evidence:** evidence/T-004.md
**Why now:** sem integração, a nova skill continuaria presa à cadeia antiga.

#### Exit criteria

- [x] Fluxo 3 usa apenas autoria/conteúdo/visual antes do relato.
- [x] Estado/relato não autoriza tasks nem falsifica approve.
- [x] Leitura e hashes 1/2 preservados.
- [x] Regressão do bundle e standalone afetados passam ou têm disposição aceita.
- [x] Evidence pack com evaluator distinto.

### T-005 — Aceitação nos oito mocks congelados

**Objective:** demonstrar recuperabilidade dos fatos e experiência do novo
caminho em domínios variados, sem questionar os MD.
**Requirement IDs:** FR-001..017
**Acceptance criteria IDs:** AC-001..017
**Outcome served:** O-001..005
**Increment:** oito briefs novos pelo fluxo completo, matriz factual e provas.
**Expected files:** apenas nova raiz em testes/mock-runs/ e evidence/T-005.md;
não sobrescrever qualquer fixture/revisão histórica.
**Scope:** fontes copiadas/hash, A+B high/xhigh, comparar fatos da matriz,
browser com/sem JS/mobile/print e limites; medir custos se observáveis.
**Out of scope:** corrigir fontes, executar aplicação, criar HTML031,
deduzir percentual de economia ou introduzir terceira skill por geração.
**Dependencies:** T-001..004 done.
**Risk:** high. **Assurance:** A2, V-001..017; evaluator distinto aceita a
mudança do bundle uma vez. Seu aceite não entra na operação futura do brief.
**Builder/Evaluator:** atribuir identidades distintas.
**Evidence:** evidence/T-005.md
**Why now:** mede o outcome real, em vez de concluir por schema/código verde.

#### Exit criteria

- [x] Oito casos executados com fontes intactas e limites de fonte separados.
- [x] Fatos materiais existentes recuperáveis, sem distorções/invenções.
- [x] Navegação/diagramas/explicação demonstrados; relato e esforço reais.
- [x] Nenhuma implementação de produto ou autoridade fabricada.
- [x] Aceitação independente da mudança/evidence registrada.

## Execution boundary

Tasks Ready = true após OK humano D-010 e snapshot preimplementação; task done ainda exige evidence/evaluator distinto. A dispensa de
HTML031 vem de D-002; não obriga gerar um brief só para aprovar planejamento.
