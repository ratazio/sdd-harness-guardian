# Spec: 009-stakeholder-brief-tabbed-decision-surface

**Status:** spec_ready  
**Sequence:** 009  
**Owner:** platform-engineering  
**Created / updated:** 2026-08-26  
**Risk:** medium  
**Assurance profile:** A2-elevated

## 1. Problem

O stakeholder brief v2 concentra valor, arquitetura, impacto, execução,
validação, evolução, decisão e cobertura em uma única leitura vertical. Embora
completo, isso torna a reunião cansativa, esconde a intenção de cada domínio e
incentiva sínteses superficiais — principalmente em execução e validação, onde
títulos de task não explicam o que será entregue, provado ou evitado.

O mesmo padrão deve continuar útil para software, operações, pesquisa, política
e mudanças locais. Nem toda iniciativa possui arquitetura rica, testes ou
detalhes de entrega. A ausência de fatos não pode ser preenchida por texto
genérico, nem a nova interface pode exigir informação que não seja material.

## 2. Objective

Fazer cada brief v2 ser uma única página HTML offline, organizada em abas
acessíveis e progressivas, onde cada visão apresenta sua missão, contexto e
profundidade recuperável a partir dos Markdown canônicos — e onde lacunas
materiais são explicitamente descobertas ou perguntadas antes de serem
inventadas.

## 3. Delivery outcome

- **Produto/usuário:** stakeholders conseguem abrir apenas a visão relevante
  para a decisão atual e entender seu propósito antes dos detalhes; autores
  recebem sinais claros de quando o Markdown não sustenta essa visão.
- **Incremento demonstrável:** um brief v2 de referência alterna entre oito
  abas na mesma URL/documento, preserva leitura completa sem JavaScript e em
  impressão, e mostra task/validação com profundidade derivada das fontes.
- **MVP/slice:** contrato de informação, guidance de discovery, template/CSS
  de aba, fixtures e checks proporcionais para briefs v2 novos ou
  materialmente atualizados. Não há roteador, página separada, framework,
  serviço ou avaliação semântica automática.
- **Prioridade:** solicitação explícita do mantenedor em 2026-08-26, motivada
  pela leitura do sandbox news/blog.

## 4. Users or actors

- **Stakeholder decisor:** alterna para valor, risco, decisão ou execução sem
  percorrer informação de outro domínio.
- **Spec author / planner:** compõe cada aba a partir de Markdown e registra a
  falta material como pergunta ou unknown acionável.
- **Builder / evaluator:** recupera task, contrato, evidência e critério de
  aceite com detalhe suficiente para construir e revisar sem adivinhação.
- **Leitor operacional não-software:** vê contexto, handoffs, controles e
  decisões sem terminologia de API ou diagrama decorativo.

## 5. Observable outcomes

- **O-001:** a navegação apresenta oito abas: Valor e escopo, Arquitetura,
  Impacto, Execução, Validação, Evolução, Decisão e Cobertura; um clique/foco
  mostra a visão correspondente dentro do mesmo HTML.
- **O-002:** cada aba abre com uma missão e uma visão textual próprias; ela só
  mostra blocos cujo fato seja sustentado por fonte canônica ou por uma
  disposição explícita de ausência/unknown.
- **O-003:** a aba Execução descreve cada task com outcome, escopo, limites,
  dependências, risco, validação, evidência e exit criteria, quando esses
  dados existirem em `tasks.md`.
- **O-004:** a aba Validação apresenta a matriz AC → método/ambiente → oracle
  → evidência e explica validações não aplicáveis ou não disponíveis.
- **O-005:** quando uma informação material prevista para uma visão não está
  nos Markdown, o processo cria pergunta específica para o owner ou unknown
  com impacto e caminho de resolução; não usa placeholder ou prosa inventada.
- **O-006:** um brief simples pode apresentar N/A justificado ou uma visão
  compacta sem diagrama e sem formulário de esclarecimento desnecessário.

## 6. Non-goals

- **NG-001:** transformar o brief em múltiplos arquivos, rotas, aplicação web
  ou dependência externa.
- **NG-002:** obrigar arquitetura, diagrama, dados, testes, comandos ou task
  detalhada quando a fonte prova que o tópico não é material.
- **NG-003:** criar score de qualidade, contagem de campos/palavras, parser de
  prosa, LLM juiz, schema semântico ou aprovação automática.
- **NG-004:** preencher lacunas com fatos fictícios fora de sandbox autorizado,
  ou bloquear uma iniciativa simples apenas por não possuir detalhe técnico.
