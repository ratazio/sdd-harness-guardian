# Spec: 008-semantic-brief-review-calibration

**Status:** spec_ready  
**Sequence:** 008  
**Owner:** platform-engineering  
**Created / updated:** 2026-08-25  
**Risk:** medium  
**Assurance profile:** A2-elevated

## 1. Problem

O Guardian valida estrutura, provenance, gates e freshness de briefs v2, mas um brief pode cumprir tudo isso e ainda comprimir decisões materiais a ponto de não servir à reunião. A revisão semântica já é exigida, porém seu output não demonstra se produto, arquitetura/operação e entrega continuam recuperáveis depois da síntese/renderização.

## 2. Objective

Calibrar a revisão independente existente para bloquear briefs semanticamente rasos e orientar sua recuperação, sem transformar qualidade contextual em score, schema ou checklist determinístico rígido.

## 3. Delivery outcome

- **Produto/usuário:** autores e stakeholders recebem parecer útil sobre o que o brief preserva, superficializa ou omite.
- **Incremento demonstrável:** exemplos software e não-software mostram fontes, review e brief; review detecta síntese rasa e aponta fonte/ajuste.
- **MVP:** reforçar instruções, workflow e template de parecer; adicionar exemplos e fixtures focadas. Sem serviço, agente permanente, pontuação semântica, LLM automático ou banco de estado.
- **Prioridade:** decisão humana do solicitante em 2026-08-25.
- **Sucesso operacional:** em cada exemplo de referência, um reviewer independente consegue recuperar do brief o outcome, risco/controle, estado, decisão e próximo passo; o mantenedor aceita a evidência de T-004 antes de liberar a mudança do bundle.

## 4. Actors and outcomes

Autor, reviewer independente, stakeholder de produto, arquitetura/operação e entrega, e mantenedor do bundle. O-001: parecer por lente `recuperável`, `superficial`, `ausente` ou `não aplicável`, com exemplo/fonte. O-002: review pós-render responde o que permanece impossível decidir sem MD. O-003: exemplos calibram profundidade proporcional. O-004: validator continua estrutural.

## 5. Non-goals

- Score de palavras, tabelas, diagramas ou qualidade textual.
- Novo workflow engine, agente permanente, sidecar, estado duplicado ou CI que certifique semântica.
- Migrar v1 histórico ou exigir arquitetura de software para política, pesquisa ou operação.

## 6. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | Review SHALL emitir lentes produto, arquitetura/operação e entrega, com N/A justificado. | Julgamento observável, não automatizado. |
| FR-002 | Finding SHALL ligar fonte, fato perdido e ação de recuperação. | Correção acionável. |
| FR-003 | Lifecycle SHALL separar coverage pré-render de significado pós-render. | Headings não equivalem síntese útil. |
| FR-004 | Pós-render SHALL perguntar qual decisão material é impossível sem MD. | Teste de perda de decisão. |
| FR-005 | Bundle SHALL incluir exemplo software e não-software com composição, parecer e brief. | Calibração generalizável. |
| FR-006 | Validator SHALL permanecer limitado a estrutura/estado/provenance. | Evita overfitting. |
| FR-007 | Mirror futuro SHALL registrar necessidade, custo e remoção. | Complexidade proporcional. |

## 7. Acceptance criteria

| ID | Criterion | Validation |
|---|---|---|
| AC-001 | Reviewer produz três lentes/N-A com exemplos. | V-001 fixture review |
| AC-002 | Síntese rasa de risco, validação, decisão ou next step gera finding fonte+revisão. | V-002 negative fixture |
| AC-003 | Pré-render e pós-render possuem records distintos, sem papel novo. | V-003 lifecycle fixture |
| AC-004 | Exemplo software cobre API/dados/trust/falha/validação; não-software usa superfícies equivalentes. | V-004 example review |
| AC-005 | Nenhum score/parser de qualidade/gate semântico determinístico é adicionado. | V-005 diff review |
| AC-006 | v1 histórico segue compatível. | V-006 fixture |
| AC-007 | Brief mantém scan de 60 segundos e recuperação progressiva. | M-001 rendered review |
| AC-008 | Evidência final mostra que os exemplos permitem recuperar outcome, risco/controle, estado, decisão e próximo passo; mantenedor aceita ou devolve a mudança. | V-007 release review |

## 8. Edge cases, constraints and assumptions

Sem arquitetura técnica, reviewer usa operação/contexto ou N/A fundamentado. Sem reviewer distinto, gate fica pendente ou humano nomeado revisa. v1 histórico não recebe v2 sem refresh. Reutilizar agentes, lifecycle, decision log, state e brief existentes; exemplos são fictícios/estáticos; A1 simples não recebe custo adicional. Presume papéis de reviewer e espaço para dois exemplos no bundle.

## 9. Risks and dependencies

R-001: rubrica vira burocracia (mitigação: quatro julgamentos curtos/N-A). R-002: exemplo software vira obrigatório (exemplo não-software/regra proporcional). R-003: review subjetivo bloqueia sem ação (fonte+fato+revisão). R-004: parser semântico retorna (FR-006/007). Dependem de agentes, skills, lifecycle e template existentes, e de fixtures/exemplos a criar.

## 10. Validation notes

Fixture negativa “formalmente coberta, semanticamente rasa”, exemplos cruzados e revisão renderizada. Determinismo verifica somente a existência de parecer/locator; profundidade continua decisão independente/humana.

## 11. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex / Spec Guardian  
**Reviewed at:** 2026-08-25  
**Blocking issues:** nenhum para planejamento.  
**Decision evidence:** solicitação humana desta conversa.
