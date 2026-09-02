# Decision log — SPEC 025

## D-025-001 — Evolve the canonical composition path, do not replace it

**Date:** 2026-09-01  
**Status:** proposed pending independent SPEC review  
**Owner:** Guardian maintainers + brief experience owner  
**Decision:** use `plan.md` as the single intermediate editorial handoff,
introduce an initiative-specific non-promotable candidate skeleton and retain
the guarded renderer as promotion-only.

**Rationale:** workflow/design already contain coverage composition,
source-aware cards, distinct review and the eight-route shell. The missing
bridge is skeleton instantiation and slot continuity, not a second semantic
renderer.

**Boundary:** SPEC 024 references remain non-canonical evidence. This decision
does not migrate briefs or grant task authorization.

## D-025-002 — Lifecycle and disposition repair after independent REVISE

**Date:** 2026-09-01  
**Status:** repaired; awaiting re-review  
**Reviewer finding:** the first draft placed rendered experience review before
promotion, left skeleton identity/location undefined and used `discovery` as a
coverage disposition.  
**Decision:** retain the current order: reviewed map → skeleton → composed
candidate → exact pre-render candidate attestation → guarded promotion →
post-render experience review → meeting propagation. The skeleton lives only
at `brief-candidates/stakeholder-brief.skeleton.html`, does not change
`run-state` from `not_rendered`, and cannot be renderer input. `discovery` is
an owned handoff state; coverage remains the four existing v2 dispositions.

## D-025-003 — SPEC and plan approved after lifecycle repair

**Date:** 2026-09-01  
**Status:** approve  
**Reviewer:** `/root/spec025_independent_review`  
**Decision:** the repaired sequence respects the existing v2 lifecycle and
does not add a second canonical source, a competing renderer or deterministic
semantic approval. The skeleton identity/location and the separation of
coverage disposition from discovery/handoff state are accepted.

**Consequence:** SPEC 025 and its plan are ready. T-001 remains preliminary
until the ordinary v2 coverage, brief and meeting-propagation gates authorize
implementation.

## D-025-004 — Cobertura editorial do brief aprovada

**Date:** 2026-09-01  
**Status:** approve  
**Reviewer:** `/root/spec025_coverage_rereview`  
**Scope:** fontes canônicas da SPEC 025 e §7 de `plan.md`.

**Decision:** o mapa editorial cobre outcome, limites, requisitos, impactos,
riscos/rollback, T-001–T-004, V-025-01–V-025-07, decisões D-025-001–003,
estado/gates, públicos e garantias preservadas.

**Composition provenance:** verified.  
**Human attestation:** confirmed.

**Consequence:** a composição do candidate pode iniciar; a promoção continua
bloqueada até a atestação independente do hash do candidate exato e a revisão
pós-render.

## D-025-005 — Candidate do brief aprovado para promoção guardada

Date: 2026-09-01
Author: /root
Reviewer: /root/spec025_prerender_brief_review
Scope: `brief-candidates/stakeholder-brief.candidate.html` confrontado com
as fontes canônicas e o §7 de `plan.md`.

**Decision:** a instância recupera T-001–T-004, adições/ajustes/remoções,
entrega final, limite entre integridade determinística e julgamento humano,
fluxo, V-025-01–V-025-07, rollback, fronteira do laboratório, gates e
públicos. A arquitetura contém topologia fonte-apoiada, mapa de superfícies,
zoom e legenda verificável. A identidade Pearson é válida no candidate e no
artefato promovido.

Candidate SHA-256: 17275ec4cf7eceacb63c19848b8ea2d6c5dc58a0979fdb36ec436953ac89ebe8
Composition manifest SHA-256: bb5b1a318efbc9c7926356f5d67bce0cf3717d6ba3aaac3c09468d2ea8a6274e
Review outcome: approve
Composition provenance: verified
Human attestation: confirmed

