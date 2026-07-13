# Changelog

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
