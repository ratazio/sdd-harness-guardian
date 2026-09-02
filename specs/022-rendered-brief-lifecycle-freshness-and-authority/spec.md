# SPEC 022 — Lifecycle, freshness e autoridade do brief renderizado

**Status:** draft, source-only corrective initiative. **Owner:** Guardian
maintainers. **Risk:** high / A2. **Origin:** SPEC 021 rendered-decision
review, 2026-08-28.

## Problem

`render_stakeholder_brief.py` promove copiando os bytes do candidato e só
depois altera `run-state.yaml` para `brief_phase: rendered`. O HTML entregue
retém `data-brief-phase="authored"`, texto de candidato, o revisor pré-render e
o digest do estado anterior. Assim, o HTML e as fontes canônicas contradizem a
autoridade atual; o problema é independente de domínio e reproduzível em
qualquer iniciativa que renderize uma composição com proveniência de estado.

## Objective and outcome

Fazer com que uma promoção deixe um brief renderizado que prove, por fontes
atuais e texto visível, sua fase, identidade, autoridade e revisão pendente —
sem editar HTML isoladamente, enfraquecer digest/proveniência ou fazer código
avaliar significado.

**Demonstrable increment:** transição promocional atômica com fonte/HTML
sincronizados, regressões de estado/digest/autoridade e uma revisão independente
do HTML pós-render. **Non-goals:** mudar a semântica de domínio, substituir o
hook humano da SPEC 021, ou autorizar baseline por um PASS determinístico.

**Bootstrap limitado:** por autorização explícita do usuário, T-001 reúne a
implementação mínima completa que torna o promotor capaz de renderizar esta
própria SPEC. A exceção não alcança prosa de domínio nem T-002–T-004; cada
etapa mantém evidence e avaliação independente.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-022-01 | A promoção deve materializar `brief_phase: rendered` e atualizar somente a allowlist fechada de blocos/atributos de lifecycle declarados, com fase, estado ou digest dessa fonte, antes de expor o artefato. |
| FR-022-02 | O HTML renderizado deve declarar autoridade pós-render verdadeira: a composição pré-render foi concluída, a revisão qualitativa renderizada ainda é o próximo gate e nenhum texto pode chamá-lo de candidato pendente. |
| FR-022-03 | Falha no sync deve deixar um estado recuperável definido por journal/backup, sem HTML contraditório apresentado como entrega; a retomada deve reparar ou recusar esse estado antes de outra promoção. |
| FR-022-04 | Verificações determinísticas devem comparar identidade, fase e bytes atuais, mas não avaliar suficiência de prosa, materialidade, domínio ou qualidade visual. |
| FR-022-05 | SPEC 021 deve ser recomposta em nova tentativa e passar revisão pré-render ligada ao candidato exato e cinco lentes pós-render distintas ligadas ao HTML exato antes de liberar T-001. |

## Acceptance criteria

| ID | Criterion | Validation |
|---|---|---|
| AC-022-01 | Fixture promovida mostra `rendered` e digests de fonte atuais em cada marcador da allowlist; marcador desconhecido/duplicado é recusado. | V-022-01 |
| AC-022-02 | HTML pós-render diferencia corretamente aprovação pré-render, revisão renderizada pendente e Tasks Ready falso. | V-022-02 |
| AC-022-03 | Falha injetada em cada ponto do protocolo de commit deixa apenas o estado recuperável documentado; a próxima execução o repara ou recusa antes de expor entrega. | V-022-03 |
| AC-022-04 | Regressões confirmam que o novo contrato não vira score, taxonomia ou aprovação semântica. | V-022-04 |
| AC-022-05 | Nova tentativa da SPEC 021 recebe APPROVE pré-render do candidato exato e APPROVE pós-render de cinco identidades/lentes distintas; qualquer REVISE material bloqueia T-001/Human Visibility/Tasks Ready. | V-022-05a/V-022-05b |

## Constraints and risks

- Preservar source-only scaffold, exact-record digest, proveniência por bloco,
  Pearson opt-in e revisão humana de suficiência.
- Nenhum rewrite pode fabricar conteúdo de domínio; ele só sincroniza fatos de
  lifecycle já declarados em fontes canônicas.
- R-022-01: uma reescrita amplia-se a prosa arbitrária; controle: transformação
  delimitada a atributos/fragmentos de lifecycle e testes adversários.
- R-022-02: o brief afirma revisão pós-render não executada; controle: estado
  pendente explícito e gate humano distinto.

`evidence/T-000-spec021-rendered-review.md` conserva a reprodução. Esta SPEC
não possui HTML até que o pacote de fonte esteja completo e revisado.
