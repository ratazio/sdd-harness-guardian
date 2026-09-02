# Decision log — SPEC 023

## D-023-001 — Direção visual executiva aprovada para execução

- **Status:** approved by requester, 2026-08-31.
- **Contexto:** o requester revisou M-023-A/B/C, considera a direção aprovada
  e autorizou a execução completa. A composição pode ficar mais vertical
  durante a implementação. Não haverá avatar/login decorativo; o responsável
  da SPEC aparece apenas se estiver determinado nas fontes.
- **Decisão proposta:** adotar subpáginas internas integrais, narrativa
  executiva por domínio, arquitetura fonte-apoiada em macro/change map/zoom e
  sistema Pearson local como descritos em `spec.md`.
- **Entrada de revisão:** M-023-A, M-023-B e M-023-C, apresentados nesta
  conversa e preservados em `evidence/visual-mocks/`; são hipóteses de
  composição e não fontes canônicas.
- **Owner:** requester.
- **Consequência:** iniciar cobertura/composição e Human Visibility pelo fluxo
  v2. A autorização não elimina os gates de proveniência, reviewer distinto,
  evidence ou Tasks Ready, e não autoriza reescrever briefs históricos.
- **Diretriz de execução:** criar skills e papéis adicionais, isolados dos
  existentes, para composição editorial e revisão de profundidade visual;
  usar builders/reviewers Terra distintos e evitar score semântico ou receita
  determinística.

## D-023-002 — Coverage review do candidato inicial

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** /root/spec023_coverage_reviewer (distinto do compositor).
- **Input:** tmp/spec023-brief-candidate.html SHA-256
  f06ff9c4db1c84fa7ae8af1bc726c8e205c5da5fc2a4c6f0cb1c2a94d119bc81.
- **Decisão:** o candidato não pode ser renderizado. Ele usa âncoras, não
  subpáginas internas; declara locators de cobertura inexistentes; concentra
  proveniência em contêineres que não sustentam os cartões; simplifica a
  arquitetura sem escala/unidade; e diverge do guia Pearson por gradiente,
  peso, logo e rodapé.
- **Reparo exigido:** o compositor deve criar o router de candidato com
  fallback, corrigir fonte → bloco → locator, representar o fluxo e a escala
  fonte-apoiados do bundle e aplicar o Pearson vertical sem avatar/login.
  Novo candidato exige revisão independente e novo hash.
- **Limite:** esta decisão não autoriza T-001 nem altera fatos canônicos.

## D-023-003 — Segunda coverage review do candidato reparado

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** /root/spec023_coverage_reviewer_r2 (distinto do compositor).
- **Input:** tmp/spec023-brief-candidate.html SHA-256
  a29886e50333dc003ce04634dbb42b5237ad7ff2f407460a088df12d97e7264f.
- **Progresso confirmado:** router com rota ativa exclusiva, histórico, foco,
  fallback linear/print, layout vertical, ausência de avatar e ausência de
  gradiente decorativo.
- **Reparo exigido:** completar proveniência em cada bloco material; declarar
  superfícies previstas, não já alteradas; corrigir zoom para lacuna do corpus
  com owner/caminho; regenerar todos os digests; separar governança preservada
  de papéis novos previstos; e cumprir os hooks do perfil Pearson exigidos
  pelo preflight.
- **Limite:** a composição continua pré-render e nenhuma tarefa se torna ready
  por esta revisão.

## D-023-004 — Terceira coverage review do candidato pós-D-023-003

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r3` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `d32a7c5875aef2d81480a19a7d64916a0ae3a4751600dfbf8651feee395f6e4d`.
- **Progresso confirmado:** oito rotas internas substituem exclusivamente a
  região principal, com `pushState`, voltar/avançar, foco no H1, fallback
  linear e impressão. A composição está mais vertical, sem avatar/login ou
  gradiente decorativo.
- **Reparo exigido:** regenerar digests/fragmentos atuais; vincular cada bloco
  material à sua fonte, heading, disposição e fragmento; espelhar o registro
  completo de coverage em targets existentes; ligar escala e quatro superfícies
  previstas a `plan.md`; tornar a lacuna de zoom acionável (fonte, owner e
  caminho) ou N/A; e reutilizar os hooks-base do shell Pearson, inclusive
  `--lavender`, `.brief-client-logo` e reduced motion.
- **Limite:** o preflight Pearson e a proveniência ainda impedem renderização,
  Human Visibility e Tasks Ready. Esta decisão não autoriza T-001–T-004.

## D-023-005 — Quarta coverage review do candidato pós-D-023-004

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r4` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `dbd3ff41adc71af9f52da79d40f0429409de1ed76c38a6c77e43d0ae737a97ee`.
- **Progresso confirmado:** as oito rotas continuam subpáginas internas reais,
  com histórico, foco, fallback linear/print e sem chamada de rolagem. A policy
  Pearson passa diretamente, preservando layout vertical e sem avatar/login.