- **NG-005:** migrar briefs v1 históricos sem refresh material e decisão de
  migração existente.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | O template v2 SHALL manter um único `stakeholder-brief.html` offline e apresentar as oito visões como abas acessíveis, sem trocar URL para outro arquivo. | A organização visual não pode fragmentar a fonte de leitura. |
| FR-002 | Cada aba SHALL declarar uma missão curta e uma visão textual inicial: valor/escopo explica missão, valor, outcome, limite, risco e autoridade; arquitetura e impacto explicam missão/visão antes dos detalhes. | A aba deve orientar a leitura, não só agrupar tabelas. |
| FR-003 | A composição SHALL usar fatos de fonte, `not_applicable` justificado ou unknown acionável; para lacuna material, o autor SHALL formular pergunta, owner, impacto **na decisão** e caminho de resolução. | Evita invenção e placeholders, preservando descoberta proporcional. |
| FR-004 | Execução SHALL projetar o contrato completo de cada task disponível: objetivo/outcome, FR/AC, incremento, escopo/anti-escopo, artefatos/contratos, dependências, risco, assurance, validação, evidência, exit criteria e por que é o próximo passo seguro. | Títulos não bastam para orientar implementação ou avaliação. |
| FR-005 | Validação SHALL projetar a rastreabilidade de AC, método, comando ou ambiente, fixture, oracle, evidence pack e limite/skip justificado. | Uma decisão de qualidade exige entender o que a prova demonstra. |
| FR-006 | Arquitetura, impacto, fluxo, dados e controles SHALL usar o perfil proporcional existente: incluir visual/estrutura somente quando há relação material; caso contrário declarar N/A/unknown com fonte. | Generaliza para contextos não-software e mudanças pequenas. |
| FR-007 | Sem JavaScript, com teclado, em 390px e em impressão, o leitor SHALL recuperar todas as visões e seu conteúdo sem depender de cor, hover ou painel oculto. | A aba é melhoria progressiva, não barreira de acesso. |
| FR-008 | A evolução SHALL mostrar decisões, gates, estado verdadeiro, unknowns e próximo passo; a decisão SHALL mostrar owner, consequência, autorização e próxima ação exata. | Estado e autoridade não podem ficar dispersos. |
| FR-009 | Provenance v2, cobertura humana, lifecycle e compatibilidade v1 SHALL permanecer compatíveis; abas são projeção, nunca fonte canônica adicional. | Preserva contratos existentes e evita sidecar. |
| FR-010 | Checks determinísticos SHALL validar estrutura, fallback, provenance e wiring estáveis, mas SHALL NOT declarar profundidade, qualidade semântica ou estética como aprovação automática. | Mantém julgamento contextual independente. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | Uma referência v2 contém as oito abas, uma única página HTML e painel ativo discernível; não cria arquivo/rota por aba. | V-001 |
| AC-002 | Cada aba inclui missão/visão e apenas blocos sustentados por fonte, N/A justificado ou unknown acionável. | V-002, E-001 |
| AC-003 | Valor e escopo exibem missão, pilares de valor, pilares técnicos altos quando materiais, outcome, limite, risco principal e autoridade atual. | V-003, M-001 |
| AC-004 | Arquitetura e impacto exibem introdução própria e detalhe proporcional; exemplos simples/não-software não recebem visual ou detalhe fabricado. | V-004, E-002 |
| AC-005 | Cada task material no fixture rico é recuperável como contrato de execução, não apenas título/estado. | V-005, M-002 |
| AC-006 | A matriz de validação permite recuperar AC, método, ambiente/comando, oracle e evidência ou razão de ausência. | V-006, M-003 |
| AC-007 | Falta material nas fontes produz pergunta/unknown com owner, impacto na decisão e resolução; falta não material não gera burocracia. | V-007, E-003 |
| AC-008 | Teclado, no-script, 390px e print preservam acesso a todo conteúdo; a aba não depende somente de JavaScript. | V-008, M-004 |
| AC-009 | v1 permanece no caminho legado e a projeção v2 mantém provenance, coverage e estados/gates sem nova fonte de verdade. | V-009, V-REG-001 |
| AC-010 | Nenhum score, parser semântico, LLM juiz ou gate automático de conteúdo é introduzido. | V-010, V-REG-002 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Iniciativa tem uma alteração local e arquitetura é somente uma fronteira. | Aba Arquitetura mostra visão curta e N/A/omissão fundada; não cria diagrama ornamental. |
| EC-002 | `tasks.md` contém somente discovery ou uma task ainda sem contrato detalhado. | Aba Execução mostra o que existe, marca a lacuna específica e aponta owner/resolução; não inventa implementação. |
| EC-003 | Não existe comando/teste aplicável. | Aba Validação explica o motivo, risco residual, owner e a prova manual/operacional proporcional, se houver. |
| EC-004 | JavaScript falha, está desativado ou leitor imprime o arquivo. | Todos os painéis ficam recuperáveis por âncora/details/ordem de documento e print revela conteúdo. |
| EC-005 | Uma fonte contradiz o brief ou um fato material não é recuperável em uma aba. | Reviewer devolve para correção canônica; HTML não é corrigido isoladamente. |
| EC-006 | A pergunta de discovery exige decisão de produto/negócio não registrada. | Processo para antes do gate afetado e pede esclarecimento humano específico. |

