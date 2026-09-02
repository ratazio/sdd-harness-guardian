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
4. localize a iniciativa em `specs/NNN-slug/`;
5. prefira iniciativas canônicas em `specs/NNN-slug/` e leia
   `specs/INDEX.md` quando existir;
6. se a iniciativa não existir, use `.harness/templates/README.md` ou
   `scripts/new_initiative.py` para criá-la;
7. em retomadas, siga a ordem de leitura definida em
   `.harness/rules/state-and-memory.md`.

Todos os caminhos deste bundle são relativos à raiz do bundle. Todos os
artefatos de iniciativa são relativos à raiz do projeto consumidor.

## Invariantes protegidas

- nenhuma implementação começa antes de `Spec Ready`;
- nenhuma implementação ou expansão de tasks começa sem outcome e incremento
  demonstrável declarados;
- iniciativa não trivial mantém `stakeholder-brief.html` legível e sincronizado
  com os artefatos fonte depois de `brief_phase: rendered`; antes disso, a
  ausência do HTML é obrigatória e não deve ser apresentada como entrega;
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
| Harness Auditor | auditar SDD, harness, grafo e evidência | não confundir existência com uso |
| Harness Graph Mapper | mapear artefatos e referências alcançáveis | não inferir edges sem prova |
| Brief Experience Composer | preencher o candidate v3 a partir do skeleton e fontes canônicas | não aprovar a própria composição |
| Executive Brief Reviewer | avaliar construção e HTML renderizado para decisão executiva | não editar durante a avaliação |

As definições completas estão em `.harness/agents/`.

## Fluxo obrigatório

```txt
1. Specify
2. Outcome Review -> Gate: Outcome Ready
3. Spec Review -> Gate: Spec Ready
4. Impact Map
5. Technical Plan -> Gate: Plan Ready
6. Validation Plan -> Gate: Validation Ready
7. v2 only: Preliminary Task Draft -> Gate: Tasks Drafted (not authorized)
8. v2 only: Coverage Composition + distinct review -> Gate: Brief Coverage Ready
9. Stakeholder Brief -> Gate: Human Visibility Ready
10. v2 only: Meeting decision propagation + refreshed brief -> Gate: Tasks Ready
11. Implementation of one ready task
12. Evidence draft
13. Independent Evaluation
14. Evidence approval
15. Task done + state update
16. Initiative Validation Done
17. Ratchet update when triggered
```

Auditorias usam o workflow `.harness/workflows/sdd-harness-audit.md` e a skill
`.harness/skills/sdd-harness-audit/SKILL.md`. O relatório final deve seguir
`.harness/templates/audit-report.html` e incluir grafo, achados por severidade,
evidência e roadmap de remediação.

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
specs/NNN-slug/
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

Novas iniciativas devem usar `specs/NNN-slug/` e manter `specs/INDEX.md`
atualizado. O número é identidade sequencial/cronológica, não prioridade.
Projetos consumidores legados com specs sem número devem ser normalizados por
inventário, mapa de renome, atualização de referências e decisão humana quando
houver risco.

Bugfixes também usam `reproduction.md`. Os templates canônicos estão em
`.harness/templates/`.

O scaffolder cria somente fontes canônicas. Para materializar um brief, o autor
prepara um candidato após cobertura revisada, define `brief_phase:
ready_to_render` e usa `scripts/render_stakeholder_brief.py`; o promotor recusa
casca, placeholders, estado incorreto e logo divergente. Renderizar não é
aprovar ou entregar: a revisão independente do HTML continua obrigatória.

## Gates de bloqueio

Bloqueie avanço quando:

- objetivo ou não objetivos estão ausentes;
- outcome de produto/usuário, incremento demonstrável ou incerteza a reduzir
  não estão declarados;
- iniciativa não trivial não possui brief humano ou o brief contradiz spec,
  impact map, plan ou validation plan;
- uma iniciativa v2 não possui source inventory/coverage disposition para cada
  heading principal aplicável, provenance `data-*`, razão exigida ou tabela
  humana de coverage;
- cobertura v2 usa `link_only` para heading material de fonte core, ou autor e
  reviewer de coverage não são identidades distintas;
- tarefa preliminar é tratada como `ready`, ou Tasks Ready ocorre antes de
  propagação de decisões de reunião e refresh de coverage/brief;
- perfil de arquitetura S/M/L/high/unknown não está sustentado por fontes, ou
  informação ausente não foi bloqueada/transformada em discovery;
- brief v1 histórico/pinned é forçado pelos gates v2 antes de refresh material
  ou migração explícita.
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
