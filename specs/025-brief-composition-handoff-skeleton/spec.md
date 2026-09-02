# SPEC 025 — Handoff de composição e esqueleto do stakeholder brief

**Status:** spec ready; implementação ainda não autorizada pelo lifecycle.  
**Owner:** Guardian maintainers + brief experience owner.  
**Created / updated:** 2026-09-01.  
**Risk / assurance:** high / A2-elevated.  
**Origin:** auditoria solicitada pelo requester após identificar que o M-003
visual omitiu tasks, provas e impactos existentes nos Markdown.

## 1. Problema

O fluxo v2 já determina fontes canônicas, composição de cobertura, revisão
distinta, candidate, render e revisão pós-render. Também existe um shell de
oito domínios. Entretanto, a composição vive como tabela livre em `plan.md` e
o candidate é escrito manualmente fora de um handoff operacional. Não há uma
instância de esqueleto por iniciativa que converta, de modo visível, cada fato
material planejado em bloco ainda a preencher.

O caminho paralelo de laboratório
`build_spec024_heterogeneous_references.py` transformou campos curtos em
cartões visuais sem ler `tasks.md`, `validation-plan.md` ou `impact-map.md`.
No M-003, cinco tasks e sete provas canônicas não se tornaram conteúdo de
Execução/Validação. O laboratório permanece evidência histórica; não é entrega
canônica e não será promovido.

## 2. Objetivo

Fazer com que toda nova composição v2 percorra um único handoff explícito:
Markdown canônico → plano editorial revisado no `plan.md` → candidate-esqueleto
por iniciativa → candidate composto e atestado → promoção guardada → revisão
renderizada independente → `stakeholder-brief.html` e decisão de reunião.

## 3. Resultado de entrega

- **Resultado para o usuário:** cada brief final permite recuperar decisão,
  impacto, tasks, provas, estado e limites sem uma caça aos Markdown.
- **Incremento demonstrável:** um M-003 descartável recomposto por essa cadeia
  contém os cinco contratos de task e os sete caminhos de validação, além da
  arquitetura e impacto fonte-apoiados.
- **Fronteira do slice:** processo e ferramentas do bundle; não migra ou
  sobrescreve briefs históricos, candidates T-004 ou referências SPEC 024.
- **Fonte de prioridade:** solicitação humana explícita em 2026-09-01.

## 4. Pessoas e decisões atendidas

| Pessoa | Precisa decidir / entender | Resposta esperada |
|---|---|---|
| Compositor do brief | O que precisa ser transposto sem inventar fatos. | Plano por rota/bloco, locator e ausência tratada. |
| Revisor distinto | Se uma fonte material se perdeu antes do render. | Mapa revisável, candidate e pergunta de recuperação. |
| Decisor executivo | Como a entrega avança, é provada e é controlada. | Tasks, impactos, evidências, limites e próxima decisão legíveis. |
| Mantenedor Guardian | Qual é o único caminho de entrega. | Laboratório separado; fluxo canônico sem renderer concorrente. |

## 5. Resultados observáveis

- **O-025-01:** `plan.md` contém plano editorial por domínio e bloco: pergunta
  de decisão, fonte/locator, fato recuperável, forma, destino HTML e estado.
- **O-025-02:** candidate-esqueleto contém todas as oito rotas e um slot para
  cada item material; ele não pode ser promovido nem apresentado como final.
- **O-025-03:** candidate composto só passa quando cada slot material está
  preenchido ou tem ausência fonte-apoiada; tasks e provas aparecem nos
  domínios corretos.
- **O-025-04:** revisão independente julga utilidade, profundidade,
  proporcionalidade, clareza visual e fidelidade factual, sem score de prosa.
- **O-025-05:** o gerador SPEC 024 fica explicitamente fora do caminho de
  entrega e não ganha responsabilidade de renderer canônico.
- **O-025-06:** o plano editorial e o esqueleto passam a comprometer, antes do
  preenchimento factual, a narrativa executiva, os elementos visuais e as
  relações recuperáveis de cada rota. Esse contrato funciona para qualquer
  domínio de SPEC; ele não toma M-003, software ou uma arquitetura específica
  como modelo implícito.
- **O-025-07:** o candidate composto parte de uma cópia rastreável do
  skeleton, em vez de usar o skeleton apenas como uma referência estética. A
  visão arquitetural pode representar a solução inteira, uma operação, uma
  política ou outra paisagem fonte-apoiada; quando houver relação material,
  ela separa o panorama de mudança do fluxo de informação, uso ou controle.

## 6. Não objetivos

- Gerar narrativa, diagramas, decisões ou arquitetura automaticamente a partir
  de Markdown por heurística, LLM ou Python.
- Criar segunda fonte de verdade (`brief-plan.md`, JSON, banco ou sidecar)
  paralela ao `plan.md` e às fontes canônicas.