- **Reparo exigido:** compor as rotas sobre os hooks do brief v2 e seus markers
  de lifecycle, em vez de manter um HTML paralelo; completar proveniência local
  e digests atuais por bloco; espelhar a tabela de coverage inteira em targets
  existentes; corrigir fonte/owner/caminho de arquitetura; e completar a
  abertura, limite e fechamento de cada domínio executivo.
- **Limite:** ainda não há pre-render authorization, renderização, Human
  Visibility ou Tasks Ready. Esta decisão não autoriza T-001–T-004.

## D-023-006 — Quinta pre-render review do candidato R2

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r5` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `cb5fc6af87ac18984165a08fc5b57ab114add0c49c4667c5a1053f152939d93f`.
- **Progresso confirmado:** as oito subpáginas, o router, o foco, o fallback,
  a impressão, o lifecycle authored pendente e o shell Pearson satisfazem os
  contratos mecânicos verificados. Isto não substitui a revisão de profundidade.
- **Reparo exigido:** restaurar `aria-current="page"` após a navegação;
  atualizar o checkpoint de Execução para D-023-005/D-023-006 pendente;
  recuperar grupos V-023-02 e V-023-04–08 e a evolução D-023-001–005;
  tornar a descoberta de zoom acionável com corpus, dono e caminho ou N/A;
  completar abertura/pilares/limite/fechamento por rota; e marcar o hero de
  Confiança com proveniência local.
- **Limite:** este resultado não é pre-render approval; não há renderização,
  Human Visibility, Tasks Ready ou autorização de T-001–T-004.

## D-023-007 — Sexta pre-render review do candidato R3

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r6` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `7fcc31023a12480f15b32fd7d39cb4e1ab40cf8bc2ebbc37ff47ad9d918127d0`.
- **Progresso confirmado:** subpáginas, histórico/foco, `aria-current`, fallback,
  impressão, estrutura v2, lifecycle authored e policy Pearson estão corretos.
- **Reparo exigido:** fechar Impacto com risco/controle/dono e próxima ação;
  usar as quatro áreas reais do plano na escala arquitetural; preservar fonte
  própria por decisão histórica em Evolução; corrigir a fonte positiva de
  Valor e escopo; e tornar premissas/riscos de Confiança recuperáveis.
- **Limite:** o record futuro D-023-008 continua mecânico e não existe ainda.
  Este resultado não permite renderização, Human Visibility, Tasks Ready ou
  autorização de T-001–T-004.

## D-023-008 — Sétima pre-render review do candidato R4

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r7` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `cbf9c4ffa8b0fb82563796c65af7f50038b4178f3a880a688d7723488d43f8cf`.
- **Progresso confirmado:** a mecânica de subpágina e o shell Pearson podem
  seguir para renderização; esse fato não substitui suficiência editorial.
- **Reparo exigido:** granularizar source→target no registro de coverage,
  aprofundar por rota pergunta/pilares/limite/fechamento sem fórmula e restaurar
  na topologia Pessoa/operação, contexto preservado, relação material,
  superfície alterada e controle/dependência.
- **Limite:** D-023-009 é o record mecânico futuro; este resultado não permite
  renderização, Human Visibility, Tasks Ready ou autorização de T-001–T-004.

## D-023-009 — Oitava pre-render review do candidato R5

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r8` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `ae5e7936c849024d91428a83c1d5d660bb800cde23869ee65a22964574ec663a`.
- **Progresso confirmado:** a experiência, a arquitetura, a distinção de
  decisões e os contratos mecânicos estão adequados; o defeito restante é de
  cobertura/proveniência granular.
- **Reparo exigido:** uma linha por heading material no registro humano e um
  bloco local que corresponda àquela fonte/heading/fragmento; separar limites,
  decisão, autorização e validation strategy/future evidence hoje agrupados.
