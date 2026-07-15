# Operating Model

## Loop central

```txt
specify -> outcome review -> spec review -> impact -> plan -> validation plan -> tasks
-> implement one task -> evidence draft -> independent evaluation
-> approved evidence -> done -> initiative validation -> ratchet
```

Cada seta é uma transição explícita. O workflow comum está em
`.harness/workflows/sdd-lifecycle.md`; feature, bugfix e refactor adicionam
constraints próprios.

## Quality gates

| Gate | Owner | Entrada mínima | Saída verificável |
|---|---|---|---|
| Outcome Ready | Spec Guardian/Orchestrator | objetivo inicial | outcome, incremento demonstrável e prioridade/decisão |
| Spec Ready | Spec Guardian | spec completa | decisão e blockers |
| Impact Mapped | Impact Mapper | spec ready + contexto | superfícies, risco, unknowns |
| Plan Ready | Orchestrator | spec + impact | abordagem, decisões, rollback |
| Validation Ready | Harness Planner | ACs estáveis | cada AC mapeado |
| Tasks Ready | Orchestrator | plano + validação | tasks atômicas com outcome/exit/evidence |
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