- Obrigar diagrama, quota de cartões ou layout único; profundidade continua
  proporcional às fontes.
- Reescrever automaticamente HTMLs de laboratório ou históricos.

## 7. Requisitos funcionais

| ID | Requisito | Razão |
|---|---|---|
| FR-025-01 | O plano de cobertura em `plan.md` SHALL evoluir para plano editorial por rota e bloco, sem sidecar. | Dá ao compositor um handoff concreto. |
| FR-025-02 | O plano SHALL declarar pergunta, locator, fato/ausência, forma visual, alvo HTML, disposição de cobertura canônica e estado de handoff separado para cada item material. | Evita perda em síntese genérica sem mudar o contrato v2. |
| FR-025-03 | O bundle SHALL criar em `brief-candidates/stakeholder-brief.skeleton.html` um esqueleto por iniciativa, com oito rotas, slots fonte-apoiados, `data-harness-template-kind="skeleton"`, `data-brief-phase="skeleton"` e `a preencher`. | Torna a promessa de cobertura visível antes da redação. |
| FR-025-04 | O esqueleto SHALL ficar fora de `stakeholder-brief.html`, conservar `run-state.brief_phase: not_rendered`, nunca ser passado ao renderer e ser recusado se tentarem promovê-lo. O candidate preenchido muda para `brief-candidates/stakeholder-brief.candidate.html`, `data-harness-template-kind="composed"` e `data-brief-phase="authored"`. | Não confunde casca com final e respeita o lifecycle existente. |
| FR-025-05 | Compositor preenche o candidate com fatos/ausências do plano; revisor distinto revisa mapa antes do esqueleto, atesta o hash do candidate exato antes da promoção e revisa a experiência do HTML já renderizado depois da promoção. | Mantém autoria agêntica e revisão independente. |
| FR-025-06 | Checks determinísticos SHALL conferir links, slots, proveniência, task IDs e AC/provas, não qualidade narrativa/estética/materialidade. | Controle mínimo sem substituir julgamento. |
| FR-025-09 | Uma composição v3 MAY continuar com um achado editorial determinístico somente quando a exceção está visível no candidate, é ligada à revisão pré-render exata (SHA-256 + manifesto), identifica achado/origem/alvo/impacto/risco/owner/decisão/prazo/próxima ação e ainda está vigente. Integridade, segurança, proveniência, lifecycle, identidade do skeleton e revisão exata continuam bloqueantes. | Uma omissão explícita vira dívida decidível; não pode apagar o relatório nem virar bypass silencioso. |
| FR-025-07 | Workflow, papéis e handoffs SHALL declarar a sequência única e separar laboratório de promoção. | Remove ambiguidade e fragmentação. |
| FR-025-08 | Fluxo SHALL manter HTML offline, Pearson quando selecionado, acessibilidade, no-script, impressão e históricos. | Não regride garantias existentes. |
| FR-025-10 | `plan.md` SHALL conter um contrato de construção profunda por rota: pergunta de decisão, arco narrativo, evidência fonte-apoiada, relações a tornar visíveis, forma visual escolhida com razão, público, estado de incerteza e critério de recuperação. Para componentes repetíveis, o plano SHALL declarar o modelo de ficha e a regra de repetição, não somente o nome de um card. | O compositor não pode depender de memória para decidir o que uma topologia, zoom, task ou prova precisa explicar. |
| FR-025-11 | O template canônico SHALL definir o contrato estrutural visual completo; o perfil selecionado SHALL fornecer a identidade e o shell visual correspondente; e o skeleton por iniciativa SHALL declarar que contrato/perfil e materializar os mesmos oito `tabpanel`s, rotas e modelos de componente, com diferenças permitidas somente para identidade selecionada, lifecycle, slots e repetições fonte-apoiadas. Uma rota fica visível por vez; não existe página longa de âncoras. | A forma do resultado fica comprometida antes da redação sem confundir um template neutro com uma identidade de cliente, nem converter estética ou profundidade em score determinístico. |
| FR-025-12 | O composer SHALL criar o candidate como cópia declarada do skeleton da iniciativa e preenchê-lo in situ. A rota Arquitetura SHALL oferecer modelos distintos para (a) panorama contextual da solução/ambiente, com superfícies alteradas, preservadas e fora de escopo visualmente distinguíveis, e (b) fluxo/seqüência da relação material — dados, navegação, uso, decisão, contrato ou controle. O plano escolhe ambos, um deles, ou uma ausência justificada conforme as fontes; nunca uma topologia fixa por default. | O skeleton deixa de ser um exemplo frouxo, enquanto a arquitetura fica rica sem pressupor que toda SPEC descreve software ou o mesmo fluxo. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-025-01 | Plano M-003 associa seis impactos, cinco tasks, sete provas e decisões materiais a rotas/blocos. | V-025-01 |
| AC-025-02 | Esqueleto M-003 contém rotas e slots `a preencher`, fica em `brief-candidates/` com identidade `skeleton` e render/promoção o recusam. | V-025-02 |
| AC-025-03 | Candidate M-003 composto tem T-001–T-005 em Execução e V-01–V-07/AC em Validação, com proveniência/estado verdadeiro. | V-025-03 |
| AC-025-04 | Impacto mostra footprint/controles/owners; Evolução recupera decisões, gates, rollback e riscos. | V-025-04 |
| AC-025-05 | Revisor distinto aprova ou retorna M-003 por perda fonte → decisão prejudicada → correção canônica. | V-025-05 |
| AC-025-06 | Regressões preservam promoção, v1/v2, template, arquitetura visual, no-script, print e Pearson. | V-025-06 |
| AC-025-07 | Laboratório SPEC 024 permanece inalterado e fora da nova cadeia. | V-025-07 |
| AC-025-08 | Um fixture v3 prova que omissão editorial sem ressalva recusa promoção, enquanto a mesma omissão só promove com ressalva visível, exata, não expirada e revisada; nenhum gate de Human Visibility/Tasks Ready é aberto por ela. | V-025-08 |
| AC-025-09 | Um skeleton instanciado mostra, em cada rota, a estrutura final de storytelling e os componentes apropriados ainda como `a preencher`; Arquitetura oferece visão global, pilares e zooms; Execução oferece arco de épicos e dossiês completos de task; Validação oferece pilares, fluxo, dossiês de prova e critérios de aceite. Navegação troca a subpágina inteira. | V-025-09 |
| AC-025-10 | Um candidate de demonstração é derivado do skeleton da própria SPEC 025, declara sua base e apresenta panorama contextual e fluxo arquitetural distintos, escolhidos a partir das fontes. Ele permanece candidate não promovido até atestação e revisão próprias. | V-025-10 |

