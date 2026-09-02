# Progress — SPEC 027

**Current phase/status:** validation_done  
**Current task:** nenhuma; T-001..T-004 concluídas  
**Last safe checkpoint:** R2 completo e aprovado em 2026-09-01; candidates não promovidos preservados como regressão  
**Stakeholder brief:** not rendered by design

## Outcome context

Create a reusable composition-plan and skeleton-integrity contract so a candidate cannot replace the approved visual shell or bypass a meaningful plan.

## Decisions

| ID | Summary |
|---|---|
| D-027-001..006 | Focus on plan + lineage; keep vendor-neutral and agentic composition. |

## T-001 evaluation checkpoint

O `plan.md` mantém o mapa de cobertura e agora acrescenta o registro de
construção: tese/audiência, oito rotas, relação/forma/razão, repetição,
ausência/discovery e fechamento. A revisão distinta pré-skeleton retorna
`APPROVE` ou `REVISE` e registra fonte → perda/ambiguidade → decisão
prejudicada → correção canônica. A avaliação independente aprovou a task e
registrou que ela não introduz score, quotas, SVG obrigatório, marca mandatória
ou geração de HTML. Evidências: `evidence/T-001.md` e
`evidence/evaluation-T-001.md`.

## T-003/T-004 evaluation checkpoint

A run R2 heterogênea entregou M-001..M-008, cada qual com plano pré-skeleton
`APPROVE`, skeleton local, candidate in-situ aprovado pelo guard e revisão
qualitativa final `APPROVE`. Não há `stakeholder-brief.html` final sob as
iniciativas dos mocks. O browser não abriu `file://`; a inspeção desktop foi
estática (markup/JS, URLs, teclado e impressão), suficiente sob a cláusula
“quando disponível”, sem alegar screenshot live. Ajustes manuais MA-001..003
estão registrados no run como possíveis insumos de melhoria futura. Evidência:
`evidence/evaluation-T-003-T-004.md`.

## Exact next safe step

Nenhuma task desta SPEC permanece. Não promover os candidates de mock; usar as
observações de ajuste manual apenas em uma SPEC futura explicitamente aprovada.

## T-002 implementation checkpoint

O template agora marca casca/slots, stylesheet e comportamento de navegação
base. O guard compara essas regiões com o skeleton local, além do caminho/hash,
para rejeitar uma página paralela que só copie IDs e lineage. A fixture positiva
é uma cópia editada in-situ; a negativa preserva hash/rotas, mas falha por
perder shell/CSS/JS. A avaliação distinta aprovou a entrega e confirmou que o
guard não lê Markdown nem julga narrativa ou estética. Evidências:
`evidence/T-002.md` e `evidence/evaluation-T-002.md`.