## 10. Constraints and non-functional requirements

- **Architecture:** HTML único, assets inline ou locais; nenhum framework,
  roteador, rede ou estado persistente novo.
- **Security/privacy:** não expor PII, credenciais ou topologia sensível;
  unknowns descrevem a necessidade sem revelar dados.
- **Data:** Markdown, estado e decision log continuam canônicos; o brief é
  derivado e não recebe sidecar de composição.
- **Performance/reliability:** alternância local e determinística; sem
  carregamento remoto; falha de script mantém leitura íntegra.
- **Compatibility/accessibility:** manter v1; v2 atende teclado, foco visível,
  semântica de aba/painel ou equivalente acessível, 390px, contraste e print.
- **Operational:** design deve caber em bundles consumidores sem exigir setup;
  as perguntas de discovery ficam em fontes existentes, com checkpoint.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| O brief v2 já possui seções ancoradas e provenance local que podem ser reorganizadas sem criar fonte paralela. | T-001 / planner verifica template, validator e fixtures. |
| Um padrão de abas pode ser enhancement progressivo com fallback nativo. | T-001 / accessibility reviewer valida protótipo sem script e teclado. |
| O contrato detalhado de task já é canônico em `tasks.md`. | T-003 / planner compara template, sandbox e fixtures. |
| Nem toda fonte terá todos os fatos de uma aba. | T-003 / discovery policy define pergunta ou N/A proporcional. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Aba oculta decisão material ou cria ilusão de página incompleta. | medium | high | Fallback completo, indicadores de conteúdo e review pós-render; template owner. |
| R-002 | Profundidade vira checklist rígido para iniciativa simples/não-software. | medium | high | Missão fixa, conteúdo condicional e N/A/unknown fundamentado; Spec Guardian. |
| R-003 | Detalhe de task/validação diverge dos Markdown. | medium | high | Provenance por bloco, composição/review e fixtures ricos; planner/reviewer. |
| R-004 | Perguntas de discovery viram burocracia ou impedem avanço sem motivo. | medium | medium | Só perguntar quando a falta bloqueia decisão material; registrar impacto/owner; Orchestrator. |
| R-005 | Interação de abas falha em teclado, sem script, narrow ou print. | medium | high | Protótipo progressivo e checks manuais/automatizados; accessibility reviewer. |
| R-006 | Validator passa a medir prosa. | low | high | FR-010 e diff review; maintainer. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| v2 brief template/design, Human Visibility rule e validator existentes | available; needs discovery | platform-engineering | yes for implementation |
| sandbox news/blog e fixtures de revisão semântica | available | planner | no |
| decisão humana sobre informação de negócio ausente em uma iniciativa consumidora | on demand | stakeholder owner | blocks only the affected consumer gate |
| revisão independente de acessibilidade e significado renderizado | required before Human Visibility | distinct evaluator | yes for final rollout |

## 14. Validation notes

Use fixture software rica, fixture não-software/localizada e fixture de fonte
incompleta. Determinismo prova abas/atributos/fallback estável; revisão
independente avalia se cada visão permite a decisão sem reabrir Markdown. Não
há métrica automática de “detalhamento suficiente”.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex / Spec Guardian  
**Reviewed at:** 2026-08-26  
**Blocking issues:** nenhum para planejamento; T-001 deve resolver a técnica
de interação acessível antes de qualquer alteração de template.  
**Required revisions:** nenhuma fonte pode introduzir detalhes ausentes sem a
pergunta/unknown definido em FR-003.  
**Decision evidence/link:** solicitação explícita do mantenedor nesta conversa.
