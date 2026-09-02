# T-003 — mapa editorial de composição (rascunho para avaliação independente)

**Compositor:** `/root/spec023_t003_builder`  
**Pedido efetivo:** cada subpágina deve sustentar uma conversa de reunião; a
camada é derivada dos Markdown, não altera a autoridade deles.  
**Candidato de referência:** `tmp/spec023-brief-candidate.html` (input
derivado; está desatualizado em relação ao `run-state.yaml` após T-001/T-002 e
não é proposta de promoção nesta task).

## Mapa de rotas

| Rota / pergunta de decisão | Fonte e locator | Síntese permitida | Limite ou descoberta | Blocos derivados de referência |
|---|---|---|---|---|
| Visão geral — por que a decisão importa agora? | `spec.md#1 Problema`, `#2 Objetivo`, `#3 Resultado de entrega`, `#4 Pessoas e decisões atendidas`, `#5 Resultados observáveis` | Uma conversa completa por domínio evita reconstrução mental e torna arquitetura recuperável. | Não afirma que um stakeholder já compreendeu o material; essa é a pergunta da revisão distinta. | `#decision-snapshot`, `#overview-problem`, `#overview-outcome`, `#overview-decision`, `#overview-observables` |
| Valor e escopo — o que esta frente compra e o que protege? | `spec.md#3 Resultado de entrega`, `#6 Não objetivos`, `#7 Requisitos funcionais`, `#8 Critérios de aceite`, `#10 Direção visual documentada` | A camada melhora o briefing, não implementa os produtos descritos nem substitui Markdown. | Não converte intenção visual em fonte de fatos ou em autorização de task. | `#scope-boundary`, `#scope-limit`, `#scope-functional-contract`, `#scope-acceptance`, `#scope-visual-direction` |
| Arquitetura — onde a camada muda e onde não muda? | `plan.md#Estratégia`, `#Decisões de desenho`, `#Topologia conceitual a implementar somente quando fontes a suportarem`, `#Limites de mudança previstos`; `ratchet.md#RATCHET-023-001` | A camada fica entre fonte e reunião; macro mostra intenção/operação, contexto preservado, superfície alterada e controle/revisão. | Não há subsistema consumidor nomeado para zoom. `RATCHET-023-001` sustenta Guardian maintainer + revisão distinta como descoberta; nenhum frontend é inferido. | `#architecture-hero`, `#architecture-macro`, `#architecture-change-map`, `#architecture-scale`, `#architecture-zoom`, `#architecture-limits` |
| Impacto — quem muda e como a transição é controlada? | `impact-map.md#Mudança e beneficiários`, `#Cadeias de impacto e controle`, `#Fora do alcance desta iniciativa` | Organiza benefício por superfície e relação evento → sinal → consequência → controle → dono. | Não deduz consumidores, APIs ou deployment. | `#impact-footprint`, `#impact-risk-chain`, `#impact-exclusions` |
| Execução — que incrementos deixam a entrega segura? | `tasks.md#Contrato de autorização A2`, `#T-001`, `#T-002`, `#T-003`, `#T-004`; `plan.md#Sequência de implementação após D-023-001` | Cada task mostra outcome, dependência, assurance/evidência e por que é a próxima etapa. | Estado/autoridade vêm de fonte corrente; um candidato não concede aprovação. | `#execution-authority`, `#execution-sequence`, `#task-001`, `#task-002`, `#task-003`, `#task-004` |
| Validação — o que prova avanço e o que não prova? | `validation-plan.md#Estratégia de validação`, `#V-023-01` a `#V-023-08`, `#Evidência futura` | Distingue oráculos estruturais da revisão agente/humana de narrativa e experiência. | Um teste verde não decide suficiência visual, materialidade ou compreensão. | `#validation-strategy`, `#validation-route`, `#validation-access`, `#validation-narrative`, `#validation-architecture`, `#validation-scale`, `#validation-pearson`, `#validation-corpus`, `#validation-limits` |
| Evolução — o que foi decidido, corrigido e permanece aberto? | `decision-log.md` nos registros aplicáveis; `progress.md`; `run-state.yaml#status`, `#quality_gates` | Mantém revisões/reparos como histórico recuperável e apresenta checkpoint factual. | Deve ser recomposto contra o registro e estado atuais antes de render/promoção; não copia rótulos pré-render como estado atual. | `#evolution-review`, `#evolution-progress`, `#evolution-state`, `#evolution-next` |
| Confiança — por que desafiar ou aceitar esta leitura? | `spec.md#9 Comportamentos de borda e falha`, `#11 Restrições não funcionais`, `#12 Premissas e dependências`, `#13 Riscos`; `ratchet.md#RATCHET-023-001`; `run-state.yaml#approvals` | Proveniência local, lifecycle, limites e gates ficam recuperáveis sem dominar a abertura executiva. | Fonte/locator não substituem o parecer independente; artefato derivado não é a autoridade canônica. | `#trust-constraints`, `#trust-nfr`, `#trust-assumptions`, `#trust-risks`, `#trust-ratchet`, `#trust-state`, `#trust-approval` |

## Leitura arquitetural proporcional

| Caso | Relação fonte-apoiada | Macro / change map / escala / zoom | Disposição honesta |
|---|---|---|---|
| `learning-release` | learner shell, publishing contract e entitlement guard têm relação e superfícies declaradas. | Macro de confirmação; 3 superfícies alteradas de 4 nomeadas; zoom no result panel. | Material e representável. |
| `reservoir-operations` | alarme → hold → segunda amostra → autorização do water-quality lead → recuperação é um fluxo operacional. | Fluxo e limite de reinício; escala física é desconhecida porque a fonte não declara ativos/superfícies nem denominador; não há zoom de frontend. | Equivalente operacional; escala desconhecida, não N/A nem zero. |
| `missing-internal-detail` | A fonte só estabelece a fronteira do gateway. | Macro da fronteira; superfície, unidade de escala e zoom internos são desconhecidos. | Discovery explícito; owner/path não estabelecidos pela fonte; não é zero. |

Os três candidatos mínimos correspondentes ficam em
`scripts/fixtures/executive-brief-editorial-contract/*/candidate.html`; eles
calibram a relação fonte → bloco, não são templates universais nem artefatos
de produção.

## Pergunta para o revisor distinto

Comparando pedido, fontes, mapa, candidatos de calibração e o candidato SPEC
023 apenas como referência derivada: a abertura de cada domínio permite que um
decisor recupere propósito, perímetro, trade-off/limite e próxima conversa sem
fingir arquitetura, escala ou ownership que as fontes não estabelecem? Julgar
também se a arquitetura material é profunda o bastante e se os dois casos de
ausência são proporcionais, sem exigir uma gramática visual universal.
