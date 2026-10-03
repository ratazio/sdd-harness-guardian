# Validation Plan: 029-brief-content-model-and-doctrine-consolidation

**Status:** validation_ready
**Spec:** ./spec.md
**Plan:** ./plan.md
**Owner:** Guardian maintainers + responsável pela experiência do brief
**Last updated:** 2026-09-19

## 1. Strategy

Três níveis, com fronteira explícita entre eles porque a confusão entre os dois
primeiros e o terceiro é um defeito recorrente deste repositório:

1. **Determinístico** — pytest sobre fixtures. Prova estrutura, proveniência,
   lifecycle e preservação de invariantes. **Nunca** prova qualidade.
2. **Comparativo estático** — medições sobre artefatos já versionados em
   `testes/` e `specs/`. Custo zero, nenhuma reexecução da esteira antiga
   (D-009).
3. **Qualitativo independente** — revisão humana/agêntica por identidade
   distinta, sobre HTML servido em loopback. É a única coisa que julga se o
   brief serve para decidir.

Um PASS determinístico não pode ser reportado como aprovação de experiência.

### Assurance selection

| Profile/task | Risk or claim | Technique selected/inapplicable rationale | Oracle and evidence | Executor | Evaluator | Failure/waiver behavior |
|---|---|---|---|---|---|---|
| A2 / T-001 schema | Schema não representa a realidade dos briefs existentes | Round-trip contra briefs de `testes/mock-runs/`. Property-based rejeitado: o universo de entrada são oito casos reais conhecidos, não um espaço a explorar | Todo brief amostrado é representável; oracle é a representabilidade, não a igualdade de bytes | Builder | Evaluator distinto | Falha → schema volta a T-001; nunca ajustar o brief para caber no schema |
| A2 / T-002 projetor | Projetor perde garantia que o pipeline antigo dava | Fixtures negativas existentes de `scripts/fixtures/**` rodadas contra a esteira nova | Toda fixture negativa continua falhando | Builder | Evaluator distinto | Qualquer fixture que pare de falhar bloqueia; restaurar o check equivalente |
| A2 / T-004 doutrina | Consolidação remove invariante protegida | Diff de lista de invariantes antes/depois + revisão humana | Conjunto de invariantes semanticamente preservado; igualdade textual não exigida | Builder | **Humano nomeado** — IR-001 é crítico e não tem controle puramente determinístico | Falha → reverter remoção e registrar no decision log |
| A2 / T-009 matriz | Modelo rígido quebra em domínio não-software | Execução real de M-001…M-008 + revisão qualitativa | M-006 e M-007 sem detalhe técnico inventado | Builder | Evaluator distinto + humano nomeado | Falha → ampliar enumeração de formas; **nunca** autorizar HTML paralelo |
| A1 / T-005 versão | Eixo único quebra brief histórico | Teste sobre brief pinned existente | Bytes inalterados | Builder | Evaluator distinto | Falha → manter leitura version-aware dos valores antigos |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | determinístico | `python -m pytest scripts/test_brief_model_authoring.py` + inspeção de diff da iniciativa fixture | O único artefato editorial autorado é `brief-model.yaml`; nenhum HTML de brief é autorado | evidence/T-001.md | Builder |
| V-002 | AC-002 | determinístico | `python -m pytest scripts/test_project_brief.py` e todas as fixtures negativas de `scripts/fixtures/**` | Projeção passa nos checks atuais; **toda** fixture negativa continua falhando | evidence/T-002.md | Builder |
| V-003 | AC-003 | determinístico | fixture com `fragment` ausente na fonte | Projeção recusada; mensagem nomeia bloco, fonte e fragmento | evidence/T-002.md | Builder |
| V-004 | AC-004 | determinístico | fixture com relação material + fixture com dois zooms de nós idênticos | SVG com `role="img"`, `aria-label` e equivalente textual não vazio; zooms duplicados reportados | evidence/T-003.md | Builder |
| V-005 | AC-005 | determinístico + qualitativo | `profile: minimal` + `domain: docs` sobre M-007 | Subconjunto de rotas; nenhuma disposição `N/A` exigida para rota não selecionada | evidence/T-003.md | Builder + revisor distinto |
| V-006 | AC-006 | determinístico | check que enumera os itens do Anexo A contra `decision-log.md` | Todo item com correção aplicada ou decisão registrada; falha se algum ficar sem disposição | evidence/T-004.md | Builder |
| V-007 | AC-007 | determinístico, **condicionado** à declaração do sinal detectável em T-004 | check de unicidade de `BC-NNN` e de citação por ID em skills/agents/workflows | Cada `BC-NNN` definido em exatamente um arquivo; nenhum consumidor com texto normativo de brief fora de citação por ID | evidence/T-004.md | Builder |
| V-008 | AC-008 | determinístico | fixture com AC sem caminho de validação | Bloqueio **antes** de qualquer composição | evidence/T-006.md | Builder |
| V-009 | AC-009a, AC-009b | determinístico + comparativo | reprojetar cada brief a partir do seu `brief-model.yaml` e comparar bytes; contar chars de doutrina por papel, com os papéis enumerados | Todo brief byte-reproduzível, incluindo o da própria 029; doutrina ≤ 15.000 chars por papel | AC-009a: `evidence/T-009.md` e `evidence/T-010.md`. AC-009b: medição inicial em `evidence/T-004.md`, confirmação final autoritativa em `evidence/T-009.md` | Builder |
| V-010 | AC-009c, AC-009d, AC-010 | comparativo + medição | executar M-001…M-008; contar execuções até PASS + `APPROVE`; instrumentar custo por etapa; resolver um `REVISE` editando só o modelo | ≤2 execuções contra 6/9/15 do histórico; custo registrado em absoluto; `REVISE` resolvido sem reautorar HTML; `APPROVE` com achados registrados | evidence/T-009.md | Builder + revisor distinto |
| V-011 | AC-011 | determinístico | checks atuais sobre um brief histórico pinned | Bytes inalterados; checks passam | evidence/T-005.md | Builder |
| V-012 | AC-012 | determinístico + **humano nomeado** | diff das invariantes de `AGENTS.md` antes/depois + leitura humana | Conjunto semanticamente preservado; igualdade textual não exigida (a invariante de brief vira citação por ID) | evidence/T-004.md | Builder + humano nomeado |
| V-013 | AC-013 | determinístico | check de referência pendente após a remoção | Os dois scripts, seus testes e a §9.1 não existem; nenhum artefato os referencia | evidence/T-008.md | Builder |
| V-014 | AC-014 | determinístico | check de contrato da cadeia de revisão | Exatamente duas passagens com mandatos disjuntos; nenhum artefato instrui uma terceira | evidence/T-007.md | Builder |

