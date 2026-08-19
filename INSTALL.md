# Instalação, consumo e versionamento

## Pré-requisitos

- Git com suporte a submódulos;
- acesso de leitura ao repositório do bundle;
- um agente capaz de ler arquivos Markdown/YAML;
- Python 3 apenas para os scripts opcionais de scaffolding e validação.

Nenhum provedor de LLM, IDE ou workflow engine específico é obrigatório.

## 1. Instalar e fixar uma versão

Na raiz do projeto consumidor:

```bash
git submodule add https://github.com/SUA-ORG/sdd-harness-guardian.git vendor/sdd-harness-guardian
git -C vendor/sdd-harness-guardian checkout v0.1.2
git add .gitmodules vendor/sdd-harness-guardian
git commit -m "vendor sdd-harness-guardian@0.1.2"
```

Clones posteriores devem inicializar o submódulo:

```bash
git clone --recurse-submodules <consumer-url>
# ou, em clone existente:
git submodule update --init --recursive
```

Confirme o pin:

```bash
git -C vendor/sdd-harness-guardian describe --tags --exact-match
git submodule status vendor/sdd-harness-guardian
```

## 2. Criar o adaptador local

O `AGENTS.md` do consumidor deve apontar para o bundle sem copiar seu conteúdo:

```md
# Agent Instructions

Read project-local instructions and specs first.
Also read `vendor/sdd-harness-guardian/.harness/AGENTS.md`.

Use SDD Harness Guardian for software-delivery initiatives. Local rules may
adapt bundle defaults but may not weaken safety, destructive-operation
approval, Outcome Ready, Spec Ready, validation traceability, evidence-before-done,
independent evaluation, or resumable-state invariants.
```

Adaptadores equivalentes podem existir em `CLAUDE.md`, `GEMINI.md` ou regras
da IDE. O bundle continua isolado em `vendor/`.

## 3. Criar uma iniciativa

Opção recomendada, na raiz do consumidor:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py minha-feature
```

Isso cria `specs/001-minha-feature/` no primeiro uso e registra a linha em
`specs/INDEX.md`. O novo scaffold usa a linhagem v2 e começa com todos os gates
falsos; ele não autoriza task ou implementação.

Para bugfix:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py corrigir-login --kind bugfix
```

O script falha se `specs/NNN-<initiative>` já existir e nunca sobrescreve trabalho.
Ele falha também ao detectar sequência reutilizada, slug duplicado ou iniciativa
legada sem número com o mesmo slug. Ele apenas copia templates, cria
`evidence/` e `handoffs/`, atualiza o índice e não executa o workflow.

Sem Python, crie `specs/NNN-<initiative>/`, mantenha `specs/INDEX.md`, e copie
os arquivos listados em `.harness/templates/README.md`. Substitua os placeholders antes do
Outcome/Spec Review e mantenha `stakeholder-brief.html` sincronizado para
iniciativas não triviais.

Iniciativas históricas/pinned com brief v1 continuam válidas sob o contrato
v1. Não as reescreva automaticamente: em refresh material, siga o diagnóstico
de migração do validador ou registre uma exceção legacy revisada.

## 4. Operar e retomar

Instrua o agente a ler, nesta ordem:

1. regras locais;
2. `vendor/sdd-harness-guardian/.harness/AGENTS.md`;
3. `specs/INDEX.md`;
4. `specs/NNN-<initiative>/run-state.yaml` em retomadas;
5. os demais artefatos indicados pelo estado;
6. o workflow correspondente em `.harness/workflows/`.

Em projetos legados com `specs/<slug>/`, faça inventário, proponha mapa de
renome para `specs/NNN-slug/`, atualize referências e registre a decisão antes
de continuar a criar novas iniciativas.

Uma task só chega a `done` depois de evidence pack e avaliação independente.
Se não houver evaluator distinto disponível, mantenha `needs_evaluation`.

Para v2, tasks preliminares são apenas discussão. Depois da reunião, acrescente
a decisão no `decision-log.md`, propague-a para cada fonte canônica afetada,
refaça os checks de coverage/freshness e regenere o brief. Só então o
Orchestrator pode declarar `tasks_ready`; HTML nunca é o único registro.

## 4.1 Aplicar o gate Human Visibility no consumidor

Crie um comando local que execute o validador antes de task breakdown ou implementacao para iniciativas nao triviais:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/NNN-slug
```

Em CI, passe tambem `--base-ref <ref-base-da-PR>`; fora de Git, use o baseline local depois da revisao independente. O retorno nao-zero bloqueia o wrapper, hook ou job. O contrato completo esta em [`docs/consumer-enforcement.md`](docs/consumer-enforcement.md).

## 5. Atualizar ou fazer rollback do bundle

Atualize para uma tag revisada:

```bash
git -C vendor/sdd-harness-guardian fetch --tags
git -C vendor/sdd-harness-guardian checkout v0.2.0
git add vendor/sdd-harness-guardian
git commit -m "vendor sdd-harness-guardian@0.2.0"
```

Rollback é o mesmo processo apontando para a tag anterior e registrando o
motivo no commit. Não edite arquivos dentro do submódulo a partir do consumidor;
proponha mudanças no repositório fonte e publique nova versão.

## 6. Publicar uma versão do bundle

No repositório fonte:

1. atualize `VERSION`, `manifest.yaml` e `CHANGELOG.md`;
2. execute `python scripts/validate_bundle.py`;
3. obtenha avaliação independente e feche o evidence pack da release;
4. revise o diff e faça commit;
5. crie e envie uma tag imutável.

```bash
git add .
git commit -m "sdd-harness-guardian 0.1.2"
git branch -M main
git remote add origin https://github.com/SUA-ORG/sdd-harness-guardian.git
git push -u origin main
git tag -a v0.1.2 -m "sdd-harness-guardian 0.1.2"
git push origin v0.1.2
```

Nunca mova uma tag publicada. Correções exigem nova versão SemVer.

## Verificação operacional

No source bundle:

```bash
python scripts/validate_bundle.py
```

Em um consumidor temporário, valide que um segundo agente consegue: ler o
entrypoint, criar a iniciativa, completar Spec/Impact/Plan/Validation/Brief/Tasks,
implementar uma task, produzir `evidence/<task-id>.md`, obter avaliação
independente e retomar a partir de `run-state.yaml` sem instruções externas.
