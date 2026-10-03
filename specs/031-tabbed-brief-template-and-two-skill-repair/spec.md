# SPEC 031 — Template de brief com abas e duas skills de correção

**Status:** complete — T-001..005 done; evidências aprovadas por /root em D-016
**Sequence:** 031
**Slug:** tabbed-brief-template-and-two-skill-repair
**Owner:** Guardian maintainers / owner do bundle
**Created:** 2026-10-02
**Last updated:** 2026-10-02
**Risk:** high — mudança do contrato público de composição/revisão
**Assurance profile:** A2-elevated
**Antecedentes:** 029 implementada localmente; substitui a proposta draft 030.

> Planejamento entregue em Markdown e estado YAML, sem HTML desta iniciativa.
> O owner dispensou HTML031. O OK posterior foi recebido em
> D-010; execução integral autorizada, preservando os limites desta spec.

## 1. Problema

A execução testes/mock-runs/20261002-brief-quality-check/ aceitou o schema e
gerou HTML reproduzível para oito modelos minimal existentes. Os oito
receberam pedido de revisão como briefs completos. A execução não refez
autoria e não prova que todo modelo possível falhe.

Os achados materiais para este escopo são:

- o modelo intermediário seleciona pouco e omite fatos já presentes nos MD,
  incluindo arquitetura, tasks, validação, riscos, estado e fronteiras;
- coverage e tab-coverage duplicados deixam cobertura permanentemente visível;
- a tabela automática lista blocos emitidos, não tudo que deveria estar ali;
- modelo e HTML podem ficar obsoletos após mudança dos MD, como T-010/gates
  da 029; nesse caso a recusa de regeneração foi uma proteção correta.

O owner escolheu simplificar a parte de HTML e assumir os Markdown corretos.
Esta iniciativa não reabre sua metodologia de autoria nem amplia o escopo
por fraquezas nos mocks.

## 2. Objetivo

Entregar um brief rico, objetivo e visualmente explicativo em um único HTML
com abas, preenchido a partir dos Markdown existentes e finalizado por duas
skills corretivas sequenciais, sem reaprovações e sem terceira validação.

## 3. Delivery outcome

- **Product/user outcome:** stakeholder recupera transformação, benefício,
  escopo, arquitetura, impactos, execução, prova e decisão no próprio HTML.
- **Benefício concreto esperado:** menos omissões e retrabalho de composição,
  sem duplicar narrativa em modelo editorial e sem fila de reviews repetidos.
- **Demonstrable increment:** os oito casos são concluídos pelo mesmo template
  e pelas mesmas duas skills; fatos materiais de aceite recuperáveis, fontes
  imutáveis e navegação sem empilhar todas as abas.
- **MVP/slice boundary:** template, compositor, duas skills e adaptação dos
  entrypoints/contratos que ainda exigem a cadeia antiga.
- **Priority source:** pedido direto do owner nesta conversa em 2026-10-02.
- **Medição:** fatos esperados versus HTML; integridade das fontes; três etapas
  operacionais; esforço efetivo e comportamento no navegador. Tempo/tokens
  somente com medição real, sem percentual contra baseline não medida.

## 4. Users or actors

| Ator | Papel |
|---|---|
| Stakeholder / owner | Entender benefício, decisão e limites; autorizar implementação quando aplicável. |
| A — compositor | Ler fontes e preencher o template HTML, sem aprovar sua entrega. |
| B — reparador | Distinto de A; executar conteúdo e depois visual no mesmo HTML, com esforço alto/muito alto. |
| Orquestrador | Encadear A → B/conteúdo → B/visual → relato, sem nova revisão. |
| Builder/evaluator de implementação | Mantêm regras de tasks/evidence; gerar brief não executa o produto. |

## 5. Observable outcomes

- **O-001:** fato material selecionado das fontes é recuperável no HTML; ausência
  realmente na fonte aparece como limitação, não como fato inventado.
- **O-002:** somente um painel principal visível por vez, também sem JS.
- **O-003:** autoria, correção de conteúdo e correção visual são as únicas
  etapas do caminho normal; não há modelo editorial/reaprovação obrigatória.
- **O-004:** nenhum reparo de HTML altera as fontes Markdown.
- **O-005:** benefício e critério mensurável, limites e autoridade da spec estão
  visíveis tal como declarados na fonte.

## 6. Non-goals

- **NG-001:** questionar/corrigir/regenerar MD ou redesenhar autoria de spec,
  plan e tasks, inclusive para melhorar os mocks.
- **NG-002:** implementar produtos fictícios, autorizar tasks por gerar HTML,
  retirar evidence/evaluation de implementação ou substituir o owner.
