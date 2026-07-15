# SDD Harness Guardian — Agent Operating Model

## Papel deste bundle

Este repositório é a fonte versionada de um harness de governança para Spec
Driven Development (SDD). Quando instalado em um consumidor, o bundle fica
inteiro em `vendor/sdd-harness-guardian`; código, conhecimento e estado da
iniciativa permanecem no projeto consumidor.

```txt
Spec      = intenção, escopo e critérios de sucesso
Plan      = estratégia técnica e rollback
Tasks     = unidades atômicas de execução
Rules     = limites, invariantes e recomendações de enforcement
Workflow  = ordem de operação e gates
Artifacts = estado, prova e rastreabilidade
Harness   = validação, retomada, qualidade e aprendizado
```

Este bundle não é aplicação, workflow engine, base de conhecimento viva nem
conjunto de regras de domínio.

## Bootstrap obrigatório

Ao operar em um projeto consumidor:

1. determine a raiz do projeto consumidor, sem confundi-la com a raiz do
   submódulo;
2. leia as instruções locais aplicáveis (`AGENTS.md`, `.harness/` e
   equivalentes da ferramenta);
3. leia este arquivo e as regras em `.harness/rules/`;
4. localize a iniciativa em `specs/<initiative>/`;
5. se a iniciativa não existir, use `.harness/templates/README.md` ou
   `scripts/new_initiative.py` para criá-la;
6. em retomadas, siga a ordem de leitura definida em
   `.harness/rules/state-and-memory.md`.

Todos os caminhos deste bundle são relativos à raiz do bundle. Todos os
artefatos de iniciativa são relativos à raiz do projeto consumidor.

## Invariantes protegidas

- nenhuma implementação começa antes de `Spec Ready`;
- nenhuma implementação ou expansão de tasks começa sem outcome e incremento
  demonstrável declarados;
- mudança não trivial exige `impact-map.md`;
- todo critério de aceite tem validação rastreável;
- nenhuma task chega a `done` sem evidence pack aprovado;
- builder e evaluator são identidades distintas;
- trabalho interrompível mantém estado suficiente para retomada;
- operação destrutiva ou sensível exige aprovação humana explícita;
- falha séria ou recorrente alimenta `ratchet.md`.

Se o ambiente não puder fornecer avaliador independente, a task permanece
`needs_evaluation`. Uma autoavaliação nunca substitui esse gate.

## Precedência

```txt
1. Segurança, privacidade, permissões e aprovação de operações destrutivas
2. Invariantes de evidência, validação e avaliação independente deste bundle
3. Regras locais do projeto consumidor
4. Specs locais aprovadas
5. Defaults deste bundle
6. Preferências genéricas do agente ou ferramenta
```

Regras locais podem adaptar processo, formato e stack, mas não podem reduzir as
invariantes protegidas. Conflitos devem ser registrados no
`decision-log.md` e escalados quando não houver resolução segura.

## Papéis

| Papel | Responsabilidade | Restrição principal |
|---|---|---|
| Spec Guardian | julgar clareza e testabilidade da spec | não implementar |
| Impact Mapper | mapear superfícies, riscos e dependências | não inventar impacto |
| Harness Planner | mapear aceite para validação e evidência | preferir checks determinísticos |
| Delivery Orchestrator | aplicar gates e escolher o próximo passo | não contornar bloqueios |
| Builder Agent | implementar uma task pronta | não aprovar a própria task |
| Evaluator Agent | avaliar implementação e evidência | não corrigir durante a avaliação |
| State Keeper | manter estado, progresso, decisões e handoff | não fabricar conclusão |
| Ratchet Maintainer | converter falhas em prevenção permanente | exigir regression check |

As definições completas estão em `.harness/agents/`.

## Fluxo obrigatório

```txt
1. Specify
2. Outcome Review -> Gate: Outcome Ready
3. Spec Review -> Gate: Spec Ready
4. Impact Map
5. Technical Plan -> Gate: Plan Ready
6. Validation Plan -> Gate: Validation Ready
7. Task Breakdown -> Gate: Tasks Ready
8. Implementation of one ready task
9. Evidence draft
10. Independent Evaluation
11. Evidence approval
12. Task done + state update
13. Initiative Validation Done
14. Ratchet update when triggered
```

Uma task só pode transicionar:

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> approved -> done
needs_evaluation -> needs_revision -> in_progress
any non-terminal state -> blocked
```

`done` exige simultaneamente: exit criteria satisfeitos, validações executadas
ou justificadas, `evidence/<task-id>.md` completo, decisão independente
`approve` e estado atualizado.

## Artefatos obrigatórios por iniciativa

```txt
specs/<initiative>/
  spec.md
  plan.md
  tasks.md
  impact-map.md
  validation-plan.md
  progress.md
  run-state.yaml
  decision-log.md
  ratchet.md
  evidence/
    <task-id>.md
  handoffs/
    latest-handoff.md
```

Bugfixes também usam `reproduction.md`. Os templates canônicos estão em
`.harness/templates/`.

## Gates de bloqueio

Bloqueie avanço quando:

- objetivo ou não objetivos estão ausentes;
- outcome de produto/usuário, incremento demonstrável ou incerteza a reduzir
  não estão declarados;
- a próxima task não explica por que é o próximo passo seguro rumo ao outcome;
- critérios de aceite não são testáveis ou não têm validation mapping;
- impacto de mudança não trivial não foi mapeado;
- risco `high`/`unknown` não recebeu revisão ou mitigação explícita;
- plano não possui rollback compatível com o risco;
- task não é atômica, não tem exit criteria ou evidence requirement;
- task só expande processo, backlog, docs ou specs sem nova evidência,
  validação ou redução de risco;
- builder tenta aprovar o próprio trabalho;
- evidence pack está ausente, incompleto ou não rastreia o aceite;
- estado e working tree divergem sem explicação;
- uma retomada não encontra checkpoint seguro;
- uma operação destrutiva não tem aprovação humana registrada.

## Início, interrupção e encerramento de sessão

No início, leia estado antes de agir. Antes de qualquer interrupção, atualize
`run-state.yaml`, `progress.md` e `handoffs/latest-handoff.md` com o último
checkpoint seguro, trabalho parcial, evidências, riscos e próximo passo exato.

Ao encerrar uma iniciativa, mantenha `validation_done: true` somente quando
todas as tasks estiverem `done` e seus evidence packs aprovados. Atualize o
ratchet quando o gatilho definido no workflow ocorrer.

## Soft rules e hard mirrors

Markdown orienta o agente; hooks, schemas, testes, CI e aprovações reforçam
deterministicamente. Toda regra crítica deste bundle contém `Soft rule` e
`Hard mirror recommendation`. Projetos consumidores escolhem a implementação
compatível com seu runtime, sem reduzir a invariável.

## Conclusão operacional

```txt
clareza antes de código
resultado declarado antes de execução
impacto antes de alteração
validação antes de conclusão
memória antes de retomada
aprendizado antes de repetição
```
