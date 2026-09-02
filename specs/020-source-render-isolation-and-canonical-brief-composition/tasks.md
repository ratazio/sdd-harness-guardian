# Tasks — SPEC 020

| ID | Status | Título | Dependência | Risco | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Tornar o scaffold inequivocamente source-only | nenhuma | high | codex-builder-020 | spec020_t001_evaluation | evidence/T-001.md |
| T-002 | done | Promover briefs somente por composição revisada | T-001 | high | codex-builder-020 | /root/t002_final_evaluation | evidence/T-002.md |
| T-003 | done | Provar isolamento fonte→brief contra mistura entre mocks | T-002 | high | codex-builder-020 | /root/t003_nesting_evaluation | evidence/T-003.md |
| T-004 | done | Rodar mocks e revisão humana em duas passagens | T-001–T-003 | high | codex-builder-020 | /root/t004_completion_audit | evidence/T-004.md |

## T-001 — Tornar o scaffold inequivocamente source-only

**Objetivo:** eliminar criação e apresentação de HTML vazio como artefato de SPEC.
**FR/AC:** FR-001, AC-001. **Incremento:** `new_initiative` cria fontes e
`brief_phase: not_rendered`; validação detecta fase/artefato incompatíveis.
**Validação:** V-001/V-002. **Por que agora:** sem essa fronteira qualquer
composição posterior pode ser confundida com entrega.
**Saída:** nenhum HTML/asset em consumer temporário; estado e docs coerentes.
**Evidence/exit:** comandos V-001/V-002 PASS, diff de criação e avaliador
distinto confirmam ausência de HTML; `evidence/T-001.md` mapeia AC-001.

## T-002 — Promover briefs somente por composição revisada

**Objetivo:** introduzir a fronteira oficial de promoção de candidato para HTML.
**FR/AC:** FR-002, FR-003, AC-002. **Incremento:** promotor exige revisão
distinta/digest, política Pearson, logo local, sem sobrescrita e pós-review.
**Validação:** V-003/V-004. **Dependência:** T-001. **Risco:** alto.
**Saída:** negativos para shell, reclassificação, hotlink e HTML precoce.
**Evidence/exit:** V-003/V-004 PASS, registro de digest/revisão e avaliador
distinto confirmam AC-002; `evidence/T-002.md` registra limites residuais.

## T-003 — Provar isolamento fonte→brief contra mistura entre mocks

**Objetivo:** detectar e impedir conteúdo de uma iniciativa em outra.
**FR/AC:** FR-004, AC-003. **Incremento:** fixture com sentinelas e teste de
origem; guidance de composição reporta fonte faltante em vez de reutilizar texto.
**Validação:** V-005. **Dependência:** T-002. **Risco:** alto.
**Evidence/exit:** teste negativo introduz fato estrangeiro com origem inválida,
teste positivo prova allowlist/locator/digest por bloco; `evidence/T-003.md`
liga resultado a AC-003 e o avaliador confirma que não é simples busca textual.

## T-004 — Rodar mocks e revisão humana em duas passagens

**Objetivo:** provar qualidade decisória em casos diversos, não só estrutura.
**FR/AC:** FR-005, FR-006, AC-004/AC-005. **Incremento:** nova raiz de mocks, avaliações
HTML-first e HTML×Markdown por arquiteto, system designer, delivery,
diretor/C-level, desenvolvedor e stakeholder geral.
**Validação:** V-006. **Dependência:** T-001–T-003. **Risco:** alto.
**Saída:** matriz de pareceres; qualquer `REVISE` material bloqueia aprovação.
Defeito isolado é corrigido, rerenderizado e reavaliado; causa sistêmica/recorrente
gera SPEC corretiva, nunca PASS cosmético.
**Evidence/exit:** todos os mocks descobertos em `testes/mock-tests` têm raiz
nova, digest de pedido/fontes/HTML e sete lentes × duas passagens; nenhum caso
recebe baseline/APPROVE com REVISE material. `evidence/T-004.md` contém matriz,
comandos e link da SPEC corretiva quando aplicável.
