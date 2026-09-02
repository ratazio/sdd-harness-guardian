# Technical Plan — SPEC 021

## Approach

1. Definir inventário de fontes materiais: core fixas e condicionais, como
ratchet não vazio ou estado vazio que muda governança.
2. Introduzir um hook de revisão semântica em linguagem natural. Um agente
distinto recebe pedido, corpus canônico e candidato e responde, para aquele
caso: “que decisão permanece impossível só pelo HTML?”, “que relação/fonte
muda essa decisão?”, “o que é N/A e por quê?”. O retorno é um parecer citado,
não um score, checklist de domínio ou classificação por palavras.
3. Estender coverage/composição para registrar a disposição do parecer:
representação ou N/A com razão, locator, digest e fragmento factual.
4. Projetar relações fonte-driven por pipeline, máquina de estados, trust
boundary, topologia/contrato ou matriz de recuperação — ou outro formato que
o revisor justifique pelo caso; nunca por quota visual.
5. Limitar código a verificar identidade distinta, o manifesto de entradas
declarado pelo revisor (caminhos/identidades e digests do pedido, fontes e
candidato) e o registro de parecer. O promotor não infere se o manifesto é
suficiente ou se uma fonte é material, nem transforma o parecer em aprovação
automática.
6. Provar negativos estruturalmente válidos que perdem ratchet ou relação.
Somente depois de `evidence/T-001.md`, `evidence/T-002.md` e
`evidence/T-003.md` aprovadas independentemente, recompor M-001–M-008 em raiz
nova como oito consumidores, guardar digests request/fonte/HTML e repetir as
sete lentes nas duas passagens. Um `REVISE` material corrige fontes, rerenderiza
e reinicia ambas as passagens antes de baseline.

| ID | Decision | Consequence |
|---|---|---|
| D-021-01 | Ratchet é fonte condicional material, não nona fonte cega. | Estado vazio/N/A exige razão recuperável. |
| D-021-02 | Relação material usa representação estruturada proporcional. | Texto com setas não prova caso complexo. |
| D-021-03 | Hook de agente revisor deriva materialidade das fontes concretas. | O corpus, não uma taxonomia de mocks, define o que precisa ser recuperável. |
| D-021-04 | Determinístico verifica apenas a integridade do hook. | Sem score de prosa/visual, reconhecimento de domínio ou aprovação automática. |

Mudanças serão aditivas para briefs novos. Brief histórico só migra com fonte
atualizada e revisão explícita. A execução posterior começa por T-001; T-004
depende de evidence aprovada de T-001–T-003 e não entrega baseline com REVISE.

## Coverage composition candidate — proposed

Esta é a disposição humana proposta para o candidato `evidence/T-000-stakeholder-brief.candidate.html`; ela não fecha o gate de coverage nem substitui a revisão distinta.

| Fonte / heading material | Alvo estável | Disposição proposta | Razão recuperável |
|---|---|---|---|
| `spec.md` / Problem, Objective and outcome, FR/AC, Risks | `#scope`, `#architecture`, `#validation` | synthesized + represented | Expõe a decisão que muda, os limites, requisitos e critérios sem criar taxonomia ou score. |
| `impact-map.md` / surfaces, IR-021-01–04 | `#impact` | represented | Mantém superfícies, sinais, controles, owners e impacto decisório. |
| `plan.md` / Approach, D-021-01–04 | `#architecture`, `#coverage` | represented | Mostra o encadeamento fonte condicional → hook → disposição → composição → revisão e o limite do contrato determinístico. |
| `tasks.md` / T-001–T-004 | `#execution` | represented | Projeta objetivos, dependências, inclusive evidence independente antes de T-004, validação, limite e status `pending`; não libera execução. |
| `validation-plan.md` / V-021-01–05 e regressões | `#validation` | represented | Relaciona AC, método/oráculo, raiz nova/oito consumidores/digests, re-review em dois passes e a limitação de que teste não aprova materialidade. |
| `decision-log.md` / D-021-001–004, D-021-100 | `#evolution`, `#decision` | represented | Distingue decisões aceitas da proposta de revisão deste candidato, sem simular aprovação. |
| `run-state.yaml` / quality_gates, next_safe_step | `#gates`, `#decision` | represented | Torna visíveis os gates ainda falsos e a próxima ação segura. |
| `progress.md` / Outcome context, Exact next safe step | `#decision` | represented | Mantém o checkpoint e a sequência de revisão independente. |
| `ratchet.md` / RATCHET-021-001 | `#ratchet` | represented | A fonte está material e não vazia: recupera falha, owner, consequência e check; não a trata como fonte universal cega. |

O candidato usa relações estruturadas proporcionais: a cadeia de governança é
uma tabela de relações com direção e consequência, e a arquitetura expõe o
limite entre corpus/hook humano e contrato determinístico. Sem JavaScript,
todas as oito views permanecem em ordem de fonte e abertas; o script, se
habilitado, serve apenas para navegação por abas.