Todos os ACs da spec (AC-001…AC-014, incluindo AC-009a/b/c/d) estão mapeados.

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | IR-002 — projetor perde garantia | Todas as fixtures negativas de `scripts/fixtures/**` contra a esteira nova | Todas continuam falhando | evidence/T-002.md |
| V-REG-002 | IR-004 — HTML autorado à mão reaparece | Byte-reprodutibilidade de todo brief a partir do seu modelo | Todo brief reproduzível, incluindo o da própria 029; qualquer não reproduzível reprova | evidence/T-009.md e evidence/T-010.md |
| V-REG-003 | IR-005 — eixo único quebra histórico | `python scripts/validate_bundle.py` + checks sobre `specs/0*/stakeholder-brief.html` | Passam sem alteração de bytes | evidence/T-005.md |
| V-REG-004 | IR-006 — a iniciativa vira aditiva | `git diff --stat` em `.harness/` e `scripts/` | **Redefinido por D-033:** sinal de alerta para revisão humana, não gate binário. O critério real de sucesso é convergência/custo por composição (V-010, AC-009c/AC-009d). Saldo cumulativo desta iniciativa: +3.826 linhas, aceito pelo owner como investimento único válido | evidence/T-008.md |
| V-REG-005 | NG-003 — regressão de acessibilidade | Comparar HTML projetado com a evidência aprovada de 013/014 | Foco visível, ordem sem script, print e reduced-motion preservados | evidence/T-002.md |
| V-REG-006 | Regressão geral do bundle | `python scripts/validate_bundle.py` | Nenhum check regride para falha. Toda redução na contagem é explicada por remoção registrada; o número absoluto **vai** cair com T-008 e isso não é regressão | evidence de cada task |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | raiz do bundle | exit 0 | todas |
| `python -m pytest scripts/ -q` | raiz do bundle | exit 0 | todas |
| `python scripts/project_brief.py <initiative>` | raiz do bundle | exit 0 e HTML projetado | T-002…T-010 |
| `python -m http.server 4173 --bind 127.0.0.1` | raiz do consumidor | serve loopback para revisão renderizada | T-009, T-010 |
| `git diff --stat` | raiz do bundle | saldo líquido de remoção | T-008 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-01 | Abrir cada rota selecionada de cada mock, e do brief da própria 029, em `http://127.0.0.1:4173/...` | Decisão recuperável sem abrir Markdown | evidence/T-009.md e evidence/T-010.md |
| M-02 | Ler M-006 e M-007 procurando detalhe técnico inventado | Nenhuma API, componente ou teste fabricado | evidence/T-009.md |
| M-03 | Comparar com `testes/visual-reference-runs/20260831-m005-executive-reference` | Sem regressão visual material | evidence/T-009.md |
| M-04 | Leitura humana do conjunto de invariantes antes/depois | Nenhuma invariante protegida perdida em substância | evidence/T-004.md |