- **NG-003:** implementar a transposição literal da 030 ou um renderer Markdown
  genérico. A nova autoria é agêntica sobre template.
- **NG-004:** obrigar brief-model.yaml, mapa editorial paralelo ou review
  pré-render; nenhuma nova fonte de narrativa compete com os MD.
- **NG-005:** reescrever históricos, apagar em massa legado, mudar marca do
  consumidor ou instalar skills globais.
- **NG-006:** deploy, vários arquivos/páginas por brief ou HTML da própria 031
  sem novo pedido explícito.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | O fluxo SHALL tratar os MD canônicos como autoridade de conteúdo e manter seus bytes inalterados. | Escopo escolhido pelo owner. |
| FR-002 | A SHALL preencher diretamente .harness/templates/stakeholder-brief.html, preservando identidade visual, estrutura e componentes. | Evitar reconstrução da casca e modelo narrativo duplicado. |
| FR-003 | A entrega SHALL ser um único stakeholder-brief.html autossuficiente: CSS, navegação e SVG inline, sem rede/arquivo auxiliar para exibir o brief. | Portabilidade offline. |
| FR-004 | O template SHALL conter as oito abas de §7.1, com um painel principal ativo por vez em tela, inclusive sem JS. | Evitar página contínua gigantesca; impressão pode reunir todas. |
| FR-005 | Cabeçalho/valor SHALL recuperar identidade, problema, objetivo de negócio, beneficiários, transformação, benefício/métrica/critério de sucesso, escopo e anti-escopo da fonte. | Spec deve trazer benefício concreto. |
| FR-006 | Cada slot SHALL instruir fonte, pergunta, campos materiais e representação adequada, não apenas dar nome ao bloco. | Placeholders efetivamente preenchíveis pelo agente. |
| FR-007 | Arquitetura material SHALL ter SVG inline conectado e equivalente textual, distinguindo preservado/mudança, relações, contratos/dados e limites/falhas declarados. | Diagrama que explica; não lista decorativa/setas de texto. |
| FR-008 | Cards, tabelas e detalhes recolhíveis SHALL preservar campos/contratos materiais em linguagem objetiva, com densidade proporcional. | Riqueza sem parede de texto/card vazio. |
| FR-009 | B SHALL comparar HTML com fontes aplicáveis e blocos exigidos, localizar omissões/contradições/invenções e corrigi-las diretamente no mesmo HTML, na primeira skill. | Recuperação do que já está no MD. |
| FR-010 | O mesmo B SHALL abrir todas as abas e corrigir explicação visual, SVG, cards, títulos, concisão e navegação, na segunda skill. | Finalizar experiência sem devolver rotina a A. |
| FR-011 | B SHALL usar high ou xhigh, ou esforço superior explicitamente suportado, em ambas as skills, registrando identidade e esforço efetivo. Medium não é permitido. | Exigência do owner. |
| FR-012 | Depois das duas skills SHALL haver somente relato de correções/limites; não SHALL haver terceira validação, reaprovação nem nova execução obrigatória da skill anterior. | Simplificação expressa; inspeção enquanto se corrige integra a própria skill. |
| FR-013 | Ausência realmente na fonte SHALL aparecer como limite/N/A fundamentado, sem inventar métrica, relação, owner, aprovação ou decisão e sem corrigir MD. | Confiança dentro do escopo. |
| FR-014 | A aba de fontes SHALL rastrear arquivo/heading → fato material → aba/bloco e expor omissões; não SHALL declarar cobertura por listar somente blocos emitidos. | Comparação honesta com o que deveria estar presente. |
| FR-015 | O relato final SHALL registrar autoria, duas passagens, esforço, fatos recuperados e limites; não SHALL aprovar tasks/evidence nem fabricar independência sobre bytes que B editou. | Conclusão de reparo não é aprovação de implementação. |
| FR-016 | O novo caminho SHALL declarar data-brief-contract="3"; leitura de históricos 1/2 SHALL permanecer sem regeneração ou gates 3 impostos silenciosamente. | Migração explícita do contrato público. |
| FR-017 | O fluxo SHALL reaproveitar as três skills de §7.2 e substituir os mandatos antigos no caminho 3, preservando utilitários técnicos proporcionais. | Não somar duas skills à cadeia antiga. |

### 7.1 Template mínimo e fontes dos slots

Abas não desaparecem por perfil minimal. Campo material não fica vazio.
Bloco não material traz motivo curto; falta real na fonte é limite explícito.

