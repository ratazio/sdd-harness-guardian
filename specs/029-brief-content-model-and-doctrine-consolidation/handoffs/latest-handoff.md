# Handoff — 029-brief-content-model-and-doctrine-consolidation

**Data:** 2026-09-19
**De:** Delivery Orchestrator (sessão de construção)
**Para:** próximo operador humano ou agente
**Estado:** `executing`, interrompido em checkpoint seguro
**Working tree:** limpa em `validate_bundle.py` (315 checks) e `pytest` (63 passed). **Nada commitado.**

## Por que parou

Tudo o que resta depende de **T-004**, e T-004 está em `escalate_to_human`
porque **AC-012 exige confirmação por humano nomeado**. Nenhum agente pode
suprir essa confirmação sem quebrar a invariante que a própria SPEC protege.

```
T-006 → T-004      T-008 → T-001…T-007      T-010 → T-009
T-007 → T-004      T-009 → T-008
```

## A decisão pendente, em uma leitura

As **10 invariantes protegidas** de `.harness/AGENTS.md` estão **bit a bit
idênticas** antes e depois de T-004. Houve uma única alteração:

```diff
- ausência do HTML é obrigatória e não deve ser apresentada como entrega;
+ ausência do HTML é obrigatória e não deve ser apresentada como entrega
+ (regras detalhadas: `.harness/rules/brief-contract.md`, BC-001);
```

A regra permanece por extenso; a citação é rastreio adicional, não
substituição. Quem ler só o `AGENTS.md` e ignorar o ponteiro ainda tem a regra
completa. Duas identidades independentes verificaram e julgaram preservado.

**Ação:** registrar a confirmação humana nomeada em `decision-log.md`, mover
T-004 para `approved` → `done`, e liberar T-006 e T-007.

## Concluídas, com evidência aprovada por identidade distinta

| Task | Entrega | Ciclos de revisão |
|---|---|---|
| T-001 | Schema `brief-model.yaml` | 1 |
| T-002 | Projetor modelo → HTML | 2 (colisão de locator) |
| T-003 | Formas, perfil × domínio, SVG de topologia | 4 (A-17, IR-003, medição) |
| T-005 | Eixo único de versão + reconciliação de vocabulário | 2 (valor vs presença, D-027) |

## Pendências nomeadas, todas com dono e disposição

- **AC-009b** não atingido. Medição honesta: 23.573 a 34.493 chars por papel,
  contra meta de 15.000. Renegociação adiada para depois de T-008 (**D-025**),
  quando a absorção de `human-visibility.md` e `stakeholder-brief-design.md`
  tornar o número final.
- **IR-003 aberto**, rebaixado para médio (**D-029**). O modelo de conteúdo
  generaliza para domínio não-software; o inventário de fontes não (**D-028**).
- **A-13** `deferred` (**D-006**): vocabulário misto de status do `INDEX.md`
  continua vivo, fora do MVP.
- **Fallback legado** de lineage ainda existe. Nenhuma task assume sua remoção;
  precisa de plano explícito antes de T-008.
- **AC-007, segunda cláusula**: o sinal determinístico de "texto normativo
  disperso" é exit criterion pendente de T-004. Até existir, a separação
  regra/tabela entre contrato e SKILL do compositor vale por julgamento
  textual.

## Riscos vivos

- **IR-006** — a iniciativa virar aditiva. T-004 e T-003 **aumentaram** o
  corpus por papel. O saldo de remoção depende inteiramente de T-008.
- **IR-007** — tasks paralelas produzindo vocabulários divergentes.
  **Ocorreu duas vezes** nesta sessão. Não paralelizar tasks que tocam o mesmo
  contrato normativo sem passo de reconciliação declarado.

## Ratchet

**R-029-001** — verificação de baseline por manipulação de árvore falha em
silêncio neste repositório. `git stash` falhou duas vezes e `git apply -R` uma,
sempre concordando com a conclusão errada. Método correto:
`git worktree add --detach <dir> HEAD` **seguido de** `cp -r testes/ <dir>/`,
porque `testes/` é gitignored. E `pytest` coleta só parte dos 35 arquivos
`scripts/test_*.py` — os standalone precisam rodar direto.

## Próximo passo exato

1. Confirmação humana nomeada de AC-012 → fecha T-004.
2. T-006 e T-007 em paralelo (independentes entre si).
3. T-008 — **única task destrutiva**, exige aprovação humana. Remove os dois
   scripts, a §9.1 e absorve a doutrina residual. É onde o saldo de remoção
   acontece ou a iniciativa falha seu próprio critério.
4. T-009 mede; T-010 projeta o brief da própria 029 e resolve os três gates
   suspensos por D-007/D-011/D-012.
