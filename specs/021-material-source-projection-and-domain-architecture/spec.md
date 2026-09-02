# SPEC 021 — Projeção de fontes materiais e arquitetura por domínio

**Status:** draft, source-only corrective initiative. **Owner:** Guardian maintainers.
**Risk:** high / A2. **Origin:** SPEC 020 T-004, 2026-08-28.

## Problem

Na suíte nova M-001–M-008, todos os HTMLs passaram promoção estrutural, mas as
sete lentes independentes recusaram baseline. A composição não projetou
`ratchet.md` quando continha regra material — e não declarava de modo
recuperável quando estava vazio. Ela também reduziu relações específicas de
arquitetura, dados, trust boundary, falha e recuperação a quatro nós genéricos
e texto com setas.

## Objective and outcome

Tornar recuperável no stakeholder brief: (a) toda fonte canônica que possa
mudar decisão, inclusive o estado justificado de `ratchet.md`; e (b) relações
arquiteturais que pedido e fontes tornem materiais, sem impor quota de abas,
cards, palavras ou SVG.

**Demonstrable increment:** inventário de fonte material, um hook de revisão
semântica orientado pelas fontes, compositor orientado por relações e regressões
positiva/negativa em domínios heterogêneos. **Non-goal:** implementar os
produtos mock, codificar uma taxonomia fixa de domínios, ou converter revisão
humana em score determinístico.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-021-01 | Quando `ratchet.md` contiver regra preventiva material, o HTML deve projetar gatilho, check, owner e consequência com proveniência; quando vazio, deve declarar esse estado/N/A com razão. |
| FR-021-02 | Quando fontes descrevem relação material entre componentes, dados, trust boundary, falha ou recuperação, o brief deve usar uma representação estruturada proporcional. |
| FR-021-03 | Antes da promoção/baseline, um hook de agente revisor, distinto do compositor, deve comparar pedido + todas as fontes canônicas + candidato. Ele determina materialidade no contexto do caso e registra `APPROVE`/`REVISE`, decisões ainda impossíveis, fontes/locators, impacto, reparo e N/A justificado. |
| FR-021-04 | O contrato determinístico pode verificar somente identidade distinta, o manifesto de entradas declarado pelo revisor, integridade/digests e a existência/escopo do registro semântico; ele não pode inferir quais fontes são materiais, pontuar prosa, contar elementos visuais, reconhecer domínios ou decidir suficiência semântica. |
| FR-021-05 | M-001–M-008 devem ser recompostos em raiz nova, como oito consumidores novos, com digests de request/fonte/HTML; as sete lentes os reavaliam nas duas passagens antes de baseline. Qualquer `REVISE` material exige corrigir fontes, rerenderizar e repetir ambos os passes. |

## Acceptance criteria

| ID | Criterion | Validation |
|---|---|---|
| AC-021-01 | Ratchet material e vazio justificado são recuperáveis no HTML, com locator/proveniência. | V-021-01 |
| AC-021-02 | O hook semântico detecta uma relação/decisão material ausente em domínio não predefinido e exige fonte, locator, impacto e reparo — sem taxonomia ou score rígido. | V-021-02 |
| AC-021-03 | Dois domínios arquiteturalmente distintos recuperam relações que seus pedidos/fontes tornam materiais; a representação é escolhida pela fonte, não por template fixo. | V-021-03 |
| AC-021-04 | Código só aceita o registro semântico de revisor distinto, ligado aos digests corretos; veredito humano, não o código, decide suficiência. | V-021-04 |
| AC-021-05 | Raiz nova com oito consumidores e digests request/fonte/HTML não recebe baseline com REVISE material; o reparo corrige fontes, rerenderiza e repete as duas passagens. | V-021-05 |

## Risks and constraints

- Preservar source-only scaffold, promoção por record exato, proveniência por
  bloco, Pearson opt-in e avaliação humana de SPEC 020.
- Ausência aceita somente com fonte/N/A justificado; nunca inventar arquitetura.
- O hook recebe o corpus efetivo, não rótulos de mock: pergunta o que um leitor
  não consegue decidir pelo HTML e exige uma razão citada para qualquer N/A.
- R-021-01: tornar ratchet universal; controle: materialidade e estado vazio.
- R-021-02: layout decorativo satisfazer relação; controle: hook semântico e
  revisão, sem detector de palavras, nós ou diagramas.

`evidence/T-000-mock-lab-reproduction.md` conserva a reprodução de T-004.
Esta SPEC não possui stakeholder HTML.
