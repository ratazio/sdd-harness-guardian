# Architecture: SDD Harness Guardian

## Posição arquitetural

O bundle é uma dependência Git passiva: arquivos declarativos lidos por agentes
ou por um orquestrador opcional. Ele governa SDD sem implementar produto,
frontend, serviço hospedado, banco, knowledge base ou workflow engine.

```txt
Consumer repository
├── project-local rules, code and knowledge
├── specs/INDEX.md                   # compact initiative map
├── specs/NNN-<initiative>/          # mutable execution state
└── vendor/sdd-harness-guardian/      # immutable pinned bundle
    ├── .harness/AGENTS.md
    ├── .harness/{agents,rules,skills,workflows,templates}/
    ├── scripts/
    └── docs/
```

## Camadas

| Camada | Fonte de verdade | Responsabilidade |
|---|---|---|
| Intent | `spec.md` | problema, objetivo, escopo e aceite |
| Visibility | `stakeholder-brief.html` | leitura humana derivada para alinhamento |
| Design | `impact-map.md` + `plan.md` | superfícies, riscos e estratégia |
| Validation | `validation-plan.md` | mapeamento AC → check → evidência |
| Execution | `tasks.md` + `run-state.yaml` | unidades, gates e transições |
| Proof | `evidence/` | resultados verificáveis e decisão |
| Memory | `progress.md`, `handoffs/`, `decision-log.md` | retomada e contexto |
| Learning | `ratchet.md` | prevenção de falhas recorrentes |
| Audit | `sdd-harness-audit` + `audit-report.html` | grafo, gaps, maturidade e remediação |

`specs/INDEX.md` é a primeira camada de descoberta. Ele reduz contexto inicial,
preserva ordem sequencial e orienta humanos/agentes antes de abrir artefatos
longos. Busca semântica, embeddings ou MCP memory podem complementar o índice,
mas não substituem o contrato de arquivos versionados.

## Fluxo de controle

```txt
Spec Guardian -> Impact Mapper -> Harness Planner
       |                |                 |
       +---------- Delivery Orchestrator -+
                           |
                        Builder
                           |
                    evidence draft
                           |
                       Evaluator
                      /         \
                 revision      approve
                    |             |
                  Builder      State Keeper -> done
                                      |
                               Ratchet Maintainer
```

Builder e evaluator têm identidades distintas. Um workflow engine pode
automatizar as transições, mas execução manual, CI ou DAG customizado também
são compatíveis.

## Estado e atomicidade

`run-state.yaml` contém o estado compacto e machine-readable.
`stakeholder-brief.html` é o resumo de reunião derivado dos artefatos fonte.
Ele é a superfície principal de decisão humana, mas não uma fonte concorrente:
o autor o sintetiza depois das fontes, e o Spec Guardian julga coerência,
proporcionalidade e significado visual no gate já existente.
`progress.md` e `handoffs/latest-handoff.md` explicam o contexto humano.
`tasks.md` é o ledger de trabalho; `evidence/<task-id>.md` é o ledger de prova.

Atualizações relacionadas devem convergir antes do fim da sessão. Se working
tree, task status e run-state divergirem, a retomada bloqueia até reconciliação.
O último checkpoint seguro sempre precede trabalho parcial não validado.

## Portabilidade

O contrato depende apenas de arquivos. Scripts Python são conveniências
opcionais e não participam da semântica do workflow. O consumidor escolhe
LLM, IDE, CI, hooks, schemas e workflow engine.

## Trust boundaries

O bundle define defaults e invariantes de processo. O consumidor define domínio,
stack, arquitetura, segredos, permissões, deploy e políticas adicionais. Dados
de domínio e memória viva nunca devem ser gravados dentro do submódulo.

Auditorias podem ler artefatos do consumidor, mas não devem mover, apagar ou
normalizar arquivos sem uma iniciativa explícita de remediação. O relatório é
evidência e direcionamento, não alteração automática do projeto.

Regras locais podem especializar o bundle, mas não reduzir suas invariantes
protegidas. Operações destrutivas cruzam um boundary humano e exigem aprovação
registrada.
