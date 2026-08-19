# Operating Model

## Loop central

```txt
specify -> outcome review -> spec review -> impact -> plan -> validation plan
-> preliminary task draft -> coverage composition + distinct review
-> stakeholder brief -> meeting decision propagation -> tasks ready
-> implement one task -> evidence draft -> independent evaluation
-> approved evidence -> done -> initiative validation -> ratchet
```

Cada seta é uma transição explícita. O workflow comum está em
`.harness/workflows/sdd-lifecycle.md`; feature, bugfix e refactor adicionam
constraints próprios.

O ramo mostrado com task draft/coverage/propagação é v2. Briefs históricos ou
pinned com lineage v1 preservam o caminho legado `brief -> Human Visibility ->
task breakdown -> Tasks Ready` até refresh material/migração explícita; os gates
de evidence/evaluator são iguais para ambas as lineages.

Antes do loop, o agente localiza a iniciativa pelo `specs/INDEX.md` e pelo
diretório canônico `specs/NNN-slug/`. O índice e `run-state.yaml` são o contexto
mínimo; artefatos completos e busca semântica entram sob demanda.

Quando a estrutura estiver fora do padrão, use
`.harness/workflows/spec-structure-normalization.md`: State Keeper inventaria,
Impact Mapper encontra referências quebráveis, Delivery Orchestrator propõe o
mapa `slug -> NNN-slug`, Builder/State Keeper aplica e Evaluator confere
índice, estado e caminhos.

## Quality gates

| Gate | Owner | Entrada mínima | Saída verificável |
|---|---|---|---|
| Outcome Ready | Spec Guardian/Orchestrator | objetivo inicial | outcome, incremento demonstrável e prioridade/decisão |
| Spec Ready | Spec Guardian | spec completa | decisão e blockers |
| Impact Mapped | Impact Mapper | spec ready + contexto | superfícies, risco, unknowns |
| Plan Ready | Orchestrator | spec + impact | abordagem, decisões, rollback |
| Validation Ready | Harness Planner | ACs estáveis | cada AC mapeado |
| Tasks Drafted (v2) | Harness Planner/Orchestrator | plano + validação | tarefas preliminares, visíveis mas não autorizadas |
| Brief Coverage Ready (v2) | Spec Guardian/Orchestrator | inventário/fonte + revisão distinta | disposição por heading e gaps resolvidos |
| Human Visibility Ready | Spec Guardian/Orchestrator | artefatos fonte + render corrigido | brief derivado, sincronizado e revisado |
| Tasks Ready | Orchestrator/State Keeper | decisão de reunião propagada | tasks atômicas com outcome/exit/evidence autorizadas |
| Implementation Done | Builder | uma task ready | mudança + evidence draft |
| Independent Evaluation | Evaluator | diff + checks + draft | approve/revise/block/escalate |
| Evidence Pack Ready | Evaluator/State Keeper | avaliação concluída | pack completo e aprovado |
| Validation Done | Evaluator | todas as tasks done | aceite coberto, riscos registrados |

## Transições de task

```txt
pending -> ready
ready -> in_progress
in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
pending|ready|in_progress|needs_evaluation|needs_revision -> blocked
```

`approved` é decisão do evaluator. `done` é atualização de estado realizada
depois que o evidence pack registra essa decisão. Sem evaluator distinto, o
estado terminal é proibido.

Para v2, `tasks_drafted` não é um status de execução. A composição usa o
inventário de fontes aplicáveis e uma disposição por heading; os blocos
renderizados usam `data-source`, `data-source-section` e `data-coverage`, com
tabela humana correspondente, sem JSON/sidecar duplicado. O reviewer de
coverage é distinto do autor (ou humano nomeado), e a reunião grava decisões no
log, propaga fontes e regenera o brief antes de Tasks Ready.

## Risco e aprovação humana

| Condição | Ação |
|---|---|
| low, local e reversível | fluxo normal |
| medium | avaliação independente obrigatória |
| high | mitigação explícita + revisão humana |
| unknown | discovery task ou revisão humana antes de implementar |
| destrutiva/irreversível/sensível | preview, rollback e aprovação humana |

Ambiguidade de produto, prioridade de negócio, mudança de dado de produção,
segurança, autorização, billing e migração irreversível nunca são resolvidos por
suposição do agente.

## Sessões e retomada

Antes de pausar:

1. pare em um checkpoint seguro;
2. registre working tree e trabalho parcial;
3. atualize run-state, progress e handoff;
4. vincule evidências já criadas;
5. informe riscos e próximo passo exato.

Na retomada, reconcilie esses arquivos com o repositório. Se não houver caminho
seguro, crie discovery task ou escale; não continue por adivinhação.

## Evaluation protocol

O evaluator recebe spec, task, plan, validation plan, diff e evidence draft.
Ele não edita a implementação durante o julgamento. Findings apontam critério,
evidência e severidade. A decisão permitida é `approve`, `request_revision`,
`block` ou `escalate_to_human`.

## Evidence protocol

O pack registra identidade do builder/evaluator, commit ou working tree,
arquivos, ACs, comandos, resultados, artifacts, gaps e risco residual.
Comandos não executados precisam de razão e impacto. “Parece correto” não é
evidência.

## Learning loop

Falha séria entra no ratchet mesmo na primeira ocorrência. Falha menor entra
quando recorrente:

```txt
failure -> root cause -> prevention -> artifact owner
-> hard mirror/test/eval -> regression check -> verification
```

Uma entrada só fica `implemented` quando a prevenção e seu regression check
existem e foram verificados.

## Harness audit

Auditorias seguem `.harness/workflows/sdd-harness-audit.md` e usam
`.harness/skills/sdd-harness-audit/SKILL.md`. O auditor deve montar o grafo de
entrypoints, agentes, skills, regras, workflows, templates, scripts, specs,
estado, memória e evidência; depois julgar SDD, harness, contratos agênicos,
enforcement e recuperação.

O relatório HTML usa `.harness/templates/audit-report.html`. Ele deve conter
decisão, maturidade, grafo, achados por severidade, artefatos órfãos ou
decorativos, roadmap de remediação, assumptions e open questions.
