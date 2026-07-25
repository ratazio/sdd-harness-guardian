# SDD Harness Guardian

Bundle agêntico, versionado em Git e vendor-neutral para governar Spec Driven
Development com gates, evidência, memória de execução e retomada.

**Versão:** `0.1.2`  
**Entrypoint:** `.harness/AGENTS.md`  
**Instalação recomendada:** submódulo em
`vendor/sdd-harness-guardian`  
**Status:** ready

## O que este bundle resolve

Ele fornece contratos reutilizáveis para:

- tornar specs claras, limitadas e testáveis;
- exigir outcome e incremento demonstrável antes de implementar ou expandir
  tasks;
- produzir um `stakeholder-brief.html` conciso para alinhamento humano em
  iniciativas não triviais;
- mapear impacto antes de mudanças não triviais;
- transformar aceite em plano de validação e tasks atômicas;
- separar implementação de avaliação;
- impedir `done` sem evidence pack aprovado;
- preservar estado entre sessões e agentes;
- manter iniciativas numeradas e encontráveis via `specs/INDEX.md`;
- converter falhas sérias ou recorrentes em ratchets.

Harness Engineering aparece apenas como a camada de regras, execução,
validação, memória e qualidade ao redor do SDD. Este repositório não é SaaS,
frontend, workflow engine, knowledge base ou regras de um domínio consumidor.

## Estrutura

```txt
.harness/
  AGENTS.md               # entrypoint operacional
  agents/                 # papéis e limites
  rules/                  # soft rules + hard mirror recommendations
  workflows/              # lifecycle, feature, bugfix, refactor, recovery
  skills/                 # métodos reutilizáveis
  templates/              # artefatos canônicos copiáveis
  gc/ratchet.md           # aprendizado do próprio bundle
  memory/MEMORY.md        # princípios estáveis do bundle
docs/                     # arquitetura, operação, aceite e referências
scripts/
  new_initiative.py       # scaffolding opcional, sem workflow engine
  validate_bundle.py      # validação determinística do bundle
specs/                    # iniciativas numeradas e INDEX.md deste source bundle
```

## Consumo rápido

No projeto consumidor:

```bash
git submodule add https://github.com/SUA-ORG/sdd-harness-guardian.git vendor/sdd-harness-guardian
git -C vendor/sdd-harness-guardian checkout v0.1.2
python vendor/sdd-harness-guardian/scripts/new_initiative.py minha-feature
```

Depois, o agente deve ler:

```txt
AGENTS.md do projeto consumidor
vendor/sdd-harness-guardian/.harness/AGENTS.md
specs/INDEX.md
specs/001-minha-feature/spec.md
specs/001-minha-feature/stakeholder-brief.html
```

O script de scaffolding é conveniência; os templates também podem ser copiados
manualmente. Veja `INSTALL.md` para instalação, pin, upgrade, rollback,
adaptação local e versionamento.

Novas iniciativas usam `specs/NNN-slug/`. O número é identidade sequencial e
ordem cronológica, não prioridade. `specs/INDEX.md` é o mapa compacto lido antes
de carregar artefatos completos ou acionar busca semântica opcional.

## Contrato de isolamento

O bundle permanece inteiro em `vendor/sdd-harness-guardian/`. Specs, código,
segredos, decisões de domínio e estado da iniciativa pertencem ao consumidor.
Adaptadores finos na raiz podem apontar para o entrypoint do bundle.

## Precedência e overrides

O consumidor pode adaptar defaults do bundle. Não pode enfraquecer segurança,
privacidade, aprovação destrutiva, Outcome Ready, Spec Ready, rastreabilidade de validação,
evidência antes de done, avaliação independente ou estado retomável. Conflitos
devem ser registrados e escalados.

## Manutenção e release

```bash
python scripts/validate_bundle.py
```

Para publicar, mantenha `VERSION`, `manifest.yaml` e `CHANGELOG.md` alinhados,
execute o validador, obtenha avaliação independente, faça commit e crie a tag
imutável `v<versão>`. O procedimento completo está em `INSTALL.md`.
