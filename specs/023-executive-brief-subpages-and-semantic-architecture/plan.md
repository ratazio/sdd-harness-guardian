# Technical plan — SPEC 023

## Estratégia

1. **Fixar a intenção visual primeiro.** Registrar M-023-A/B/C, obter a
   decisão visual do requester e traduzir somente o feedback aprovado em
   requisitos/tarefas. Nenhum mock é HTML, fonte de verdade ou evidência de
   acessibilidade.
2. **Definir um contrato de rota interna.** Um único HTML terá rotas de domínio
   completas, estado de URL/histórico e troca da região principal. Navegação,
   foco, no-script, print e reduced motion são parte do contrato, não polimento
   posterior.
3. **Introduzir o mapa editorial humano/agêntico.** Antes da composição, um
   agente compositor lê pedido + fontes e propõe para cada rota a pergunta,
   tese, pilares, visual necessário, locators, limitações e próximo passo. Um
   revisor independente lê o mesmo corpus e o candidato; ele pode exigir
   revisão, mas não é substituído por checklist de palavras/contagens.
4. **Modelar arquitetura por relação declarada.** O candidato usa uma lista de
   superfícies fonte-apoiadas, relações e estados de mudança; a representação
   é escolhida pelo caso. O registro explica a unidade de cada quantidade e o
   zoom abre apenas o subsistema que a fonte descreve.
5. **Aplicar o Pearson como sistema.** Reutilizar a referência/ativo local da
   SPEC 014, tokens, tipos, grades e componentes de produto. A nova composição
   não injeta uma segunda base CSS nem carrega recursos remotos.
6. **Provar em corpus diverso.** Testes de contrato cuidam de integridade e
   comportamento; uma revisão de renderização e cinco lentes semânticas avaliam
   clareza, fidelidade visual e limites em M-001–M-008 de raiz nova.

## Decisões de desenho

| ID | Decisão | Consequência |
|---|---|---|
| D-023-01 | “Subpágina” significa rota interna com região principal inteira substituída, não âncora nem painel parcial. | Persistem somente moldura institucional e navegação; cada rota reinicia sua narrativa. |
| D-023-02 | O HTML continua único e progressivo. | Hash/histórico suportam compartilhamento; fallback linear é intencional. |
| D-023-03 | Mapa editorial é instrumento de composição/review, não fonte canônica paralela. | Todo fato visível aponta para fontes; o mapa pode registrar síntese, lacuna e escolha visual. |
| D-023-04 | Arquitetura é condicional à materialidade fonte-apoiada. | Não há diagrama mínimo obrigatório; quando aplicável, macro + superfície + zoom formam uma conversa conectada. |
| D-023-05 | Escala mede unidades declaradas pela própria composição. | Não há proxy de LOC, contagem por parser ou zero para ausência. |
| D-023-06 | A identidade Pearson é base de produto/editorial, não decoração. | Cabeçalho, tipografia, canvas, cartões, CTA, estado e acessibilidade seguem o guia local. |

## Topologia conceitual a implementar somente quando fontes a suportarem

```text
Pessoa / operação
        │ intenção, decisão ou handoff
        ▼
Contexto preservado ── relação material ── Superfície alterada
                                             │ contrato / evento / dado
                                             ▼
                                      Controle ou dependência

Zoom: Superfície alterada
  ponto interno alterado ── contrato ── ponto preservado
```

O desenho não é uma taxonomia. Os rótulos, número de superfícies, relação e
zoom vêm do mapa editorial/fonte. `Preservado`, `fora de escopo` e `desconhecido`
precisam ser semanticamente diferentes e visíveis também sem cor.

## Sequência de implementação após D-023-001

1. Criar fixtures positivas/negativas e o formato de mapa editorial.
2. Implementar rota interna e shell Pearson, preservando contratos v2.
3. Implementar projeções de narrativa, topologia, change map e zoom; adicionar
   revisão semântica/visual distinta.
4. Recompôr M-001–M-008, validar browser e conduzir a revisão humana antes de
   qualquer baseline ou migração.

## Limites de mudança previstos

| Área do bundle | Tipo de alteração prevista | Não alterar sem decisão posterior |
|---|---|---|
| `.harness/templates/` | Shell, orientação de composição e contrato de rota. | Fatos das iniciativas consumidoras. |
| `scripts/` | Validação estrutural/comportamental e suporte ao mapa editorial. | Decisão automática de suficiência. |
| `scripts/fixtures/` e `testes/mock-tests/` | Casos fonte-apoiados, positivos e negativos. | Corpus histórico como se fosse dado descartável. |
| `specs/` | Esta SPEC e decisões/evidências futuras. | Briefs renderizados antigos sem refresh. |

## Brief coverage composition (v2)

