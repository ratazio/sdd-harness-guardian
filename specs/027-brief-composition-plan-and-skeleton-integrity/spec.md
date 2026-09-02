# SPEC 027 — Plano de composição e integridade do skeleton

**Status:** spec_ready  
**Sequence:** 027  
**Owner:** Guardian maintainers + brief experience owner  
**Created / updated:** 2026-09-01  
**Risk / assurance:** medium / A2-elevated

## 1. Problema

A R3 de SPEC 026 confirmou que as fontes Markdown podem preservar relações
materiais. Ela também revelou uma quebra posterior: alguns `plan.md` tinham
apenas um parágrafo de cobertura, e candidatos como M001–M003 declararam o
hash de um skeleton local rico, mas substituíram sua casca por HTML/CSS mínimo.
O guard atual reconhece rotas, classes e hash; não prova que a cópia física do
skeleton foi preenchida *in situ*. O resultado pode ser semanticamente
rastreável e, ainda assim, ser visualmente cru, sem subpáginas dignas de
reunião ou representação das relações previstas.

## 2. Objetivo

Fazer da composição de brief uma cadeia única e verificável:

```text
Markdown canônico → plano de composição revisado em plan.md
→ cópia preservada do skeleton local → candidate agêntico
→ revisão visual/estrutural distinta → promoção dos bytes exatos
```

O objetivo não é gerar HTML por código, impor diagramas nem selecionar uma
marca. É impedir que o plano esqueça decisões visuais materiais e que um agente
recrie o brief fora do skeleton aprovado.

## 3. Resultado de entrega

- **Resultado para o usuário:** todo candidate apresenta uma narrativa e uma
  estrutura visual coerentes antes de qualquer promoção; não há página mínima
  disfarçada de composição.
- **Incremento demonstrável:** uma composição que recompõe um candidate a
  partir do skeleton, mantém sua casca e recebe `APPROVE` distinto após
  comparação com plano, fontes, experiência desktop e navegação.
- **Fronteira do slice:** plano de composição, contractos do skeleton,
  guard/hook e revisão. Não redesenha identidade, não escolhe Pearson e não
  promove os candidatos R3 atuais.
- **Fonte de prioridade:** pedido humano explícito e diagnóstico da R3.

## 4. Atores

| Ator | Responsabilidade |
|---|---|
| Autor do plano | Traduzir fontes canônicas em decisões narrativas e visuais no `plan.md`. |
| Compositor | Copiar o skeleton local e preencher somente seus slots com HTML/CSS/JS agêntico e fonte-apoiado. |
| Revisor de composição | Identidade distinta; compara fontes, plano, candidate e experiência desktop. |
| Renderer/State Keeper | Promover somente bytes exatos já revisados; nunca compor ou redesenhar. |

## 5. Resultados observáveis

- **O-027-01:** todo `plan.md` v2 contém um plano de composição por rota e por
  item repetido material (task, prova, impacto, domínio ou decisão).
- **O-027-02:** a revisão independente retorna `PASS`/`REVISE` para o plano
  antes da instância do skeleton e registra perda → decisão prejudicada →
  correção canônica.
- **O-027-03:** candidato que conserva hash mas substitui shell, stylesheet ou
  regiões imutáveis do skeleton falha antes de revisão qualitativa.
- **O-027-04:** candidate aprovado tem uma rota principal por vez, navegação
  desktop verificável e conteúdo/fatos escolhidos pelo plano; a forma continua
  proporcional e agêntica.
- **O-027-05:** a suíte heterogênea comprova o contrato sem regra específica
  para um mock, domínio, marca ou arquitetura.

## 6. Não objetivos

- Tornar Pearson obrigatório ou alterar agora a escolha vendor-neutral.
- Criar parser de Markdown, score, quota de cards/gráficos, JSON ou gerador
  determinístico de narrativa, arquitetura ou HTML.
- Obrigar SVG, topologia, frontend, tarefa, prova ou arquitetura em casos onde
  as fontes não os tornam materiais.
- Promover, corrigir manualmente ou reclassificar os HTMLs da R3 como final.

## 7. Requisitos funcionais

