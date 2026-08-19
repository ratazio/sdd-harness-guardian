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
3. Leia `specs/INDEX.md` e localize a spec alvo em `specs/NNN-slug/`.
4. Se a iniciativa não existir, leia
   `vendor/sdd-harness-guardian/.harness/templates/README.md` e crie-a por
   cópia ou com `scripts/new_initiative.py`.
5. Leia `vendor/sdd-harness-guardian/.harness/workflows/sdd-lifecycle.md` e o
   workflow específico (feature, bugfix ou refactor).

Modo de operação:
- Trabalhe pelo fluxo completo specify -> outcome review -> review -> impact -> plan ->
  validation plan -> task draft -> coverage review -> stakeholder brief -> meeting ->
  decisão no log + propagação para fontes -> regeneração -> Tasks Ready -> implement ->
  evidence -> independent evaluation. O trecho task draft/coverage/reunião é v2;
  briefs v1 históricos/pinned seguem o caminho legado até migração explícita.
- Não implemente nem expanda tasks enquanto outcome, incremento demonstrável,
  validação e `why now` não estiverem declarados.
- Não implemente nada enquanto a spec não estiver Outcome Ready e Spec Ready.
- Para trabalho v2 não trivial, tasks preliminares podem ser geradas para a
  reunião, mas não execute nem marque `ready` antes de coverage review distinta,
  decisão propagada, checks refeitos e brief regenerado. Para v1 histórico,
  preserve o contrato pinned até a rota de migração/exception revisada.
- Não marque task como done sem evidence pack aprovado por evaluator distinto.
- Separe implementação de avaliação.
- Preserve estado em `specs/NNN-<initiative>/progress.md` e `specs/NNN-<initiative>/run-state.yaml`.
- Registre decisões em `specs/NNN-<initiative>/decision-log.md`.
- Registre handoff em `specs/NNN-<initiative>/handoffs/latest-handoff.md`.
- Mantenha `specs/INDEX.md` sincronizado com status, resumo, owner e data.
- Se encontrar erro sério ou recorrente, registre uma entrada de ratchet.
- Se houver interrupção, atualize checkpoint, trabalho parcial, handoff e
  `resume_required` antes de encerrar.

Para iniciativas nao triviais, antes de task breakdown ou implementacao, execute:

```txt
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/NNN-slug
```

Ao criar ou atualizar o brief, popule o template canônico do Guardian e leia
`vendor/sdd-harness-guardian/.harness/templates/stakeholder-brief-design.md`.
Não reconstrua uma página mínima. Um layout materialmente customizado exige
exceção revisada, com rationale, owner e decision surfaces retidas no
`decision-log.md` da iniciativa.

Depois de uma reunião v2, extraia decisões para o `decision-log.md` append-only,
atualize todas as fontes canônicas afetadas, refaça checks de coverage/freshness
e regenere o brief. Nunca altere somente HTML nem declare `tasks_ready` antes
desse ciclo; o consumidor é dono dessas ações.

Em CI, acrescente `--base-ref <base-da-PR>`. Um passe estrutural nao substitui
a revisao semantica/renderizada curta e independente; ambas sao obrigatorias
para alegar Human Visibility Ready.

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