**Compositor:** `/root/spec023_coverage_author` (Codex).  
**Estado desta composição:** candidato pré-review; não autoriza renderização,
Human Visibility nem tasks. Um revisor distinto deve comparar cada linha com
o corpus antes de `brief_coverage_ready` poder mudar.

| Fonte / heading material | Disposição | Alvo de rota / bloco único | Rationale de composição |
|---|---|---|---|
| `spec.md` — 1 Problema | synthesized | `#overview-problem` | Nomeia a reconstrução mental e a insuficiência arquitetural que a decisão precisa resolver. |
| `spec.md` — 2 Objetivo | synthesized | `#decision-snapshot` | Declara a tese de um único HTML com subpáginas integrais e arquitetura recuperável. |
| `spec.md` — 3 Resultado de entrega | represented | `#overview-outcome` | Torna resultado e incremento demonstrável recuperáveis sem ampliar o slice. |
| `spec.md` — 4 Pessoas e decisões atendidas | represented | `#overview-decision` | Mantém as perguntas dos públicos antes do detalhe técnico. |
| `spec.md` — 5 Resultados observáveis | represented | `#overview-observables` | Amarra a promessa às quatro condições observáveis, sem criar uma métrica artificial. |
| `spec.md` — 6 Não objetivos | represented | `#scope-limit` | Declara a fronteira que a camada não pode fingir, reescrever ou transformar em score. |
| `spec.md` — 7 Requisitos funcionais | synthesized | `#scope-functional-contract` | Resume o contrato de domínios, narrativa, arquitetura e proveniência. |
| `spec.md` — 8 Critérios de aceite | represented | `#scope-acceptance` | Faz do aceite a atenção que antecede execução, e não uma lista escondida. |
| `spec.md` — 9 Comportamentos de borda e falha | represented | `#trust-constraints` | Explicita fallback, ausência de fonte e telas estreitas como condições de confiança. |
| `spec.md` — 10 Direção visual | represented | `#scope-visual-direction` | Recupera a gramática vertical Pearson e a proibição de tabs-âncora. |
| `spec.md` — 11 Restrições não funcionais | represented | `#trust-nfr` | Mantém acessibilidade, privacidade, compatibilidade e qualidade humana visíveis. |
| `spec.md` — 12 Premissas e dependências | represented | `#trust-assumptions` | Exibe as quatro premissas e seus donos/validações. |
| `spec.md` — 13 Riscos | represented | `#trust-risks` | Mantém os cinco riscos e suas respostas declaradas. |
| `spec.md` — 14 Decisão da SPEC | represented | `#decision-boundary` | Separa direção aprovada de autorização de tasks. |
| `plan.md` — Estratégia | synthesized | `#architecture-hero` | Mostra a composição e o review como camada derivada, não como nova autoridade. |
| `plan.md` — Decisões de desenho | represented | `#architecture-design-decisions` | Recupera as seis escolhas que definem subpágina, escala e Pearson. |
| `plan.md` — Topologia conceitual a implementar somente quando fontes a suportarem | represented | `#architecture-macro` | Mostra todas as relações textuais do macro, incluindo o zoom condicional. |
| `plan.md` — Sequência de implementação após D-023-001 | represented | `#execution-sequence` | Expõe a ordem segura antes de qualquer task: fixtures, shell, composição e corpus. |
| `plan.md` — Limites de mudança previstos | represented | `#architecture-change-map` | Declara a unidade de quatro áreas previstas e a fronteira preservada de cada uma. |
| `impact-map.md` — Mudança e beneficiários | represented | `#impact-footprint` | A rota Impacto recupera benefício e controle por superfície, em vez de inferir sistemas consumidores. |
| `impact-map.md` — Cadeias de impacto e controle | represented | `#impact-risk-chain` | Mantém evento, sinal, consequência, controle e dono como relação rastreável. |
| `impact-map.md` — Fora do alcance desta iniciativa | represented | `#impact-exclusions` | Impede que o leitor trate entrega em um consumidor, migração histórica ou certificação automática como escopo desta SPEC. |
| `tasks.md` — Contrato de autorização A2 | represented | `#execution-authority` | Abertura e fechamento deixam explícito que os quatro contratos permanecem pending. |
| `tasks.md` — T-001 — Contrato editorial e fixtures de arquitetura explicável | represented | `#task-001` | Expõe outcome, dependência e evidência futura do primeiro draft. |
| `tasks.md` — T-002 — Shell Pearson e router de subpáginas internas | represented | `#task-002` | Expõe outcome, dependência e evidência futura do segundo draft. |
| `tasks.md` — T-003 — Composição executiva, topologia, change map e zoom | represented | `#task-003` | Expõe outcome, dependência e evidência futura do terceiro draft. |
| `tasks.md` — T-004 — Recompose, revisão C-level e adoção controlada | represented | `#task-004` | Expõe outcome, dependência e evidência futura do quarto draft. |
| `validation-plan.md` — Estratégia de validação | synthesized | `#validation-strategy` | Separa o que o código verifica do julgamento independente. |
| `validation-plan.md` — V-023-01 | represented | `#validation-route` | Recupera as rotas reais, URL/histórico e ausência de rolagem disfarçada. |
| `validation-plan.md` — V-023-02 | represented | `#validation-access` | Recupera foco, landmarks, no-JS, print, 200% e movimento reduzido. |
| `validation-plan.md` — V-023-03 | represented | `#validation-narrative` | Mantém revisão distinta e proíbe score de compreensão. |
| `validation-plan.md` — V-023-04 | represented | `#validation-architecture` | Mantém macro, escala e zoom/N/A ligados às fontes. |
| `validation-plan.md` — V-023-05 | represented | `#validation-scale` | Recupera os casos negativos de escala e detalhe inventado. |
| `validation-plan.md` — V-023-06 | represented | `#validation-pearson` | Mantém origem local, shell, contraste e julgamento de marca. |
| `validation-plan.md` — V-023-07 | represented | `#validation-mocks` | Mantém a decisão sobre os mocks sem tratá-los como implementação. |
| `validation-plan.md` — V-023-08 | represented | `#validation-corpus` | Mantém corpus, digests e avaliações independentes. |
| `validation-plan.md` — Evidência futura | represented | `#validation-limits` | Separa contexto visual de evidência canônica e mantém os pacotes de task como prova futura. |
| `decision-log.md` — D-023-001 | represented | `#evolution-d001` | Preserva a direção aprovada sem confundi-la com autorização de task. |
| `decision-log.md` — D-023-002 | represented | `#evolution-d002` | Preserva o primeiro REVISE e seu limite de autorização. |
| `decision-log.md` — D-023-003 | represented | `#evolution-d003` | Preserva o segundo REVISE e os reparos de arquitetura/Pearson. |
| `decision-log.md` — D-023-004 | represented | `#evolution-d004` | Preserva o terceiro REVISE e o bloqueio de preflight. |
| `decision-log.md` — D-023-005 | represented | `#evolution-d005` | Preserva o quarto REVISE e a exigência de shell v2. |
| `decision-log.md` — D-023-006 | represented | `#evolution-d006` | Preserva o quinto REVISE e o trabalho de profundidade. |
| `decision-log.md` — D-023-007 | represented | `#evolution-d007` | Preserva o sexto REVISE e as correções semânticas. |
| `decision-log.md` — D-023-008 | represented | `#evolution-d008` | Preserva o sétimo REVISE e seu próximo checkpoint. |
| `decision-log.md` — D-023-009 | represented | `#evolution-d009` | Preserva o oitavo REVISE que exige somente granularidade final. |
| `decision-log.md` — D-023-010 | represented | `#evolution-d010` | Preserva a nona revisão: substância adequada, projeções correntes e wrappers a reparar. |
| `decision-log.md` — D-023-011 | represented | `#evolution-d011` | Preserva a décima revisão e suas quatro projeções multi-heading a separar. |
| `decision-log.md` — D-023-012 | represented | `#evolution-d012` | Preserva a décima primeira revisão: hash congelado, fato unívoco e vínculo para D-023-013 pendente. |
| `decision-log.md` — D-023-013 | represented | `#evolution-d013` | Registra que a aprovação do snapshot anterior só autorizou a renderização guardada. |
| `decision-log.md` — D-023-014 | represented | `#evolution-d014` | Preserva o REVISE pós-render, seus três achados e a recuperação por novo snapshot. |
| `decision-log.md` — D-023-015 | represented | `#overview-strategy`, `#evolution-d015`, `#evolution-review` | Registra o REVISE da recuperação e exige projeções correntes, digests e logo reparados. |
| `decision-log.md` — D-023-017 | represented | `#evolution-d017`, `#evolution-review` | Registra o REVISE mecânico do manifesto e preserva o limite: não houve assinatura ou refresh. |
| `decision-log.md` — D-023-019 | represented | `#evolution-d019`, `#evolution-review` | Registra o REVISE pós-render: projeções defasadas e registro humano de coverage inválido. |
| `decision-log.md` — D-023-021 | represented | `#evolution-d021`, `#validation-validator-defect` | Preserva o vínculo de decisão defasado e a hipótese histórica de defeito, posteriormente corrigida por D-023-023. |
| `decision-log.md` — D-023-023 | represented | `#validation-validator-audit`, `#evolution-d023` | Corrige o diagnóstico: o validador está certo; a disposição com travessão era o defeito. |
| `decision-log.md` — D-023-024 | represented | `#evolution-review` | Mantém o envelope pendente que vinculou o snapshot corrigido ao manifesto corrente. |
| `decision-log.md` — D-023-025 | represented | `#evolution-d025` | Registra o REVISE que devolve somente duas projeções estáticas que ficariam falsas após o refresh. |
| `decision-log.md` — D-023-027 | represented | `#evolution-d027` | Registra o REVISE estrutural: o marcador lifecycle-safe ainda precisa ser um bloco de proveniência v2. |
| `decision-log.md` — D-023-029 | represented | `#evolution-d029` | Registra o REVISE pós-render: frases de pré-render passam a ser contexto histórico e o parecer pós-render torna-se o passo corrente. |
| `decision-log.md` — D-023-031 | represented | `#evolution-d031` | Registra o REVISE que exige recuperar D-023-029 e retirar o rótulo corrente da aprovação histórica D-023-028. |
| `decision-log.md` — D-023-033 | represented | `#evolution-d033` | Registra o REVISE que restaura a fonte `spec.md` do cartão de aceite, sem apagar a recuperação própria de D-023-029. |
| `progress.md` — Recuperação pré-render — REVISE 2026-08-31 | represented | `#evolution-progress` | Explica o checkpoint seguro após D-023-015 e o envelope pendente D-023-016. |
| `ratchet.md` — RATCHET-023-001 | represented | `#trust-ratchet` | Torna recuperável a regra de prevenção: explicação não pode ser reduzida a CSS, score ou diagrama genérico. |
| `run-state.yaml` — status | represented | `#evolution-state` | Estado atual em execução ancora o checkpoint factual sem antecipar aprovação. |
| `run-state.yaml` — quality_gates.human_visibility_ready | represented | `#evolution-next` | Ancora o marcador de próximo passo no gate estável e permite ao renderer projetar a ação corrente sem texto pré-review congelado. |
| `run-state.yaml` — quality_gates.human_visibility_ready | represented | `#trust-state` | Human Visibility false permanece estável antes e depois do refresh e impede tratar o candidato como entrega. |
| `run-state.yaml` — brief_phase | represented | `#trust-delivery` | `ready_to_render` ainda corresponde a candidato authored, não renderizado. |
| `run-state.yaml` — approvals.human_required | represented | `#trust-approval` | Mantém visível a autoridade humana requerida. |

