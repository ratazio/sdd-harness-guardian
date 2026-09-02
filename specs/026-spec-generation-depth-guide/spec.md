# SPEC 026 — Guia de profundidade para criação de SPEC

**Status:** spec_ready  
**Sequence:** 026  
**Owner:** Spec Guardian  
**Created / updated:** 2026-09-01  
**Risk:** low  
**Assurance profile:** A1-local

## 1. Problema

O ensaio M005 mostrou uma perda de informação antes da composição do brief: um pedido rico gerou uma SPEC e um `plan.md` resumidos; por isso o HTML final só conseguiu projetar cartões e explicações superficiais. O problema não é resolvido por exigir mais HTML do compositor: o autor da SPEC precisa obter e registrar as decisões que depois alimentam arquitetura, impactos, execução e validação.

## 2. Objetivo

Antes de uma SPEC ser declarada pronta, tornar explícitas as informações mínimas que sustentam uma decisão de produto/técnica e obter uma segunda leitura independente que confronte o pedido original com a SPEC e seu plano.

## 3. Resultado de entrega

- **Resultado para o usuário:** uma SPEC nova preserva o contexto necessário para que pessoas e agentes entendam o que muda, por que muda, como será provado e o que ainda não se sabe.
- **Incremento demonstrável:** um guia reutilizável de autoria e uma revisão independente de profundidade, aplicados a dois casos de calibração: pedido com repositório acessível e pedido sem caminho de código.
- **Fronteira do slice:** orientação para agentes e um papel revisor; não um novo mecanismo de geração de SPECs.
- **Fonte de prioridade:** pedido humano e evidência M005.

## 4. Atores

- **Autor da SPEC:** investiga as fontes disponíveis, registra fatos, limites e descobertas.
- **Revisor de profundidade:** identidade distinta que avalia se relações materiais do pedido sobreviveram na SPEC e no plano.
- **Decisor humano:** resolve prioridades, lacunas materiais e conflitos de fonte.

## 5. Resultados observáveis

- **O-026-01:** a SPEC separa fato solicitado, fato verificado no repositório, inferência limitada e descoberta pendente.
- **O-026-02:** o `plan.md` contém material suficiente para orientar construção humana do brief, sem transformar o compositor em resumidor automático.
- **O-026-03:** uma revisão independente retorna `PASS` ou `REVISE` com correções rastreáveis.

## 6. Não objetivos

- Não criar Python, score numérico, banco de dados, sidecar JSON ou pipeline novo que gere narrativa, topologia, tasks ou HTML.
- Não tornar pesquisa externa obrigatória nem inventar caminhos, módulos, testes ou arquitetura quando a fonte não os estabelece.
- Não alterar o renderer, o template visual, as regras de promoção ou a composição final do stakeholder brief nesta SPEC.
- Não impor quantidade fixa de palavras, cartões, diagramas ou seções a toda SPEC.

## 7. Requisitos funcionais