| Aba / ID | Preenchimento obrigatório quando consta na fonte | Fontes / forma |
|---|---|---|
| Visão e valor / scope | O que é, problema, objetivo, benefício/como observar, atores, escopo/anti-escopo, requisitos/restrições materiais. | spec.md; síntese curta + detalhes recuperáveis, sem baseline inventada. |
| Arquitetura / architecture | Atual → alvo → delta, responsabilidades, relações/contratos/dados, limites, fluxo, o que muda/preserva. | plan.md e impact-map.md; SVG + texto/legenda. |
| Impactos e riscos / impact | Superfícies, mudança/exposição; risco → sinal → controle → contingência → owner; rollback aplicável. | impact-map.md e plan.md; footprint/cards/matriz. |
| Execução / execution | Incrementos, tasks, ordem/dependências, status/autoridade, risco, exit/evidência. | tasks.md e estado disponível; cards/ledger, detalhes recolhíveis. |
| Validação / validation | AC → método/comando ou passos → ambiente/fixture → oracle → evidência; limite da prova. | validation-plan.md + ACs de spec.md; matriz/proof cards, sem executar produto. |
| Decisões e evolução / evolution | Decisões, alternativas, consequências, evolução/ratchet materiais, propagação. | decision-log.md, progress.md, ratchet.md se material; timeline/registro. |
| Estado e próximo passo / decision | Pronto/pendente, autorização, decisão solicitada, responsável, consequência, próximo passo exato. | MD + run-state.yaml como metadado; estado verdadeiro. |
| Fontes e cobertura / coverage | Fonte/heading → fato material → aba/bloco; N/A/limites e fatos ainda ausentes. | Inventário lido pela skill; tabela no HTML, não sidecar editorial. |

MD são autoridade semântica; run-state.yaml somente informa metadados.
Conflito entre fontes é exposto, sem o reparador decidir que aprovação ocorreu.
Quando não há relação arquitetural na fonte, registrar N/A/limite; não
fabricar SVG para cumprir aparência.

### 7.2 Skills que serão ajustadas

| Skill existente | Novo mandato |
|---|---|
| .harness/skills/executive-brief-composition/SKILL.md | A: preencher template diretamente; handoff a B. |
| .harness/skills/rendered-brief-decision-review/SKILL.md | B/1: conferência e correção HTML versus fontes; deixa de apenas devolver REVISE. |
| .harness/skills/executive-brief-experience-review/SKILL.md | B/2: conferência e correção visual/explicativa do HTML; deixa de revisar modelo pré-render. |

Atualizar descriptions de descoberta para o novo mandato; manter paths
estáveis quando útil. Não instalar versões globais paralelas.

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Bytes das fontes canônicas dos oito casos permanecem iguais antes/depois. | V-001 |
| AC-002 | Cada caso entrega um único HTML exibível sem rede/arquivos auxiliares. | V-002 |
| AC-003 | Cada HTML tem oito abas, IDs únicos e um painel principal visível em tela. | V-003 |
| AC-004 | Troca de abas sem JS funciona sem empilhar todos os painéis como padrão. | V-004 |
| AC-005 | Objetivo, beneficiário e benefício/critério mensurável existente na fonte ficam recuperáveis, sem métrica acrescentada. | V-005 |
| AC-006 | Nenhum fato material definido na matriz dos oito mocks de validation-plan.md fica omitido, contraditório ou apenas linkado. | V-006 |
| AC-007 | Arquitetura material dos oito casos tem SVG conectado e texto equivalente preservando fronteiras da fonte. | V-007 |
| AC-008 | Nenhum placeholder editorial/campo material vazio sobrevive na entrega; ausência real é qualificada. | V-008 |
| AC-009 | HTML incompleto recebe correção de conteúdo pela primeira skill na mesma passagem. | V-009 |
| AC-010 | HTML mal apresentado recebe correção visual/explicativa pela segunda skill no mesmo arquivo. | V-010 |
| AC-011 | Há prova do esforço efetivo high/xhigh ou superior em ambas as skills; medium não conclui o fluxo. | V-011 |
| AC-012 | Traço normal: autoria → conteúdo → visual → relato, sem modelo/review pré-render/terceira validação obrigatórios. | V-012 |
| AC-013 | Aba de fontes rastreia fatos esperados e distingue ausência da fonte de omissão do HTML. | V-013 |
| AC-014 | Relato não concede autorização nem aprova tasks/evidence de implementação. | V-014 |
| AC-015 | Históricos 1/2 conservam bytes e leitura; apenas nova geração/migração explícita usa 3. | V-015 |
| AC-016 | Desktop e 390px têm navegação operável, sem overflow horizontal do documento nem header ocupando sozinho a primeira tela. | V-016 |
| AC-017 | Os mandatos novos substituem os antigos nos entrypoints, sem dupla execução. | V-017 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Métrica/arquitetura não consta na fonte. | Limite específico/N/A; não inventar nem reescrever MD. |
| EC-002 | HTML contradiz fato disponível. | B corrige HTML sem devolução/approval rotineiro. |
| EC-003 | MD e estado divergem. | Expor conflito/autoridade não resolvida, preservar fontes. |
| EC-004 | High/xhigh indisponível ou não confirmado pelo executor. | Relatar impedimento, não degradar para medium nem declarar conclusão qualificada. |
| EC-005 | Fonte longa ou muitas tasks. | Síntese fiel + detalhes dentro da aba, material recuperável. |
| EC-006 | Ajuste visual cortou informação. | Restaurar exposição durante a própria skill visual, sem novo gate. |
| EC-007 | Correção precisa de decisão/fato inexistente. | Registrar ponto exato e limite; não ampliar à autoria de MD. |
| EC-008 | Fonte muda durante composição. | Não declarar snapshot sincronizado; finalizar como interrompido até fonte estabilizada. |