- **Limite:** D-023-010 é o record mecânico futuro; este resultado não permite
  renderização, Human Visibility, Tasks Ready ou autorização de T-001–T-004.

## D-023-010 — Nona pre-render review do candidato R6

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r9` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `b2875c0392dddecd8f9de7198c2425d820d4581b7cefd4832e0aeb5b1db07bba`.
- **Progresso confirmado:** experiência, arquitetura, Pearson e coverage
  granular material permanecem adequados.
- **Reparo exigido:** atualizar projeções que ainda tratam D-023-009 como
  futuro e remover provenance agregada de wrappers estruturais (ou vincular
  cada wrapper a um único heading/fragmento literal), preservando provenance
  local dos blocos materiais.
- **Limite:** D-023-011 é o record mecânico futuro; este resultado não permite
  renderização, Human Visibility, Tasks Ready ou autorização de T-001–T-004.

## D-023-011 — Décima pre-render review do candidato R7

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r10` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `88036e874e669c8f8a2e0736e240737e277d3f4d3cdd1523a4b3574d5a7eb8a8`.
- **Progresso confirmado:** rotas, estado pré-render, Pearson e arquitetura
  permanecem coerentes; restam blocos materiais com heading agregado.
- **Reparo exigido:** separar source/heading/fragmento de escopo, hero de
  arquitetura e estados Evolução/Confiança, atualizando seus targets no
  registro humano sem antecipar o futuro D-023-012.
- **Limite:** D-023-012 é o record mecânico futuro; este resultado não permite
  renderização, Human Visibility, Tasks Ready ou autorização de T-001–T-004.

## D-023-012 — Décima primeira pre-render review do snapshot atual

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_coverage_reviewer_r11` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `0a6ab1e8ffd21db853723899be098db2569b7ff8b5cd51a9edf71700ed12cc3b`.
- **Progresso confirmado:** rotas, router, fallback, estado pré-render, escala
  e Pearson permanecem coerentes.
- **Reparo exigido:** congelar e revisar o hash efetivamente presente; tornar
  o registro uma relação unívoca por fato; representar D-023-010 em Evolução;
  e apontar o candidato para o futuro D-023-013, não para um REVISE passado.
- **Limite:** este resultado não permite renderização, Human Visibility, Tasks
  Ready ou autorização de T-001–T-004.

## D-023-013 — Exact pre-render approval do candidato congelado

Author: /root/spec023_coverage_author_r9
Reviewer: /root/spec023_coverage_reviewer_r12
Human attestation: confirmed
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: 18c8249d18f29dc19b9d28aa265f64a6a8e3779d0f4721f38ad9685272426c22
Candidate SHA-256: 20c95be279d90cf8e0de10f3a61a462de3f1be228b889f9b4e1a996e042aa9ff
Composition manifest SHA-256: e911c0e6ca2348b8341be02add8c9c03b105efc056f38cfb1eeb41f2a9c53bb2
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the frozen HTML against
the current canonical corpus, route experience, granular coverage and Pearson
authority. The reviewer is distinct from the author. The reviewed input digest
binds the frozen file bytes; Candidate SHA-256 binds the renderer's decoded
UTF-8 candidate text used for guarded promotion. This conversion is mechanical.
Review outcome detail: APPROVE only this frozen candidate for guarded rendering.
The D-023-013 record and renderer lifecycle transition are mechanical follow-up
to the reviewed bytes; neither grants Human Visibility, Tasks Ready, task
authorization, delivery approval or a change to canonical Markdown authority.

Historical decision context bound by this approval: D-023-001 records the
requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011 and
D-023-012 record the successive independent REVISE findings that shaped the
approved candidate. These existing facts are retained as provenance context
only; D-023-013 changes their status neither individually nor collectively.

## D-023-014 — Revisão independente pós-render do primeiro artefato promovido

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_postrender_reviewer` (distinto do autor e do
  revisor pré-render).
- **Rendered input:** `stakeholder-brief.html` SHA-256
  `da4fc7df3a2c0177ec450fde8c986ff4064a80fb5c1e869964d5f0cbb618b701`.
- **Escopo da revisão:** produto, arquitetura/operação e entrega no HTML já
  renderizado, contra as fontes canônicas e o contrato v2; não é uma decisão
  de Human Visibility ou de entrega.
- **Progresso confirmado:** as oito rotas internas trocam a região principal
  sem `scrollIntoView`; a aplicação Pearson usa logo local sem avatar; macro,
  escala e zoom preservam limites honestos.
