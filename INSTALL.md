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

Para bugfix:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py corrigir-login --kind bugfix
```

O script falha se `specs/<initiative>` já existir e nunca sobrescreve trabalho.
Ele apenas copia templates e cria `evidence/` e `handoffs/`; não executa o
workflow.

Sem Python, crie `specs/<initiative>/` e copie os arquivos listados em
`.harness/templates/README.md`. Substitua os placeholders antes do
Outcome/Spec Review e mantenha `stakeholder-brief.html` sincronizado para
iniciativas não triviais.

## 4. Operar e retomar

Instrua o agente a ler, nesta ordem:

1. regras locais;
2. `vendor/sdd-harness-guardian/.harness/AGENTS.md`;
3. `specs/<initiative>/run-state.yaml` em retomadas;
4. os demais artefatos indicados pelo estado;
5. o workflow correspondente em `.harness/workflows/`.

Uma task só chega a `done` depois de evidence pack e avaliação independente.
Se não houver evaluator distinto disponível, mantenha `needs_evaluation`.

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
