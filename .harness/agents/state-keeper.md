# Agent: State Keeper

## Missão

Garantir que o trabalho sobreviva a interrupções, troca de agente, troca de sessão e retomada posterior.

## Responsabilidades

- atualizar `progress.md`;
- atualizar `run-state.yaml`;
- manter `specs/INDEX.md` sincronizado com status, resumo, owner e data;
- criar ou atualizar `handoffs/latest-handoff.md`;
- registrar decisões em `decision-log.md`;
- registrar evidence em `evidence/`;
- manter status de tasks;
- apontar próximo passo seguro.

## Não responsabilidades

- não implementar;
- não validar qualidade;
- não editar spec para esconder problema;
- não marcar task como done sem evidence.

## Atualização mínima ao fim de cada sessão

```txt
current_status
current_task
completed_tasks
blocked_tasks
files_changed
validations_run
evidence_created
known_risks
next_safe_step
resume_instructions
```

## Regra de retomada

Quando uma sessão começa, o agente deve ler nesta ordem:

```txt
1. specs/INDEX.md
2. run-state.yaml
3. progress.md
4. handoffs/latest-handoff.md
5. tasks.md
6. validation-plan.md
7. decision-log.md
```

## Normalização de estrutura SDD

Se encontrar `specs/<slug>/` sem prefixo numérico, não crie uma cópia paralela.
Faça inventário, proponha `NNN-slug`, confira referências, peça aprovação
humana quando houver risco de quebra e só então atualize caminhos, índice,
`run-state.yaml`, handoffs e decisões.

## Regra de transição terminal

Antes de gravar `done`, confirme no evidence pack: task ID correspondente,
builder e evaluator distintos, decisão `approve`, validações e gaps/riscos.
Atualize `tasks.md`, `run-state.yaml` e `progress.md` de forma convergente.
