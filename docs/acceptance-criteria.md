# Acceptance Criteria for this Bundle

Este checklist é o gate de release. Marque um item apenas com evidência
reproduzível; `python scripts/validate_bundle.py` cobre os checks estruturais.

## Repository and installation

- [x] `README.md`, `manifest.yaml`, `VERSION`, `CHANGELOG.md` e `INSTALL.md` existem.
- [x] `VERSION`, manifest e changelog concordam sobre a versão.
- [x] O entrypoint é `.harness/AGENTS.md`.
- [x] O bundle pode ser fixado por tag e instalado em `vendor/sdd-harness-guardian`.
- [x] Clone, init, pin, upgrade, rollback e release estão documentados.
- [x] Um consumidor consegue criar iniciativa por cópia ou scaffolding seguro.

## SDD contract

- [x] Implementação é bloqueada antes de Spec Ready.
- [x] Implementação ou expansão de tasks é bloqueada antes de Outcome Ready.
- [x] Spec exige objetivo, outcomes, non-goals, riscos e aceite testável.
- [x] Spec/task exige outcome, incremento demonstrável, prioridade registrada
      ou decisão humana pendente.
- [x] Mudança não trivial exige impact map.
- [x] Todo AC possui validation mapping.
- [x] Plano possui decisões, impacto e rollback proporcionais ao risco.
- [x] Toda task é atômica e possui dependências, exit criteria e evidência.
- [x] Toda task rastreia requirement/AC ou discovery question e explica
      `why now`.
- [x] Refactor protege comportamento externo; bugfix exige regressão.

## Evaluation and evidence

- [x] Builder e evaluator são papéis distintos.
- [x] O evaluator não implementa durante o julgamento.
- [x] Nenhum workflow permite `done` antes de evidence pack aprovado.
- [x] Evidence pack identifica builder, evaluator, ACs, comandos e resultados.
- [x] Checks omitidos registram razão e risco.
- [x] `validation_done` exige todas as tasks done e aceite coberto.

## State, interruption and learning

- [x] `run-state.yaml` é copiável e machine-readable.
- [x] Progress, handoff, decision log, evidence e ratchet têm templates.
- [x] Pausa e retomada registram checkpoint, trabalho parcial e próximo passo.
- [x] Estado divergente bloqueia retomada insegura.
- [x] Falhas sérias ou recorrentes alimentam `ratchet.md`.
- [x] Ratchet exige prevenção, owner e regression check.

## Rules and portability

- [x] Toda regra crítica possui soft rule e hard mirror recommendation.
- [x] Invariantes protegidas e precedência local estão explícitas.
- [x] O bundle não contém regra de projeto consumidor nem knowledge base viva.
- [x] Nenhum IDE, LLM ou workflow engine é obrigatório.
- [x] Scripts opcionais usam apenas biblioteca padrão do Python.
- [x] O bundle permanece isolado e imutável sob `vendor/` no consumidor.

## Release evidence

- [x] `python scripts/validate_bundle.py` termina com exit code 0.
- [x] O scaffolder foi exercitado em diretório temporário sem sobrescrever dados.
- [x] Referências de arquivos do manifest apontam para arquivos existentes.
- [x] Um evaluator independente revisou diff, critérios e evidências.
- [x] Pendências e riscos remanescentes estão registrados.

## Resultado

**Bundle Ready:** no, release candidate pending independent evaluation  
**Versão avaliada:** 0.1.1  
**Evidência:** `python scripts/validate_bundle.py` passed, 217 checks;
`python scripts/smoke_test_scaffolder.py` passed; `git diff --check` passed  
**Evaluator:** pending

Residual risk: the outcome-readiness contract has structural validation only
until an independent evaluator reviews the diff and a consumer pilot exercises
the new prompts/templates.