## 9. Edge cases e falha

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-025-01 | Fonte material sem forma visual decidida. | Slot `a_preencher` bloqueia composição; compositor escolhe forma fonte-apoiada. |
| EC-025-02 | Detalhe de task/prova não existe na fonte. | Omitir opcional ou registrar `not_applicable` com razão; para fato material ausente abrir questão/discovery com owner, impacto e caminho; não inventar. |
| EC-025-03 | Candidate tem placeholder, ID perdido ou fonte sem target. | Check falha antes de promoção e devolve ao compositor. |
| EC-025-04 | Revisor entende conteúdo superficial com checks verdes. | REVISE registra fonte → perda → decisão impedida; fontes/plano corrigidos e candidate recomposto. |
| EC-025-05 | Caso simples/não software. | Profundidade proporcional e ausência justificada, sem forçar card/prova/topologia. |
| EC-025-06 | Uma projeção editorial está incompleta, mas o decisor precisa receber o brief antes da recomposição. | A promoção só pode ocorrer sob ressalva v3 visível e revisada; o próximo agente deve corrigir ou justificar de novo antes do prazo. Nunca há aprovação implícita, bypass de hash/manifesto, nem abertura de Human Visibility/Tasks Ready. |

## 10. Restrições e NFRs

- `render_stakeholder_brief.py` continua promotor seguro, não autor semântico.
- Markdown e decisões canônicos continuam fonte de verdade; candidate/esqueleto
  são derivados e revisáveis.
- Slots/estados têm texto visível; saída preserva navegação, no-script e print.
- Scripts novos têm fixtures positivas/negativas e não alteram históricos.

## 11. Riscos e dependências

| ID | Risco | Prob. | Impacto | Mitigação / owner |
|---|---|---|---|---|
| R-025-01 | Novo arquivo vira segunda fonte de verdade. | média | alta | Plano segue no `plan.md`; compositor só aponta fontes. |
| R-025-02 | Determinismo vira julgamento de prosa. | média | alta | Checks só em slots/IDs/proveniência; reviewer decide suficiência. |
| R-025-03 | Esqueleto é apresentado como entrega. | média | alta | Marker explícito, renderer recusa e workflow nomeia estado. |
| R-025-04 | Duplicação com SPEC 010/023/024. | média | média | Evoluir contratos existentes; laboratório fica externo. |

| Dependência | Estado | Owner | Bloqueia? |
|---|---|---|---|
| Contratos v2, kit SPEC 010 e subpáginas SPEC 023 | existente | Guardian maintainers | não |
| Fontes M-003 descartáveis e corpus SPEC 024 preservado | existente | mock-lab maintainer | não |
| Revisão independente da SPEC e do piloto | requerida | executive brief reviewer | sim |

## 12. Decisão do Spec Guardian

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** `/root/spec025_independent_review`  
**Reviewed at:** 2026-09-01  
**Blocking issues:** nenhum; a execução continua dependente dos gates v2.  
**Decision evidence/link:** auditoria M-003 de 2026-09-01; SPECs 010, 023,
024, workflow e templates canônicos.