## 10. Constraints and non-functional requirements

- Bundle reutilizável em vendor/sdd-harness-guardian; estado no consumidor,
  sem servidor/engine de workflow nova.
- Preservar identidade/tokens navy/violet/lavender e componentes do template;
  não obrigar marca não selecionada; fontes de sistema e gráficos inline.
- Linguagem objetiva, títulos legíveis, cards para unidades comparáveis,
  tabelas para matrizes e detalhe progressivo. Não usar quotas/scoring de
  palavras/cards como qualidade.
- Abas sem JS, teclado/foco, impressão e desktop/mobile. Scroll dentro da
  aba é aceitável; todas empilhadas em tela não é o padrão.
- Não executar conteúdo ativo copiado de MD, carregar recurso remoto ou
  inventar aprovação. JS inline é opcional para navegação.
- Duas skills operam como reparadores. A aceitação independente do bundle
  nesta implementação não se converte em terceira etapa por brief.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| As fontes existentes são a base correta; seus defeitos não serão remediados aqui. | Pedido do owner / D-001. |
| Agente distinto com esforço high/xhigh pode executar ambas as skills. | Configuração efetiva do executor; EC-004. |
| Identidade do template é aproveitável, mas slots/navegação precisam mudar. | Inspeção local e laboratório; maintainers. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Autoria direta repete perda de resumo livre. | média | alto | Slots com fonte + recuperação na primeira skill — Guardian maintainers |
| R-002 | Duas correções viram múltiplas aprovações. | alta | alto | FR-012/AC-012 delimitam traço — Guardian maintainers |
| R-003 | B edita e se apresenta como evaluator independente. | média | alto | Mandato reparador; sem approve próprio — Guardian maintainers |
| R-004 | Gates 3 quebram histórico 1/2. | média | alto | Dispatch por contrato, snapshots antigos — Guardian maintainers |
| R-005 | Fonte ausente/conflitante contamina avaliação do HTML. | média | médio | Separar ausência de omissão e não alterar fonte — Owner |
| R-006 | Executor sem esforço/browser necessário. | média | médio | Limite explícito, nenhuma prova fictícia — Executor |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Template/skills/workflows locais | Implementados e aceitos em T-001..004; oito casos pendentes T-005. | Maintainers do bundle | Aceitação final depende de T-005. |
| Oito pacotes MD | Em testes/mock-runs/20260921-spec029-t009-m00N/initiative/. | Mock lab | Não; read-only. |
| Laboratório de 02/10 | Preservado em diretório ignorado; achados resumidos aqui. | Mock lab | Não. |
| Revisão independente do planejamento | Approve em 2026-10-02; evidence/planning-review.md. | /root/review_spec031, esforço high | Satisfeita para planejamento. |
| OK para desenvolvimento | Concedido em D-010, 2026-10-02. | Owner | Satisfeita. |

## 14. Validation notes

validation-plan.md avalia uma vez a implementação do bundle, com fontes
congeladas e defeitos injetados. Isso não cria etapa extra depois das skills
na operação futura.

## 15. Spec Guardian decision

**Outcome Ready:** yes
**Spec Ready:** yes
**Reviewer:** /root/review_spec031 — independente da autoria, esforço high
**Reviewed at:** 2026-10-02
**Blocking issues:** nenhum para planejamento; execução autorizada em D-010
**Required revisions:** nenhuma; duas sugestões de precisão incorporadas
**Decision evidence/link:** evidence/planning-review.md; D-002 dispensa HTML031.
