# Tasks — SPEC 027

**Status:** T-001..T-004 concluídas após avaliações independentes; a regressão R2 permanece não promovida por desenho.  
**Spec:** [spec.md](./spec.md) | **Plan:** [plan.md](./plan.md)

| ID | Status | Entrega | Dependências | Risco | Evidência |
|---|---|---|---|---|---|
| T-001 | done | Scaffold/revisão do plano de composição | nenhuma | medium | evidence/T-001.md; evidence/evaluation-T-001.md |
| T-002 | done | Contrato de slots e guard de integridade | T-001 | medium | evidence/T-002.md; evidence/evaluation-T-002.md |
| T-003 | done | Composição agêntica em corpus heterogêneo | T-001, T-002 | medium | evidence/T-003.md; evidence/evaluation-T-003-T-004.md |
| T-004 | done | Avaliação independente desktop e regressão | T-003 | medium | evidence/evaluation-T-003-T-004.md |

## T-001 — Plano de composição revisável

**Objetivo:** acrescentar o scaffold ao \`plan.md\` e uma instrução/revisão distinta que diferencie cobertura de storytelling/forma.  
**Requisitos:** FR-027-01..03. **Validação:** V-027-01, V-027-02.  
**Escopo:** template, skill/workflow e papel de revisão existentes.  
**Fora de escopo:** novo sidecar, score, geração de HTML ou marca.  
**Exit:** plano superficial recebe \`REVISE\`; caso proporcional preserva fontes, relações, N/A/discovery e forma escolhida sem quota.

## T-002 — Skeleton preenchível e guard de integridade

**Objetivo:** tornar inequívoco o que deve permanecer e o que o compositor pode preencher; fazer o hook rejeitar falso lineage.  
**Requisitos:** FR-027-04..07. **Validação:** V-027-03, V-027-04, V-027-07.  
**Escopo:** template v3, instanciador quando necessário, guard e fixtures positivas/negativas.  
**Fora de escopo:** parser semântico, renderer autoral ou redesign de perfil.  
**Exit:** candidate do zero com hash copiado falha; cópia editada em slots passa e preserva a casca, rotas, fallback e comportamento-base.

## T-003 — Corpus heterogêneo por composição real

**Objetivo:** provar que o contrato funciona em domínios diferentes sem overfitting.  
**Requisitos:** FR-027-07, FR-027-10. **Validação:** V-027-06.  
**Escopo:** nova run descartável, fontes canônicas → plano revisado → skeleton → candidate; candidates permanecem não promovidos.  
**Fora de escopo:** alterar regras para um fixture, tarefas de produto ou HTML final.  
**Exit:** todos os candidates passam integridade e cada um carrega um plano de composição revisado; falhas permanecem \`REVISE\`, nunca são maquiadas.

## T-004 — Revisão de experiência e decisão de regressão

**Objetivo:** avaliar o que o hook não pode avaliar: narrativa, forma, desktop, navegação e fidelidade ao plano/fontes.  
**Requisitos:** FR-027-08..10. **Validação:** V-027-05..07.  
**Escopo:** revisor distinto, inspeção de browser/captura quando disponível, evidence e decisão de regressão.  
**Fora de escopo:** promoção sem aprovação, score visual ou substituição de julgamento por screenshot.  
**Exit:** cada \`APPROVE\`/\`REVISE\` explica fonte/plano → experiência → decisão; nenhum candidate cru é declarado final.

**Tasks Ready:** no — a autorização foi usada, mas a revisão de todos os planos retornou \`REVISE\`; não existe candidate elegível para T-004.
