# Prompt para usar o guardião em um projeto consumidor

Rode este prompt na raiz do projeto consumidor, depois de instalar o submódulo em `vendor/sdd-harness-guardian`.

```txt
Você está dentro de um projeto consumidor que usa o bundle `vendor/sdd-harness-guardian`.

Antes de agir:
1. Leia `vendor/sdd-harness-guardian/.harness/AGENTS.md`.
2. Leia as regras locais do projeto, se existirem:
   - `AGENTS.md`
   - `.harness/AGENTS.md`
   - `.harness/rules/`
   - `.cursor/rules/`
   - `CLAUDE.md`
   - `GEMINI.md`
3. Leia a spec alvo em `specs/`.
4. Se a iniciativa não existir, leia
   `vendor/sdd-harness-guardian/.harness/templates/README.md` e crie-a por
   cópia ou com `scripts/new_initiative.py`.
5. Leia `vendor/sdd-harness-guardian/.harness/workflows/sdd-lifecycle.md` e o
   workflow específico (feature, bugfix ou refactor).

Modo de operação:
- Trabalhe pelo fluxo completo specify -> outcome review -> review -> impact -> plan ->
  validation plan -> stakeholder brief -> tasks -> implement -> evidence ->
  independent evaluation.
- Não implemente nem expanda tasks enquanto outcome, incremento demonstrável,
  validação e `why now` não estiverem declarados.
- Não implemente nada enquanto a spec não estiver Outcome Ready e Spec Ready.
- Para trabalho não trivial, não gere ou execute tasks antes de
  `stakeholder-brief.html` estar conciso, revisável e sincronizado.
- Não marque task como done sem evidence pack aprovado por evaluator distinto.
- Separe implementação de avaliação.
- Preserve estado em `specs/<initiative>/progress.md` e `specs/<initiative>/run-state.yaml`.
- Registre decisões em `specs/<initiative>/decision-log.md`.
- Registre handoff em `specs/<initiative>/handoffs/latest-handoff.md`.
- Se encontrar erro sério ou recorrente, registre uma entrada de ratchet.
- Se houver interrupção, atualize checkpoint, trabalho parcial, handoff e
  `resume_required` antes de encerrar.

Ao final:
Entregue um resumo com:
- spec usada;
- stakeholder brief usado, quando aplicável;
- task executada;
- arquivos alterados;
- validações executadas;
- evidências;
- riscos remanescentes;
- próximo passo recomendado.
```