- **Achados bloqueadores:** (1) `coverage-register` está no wrapper, não na
  tabela lida pelo validador; (2) `validation-plan.md` apontava um destino
  genérico inexistente, em vez dos quatro pacotes de tarefa; (3)
  `#execution-authority` declara
  `decision-log.md#D-023-011`, mas o registro humano o associa corretamente a
  `tasks.md — Contrato de autorização A2`.
- **Decisão e recuperação:** não usar `--finalize-post-review`. Corrigir a
  fonte canônica e o candidato derivado, retornar a `Coverage Composition`,
  realizar nova revisão pré-render independente do novo snapshot e, somente
  então, executar um refresh guardado e uma nova revisão pós-render.
- **Limite:** D-023-013 continua sendo histórico do primeiro snapshot; este
  REVISE não autoriza alteração de gates, tarefas, Human Visibility ou
  entrega.

## D-023-015 — Revisão pré-render independente da recuperação D-023-014

- **Status:** REVISE, 2026-08-31.
- **Author:** `/root/spec023_recovery_composer`.
- **Reviewer:** `/root/spec023_recovery_prerender_review` (distinto do
  compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `dc83253bb756cd46fd5a72125a7e11a28eb6d7d6e1366d7c5f0b1b1b14073629`.
- **Progresso confirmado:** a tabela agora usa `table#coverage-register`, os
  quatro destinos de evidência existem e a abertura de Execução recupera o
  contrato A2 de `tasks.md`.
- **Achados bloqueadores:** digests de `plan.md`, `validation-plan.md`,
  `run-state.yaml` e `progress.md` ainda são defasados; Evolução/Confiança e
  Overview/Validação projetam D-023-012/D-023-013, não a recuperação atual;
  `#trust-state` declara coverage aprovada apesar do gate false; a raiz aponta
  para D-023-013; e o logo tem `alt` malformado, em desacordo com Pearson.
- **Decisão e recuperação:** sincronizar cada projeção com D-023-014 e o
  estado fonte-primeiro, corrigir o markup do logo e renovar todos os digests
  locais. Um novo snapshot deve apontar ao record pendente D-023-016 e passar
  por revisão independente completa antes de qualquer renderização.
- **Limite:** não houve aprovação, inserção de assinatura, refresh, Human
  Visibility, Tasks Ready ou autorização de task.

## D-023-016 — Record pendente para revisão do snapshot recuperado

Author: /root/spec023_recovery_composer_r2
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: 0439a84511741b31a770ca3fbdcb53c604548f6d505744c6c2d05c4cfaaff884
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the recovered
candidate against the canonical corpus, D-023-014/D-023-015 findings, the
eight route experience, granular coverage and Pearson authority. The pending
record is a non-authorizing envelope only; its signing fields may be completed
only after an independent reviewer approves the exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014 and D-023-015 retain the successive review
and recovery facts that the next snapshot must make recoverable. This context
does not approve the candidate, grant Human Visibility, make a task ready or
replace the independent review required by this record.

## D-023-019 — Revisão pós-render do snapshot D-023-018

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d018_postrender_reviewer` (independente do
  compositor e revisor pré-render).
- **Rendered input:** `stakeholder-brief.html` SHA-256
  `c5c604f1d66dc7ca186d197d50c1ca020044ba0389e27bf59467b81a49a5b55c`.
- **Progresso confirmado:** oito subpáginas exclusivas sem rolagem disfarçada,
  router/foco/fallback, Pearson local sem avatar, macro/change map/zoom
  honestos, `table#coverage-register`, quatro destinos de evidência e A2 em
  `tasks.md` permanecem corretos.
- **Achados bloqueadores:** o HTML promovido ainda se descreve como candidato
  pré-review e D-023-018 pendente, embora esteja renderizado; e as células de
  disposição do registro humano usam travessão em vez do formato canônico
  `disposição: razão`, além de alvos múltiplos não resolúveis.
- **Decisão e recuperação:** corrigir as projeções de lifecycle no candidato,
  representar a aprovação pré-render como fato histórico e ajustar o registro
  para uma linha/fato/alvo e `disposição: razão`. Repetir revisão pré-render,
  refresh guardado e pós-render; não finalizar o review atual.
- **Limite:** os erros de Human Visibility/Tasks Ready ainda falsos são gates
  esperados, mas não reduzem os defeitos reais de composição acima.

## D-023-020 — Record pendente para lifecycle e coverage recompostos

Author: /root/spec023_d020_lifecycle_coverage_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: db0cdf1c0ee3a686db13a9f7a8c4c7aae8c66784d87cd555c9b3d0425b43c4a8
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the recomposed
candidate against the canonical corpus, D-023-019 findings, eight-route
experience, granular coverage and Pearson authority. This pending record is a
non-authorizing envelope only; signing is allowed only after review of the
exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018 and D-023-019 retain the review, render and recovery facts that the
next snapshot must make recoverable. This context does not approve the
candidate, grant Human Visibility, make a task ready or replace the
independent review required by this record.

## D-023-021 — Revisão pré-render do candidate D-023-020

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d020_prerender_reviewer` (independente do
  compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `1965f00130f561caa3523b90f8117bb98bf19c7fcb7f4ffe41a410c6a783a7a5`.
- **Progresso confirmado:** narrativa, oito rotas, arquitetura/zoom honesto,
  Pearson e as 63 linhas de coverage usam disposição com razão e um alvo
  resolúvel. O formato corrigido é materialmente adequado.
- **Achado bloqueador de composição:** os blocos de `decision-log.md` ainda
  carregavam digest de D-023-020 anterior ao record corrente; a revisão exata
  não pode assinar um vínculo defasado.
- **Achado de harness separado:** `validate_human_visibility.py` registra a
  célula de coverage como `(texto, alvos)`, mas sua checagem lê o primeiro
  caractere de cada célula; por isso produz disposições inválidas falsas mesmo
  quando o formato `disposição: razão` está correto. Esse defeito deve ter
  correção testada antes que Human Visibility possa ser verificada; não é
  licença para ignorar o gate.
- **Decisão e recuperação:** reancorar o candidato no envelope D-023-022 e
  registrar o defeito do validador como bloqueio de readiness. Obter novo
  parecer pré-render sobre bytes novos; nenhuma assinatura, refresh ou gate
  é autorizado por D-023-021.

## D-023-022 — Record pendente para o vínculo atual e blocker de validador

Author: /root/spec023_d022_binding_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: 4edf5e6c17531a0e235aa013c00f47e7436ad401db54ea42dcdfb2d81db48d2b
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the decision-rebound
candidate against the canonical corpus, D-023-021 findings, eight-route
experience, granular coverage and Pearson authority. This pending record is a
non-authorizing envelope only; signing is allowed only after review of the
exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020 and D-023-021 retain the review, render and
recovery facts that the next snapshot must make recoverable. This context does
not approve the candidate, grant Human Visibility, make a task ready or
replace the independent review required by this record.

## D-023-023 — Correção do diagnóstico de validador em D-023-021

- **Status:** CORRECTION, 2026-08-31.
- **Auditor:** `/root/spec023_validator_bug_audit`, em leitura independente de
  `scripts/validate_human_visibility.py` e seus testes.
- **Fato corrigido:** D-023-021 alegou que o checker lia o primeiro caractere
  da célula de coverage. A auditoria confirmou que o parser armazena
  `(texto, alvos)` e que `[0]` seleciona o texto inteiro; o travessão era o
  defeito real, porque o contrato exige `disposição: razão`.
- **Consequência:** nenhum patch de produção ou exceção de Human Visibility é
  necessário para o validador. O candidato D-023-022 já usa o formato correto;
  a próxima revisão precisa apenas prender o snapshot ao record vigente.
- **Limite:** esta correção não aprova o candidato, não resolve gates por
  decreto e não autoriza refresh, Human Visibility, Tasks Ready ou task.

## D-023-017 — Revisão independente do vínculo de composição D-023-016

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d016_binding_reviewer` (distinto do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `dd68aaa48b32d3588174df2d1dea31b253f984e28c9d123c2122dadb35025055`.
- **Progresso confirmado:** a revisão calculou o record D-023-016, confirmou
  provenance e lifecycle do candidato, oito subpáginas, Pearson local, mapa de
  arquitetura honesto e os três reparos de D-023-014.
- **Achado bloqueador:** o `Composition manifest SHA-256` escrito em
  D-023-016 não correspondia ao manifesto canônico corrente. Não é defeito da
  narrativa; é vínculo de composição que impediria a promoção assinada.
- **Decisão e recuperação:** atualizar o mapa de coverage para registrar este
  parecer, calcular o manifesto somente após esse mapa estabilizar, e criar um
  envelope D-023-018 ligado a esse valor. O candidato seguinte recebe apenas
  as projeções/digests mecânicos correspondentes e nova revisão exata.
- **Limite:** não houve assinatura de D-023-016, render, refresh, Human
  Visibility, Tasks Ready ou autorização de task.

## D-023-018 — Record pendente para revisão do manifesto estabilizado

Author: /root/spec023_d018_composition_repair
Reviewer: /root/spec023_d018_prerender_reviewer
Human attestation: confirmed
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 94a00495fd367bdf07a0e4683d32de0ec9b659448595f02df73626609c203340
Composition manifest SHA-256: 64a8ce2ca52b445f089ae1f381e54d1e722ad4924ebc322cbaaa7bf0d44e8ca5
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, D-023-014/D-023-015/D-023-017
findings, the eight route experience, granular coverage and Pearson authority.
The approval is limited to the exact candidate and the mechanical
source/lifecycle synchronization required for guarded refresh; it does not
grant Human Visibility, Tasks Ready, delivery or task authorization.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016 and D-023-017 retain
the successive review and recovery facts that the next snapshot must make
recoverable. This context does not approve the candidate, grant Human
Visibility, make a task ready or replace the independent review required by
this record.

## D-023-025 — Revisão pré-render das projeções D-023-024

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d024_prerender_reviewer` (independente do
  compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `f27e68055bfb4159db20cbd789fe6400248ccfd40803f2475f1ac8635b2362e3`.
- **Progresso confirmado:** o vínculo D-023-024, o manifesto, proveniência,
  lifecycle, política Pearson, bundle, oito rotas, narrativa executiva,
  topologia/zoom honestos e as 68 linhas de coverage no formato
  `disposição: razão` com um alvo foram aceitos. D-023-023 permanece visível
  como correção da hipótese de bug; nenhum patch ou exceção foi inventado.
- **Achados bloqueadores:** `#trust-state` projetava
  `brief_coverage_ready: false`, valor que necessariamente muda durante a
  assinatura pré-render; `#evolution-next` dizia estaticamente que a própria
  revisão D-023-024 ainda era o próximo passo. Ambos seriam falsos no HTML
  promovido e invalidariam sua proveniência final.
- **Decisão e recuperação:** trocar somente essas duas projeções por fontes e
  marcadores estáveis através da assinatura/refresh, reancorar em D-023-026 e
  obter nova revisão independente do byte novo. Não houve assinatura,
  refresh, Human Visibility, Tasks Ready ou autorização de task.

## D-023-026 — Record pendente para as projeções lifecycle-safe

Author: /root/spec023_d026_lifecycle_projection_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: f98a3e3fa5e9fbb64c74c2a5ed6da3f09acad19dfac0f0cec23fbfed6f5d2e07
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, D-023-025 findings, the
eight-route experience, granular coverage and Pearson authority. This pending
record is a non-authorizing envelope only; signing is allowed only after
review of the exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020, D-023-021, D-023-022, D-023-023,
D-023-024 and D-023-025 retain the review, render, recovery and projection
facts that the next snapshot must make recoverable. This context does not
approve the candidate, grant Human Visibility, make a task ready or replace
the independent review required by this record.

## D-023-027 — Revisão pré-render da proveniência de D-023-026

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d026_prerender_reviewer` (independente do
  compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `31a686a8d105a928de2dc0fc30a8df1a99d8952bfa333cad1a140794f1c7bad1`.
- **Progresso confirmado:** D-023-026 tornou `#trust-state` estável em
  `human_visibility_ready: false` e converteu `#evolution-next` no marcador
  que o renderer atualiza. Proveniência/lifecycle, Pearson, bundle, oito
  rotas, narrativa, arquitetura, D-023-023 e a tabela humana passaram.
- **Achado bloqueador:** a linha de coverage para `#evolution-next` ainda
  declarava `represented` sem que o próprio marcador declarasse
  `data-source="run-state.yaml"`. O conteúdo era lifecycle-safe, mas não era
  um bloco de proveniência v2 resolúvel.
- **Decisão e recuperação:** manter o marcador e vinculá-lo à fonte estável
  `human_visibility_ready: false`, reancorar em D-023-028 e repetir o review
  exato. Não houve assinatura, refresh, Human Visibility, Tasks Ready ou task.

## D-023-028 — Record pendente para o marcador com proveniência v2

Author: /root/spec023_d028_marker_provenance_composer
Reviewer: /root/spec023_d028_prerender_reviewer
Human attestation: confirmed
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 9d7f5c9a32f76e3f8c731c4d0ea0b454f813eb0c29f88435a768f17c8b2041c4
Composition manifest SHA-256: b27defec9e302a0ce1ce9e530904379d7049b51b8cb446240200e7170f9e42cf
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, D-023-027 finding, the
eight-route experience, granular coverage and Pearson authority. This pending
record is a non-authorizing envelope only; signing is allowed only after
review of the exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020, D-023-021, D-023-022, D-023-023,
D-023-024, D-023-025, D-023-026 and D-023-027 retain the review, render,
recovery, projection and provenance facts that the next snapshot must make
recoverable. This context does not approve the candidate, grant Human
Visibility, make a task ready or replace the independent review required by
this record.

## D-023-024 — Record pendente para a composição corrigida

Author: /root/spec023_d024_binding_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: ed2cbdf4e856b6bf75d03c8d71c02c8da98eaa39378496a6827107ed1fdacd6c
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, the D-023-019 lifecycle and
coverage findings, the D-023-023 validator correction, the eight-route
experience, granular coverage and Pearson authority. This pending record is a
non-authorizing envelope only; signing is allowed only after review of the
exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020, D-023-021, D-023-022 and D-023-023 retain
the review, render, recovery and correction facts that the next snapshot must
make recoverable. This context does not approve the candidate, grant Human
Visibility, make a task ready or replace the independent review required by
this record.

## D-023-029 — Revisão pós-render do snapshot D-023-028

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d028_postrender_reviewer` (independente do
  compositor e do reviewer pré-render).
- **Rendered input:** `stakeholder-brief.html` SHA-256
  `8cbc2ecb78527efe79a46da544b98e2768ff00cbc251deb445600873770706cf`.
- **Progresso confirmado:** provenance/lifecycle finais, Pearson, bundle,
  coverage de 73 linhas, router de oito subpáginas, topologia/zoom honesto e
  narrativa executiva passaram; Human Visibility retornou apenas os gates
  esperados, sem falha estrutural.
- **Achados bloqueadores:** `#overview-strategy`, `#scope-acceptance` e
  `#evolution-d028` ainda descrevem D-023-028 como revisão pré-render
  pendente, embora ela tenha sido aprovada e o parecer pós-render seja o
  estado atual. Isso reduz a clareza de reunião e contradiz a promoção.
- **Decisão e recuperação:** reescrever apenas essas projeções para preservar
  D-023-028 como fato histórico e declarar o parecer pós-render pendente,
  reancorar em D-023-030, refazer pre-render, refresh e revisão pós-render.
  Não há finalização, Human Visibility, Tasks Ready ou task autorizada.

## D-023-030 — Record pendente para a comunicação pós-render corrente

Author: /root/spec023_d030_postrender_language_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: 51d4a57e78e6aff2d88ad668674917be933894c93e9c845025d63e4780d43279
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, D-023-029 post-render
findings, the eight-route experience, granular coverage and Pearson authority.
This pending record is a non-authorizing envelope only; signing is allowed
only after review of the exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020, D-023-021, D-023-022, D-023-023,
D-023-024, D-023-025, D-023-026, D-023-027, D-023-028 and D-023-029 retain
the review, render, recovery, projection and communication facts that the
next snapshot must make recoverable. This context does not approve the
candidate, grant Human Visibility, make a task ready or replace the
independent review required by this record.

## D-023-031 — Revisão pré-render da recuperabilidade D-023-030

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d030_prerender_reviewer` (independente do
  compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256
  `f4732f4dbf2974e53fa849c57f4a3c7cf82b893234e37497d73668cc544e4f5d`.
- **Progresso confirmado:** D-023-030 corrigiu a linguagem de estado
  pós-render e os preflights, mapa de rotas, arquitetura, Pearson e markers
  prospectivos passaram.
- **Achados bloqueadores:** faltavam `#evolution-d029` e sua linha no
  `#coverage-register`, embora o plano mapeie D-023-029 materialmente; além
  disso, a linha humana de D-023-028 ainda o chamava de envelope corrente, em
  vez de aprovação pré-render histórica limitada ao refresh guardado.
- **Decisão e recuperação:** adicionar a recuperação de D-023-029 e corrigir
  o rótulo de D-023-028, reancorar em D-023-032 e repetir a revisão exata.
  Não houve assinatura, refresh, Human Visibility, Tasks Ready ou task.

## D-023-032 — Record pendente para recuperabilidade pós-render

Author: /root/spec023_d032_recoverability_composer
Reviewer: pending independent reviewer
Human attestation: pending
Attestation basis: the requester expressly authorized agentic semantic review
as the intended human-decision layer in this initiative.
Review outcome: pending
Composition provenance: pending
Candidate SHA-256: pending
Composition manifest SHA-256: c533e6c5b5a66d275088ca1f0bbdbd9b1907f6b0296dfcbffd7e0fa8ac07ccd0
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically
rebound candidate against the canonical corpus, D-023-031 findings, the
eight-route experience, granular coverage and Pearson authority. This pending
record is a non-authorizing envelope only; signing is allowed only after
review of the exact candidate.

Historical decision context bound by this pending review: D-023-001 records
the requester visual approval; D-023-002, D-023-003, D-023-004, D-023-005,
D-023-006, D-023-007, D-023-008, D-023-009, D-023-010, D-023-011,
D-023-012, D-023-013, D-023-014, D-023-015, D-023-016, D-023-017,
D-023-018, D-023-019, D-023-020, D-023-021, D-023-022, D-023-023,
D-023-024, D-023-025, D-023-026, D-023-027, D-023-028, D-023-029,
D-023-030 and D-023-031 retain the review, render, recovery, projection and
communication facts that the next snapshot must make recoverable. This
context does not approve the candidate, grant Human Visibility, make a task
ready or replace the independent review required by this record.

## D-023-033 — Revisão pré-render da fonte de aceite D-023-032

- **Status:** REVISE, 2026-08-31.
- **Reviewer:** `/root/spec023_d032_prerender_reviewer` (independente do compositor).
- **Input:** `tmp/spec023-brief-candidate.html` SHA-256 `58a348c1f4f0d082fdb8d37573bb46480d5f77abc6b1c76ad9f71bab35e32be5`.
- **Progresso confirmado:** D-023-029 tornou-se recuperável; D-023-028 está histórico; Pearson, lifecycle, coverage e oito subpáginas passaram.
- **Achado bloqueador:** a linha `spec.md — 8 Critérios de aceite` aponta a `#scope-acceptance`, mas esse bloco passou a declarar `decision-log.md`, quebrando o vínculo fonte→alvo v2.
- **Decisão e recuperação:** restaurar `spec.md — 8 Critérios de aceite` em `#scope-acceptance`, manter D-023-029 no cartão de evolução, reancorar em D-023-034 e repetir review. Nenhuma promoção ou gate é autorizado.

## D-023-034 — Record pendente para restauração da fonte de aceite

Author: /root/spec023_d034_acceptance_source_composer
Reviewer: /root/spec023_d034_prerender_reviewer
Human attestation: confirmed
Attestation basis: the requester expressly authorized agentic semantic review as the intended human-decision layer in this initiative.
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 0bd7fbb498ced7d47475067c98878c7361d936874f7fc108866d343dc8be0144
Composition manifest SHA-256: 801c0749b337b64f843aea7b064f9f12f12ad35e8bad460b98326f20c8f2e279
Reviewed at: 2026-08-31
Review method: independent semantic and visual review of the mechanically rebound candidate against the canonical corpus, D-023-033 finding, the eight-route experience, granular coverage and Pearson authority. This pending record is non-authorizing; signing is allowed only after review of the exact candidate.

Historical decision context bound by this pending review: D-023-001, D-023-002,
D-023-003, D-023-004, D-023-005, D-023-006, D-023-007, D-023-008,
D-023-009, D-023-010, D-023-011, D-023-012, D-023-013, D-023-014,
D-023-015, D-023-016, D-023-017, D-023-018, D-023-019, D-023-020,
D-023-021, D-023-022, D-023-023, D-023-024, D-023-025, D-023-026,
D-023-027, D-023-028, D-023-029, D-023-030, D-023-031, D-023-032 and
D-023-033 retain the review, render, recovery, projection, communication and
acceptance-source facts that the next snapshot must make recoverable. This
context does not approve the candidate, grant Human Visibility, make a task
ready or replace the independent review required by this record.
