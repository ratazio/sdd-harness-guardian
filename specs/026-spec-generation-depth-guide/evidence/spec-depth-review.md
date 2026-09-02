# Revisão independente de profundidade — SPEC 026

**Revisor:** `spec-depth-reviewer` (identidade independente do autor)  
**Data:** 2026-09-01  
**Entrada revisada:** pedido humano de enriquecimento incremental da autoria de SPEC; `spec.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `impact-map.md` e `run-state.yaml`.  
**Escopo:** qualidade da proposta; nenhuma task foi implementada e nenhum artefato canônico foi reescrito por este revisor.

## Veredito: REVISE

A proposta acerta o direcionamento principal: privilegia guia agêntico e revisão distinta, preserva Markdown canônico, veda Python/score/geração semântica e torna explícita a não invenção de caminhos e arquitetura. Contudo, dois pontos ainda deixam uma abertura incompatível com o limite pedido e com a promessa de baixo acréscimo de processo.

| ID | Fonte | Perda, deformação ou risco | Decisão prejudicada | Correção canônica requerida |
|---|---|---|---|---|
| R-026-01 | Pedido: quando não há informação de caminho/pasta, o criador não deve procurar como se soubesse onde está; deve confiar no pedido e declarar o limite. | O `plan.md`, na regra “Só existe raiz, sem caminho conhecido”, manda procurar proporcionalmente pelo domínio. Isso pode levar o autor a escolher por semelhança uma pasta, um teste ou uma arquitetura e apresentá-los como contexto material. | A decisão sobre onde a mudança ocorrerá e onde será testada pode parecer verificada sem uma fonte que realmente a sustente. | Restringir a inspeção a caminho explicitamente fornecido ou inequivocamente indicado por instrução/localizador existente. Quando só há uma raiz ambígua, registrar o limite e uma descoberta/dono; não fazer busca semântica para eleger uma superfície. Ajustar `FR-026-04`, a regra do plano e V-026-02 de forma coerente. |
| R-026-02 | Pedido: melhoria incremental, curta e simples; a única complexidade adicional aceita é guia/instrução e segundo olhar crítico. | T-004 exige duas calibrações e inclui uma “perda deliberada”, mas o plano não limita nitidamente a evidência a uma revisão leve de artefatos. Em execução, isso pode virar criação/recriação extensa de SPECs ou briefs de demonstração, ampliando o sistema em vez de comprovar o guia. | O decisor não consegue saber se autoriza uma mudança pequena de instrução ou uma nova frente de fixtures e renderização. | Delimitar T-004/V-026-04: usar artefatos mínimos existentes ou exemplos curtos somente de Markdown, sem renderizar HTML, sem criar pipeline/novo conjunto de mocks e sem torná-los fonte adicional de verdade. Manter o objetivo como evidência proporcional do guia e do revisor. |

## Condições preservadas após a correção

- O revisor deve continuar qualitativo: ausência justificada é aceitável e não há contagem, score ou quota visual.
- A saída precisa comparar pedido → SPEC → plano e, em `REVISE`, manter o encadeamento `fonte → perda → decisão → correção`.
- O compositor do stakeholder brief permanece agêntico; esta SPEC não deve adicionar gerador de narrativa, topologia, tasks ou HTML.

## Reavaliação dos reparos — 2026-09-01

**Escopo reavaliado:** exclusivamente R-026-01 e R-026-02 nos artefatos canônicos.

| Achado anterior | Evidência do reparo | Resultado |
|---|---|---|
| R-026-01 — busca/elegibilidade de superfície sem localizador | FR-026-04 agora permite inspeção somente com caminho explicitamente fornecido ou localizador/instrução inequivocamente acessível. A regra 4 do `plan.md` e V-026-02 proíbem busca semântica quando há apenas raiz ambígua. | Corrigido. |
| R-026-02 — calibração potencialmente expansiva | T-004 e V-026-04 agora limitam a entrega a dois exemplos curtos de Markdown e excluem expressamente mock, SPEC completa, pipeline, renderer, HTML e brief final. | Corrigido. |

## Veredito final: PASS

A SPEC permanece incremental: uma orientação curta, uma referência no fluxo existente e uma revisão qualitativa por identidade distinta. Ela não autoriza automação semântica, score, geração de HTML ou inspeção especulativa de código.

### Condições residuais de execução

- T-004 deve continuar sendo somente evidência breve de Markdown; se a execução exigir fixture persistente, renderização ou nova SPEC completa, o escopo deve retornar para decisão humana.
- Um localizador é “inequívoco” apenas quando a fonte acessível o aponta diretamente; similaridade de nome, busca por domínio ou escolha do agente não o substituem.
- A aprovação desta revisão avalia o pacote de planejamento, não autoriza as tasks preliminares nem substitui os gates posteriores.
