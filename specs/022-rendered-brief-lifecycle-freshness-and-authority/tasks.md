# Tasks — SPEC 022

| ID | Status | Title | Dependency | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Implementar o contrato mínimo atômico de lifecycle no promotor | none | high | `spec022_t001_builder` | `spec022_t001_evaluator_r4` | evidence/T-001.md |
| T-002 | done | Integrar o contrato aos controles e caminhos de regressão | T-001 | high | `spec022_t002_builder` | `spec022_t002_evaluator_r4` | evidence/T-002.md |
| T-003 | done | Provar recusas e limites não semânticos | T-001/T-002 | high | `spec022_t003_authority_builder`; `spec022_t003_coverage_fix` | `/root/final_reevaluate_spec022_t003` | evidence/T-003.md; evidence/T-003-final-evaluation-d022060.md |
| T-004 | done | Revalidar SPEC 021 em nova tentativa completa | T-001–T-003 | high | `/root/bind_d022048_review` | `/root/review_t004_arch_system` | evidence/T-004.md |

T-003's earlier repairs were independently approved by
`/root/evaluate_closed_gate_contract` (D-022-030) and
`/root/evaluate_d022034_repair` (D-022-035). The final independent evaluation
`/root/final_reevaluate_spec022_t003` approved the finalized rendered pair in
D-022-060, including recovery/provenance/lifecycle boundaries and the 272-check
bundle run. This closes T-003 only; it does not start T-004 or authorize Human
Visibility, Tasks Ready, delivery or SPEC 021.

- **T-001 / AC-022-01/02/03:** implementa no promotor o recorte mínimo inteiro
  que rompe o bloqueio de auto-hospedagem: schema/allowlist fechado de IDs,
  localizações/atributos, fonte, fragmento e valor derivável; recusa de
  desconhecido/duplicado; transformação exclusiva dos bytes allowlisted;
  temp, journal, backup, ordem de rename e recuperação antes da exposição.
  Inclui fixtures e falhas injetadas em cada ponto de commit/recovery. Não
  interpreta prosa de domínio. Exit: promoção/recusa recuperável, V-022-01 a
  V-022-03 no recorte, evidence e APPROVE de avaliador distinto.
- **T-002 / AC-022-01/03/04:** integra o contrato mínimo aos controles de
  promoção/validação e aos caminhos de regressão ordinários, inclusive refresh
  explícito de histórico, e prova os limites não semânticos. Não reimplementa
  a transação de T-001. Exit: regressões de integração, evidence e avaliação
  independente.
- **T-003 / AC-022-03/04:** injeta falha em cada ponto de commit/recuperação,
  testa fase/digest/autoridade stale e prova que o código não decide
  materialidade/suficiência. Exit: bundle e evidence aprovada.
- **T-004 / AC-022-05:** usa uma nova tentativa de SPEC 021, candidata exata e
  revisão pré-render independente, promoção sincronizada e cinco identidades
  pós-render. Registra digests e papéis; qualquer REVISE material bloqueia
  Human Visibility, Tasks Ready e T-001 da 021.