Nenhum heading material de fonte core usa `link_only`. As rotas reutilizam uma
mesma fonte somente quando ela sustenta a decisão específica daquele bloco;
cada projeção no candidato conserva sua proveniência local e fragmento literal.

### Estado atual da composição após D-023-033

O candidato em `tmp/spec023-brief-candidate.html` substitui âncoras como
experiência principal por router interno (hash + `pushState` + back/forward),
com região ativa única, foco no H1 e fallback linear/print. D-023-014 confirmou
essa mecânica nos renders guardados e D-023-018 aprovou um snapshot para
refresh. D-023-019 devolveu o HTML promovido porque a narrativa de lifecycle
permaneceu pré-render e o registro humano não usava o formato verificável de
disposição/alvo. D-023-021 confirmou o formato corrigido, mas devolveu o
vínculo de decisão e levantou uma hipótese de defeito no validador. D-023-023
refutou essa hipótese: o formato com travessão era o defeito e o candidato
correto pode ser validado normalmente. D-023-024 vinculou o snapshot ao
manifesto corrente, mas D-023-025 devolveu duas projeções estáticas: o gate
de coverage muda com a assinatura e o próximo passo muda depois do parecer.
D-023-026 corrigiu essas duas projeções, mas D-023-027 verificou que o
marcador de próximo passo ainda não era um bloco de proveniência v2. D-023-028
resolveu essa identidade e foi promovido, mas D-023-029 devolveu o artefato
por três frases que ainda se apresentavam como pré-render. D-023-030 deve
tratá-las como fatos históricos e identificar o parecer pós-render como o
passo corrente antes de nova revisão independente. D-023-031 devolveu o
candidate D-023-030 porque a decisão pós-render D-023-029 ainda não possuía
cartão/linha de coverage e porque D-023-028 era chamado de envelope corrente.
D-023-032 corrige apenas essa recuperabilidade e esse rótulo histórico.
D-023-033 confirmou essa recuperação, mas devolveu o cartão `#scope-acceptance`
porque sua fonte canônica `spec.md — 8 Critérios de aceite` foi substituída
indevidamente pela decisão D-023-029. D-023-034 deve restaurar a fonte do
aceite e preservar D-023-029 em seu cartão de evolução.

A tabela acima continua o contrato de composição: cada alvo deve existir no
candidato e conservar `represented`/`synthesized` com fonte e locator locais;
nenhuma linha material pode virar `link_only`. A verificação linha a linha só
é declarada após o próximo review independente. Enquanto isso,
`brief_coverage_ready`, Human Visibility e a autorização das tasks permanecem
falsos.