**Consequence:** a promoção guardada pode ser considerada somente para esta
instância. Human Visibility, Tasks Ready e autorização de implementação
continuam falsos até a revisão pós-render e a propagação de decisão de reunião.

## D-025-006 — Revisão pós-render devolveu o brief por fidelidade de lifecycle

**Date:** 2026-09-01  
**Reviewer:** `/root/spec025_postrender_brief_review`  
**Outcome:** revise.

**Finding:** a primeira instância renderizada ainda declarava no rodapé que era
candidate; Evolução/Cobertura omitiam D-025-005, que autorizou a promoção; e
o fluxo em `impact-map.md` ainda invertia atestação pré-render, promoção e
revisão pós-render.

**Decision:** corrigir a fonte, o candidate e a autoridade renderizada; obter
nova atestação exata antes de executar refresh guardado. Esta devolução não
abre Human Visibility, Tasks Ready nem autorização de implementação.

## D-025-007 — Candidate corrigido aprovado para refresh guardado

Date: 2026-09-01
Author: /root
Reviewer: /root/spec025_prerender_brief_review
Scope: candidate recomposto depois de D-025-006, confrontado com fontes e §7 de `plan.md`.

**Decision:** a cadeia recupera agora, sem inversão, candidate → atestação
pré-render → promoção guardada → revisão pós-render. O rodapé projeta a
autoridade renderizada; Evolução/Cobertura mostram D-025-005; e o fluxo do
impact-map tornou-se fiel. Conteúdo, arquitetura verificável e limites de
autoridade permanecem corretos.

Candidate SHA-256: 204aebed9dd8f267f75d38545d911178fb4c8dd755aa96d3ff3f7b244476e724
Composition manifest SHA-256: d7e4b34f0e1095f925928af50f2d757632f6b3e1e01c53f57cef5660e0d1a144
Review outcome: approve
Composition provenance: verified
Human attestation: confirmed

**Consequence:** um único refresh guardado pode substituir a instância
devolvida. Human Visibility, Tasks Ready e autorização de implementação
continuam falsos até a nova revisão pós-render.

## D-025-008 — Execução integral autorizada, com exceção editorial controlada

**Date:** 2026-09-01  
**Decision owner:** requester humano  
**Decision:** executar integralmente a SPEC 025. Quando uma revisão exata
identificar uma pendência editorial mecânica, o brief pode continuar somente
se ela for exposta como ressalva revisada; o próximo agente deve saná-la ou
renovar a justificativa antes do prazo.

**Boundary:** esta autorização não relaxa Candidate SHA-256, manifesto de
composição pré-render, distinção de reviewer, proveniência, lifecycle,
integridade, segurança, recusa de skeleton ou identidade visual. Tampouco uma
ressalva torna Human Visibility ou Tasks Ready verdadeiros por si só.

**Consequence:** T-001 pode iniciar; cada task mantém evidence e avaliação
independente antes de `done`.

## D-025-009 — Avaliação independente de T-001 a T-003

**Date:** 2026-09-01  
**Reviewer:** `/root/spec025_independent_review`  
**Outcome:** approve.

**Decision:** o handoff/documentação, o skeleton não promocionável e o
contrato v3 passaram pela revisão. A avaliação inicialmente devolveu schema,
visibilidade e integração CLI; as três correções foram reapresentadas e
passaram. A CLI prova recusa no modo normal e promoção somente com
`--allow-reviewed-editorial-exceptions` e registro exato válido.

**Consequence:** T-001, T-002 e T-003 podem ser `done`. T-004 continua
necessária: o caso descartável M-003 deve provar a composição rica e obter sua
revisão renderizada distinta.

## D-025-010 — Correção do contrato visual do skeleton

**Date:** 2026-09-01  
**Decision owner:** requester humano  
**Status:** executing corrective work.

**Finding:** o skeleton entregue preserva IDs e lifecycle, mas é uma página de
parágrafos com âncoras. O `plan.md` descreve formas como "topologia", "task
card" e "proof card" sem definir o que cada uma deve explicar ou como se
relaciona com a narrativa executiva. Portanto, ele não é uma instância visual
do template e não protege o compositor de omitir ou improvisar estrutura.