| ID | Requisito | Racional |
|---|---|---|
| FR-026-01 | O bundle DEVE fornecer um guia curto, legível por agente, para autoria aprofundada de SPEC. | Reutilizar a estrutura agêntica existente sem novo motor. |
| FR-026-02 | O guia DEVE solicitar, quando aplicável: resultado e porquê; atores; contexto/impacto arquitetural; superfícies alteradas, preservadas e fora de escopo; dados/contratos; falhas e recuperação; impactos/riscos; incrementos de task; validação, evidência e critérios de aceite; incertezas e dono. | São as relações mínimas que sustentam as subpáginas e a decisão. |
| FR-026-03 | O guia DEVE orientar o autor a registrar o tipo de cada informação: pedido, inspeção de fonte, inferência limitada ou descoberta. | Evita preencher lacunas como se fossem fatos. |
| FR-026-04 | Quando um caminho de código/teste for explicitamente fornecido ou inequivocamente indicado por uma instrução/localizador acessível, o autor DEVE inspecioná-lo e registrar o local relevante de mudança e teste. Sem esse localizador, DEVE declarar a ausência, não procurar por semelhança, não adivinhar um caminho e limitar-se ao pedido. | Uma SPEC genérica precisa funcionar com e sem acesso ao projeto. |
| FR-026-05 | O guia DEVE apontar os artefatos Markdown canônicos já existentes onde cada resposta vive, incluindo o registro de construção do brief em `plan.md`. | Aumenta profundidade sem criar uma segunda fonte de verdade. |
| FR-026-06 | A criação de uma SPEC DEVE receber revisão por uma identidade distinta, `spec-depth-reviewer`, antes de `Spec Ready`. | Introduz o segundo olhar crítico solicitado. |
| FR-026-07 | Em `REVISE`, o revisor DEVE registrar no formato `fonte → fato/relação perdida ou deformada → decisão prejudicada → correção canônica`. | A crítica torna-se acionável, sem rubricar estética ou volume. |
| FR-026-08 | A revisão DEVE ser qualitativa, proporcional ao pedido e capaz de aceitar ausência justificada; não DEVE usar contagem, score ou quota visual como gate. | Evita burocracia e determinismo disfarçados. |
| FR-026-09 | Antes de abrir discoveries, o autor DEVE preservar nos artefatos canônicos cada fato ou relação material já fornecido pelo pedido — incluindo entrega, limite, risco/controle, critério de aceite, prova e incremento de task quando aplicáveis. Quando o pedido exige que algo seja definido, aplicado ou validado mas não informa seu valor/mecanismo, a obrigação e sua prova permanecem requisito; somente o detalhe ausente vira discovery. | Evita que a disciplina de não invenção comprima informação confiável da fonte. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-026-01 | Existe um único guia reutilizável que cobre as perguntas mínimas e a classificação de evidência. | V-026-01 |
| AC-026-02 | O guia deixa explícita a regra para raiz/caminho de código presente, ausente ou contraditório. | V-026-02 |
| AC-026-03 | Uma identidade independente consegue emitir `PASS` ou `REVISE` comparando pedido → SPEC → plano, sem implementar nem reescrever a SPEC. | V-026-03 |
| AC-026-04 | Uma calibração Markdown mínima sobre M005 registra relações suficientes para enriquecer arquitetura, impacto, execução e validação; um exemplo mínimo sem localizador de código declara descoberta/limite sem fabricar estrutura. | V-026-04 |
| AC-026-05 | O fluxo continua agêntico: scripts podem verificar estrutura, mas não sintetizam conteúdo, escolhem formas visuais ou geram o HTML final. | V-026-05 |
| AC-026-06 | Uma revisão de regressão sobre pedidos ricos demonstra que fatos materiais fornecidos continuam recuperáveis entre pedido, SPEC, impacto, plano, tasks e validação; discoveries cobrem somente fatos ausentes, inclusive quando a fonte exige uma política/controle sem fixar seu valor. | V-026-06 |

## 9. Casos de borda e falhas

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-026-01 | Pedido não informa repositório ou caminho-fonte. | Registrar limite de fonte; não supor árvore; criar descoberta somente se a ausência bloquear decisão. |
| EC-026-02 | Repositório acessível contradiz o pedido. | Registrar contradição, fonte e decisão pendente; não escolher silenciosamente. |
| EC-026-03 | Mudança localizada não tem impacto arquitetural material. | Registrar ausência proporcional e explicar por que uma topologia não melhora a decisão. |
| EC-026-04 | Revisor encontra uma SPEC genérica que apenas repete o pedido. | Emitir `REVISE` apontando a relação perdida e o artefato a corrigir. |
| EC-026-05 | Autor conhece o resultado/limite pedido, mas não conhece o detalhe de implementação. | Registrar o resultado/limite como fato do pedido e abrir discovery apenas para a decisão técnica ausente. |

## 10. Restrições e riscos

- **Arquitetura:** modificar somente orientação/papel de revisão e suas referências; não criar serviço ou runtime.
- **Dados e privacidade:** nenhuma nova coleta ou persistência.
- **Operação:** revisão é gate de qualidade da SPEC, não autorização de implementação.
- **Risco R-026-01:** o guia virar checklist burocrático. **Mitigação:** perguntas condicionais e revisão por perda de decisão, não por contagem.
- **Risco R-026-02:** o autor inventar detalhes técnicos. **Mitigação:** classificação de fonte e regra explícita para caminhos ausentes.
- **Risco R-026-03:** revisor carimbar superficialmente. **Mitigação:** `REVISE` rastreável e identidade distinta.
- **Risco R-026-04:** a regra de não invenção causar omissão de fato já explícito. **Mitigação:** passada qualitativa de preservação de fonte e regressão M-001/M-004/M-006.

## 11. Decisão do Spec Guardian

**Outcome Ready:** yes  
**Spec Ready:** yes — reaberta para correção incremental T-005 após a regressão heterogênea.  
**Reviewer:** `spec-depth-reviewer` (identidade distinta do autor)  
**Reviewed at:** 2026-09-01  
**Decision evidence:** [evidence/spec-depth-review.md](./evidence/spec-depth-review.md) — `PASS` após correção de R-026-01 e R-026-02.  
**Blocking issues:** nenhum para a qualidade da SPEC; autorização humana posterior continua necessária para tornar tasks `ready`.