## 6. Evals

`not_applicable`. Toda alegação de qualidade desta iniciativa é julgamento
independente registrado com locator e razão, não rubrica pontuada. NG-002
proíbe score, e um eval numérico seria exatamente o que a spec veta.

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Medição instrumentada da esteira **antiga** | Reexecutar a esteira antiga custaria o que a SPEC existe para eliminar (D-009). A linha de base é derivada de artefatos já versionados | Nenhum percentual de redução é reivindicado contra número não medido; AC-009a/b/c comparam grandezas verificáveis e AC-009d mede o lado novo em absoluto. Risco aceito e declarado em R-005 | Decisão humana do owner, 2026-09-19 |
| Responsividade mobile e breakpoints | Fora de escopo por NG-003 | A avaliação solicitada é desktop; o shell atual já carrega sua evidência de 013 | Guardian maintainers |
| Migração de briefs históricos | Fora de escopo por NG-004 | Briefs pinned permanecem sob seu contrato registrado; V-011 prova que continuam válidos | Guardian maintainers |

## Stakeholder brief projection

`not_applicable` por D-007. O brief desta iniciativa é gerado pela esteira nova
em T-010 e é a primeira prova do modelo. O escopo estrito da dispensa está em
D-008. D-011 delimita que a dispensa é de **ordenação** do gate
`human_visibility_ready`, nunca de sua existência, e D-012 estende a mesma
suspensão de ordenação a `brief_coverage_ready` e à dependência de brief em
`tasks_ready`. Os três são resolvidos em T-010.

## 8. Validation decision

**Validation Ready:** yes
**All ACs mapped:** yes — AC-001…AC-014 cobertos por V-001…V-014
**Reviewer:** revisor independente de Plan/Validation Ready, 2026-09-19 (identidade distinta do autor; dois vereditos separados numa passagem, porque a regra exige identidade distinta do autor, não uma identidade por gate)
**Blocking gaps:** nenhum. Dois achados não bloqueantes aplicados: rótulo condicional de V-007 e desambiguação de evidência de AC-009b.