| ID | Requisito | Racional |
|---|---|---|
| FR-027-01 | O bundle DEVE fornecer, dentro do `plan.md` existente, um scaffold reutilizável de plano de composição com capítulos/linhas para tese, rota, questão executiva, arco narrativo, fonte/locator, relação a tornar visível, forma escolhida e razão, alvo/slot, repetição, ausência/discovery e ação de fechamento. | A forma é planejada sem criar outra fonte de verdade. |
| FR-027-02 | O scaffold DEVE distinguir cobertura de construção: mapa fonte→alvo não substitui a decisão de como uma subpágina explica a relação. | Um parágrafo de cobertura não orienta storytelling. |
| FR-027-03 | Um revisor distinto DEVE avaliar pedido/fontes → artefatos → plano de composição antes de instanciar o skeleton; `REVISE` usa `fonte → perda/ambiguidade → decisão prejudicada → correção canônica`. | Evita que superficialidade chegue ao HTML. |
| FR-027-04 | O template/skeleton DEVE marcar casca imutável e slots composáveis. A instância conserva contrato de rota, fallback, navegação, estilos-base e identidade selecionada; o compositor preenche slots, não reconstrói o documento. | Torna “copiar e preencher” verificável. |
| FR-027-05 | O hook de herança DEVE verificar a preservação material da casca local — inclusive stylesheet-base e estrutura/rotas/slots — além do hash declarado. Ele DEVE rejeitar uma mini-página paralela com hash copiado. | O guard atual aceita a regressão observada. |
| FR-027-06 | O hook permanece estreito: não lê Markdown para escrever conteúdo, não decide suficiência, não escolhe visual e não pontua beleza. | Julgamento editorial continua agêntico. |
| FR-027-07 | O compositor DEVE partir da cópia física do `stakeholder-brief.skeleton.html` e pode acrescentar conteúdo e visuais fonte-apoiados somente nos slots previstos ou em extensão explicitamente autorizada pelo contrato. | Protege a linguagem visual aprovada sem engessar o domínio. |
| FR-027-08 | A revisão de candidate DEVE incluir inspeção desktop da rota/navegação e comparar plano, fontes e forma resultante. Ela pode aprovar ou reprovar mesmo com hook verde. | Checks estruturais não provam experiência executiva. |
| FR-027-09 | A promoção DEVE receber somente o candidate exato que a revisão vinculou; renderização não é uma etapa de embelezamento ou recomposição. | O candidate é a proposta final, ainda não entregue. |
| FR-027-10 | A regressão DEVE usar casos heterogêneos e validar comportamento comum; nenhuma regra, exceção ou visual pode ser codificado para os mocks usados como evidência. | O contrato precisa servir a qualquer SPEC. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-027-01 | O scaffold em `plan.md` comporta software, operação, política ou pesquisa e obriga resposta/ausência justificada para as oito rotas e itens repetidos aplicáveis. | V-027-01 |
| AC-027-02 | Um plano de cobertura raso, sem narrativa/relação/forma/fechamento, recebe `REVISE` distinto; um plano proporcional e fonte-apoiado pode passar sem quota. | V-027-02 |
| AC-027-03 | O skeleton local expõe regiões imutáveis e slots composáveis sem mudar a identidade vendor-neutral selecionada por padrão. | V-027-03 |
| AC-027-04 | Um candidate construído do zero, mesmo com hash/base/IDs válidos, falha no hook; cópia do skeleton com preenchimento de slots passa. | V-027-04 |
| AC-027-05 | A revisão independente encontra rota sem storytelling, relação visual material ou navegação desktop, mesmo quando os checks determinísticos passam. | V-027-05 |
| AC-027-06 | Regressão heterogênea cria candidates não promovidos; nenhum HTML final, gate ou regra específica de fixture é criado. | V-027-06 |
| AC-027-07 | O diff confirma que nenhum script novo gera narrativa, escolhe diagrama ou altera HTML fora do contrato de integridade. | V-027-07 |

## 9. Casos de borda e falha

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-027-01 | SPEC simples não possui arquitetura ou coleções repetidas materiais. | Plano usa ausência fonte-apoiada; não força gráfico ou dossiê fictício. |
| EC-027-02 | Fonte exige relação material, mas a forma visual ainda é incerta. | Plano fica em `REVISE`; agente escolhe forma antes do skeleton, não depois da promoção. |
| EC-027-03 | Compositor precisa de estilo complementar para uma relação fonte-apoiada. | Adiciona-o no slot/extensão permitida sem apagar shell, rotas, fallback ou estilo-base. |
| EC-027-04 | Hook verde, porém candidate parece cru, usa scroll como rota ou não entrega a história planejada. | Revisor devolve `REVISE`; candidate não é promovido. |
| EC-027-05 | Perfil de marca não está selecionado nas fontes. | Mantém vendor-neutral; nenhuma decisão sobre logo bloqueia esta iniciativa. |

## 10. Restrições e riscos

- **Arquitetura:** mudança limitada a template/skeleton, instrução, hook e
  revisão; nenhuma API, banco, telemetria ou serviço novo.
- **Acessibilidade:** preservar fallback sem JS, foco, teclado, impressão e uma
  rota principal visível por vez após aprimoramento.
- **R-027-01:** guard vira parser estético. **Controle:** compara regiões e
  bytes/estrutura aprovados, não texto ou beleza.
- **R-027-02:** scaffold vira checklist vazio. **Controle:** revisão decide
  materialidade e pode aceitar N/A fundamentado.
- **R-027-03:** base imutável impede composição. **Controle:** slots ricos e
  extensão delimitada; agente mantém escolha de forma e conteúdo.
- **R-027-04:** visual bonito perde fonte. **Controle:** plano, proveniência e
  revisão distinta permanecem obrigatórios.

## 11. Dependências

| Dependência | Estado | Owner | Bloqueia? |
|---|---|---|---|
| Contrato v3/skeleton da SPEC 025 | existente, mas incompleto no guard | Guardian maintainers | sim |
| `stakeholder-brief-design.md` vendor-neutral | existente | brief experience owner | não |
| Skills de composição e experiência | existentes | Guardian maintainers | sim |
| Corpus heterogêneo de mock lab | existente, somente regressão | mock-lab maintainer | sim |

## 12. Decisão do Spec Guardian

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** `/root/spec027_depth_review` (identidade distinta do autor)  
**Blocking issues:** nenhum para a qualidade da SPEC; tarefas aguardam autorização humana.  
**Decision evidence:** [revisão independente](./evidence/spec-depth-review.md) — `PASS` em 2026-09-01.
