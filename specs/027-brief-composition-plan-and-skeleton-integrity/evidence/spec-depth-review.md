# Revisão independente de profundidade — SPEC 027

## Identidade

- **Papel:** `spec-depth-reviewer`
- **Revisor:** `/root/spec027_depth_review` (identidade distinta do autor)
- **Autor avaliado:** `/root`
- **Data:** 2026-09-01
- **Escopo da revisão:** qualidade e coerência do pacote de planejamento; este
  revisor não implementou task, não alterou template, skeleton, hook, scripts
  ou índice.

## Inputs

- Pedido humano de 2026-09-01: resolver o `plan.md` raso e impedir que o
  candidate seja recriado fora do skeleton; manter vendor-neutral por ora;
  preservar composição final agêntica; aplicar hook estreito.
- SPEC 027: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`, `decision-log.md`, `run-state.yaml`, `progress.md` e
  `handoffs/latest-handoff.md`.
- Contrato antecedente: SPEC 025, em especial seu handoff de plano editorial,
  skeleton local, cópia *in situ*, atestação exata e revisão pós-render.
- Diagnóstico do guard atual:
  `scripts/validate_brief_candidate_inheritance.py`.

## Decisão: PASS

A SPEC é proporcional ao problema comprovado. Ela fecha as duas perdas que
chegaram aos mocks: planejamento que apenas mapeia cobertura e lineage que
declara um hash mas não preserva a estrutura copiada. A solução mantém o
Markdown canônico como autoridade, insere o scaffold no `plan.md` existente,
deixa narrativa/forma/diagramas como decisão agêntica e reserva o hook para
integridade estrutural. Não impõe Pearson, SVG, score, quota visual nem HTML
gerado por código.

## Materiality assessment

**Materialidade: sistêmica e média.** A lacuna fica entre artefatos canônicos
e a superfície apresentada ao decisor. O guard atual confirma apenas o hash
de base declarado, oito tabs/panels ordenados, classes de famílias e ausência
de placeholders; ele não compara a casca do candidate com a do skeleton. Uma
mini-página pode, portanto, reter esses sinais e ainda descartar stylesheet,
shell e comportamento aprovados. Como esse contrato é reutilizável e a R3
mostrou a falha em mais de um candidate, o reparo não é específico a um mock.

O plano em `plan.md` também é material: ele é o handoff que determina o que a
composição precisa tornar inteligível antes de existir HTML. FR-027-01..03 e
o registro por rota/componente tornam explícitas tese, questão, arco,
fonte/relação, forma, slot, repetição, ausência/discovery e fechamento, sem
duplicar fatos em uma segunda fonte de verdade.

## Ausências e limites

- Não há candidate, fixture nova, hook alterado nem inspeção desktop nesta
  iniciativa; isso é corretamente trabalho futuro de T-002..T-004, não prova
  já disponível.
- Esta revisão não aprova implementação, não muda `tasks_ready` e não autoriza
  promoção/renderização.
- A revisão não exige identidade Pearson nem avalia se a identidade atual é a
  melhor. O limite vendor-neutral é explícito e compatível com o pedido.
- O hook proposto não pode provar storytelling, utilidade executiva ou
  qualidade visual. A revisão desktop distinta permanece necessária; seu
  resultado é qualitativo, não um score.
- A escolha concreta de fingerprint e o mecanismo de extensão autorizada
  continuam abertos de modo adequado para T-001/T-002, com fixtures positiva e
  negativa antes de qualquer promoção.

## Findings

| ID | Fonte → perda/risco | Decisão afetada | Correção / decisão desta revisão |
|---|---|---|---|
| F-027-01 | `validate_brief_candidate_inheritance.py` → o hash do skeleton, IDs, tabs e famílias de classe podem sobreviver enquanto a casca, o stylesheet-base e o comportamento são substituídos. | Se o candidate é realmente uma composição da experiência aprovada, ou uma mini-página paralela que apenas declara lineage. | **Coberto.** FR-027-04, FR-027-05 e FR-027-07, AC-027-03/04 e V-027-03/04 delimitam shell/slots/extensão e exigem fixture negativa para a página paralela. T-002 deve escolher fingerprint sem inspecionar conteúdo editorial. |
| F-027-02 | Diagnóstico R3 e pedido humano → mapa fonte→alvo pode existir sem decidir narrativa, relação, forma e ação; isso deixa o compositor improvisar ou omitir relações materiais. | Que decisão cada rota permite recuperar e como uma relação material será entendida sem reabrir os Markdown. | **Coberto.** FR-027-01..03 e AC-027-01/02 colocam o scaffold no `plan.md`, exigem revisão distinta `PASS`/`REVISE` antes do skeleton e aceitam N/A/discovery fonte-apoiado, sem quota. |
| F-027-03 | Risco de converter a correção em regra para M001–M003, em HTML autoral automático ou em uma segunda fonte de verdade. | Se o bundle continua aplicável a SPECs de software, operação, política e pesquisa sem esconder uma implementação prescritiva. | **Coberto.** FR-027-06, FR-027-10, não objetivos, T-003 e V-027-06 proíbem geração semântica, score e regra específica de fixture; o scaffold fica no `plan.md` e a regressão é heterogênea/não promovida. |
| F-027-04 | Hook verde pode coexistir com rota longa, navegação quebrada ou narrativa crua; e uma promoção posterior poderia divergir do candidate revisado. | Se a experiência desktop corresponde ao plano/fontes e se o arquivo promovido é o mesmo que recebeu revisão. | **Coberto.** FR-027-08/09, AC-027-05 e V-027-05 separam inspeção desktop da verificação estrutural; o plano preserva a atestação SHA-256 e a promoção exata já exigida pelo contrato de SPEC 025/renderer. |

Não há finding bloqueante ou correção canônica adicional requerida para
`Spec Ready`.

## Next action

O State Keeper pode registrar esta decisão como evidência de `Spec Ready`,
mantendo todas as tasks pendentes até autorização humana. Depois, executar
T-001 antes de T-002: o scaffold/revisor de plano precisa existir e ser
revisado antes de se definir os marcadores do skeleton e o fingerprint do hook.
T-003/T-004 devem então demonstrar o contrato em corpus heterogêneo, com
revisão desktop distinta e candidates não promovidos.
