# SPEC 020 — isolamento de fonte e composição canônica do stakeholder brief

**Status:** in_review · **Owner:** platform-engineering · **Risk:** high · **Assurance:** A2-elevated

## Problema

Na rodada de mocks de 2026-08-28, um brief de conciliação financeira exibiu resíduos do caso de blog: cookie/browser, `PATCH` de publicação e tasks de notícias. Outros briefs perderam a shell v2 ou reduziram relações, contratos, riscos e provas a texto genérico. O scaffolder ainda materializava uma página HTML vazia, que pôde ser aberta como se fosse uma entrega.

Isso rompe a confiança do leitor: a fonte pode estar correta, mas o HTML pode pertencer a outra iniciativa, omitir decisões materiais ou apenas parecer pronto.

## Objetivo

Fazer com que um stakeholder brief só possa ser materializado a partir de candidato explicitamente revisado, isolado para uma iniciativa e ligado às suas fontes; impedir que casca, conteúdo de outro caso ou identidade de marca incompatível sejam apresentados como brief ou entrega.

## Resultado de entrega

- **Resultado para usuário:** página decisória confiável, cuja proveniência, fase e limites são recuperáveis sem abrir Markdown.
- **Incremento demonstrável:** scaffolding source-only; promoção guardada por revisão/digest; detecção de mistura de fontes; mocks em raiz nova.
- **Limite:** não criar gerador determinístico de prosa, diagramas ou quantidade fixa de abas. Profundidade continua julgamento independente.
- **Prioridade:** redução de risco e decisão humana de 2026-08-28.

## Atores

Autor/agente de SPEC; revisor de cobertura; revisor renderizado independente; arquiteto, delivery manager, diretor/C-level, desenvolvedor e stakeholder decisor.

## Resultados observáveis

- **O-001:** iniciativa recém-criada não contém `stakeholder-brief.html`.
- **O-002:** promoção exige candidato, revisão distinta e SHA-256 exato; casca ou hotlink é recusado sem criar HTML.
- **O-003:** mock aprovado tem julgamento HTML-first e depois comparação com fontes, sem esconder `REVISE` material.

## Não objetivos

- Provar qualidade por contagem de palavras, cards, abas, SVG ou CSS.
- Inventar arquitetura, API, dados ou testes quando a fonte não os sustenta.
- Alterar produtos consumidores, banco de dados ou integrações externas.

## Requisitos funcionais

| ID | Requisito |
|---|---|
| FR-001 | Ao criar iniciativa, o sistema deve criar somente fontes canônicas e estado `not_rendered`, sem HTML ou asset de marca. |
| FR-002 | Ao promover candidato, o sistema deve exigir fase, cobertura aprovada, autor/revisor distintos, registro resolvido e digest do candidato. |
| FR-003 | O promotor deve rejeitar shell, placeholders, HTML pré-render, sobrescrita, hotlink, logo/localidade ou acessibilidade Pearson inválidos. |
| FR-004 | A composição e o mock lab devem isolar a iniciativa: fatos sentinela, tasks, contratos e arquitetura de outro mock não podem aparecer no brief. |
| FR-005 | Cada bloco material deve declarar fonte permitida, locator e digest da iniciativa; bloco sem origem local verificável é recusado, sem usar score de prosa. |
| FR-006 | Todo mock deve receber avaliação humana em duas passagens: HTML sozinho; depois HTML comparado ao pedido original e todos os Markdown canônicos, por lentes independentes. |

## Critérios de aceite

| ID | Critério | Validação |
|---|---|---|
| AC-001 | Scaffold não produz HTML/asset e o validador rejeita HTML antes de `rendered`. | V-001, V-002 |
| AC-002 | Promoção aceita apenas candidato revisado e rejeita casca, reclassificação, hotlink e sobrescrita. | V-003, V-004 |
| AC-003 | Cada mock novo mantém apenas fatos da própria fonte; origem por bloco confere e não há resíduo do mock de notícias na conciliação. | V-005 |
| AC-004 | Nenhum mock é aprovado se qualquer lente encontrar lacuna material de narrativa, dados, arquitetura, execução, validação ou visual nas duas passagens. | V-006 |
| AC-005 | Relações materiais — subarquiteturas, dados, contratos, falhas, operação e validação — são visualizadas/explicadas ou recebem N/A justificado pela fonte. | V-006 |

## Falhas e limites

| Condição | Comportamento esperado |
|---|---|
| Fonte insuficiente | Registrar pergunta/owner e bloquear a decisão; não preencher com prosa genérica. |
| Candidato divergente após revisão | Digest não confere; promoção recusa. |
| HTML visualmente elegante, mas superficial | Revisão humana marca `REVISE`; não há baseline/entrega. |
| Projeto não-software | Rubrica adapta superfícies e usa N/A justificado; não exige diagrama técnico artificial. |

## Restrições

- Manter contratos v2, tabs quando usados, no-script, print, responsividade, foco e reduced motion.
- Pearson é perfil explícito no HTML renderizado, com logo local aprovado; não há hotlink nem `role="img"` na âncora.
- Determinismo verifica integridade e linhagem, nunca pontuação de prosa.

## Riscos

| ID | Risco | Mitigação |
|---|---|---|
| R-001 | Gate rígido impede caso incomum. | N/A com razão, rubrica contextual e revisão humana. |
| R-002 | Revisor alegado sem revisão real. | Identidades distintas, locator e digest; pós-review obrigatório. |
| R-003 | Vazamento entre casos. | Raízes descartáveis, sentinelas e comparação fonte→HTML. |

## Protocolo obrigatório de revisão de mocks

As sete lentes mínimas são **arquiteto**, **system designer**, **delivery
manager**, **diretor**, **C-level**, **desenvolvedor** e **stakeholder geral**;
uma identidade não pode revisar o próprio brief. Todas fazem: (1) HTML isolado,
sem MD; (2) pedido original + todos os MD + HTML. Em cada fase registram
APPROVE/REVISE, severidade, decisão que não conseguiram tomar, fonte/locator e
reparo. A matriz registra digests de pedido/fontes/HTML. Qualquer REVISE
material bloqueia baseline/aprovação do mock e, se a causa for sistêmica, abre
SPEC corretiva sob a autorização humana já concedida.

## Decisão do Spec Guardian

**Outcome Ready:** sim · **Spec Ready:** pendente de revisão independente das fontes.
