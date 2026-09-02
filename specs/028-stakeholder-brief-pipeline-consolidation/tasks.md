# Tasks — SPEC 028

**Status:** tasks_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Última atualização:** 2026-09-02

## Ledger

| ID | Status | Título | Dependências | Risco | Builder | Evaluator | Evidência |
|---|---|---|---|---|---|---|---|
| T-001 | done | Unificar lifecycle resiliente e autoridade de afirmação | nenhum | high | Codex | pipeline_audit | evidence/T-001.md |
| T-002 | done | Ligar plano, skeleton e contratos de conteúdo material | T-001 | high | Codex | spec027_r2_fix_m007_m008 | evidence/T-002.md |
| T-003 | done | Tornar preview HTTP e rotas internas parte da revisão final | T-001, U-003 | medium | Codex | spec027_r2_fix_m007_m008 | evidence/T-003.md |
| T-004 | done | Vincular revisão renderizada e inventariar validações existentes | T-001, T-003 | high | Codex | pipeline_audit | evidence/T-004.md |
| T-005 | done | Executar matriz fresca M001–M008 e decidir a qualidade | T-001, T-002, T-003, T-004 | high | Codex | spec027_r2_fix_m007_m008 | evidence/T-005.md |

`pending → ready → in_progress → needs_evaluation → approved → done`. Uma
task retorna a `needs_revision` quando a avaliação falhar. Para briefs, esse
retorno dispara recomposição pelo sistema e nova revisão: nunca exige aprovação
operacional do usuário. Um final com estado honesto só pode ser mantido se já
existir candidate rastreável; o retorno pre-skeleton não pula sua precondição.

## T-001 — Unificar lifecycle resiliente e autoridade de afirmação

**Objetivo:** impedir que estado, decision log, candidate, final ou alegação de
prontidão se contradigam, sem impedir autoria/promoção do HTML quando as fontes
existem.  
**Serviço:** FR-001, FR-002, FR-003, FR-008; AC-001, AC-002.  
**Incremento:** uma transição oficial decide somente se o brief pode alegar
`approved`/Human Visibility. Um `REVISE` retorna imediatamente para correção e
nova revisão; candidate/final só avançam quando as precondições da respectiva
fase existem e deixam locator/digest recuperável.  
**Por que agora:** todos os demais controles dependem de saber qual artefato é
autorizado.

### Escopo

- Inventariar os chamadores e estados que hoje criam/aceitam candidate, final e
  Human Visibility.
- Definir e implementar precondições oficiais para alegação de prontidão,
  incluindo retorno automático de `REVISE` para recomposição.
- Resolver e codificar/documentar a política D-006 de fallback desktop sem JS.
- Criar fixtures negativos que reproduzam a contradição M003 sem alterar R2.

### Fora do escopo

Autorizar conteúdo por script, redesenhar o skeleton ou tornar briefs móveis.

### Dossier de validação

| Claim/risco | Técnica/oracle | Evidência/saída |
|---|---|---|
| `REVISE` vira espera burocrática ou ignora gate | fixture pre e pós-render | pre-render repara/revisa antes do skeleton; pós-render mantém final não aprovado só com candidate rastreável |
| Record fora do estado vale como aprovação | fixture com digest/locator divergente | recusa explícita e recovery path |
| Sem JS volta a one-page | política D-006 + teste específico | contrato alinhado à experiência desktop |

**Critérios de saída:** V-001, V-002, V-009 e V-REG-002/V-REG-004 aprovados;
decisão D-006 implementada; evaluator distinto confirma que não surgiu segundo
workflow ou uma barreira burocrática de autoria.

## T-002 — Ligar plano, skeleton e contratos de conteúdo material

**Objetivo:** fazer o candidate preenchido partir do skeleton autorizado e
recuperar arquitetura, tasks e provas materiais planejadas.  
**Serviço:** FR-002, FR-005, FR-006; AC-002, AC-004, AC-006.  
**Incremento:** attestation de fonte/decisão/skeleton e ativação correta dos
contracts existentes.  
**Por que agora:** a cópia física sozinha permitiu o HTML visualmente vazio do
R2.

### Escopo

- Associar construction record, achados pre-skeleton (se houver) e skeleton
  digest ao candidate, sem exigir aprovação humana para iniciar o preenchimento.
- Tornar explícita, validada e revisável a disposição de arquitetura material,
  N/A ou discovery.
- Exigir projeção dos campos materiais já presentes em tasks e validações;
  manter autoria, forma visual e texto com o agente compositor.