**Decision:** manter `plan.md` como único handoff Markdown e manter o skeleton
em `brief-candidates/` como não-promovível. Corrigir ambos para que o template
seja o contrato visual genérico de oito subpáginas e o skeleton seja sua
instância com slots visíveis. A composição escolhe e preenche componentes com
base nas fontes; checks continuam limitados a estrutura, identidade, slots e
proveniência. A suficiência continua em revisão independente.

**Consequence:** a conclusão anterior da SPEC 025 não cobre T-005. Nenhum
brief, piloto ou referência anterior passa a ser considerado aceito pelo novo
contrato sem recomposição e revisão próprias.

## D-025-011 — T-005 aprovada após revisão independente do contrato visual

**Date:** 2026-09-01  
**Reviewer:** `/root/spec025_contract_audit`  
**Outcome:** approve.

**Evidence reviewed:** `evidence/T-005.md`; template canônico, skeleton da
SPEC 025, `plan.md` e `scripts/test_spec025_visual_skeleton.py`.

**Decision:** o teste agora faz parse dos dois HTMLs e comprova a paridade de
oito rotas, tabs, painéis, IDs, `aria-controls` e famílias visuais. Ambos usam
o contrato `executive-brief-v3`; o mapa inclui T-005 e V-025-09 e a instância
materializa seus slots. A arquitetura contém visão/pilares/topologia/zooms, a
execução contém épicos e dossiês por task e a validação contém pilares, fluxo,
dossiês, oracles e matriz de aceite. A fronteira permanece correta: agente
autora HTML/CSS/JS e decide a representação; scripts não podem resumir fontes
ou construir blocos finais.

**Consequence:** T-005 pode transicionar para `done`. A aprovação não promove
o skeleton, não cria conteúdo factual e não torna Human Visibility ou Tasks
Ready verdadeiros. Uma iniciativa futura precisa de composição fonte-apoiada,
revisão renderizada e decisão de reunião próprias.

## D-025-012 — Skeleton aceito como base obrigatória do candidate

**Date:** 2026-09-01  
**Decision owner:** requester humano  
**Status:** authorize T-006 candidate composition only.

**Decision:** o composer deve copiar o skeleton da iniciativa e preenchê-lo,
em vez de usar seu visual somente como referência.  Arquitetura precisa poder
mostrar o panorama real da solução/ambiente, com alterações destacadas, e uma
segunda representação de fluxo/seqüência quando ela explicar uma relação
distinta. A forma concreta continua dependente das fontes: pode ser aplicação,
operação, dados, navegação, decisão, contrato ou controle; não há topologia
fixa para toda SPEC.

**Boundary:** esta decisão autoriza apenas um candidate novo para a própria
SPEC 025. Não autoriza promoção, substituição do `stakeholder-brief.html`,
abertura de Human Visibility/Tasks Ready ou qualquer geração por Python.

## D-025-013 — Candidate T-006 aprovado para inspeção, não para promoção

**Date:** 2026-09-01  
**Reviewer:** `/root/spec025_contract_audit`  
**Outcome:** approve composition.

**Decision:** o candidate declara e confere a cópia-base do skeleton, usa oito
rotas reais, recupera T-001–T-006 e V-025-01–V-025-10 sem slot factual
pendente. A arquitetura separa panorama do ecossistema da SPEC de seu fluxo
material Markdown → plano/autoria → candidate, sem inventar uma arquitetura de
aplicação inexistente. Impacto, rollback, limites, evolução, decisão e
cobertura permanecem recuperáveis.

**Boundary:** a decisão aprova a composição para inspeção. Não atesta promoção,
não altera o `stakeholder-brief.html` anterior e não abre Human Visibility ou
Tasks Ready. Uma promoção futura continua exigindo atestação exata, revisão
renderizada e decisão humana própria.
