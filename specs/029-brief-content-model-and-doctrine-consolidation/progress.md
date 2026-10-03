# Progress — 029-brief-content-model-and-doctrine-consolidation

**Última atualização:** 2026-09-19
**Fase atual:** `implementation`, interrompida em checkpoint seguro
**Stakeholder brief:** ainda não existe — projetado em T-010 pela esteira nova
(D-007/D-011/D-012). Sua ausência é obrigatória até lá e não é lacuna.

## Linha do tempo

| Data | Evento |
|---|---|
| 2026-09-19 | Auditoria da doutrina: 12 contradições verificadas com arquivo e linha (Anexo A) |
| 2026-09-19 | SPEC 029 criada; 028 superseded (D-002); 010, 015–019, 021, 022, 025, 027 encerradas como passado (D-003, D-005) |
| 2026-09-19 | Spec Ready aprovado na **rodada 3** de revisão independente |
| 2026-09-19 | Plan Ready e Validation Ready aprovados numa passagem, com vereditos separados |
| 2026-09-19 | T-001 `done` — schema validado contra briefs reais |
| 2026-09-19 | T-002 `done` — projetor, após corrigir colisão de locator |
| 2026-09-19 | T-003 `done` — formas e perfis, após 3 ciclos de revisão |
| 2026-09-19 | T-005 `done` — eixo único e reconciliação de vocabulário |
| 2026-09-19 | **Interrompido:** T-006 a T-010 bloqueadas por AC-012 (humano nomeado) |

## Tasks

| Task | Estado |
|---|---|
| T-001 schema | `done` |
| T-002 projetor | `done` |
| T-003 formas e perfis | `done` |
| T-004 contrato normativo | `escalate_to_human` — AC-012 |
| T-005 eixo único | `done` |
| T-006 suficiência de fontes | `pending` (← T-004) |
| T-007 cadeia de duas revisões | `pending` (← T-004) |
| T-008 remoção (destrutiva) | `pending` |
| T-009 medição e matriz | `pending` |
| T-010 brief da 029 e gates | `pending` |

## O que a construção já ensinou

Três achados que o processo anterior não teria capturado, todos vindos de
revisão independente sobre artefatos pequenos:

1. **A contradição migra do enunciado para o procedimento.** A-17 foi corrigido
   em BC-007/BC-013 e sobreviveu em BC-009/BC-016 — a doutrina que o revisor de
   fato executa. Só a terceira rodada pegou.
2. **Proveniência falsa passando na verificação.** `resolve_locator` casava
   `Escopo` com `Fora de escopo` por substring, e no caminho `not_applicable`
   o locator resolvido virava o fragmento exibido.
3. **Medição subestimada vira decisão errada.** A contagem de doutrina por
   papel omitia `human-visibility.md`; corrigir mudou a conclusão de "26–85%
   acima da meta" para "57–130% acima", e adiou a renegociação de AC-009b.

E duas lições de processo, ambas caras:

- **Paralelizar tasks que tocam o mesmo contrato produz divergência.** Ocorreu
  duas vezes em duas tentativas (IR-007).
- **Verificação de baseline por manipulação de árvore mente em silêncio**, e
  mente concordando com a conclusão errada (R-029-001).

## Riscos e bloqueios

- **Bloqueio único:** AC-012 exige confirmação humana nomeada. Ver
  `handoffs/latest-handoff.md`.
- **IR-006** vivo: T-003 e T-004 aumentaram o corpus por papel. O saldo de
  remoção que a iniciativa promete depende inteiramente de T-008.
- **IR-003** aberto, rebaixado para médio.
- **AC-009b** não atingido; renegociação adiada para depois de T-008 (D-025).

## Evidências aprovadas

`evidence/T-001.md`, `evidence/T-002.md`, `evidence/T-003.md`,
`evidence/T-005.md` — todas com decisão `approve` de identidade distinta do
builder. `evidence/T-004.md` existe e está completa, mas sua decisão é
`escalate_to_human`.