- Preservar `validate_brief_candidate_inheritance.py` como check de integridade,
  sem vendê-lo como avaliação de qualidade.

### Fora do escopo

Escolher por código entre diagrama, cards, tabelas ou prose; forçar a mesma
topologia para toda SPEC.

### Dossier de validação

| Claim/risco | Técnica/oracle | Evidência/saída |
|---|---|---|
| Guard de arquitetura não roda | candidate material com e sem disposição válida | contract falha/pass conforme declarado |
| Zooms repetem cadeia textual | comparação plano→HTML por reviewer | recomposição automática ou visual com responsabilidade/delta/fronteira recuperáveis |
| Task vira só título | comparação de dossiers em M003/M006/M007 | campos fonte existentes aparecem ou N/A/discovery explícito |

**Critérios de saída:** V-004, V-006 e V-REG-001 passam; revisão independente
confirma que checks não são confundidos com storytelling.

## T-003 — Tornar preview HTTP e rotas internas parte da revisão final

**Objetivo:** avaliar o brief final na superfície que o stakeholder abre.  
**Serviço:** FR-004, FR-008; AC-003, AC-005.  
**Incremento:** URL loopback reprodutível e record de rota/revisão.  
**Por que agora:** abrir `file:` ou inspecionar markup não prova interação real.

### Escopo

- Escolher o mecanismo local mínimo (Node/helper existente) e documentar start,
  stop, root, URL e ausência de rede externa.
- Garantir URL recuperável, uma rota interna desktop por vez e navegação que
  respeite a política D-006.
- Capturar preview/environment no record da revisão final.

### Fora do escopo

Deploy web, monitoramento, autenticação ou teste mobile.

**Critérios de saída:** V-003 e M-001 passam em final promovido; preview ausente
produz V-005/limitação verificável, sem suprimir o HTML final.

## T-004 — Vincular revisão renderizada e inventariar validações existentes

**Objetivo:** eliminar pareceres, skills e records que existem sem governar
qualquer transição.  
**Serviço:** FR-004, FR-007; AC-005.  
**Incremento:** contrato de review final oficial e mapa de cada validação
existente como ativa, substituída, opcional justificada ou órfã removida.  
**Por que agora:** o R2 mostra review de reavaliação positiva sem poder mudar o
estado oficial.

### Escopo

- Rastrear chamadas efetivas de `rendered-brief-decision-review`,
  `validate_semantic_review_record.py`, `brief-experience-composer.md`,
  `validate_human_visibility.py` e contratos associados.
- Vincular somente um record independente do HTML final a digest, URL,
  revisor, veredito, findings/recovery e `human_visibility_ready`.
- Garantir que ausência, digest divergente ou preview indisponível retorna
  `REVISE`, nunca `APPROVE` implícito, e que o retorno chama recomposição ou
  publica limitação explícita sem pedir aprovação do usuário.

### Fora do escopo

Duplicar essa revisão em um novo agente ou criar nota numérica de design.

**Critérios de saída:** V-005 e V-REG-003 passam; o inventário de chamadas é
anexado à evidência e qualquer órfão recebe decisão explícita.

## T-005 — Executar matriz fresca M001–M008 e decidir a qualidade

**Objetivo:** provar/limitar a solução em conjunto heterogêneo, não no M003.  
**Serviço:** FR-007; AC-007, AC-008.  
**Incremento:** novo mock run, final completo para cada fonte legível, matriz de
estado e revisão qualitativa independente por amostra/materialidade.  
**Por que agora:** é a única forma de saber se o fluxo é geral.

### Escopo

- Rodar do pedido à SPEC/plano/candidate/final conforme os gates implementados,
  deixando gates governarem o estado de aprovação, não a criação do HTML.
- Não especializar prompt/template para um mock específico.
- Registrar por M001–M008: fontes/estado, checks determinísticos, decisão de
  composição, final HTTP/review e gaps remanescentes.
- Rodar bundle validation e inspecionar diff para confirmar que não foi criado
  gerador de narrativa/HTML.

### Fora do escopo

Declarar aprovação de todos os mocks antes da revisão, alterar R2, ou resolver
qualquer gap de produto descoberto durante o mock.

**Critérios de saída:** V-007, V-008, V-009, E-001 e E-002 concluídos; cada
linha tem final, estado honesto e, se necessário, limitações/recovery sem uma
pendência de aprovação do usuário.

## Decisão de tasks

**Tasks Ready:** yes — tecnicamente prontas.  
**Bloqueio de execução:** aguarda apenas a autorização de execução que o usuário
explicitamente reservou para si; não há aprovação de usuário no pipeline normal.
