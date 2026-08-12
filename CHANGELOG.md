# Changelog

## 0.2.0

Evolução compatível do bundle para tornar auditoria, organização de specs e
visibilidade humana mais operacionais.

Inclui:

- processo de auditoria do harness com papéis, skill, workflow, regra, relatório
  HTML e contrato para backlog de remediação;
- iniciativas numeradas, `specs/INDEX.md`, normalização de estrutura e scaffolder
  atualizado para o contrato canônico;
- `stakeholder-brief.html` enriquecido como síntese para decisão: outcome,
  benefício, sizing, escopo, impacto, arquitetura, fluxo e critérios de
  proporcionalidade;
- autoria e revisão explícitas do brief no lifecycle, com checklist condicional
  e validações estruturais leves no validator e no smoke test.

## 0.1.2

Evolução pequena de visibilidade humana para specs orientadas a resultado.

Inclui:

- nova regra `human-visibility`;
- novo template `stakeholder-brief.html` para leitura humana em reunião;
- scaffolder copiando o brief para novas iniciativas;
- lifecycle com gate `Human Visibility Ready` antes de task breakdown;
- Spec Guardian, Delivery Orchestrator e task breakdown instruídos a manter o
  brief sincronizado sem torná-lo fonte de verdade;
- validação estrutural e smoke test atualizados para cobrir o novo template.

## 0.1.1

Evolução pequena de outcome readiness para manter SDD orientado a resultado sem
transformar o Guardian em Product Owner.

Inclui:

- nova regra `outcome-readiness`;
- novo gate `Outcome Ready` antes de implementação e expansão de tasks;
- templates de spec, tasks, progress, evidence pack e run-state com campos de
  outcome, incremento demonstrável, validação e `why now`;
- Spec Guardian e Delivery Orchestrator instruídos a pedir esclarecimento quando
  prioridade ou objetivo de negócio estiverem ausentes;
- task breakdown bloqueando expansão de processo sem evidência, validação ou
  redução de risco;
- manifest atualizado para versionar o contrato como `0.1.1`.

## 0.1.0

Versão inicial do bundle `sdd-harness-guardian`.

Inclui:

- modelo operacional de SDD dentro de Harness Engineering;
- agentes centrais do guardião;
- skills de spec review, impact analysis, task breakdown, validation planning, evidence pack e ratchet learning;
- workflows de feature, bugfix, refactor e recuperação de interrupção;
- regras soft e critérios para hard rules;
- templates de spec, plan, tasks, impact map, validation plan, progress, run state, evidence pack e handoff;
- prompt de construção do bundle;
- instruções de instalação como submódulo Git em `vendor/`.
- lifecycle comum com gates explícitos `needs_evaluation -> approved -> done`;
- papel formal de builder e avaliação independente obrigatória;
- templates copiáveis, incluindo `run-state.yaml` direto, reprodução e ratchet;
- scaffolder seguro e validador estrutural opcionais em Python padrão;
- smoke test isolado e reproduzível para o scaffolder;
- regras críticas com soft rule e hard mirror recommendation;
- instalação, pin, upgrade, rollback, retomada e release operacionais.
