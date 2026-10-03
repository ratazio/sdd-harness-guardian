# Tasks: 029-brief-content-model-and-doctrine-consolidation

**Status:** in_progress
**Spec:** ./spec.md
**Plan:** ./plan.md
**Validation plan:** ./validation-plan.md
**Last updated:** 2026-09-19

> T-001…T-005 e agora T-006/T-007 estão autorizadas a executar por **D-012**,
> sob a autoridade de D-007: enquanto o bootstrap não fecha em T-010, a
> autorização vem da decisão registrada, não de `tasks_ready`. T-008 exige
> aprovação humana adicional por ser destrutiva. Nenhuma task pode chegar a
> `done` sem evidência aprovada por identidade distinta.

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Schema do modelo de conteúdo, validado contra briefs existentes | none | high | unassigned | unassigned | evidence/T-001.md |
| T-002 | done | Projetor modelo → HTML com proveniência computada | T-001 | high | unassigned | unassigned | evidence/T-002.md |
| T-003 | done | Formas de apresentação enumeradas e seleção por perfil × domínio | T-002 | medium | unassigned | unassigned | evidence/T-003.md |
| T-004 | done | Contrato normativo único e disposição do Anexo A | none | high | unassigned | unassigned | evidence/T-004.md |
| T-005 | done | Eixo único de versão com mapeamento dos valores históricos | T-002 | medium | unassigned | unassigned | evidence/T-005.md |
| T-006 | done | Check de suficiência de fontes antes da composição | T-004 | low | unassigned | unassigned | evidence/T-006.md |
| T-007 | done | Cadeia de duas revisões com mandatos disjuntos | T-004 | medium | unassigned | unassigned | evidence/T-007.md |
| T-008 | done | Remoção das camadas substituídas (task destrutiva) | T-001…T-007 | high | unassigned | unassigned | evidence/T-008.md |
| T-009 | done | Instrumentação de custo e execução da matriz M-001…M-008 | T-008 | high | unassigned | unassigned | evidence/T-009.md |
| T-010 | done | Brief da própria 029 pela esteira nova e liberação dos gates | T-009 | high | unassigned | unassigned | evidence/T-010.md |

**T-001…T-007 estão todas `done`.** T-008 é a única task destrutiva —
único ponto que segue exigindo aprovação humana explícita antes de executar.

---

### T-001 — Schema do modelo de conteúdo

**Status:** done
**Objective:** definir o schema de `brief-model.yaml` derivado campo a campo da
§9.1 de `.harness/templates/plan.md`, e provar que ele representa os briefs já
produzidos.
**Requirement IDs:** FR-001, FR-005, FR-006
**Acceptance criteria IDs:** AC-001
**Outcome served:** O-001 (agente não escreve markup)
**Demonstrable increment:** schema versionado + relatório de representabilidade
sobre amostra de `testes/mock-runs/`.
**Expected artifact:** `schemas/brief-model.schema.*`, fixture de modelo válido
e de modelo inválido.
**Validation method:** V-001
**Why now:** resolve U-001, que é a incerteza que governa o tamanho de tudo o
que vem depois. Se o schema não representar a realidade, T-002 constrói sobre
base errada.
**Max subtasks before validation:** 3
**Dependencies:** none
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-001.md

#### Scope
Campos do modelo; perfil × domínio; enumeração de formas; bloco `prose` como
escape; round-trip contra briefs existentes.

#### Out of scope
Projeção, HTML, CSS, remoção de qualquer arquivo.

#### Outcome linkage
- FR-001/FR-005/FR-006; **bounded discovery** que resolve U-001.
- Fonte de prioridade: decisão humana do owner, 2026-09-19.

#### Expected files and contracts
`schemas/`, `scripts/test_brief_model_authoring.py`, fixtures novas.

#### Implementation constraints
Se um brief existente não for representável, **o schema está errado, não o
brief**. Não ajustar amostra para caber.

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| Schema não representa a realidade | Round-trip contra briefs reais; property-based é N/A porque o universo são 8 casos conhecidos, não espaço a explorar | Briefs de `testes/mock-runs/`; oracle é representabilidade, não igualdade de bytes | Builder | Evaluator distinto | evidence/T-001.md | Falha devolve à T-001 |

#### Validation IDs and commands
V-001 · `python -m pytest scripts/test_brief_model_authoring.py`

#### Exit criteria
- [x] schema versionado e documentado;
- [x] amostra de `testes/mock-runs/` representável, com relatório;
- [x] fixture positiva e negativa;
- [x] `validate_bundle.py` passa (315 checks);
- [x] evidence cobre AC-001 e U-001, com lacunas declaradas;
- [x] evaluator distinto decidiu `approve` em 2026-09-19.

**Risco residual aceito:** U-001 fica fechado apenas para domínio `software`.
Nenhum dos oito mocks exercita `ops`/`docs`/`policy`/`research` — é o risco
IR-003. Follow-up registrado em T-003, não reabre T-001.

**Task Ready:** n/a — concluída

---

### T-002 — Projetor modelo → HTML

**Status:** done
**Objective:** gerar o HTML final a partir do modelo, computando proveniência,
digests e fragmentos a partir da fonte canônica.
**Requirement IDs:** FR-002, FR-003
**Acceptance criteria IDs:** AC-002, AC-003
**Outcome served:** O-001, O-002
**Demonstrable increment:** `project_brief.py` produzindo HTML que passa nos
checks atuais, com todas as fixtures negativas ainda falhando.
**Expected artifact:** `scripts/project_brief.py`, `scripts/test_project_brief.py`.
**Validation method:** V-002, V-003, V-REG-001, V-REG-005
**Why now:** é o mecanismo central; sem ele nada do resto é verificável.
**Max subtasks before validation:** 3
**Dependencies:** T-001
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-002.md

#### Scope
Projeção de casca, rotas, abas, tabela de cobertura, tuplas de proveniência,
`data-source-digest`, `data-source-fragment` + SHA-256, no-script, print, foco.

#### Out of scope
Escolher forma visual, escrever narrativa, resumir Markdown (NG-001). Remover
qualquer arquivo (é T-008).

#### Implementation constraints
PD-003: o projetor lê fonte **apenas** para resolver locator, digest e
fragmento. Nenhuma síntese semântica em código.
PD-004: CSS/JS/a11y/print do shell atual preservados byte a byte quando possível.

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| IR-002 — perde garantia do pipeline antigo | Fixtures negativas existentes contra a esteira nova; é a prova mais barata e mais completa disponível | `scripts/fixtures/**` | Builder | Evaluator distinto | evidence/T-002.md | Fixture que pare de falhar **bloqueia** |

#### Validation IDs and commands
V-002, V-003, V-REG-001, V-REG-005 · `python -m pytest scripts/test_project_brief.py` e suíte de fixtures

#### Achado bloqueante da avaliação (2026-09-19)

`resolve_locator` (`scripts/project_brief.py:158-188`) aceita match parcial por
substring em qualquer direção sobre string normalizada. Reproduzido: com apenas
`## Fora de escopo` na fonte e `Escopo` declarado no modelo, o projetor resolve
**silenciosamente** para o heading de significado oposto, sem erro. Em blocos
`not_applicable`, o locator resolvido vira o `fragment` exibido — ou seja,
proveniência falsa passando na verificação, exatamente o que FR-003 e O-002
existem para impedir.

Correção exigida: match exato normalizado, recusando com erro acionável quando
não houver exato; ou guarda que recusa colisão entre candidatos distintos.
Mais teste cobrindo `Escopo`/`Fora de escopo` nos caminhos `represented` **e**
`not_applicable`.

#### Exit criteria
- [x] projeção passa nos checks de proveniência, lifecycle, no-script e print;
- [x] `resolve_locator` não resolve silenciosamente para heading distinto
      (corrigido após `request_revision`; verificado adversarialmente);
- [x] **toda** fixture negativa de `scripts/fixtures/**` continua falhando;
- [x] fragmento irresolvível recusa a projeção com mensagem acionável;
- [~] comparação de a11y com 013/014: **não existe instrumento** no repositório.
      Disposição explícita registrada na evidência; garantia indireta é a
      preservação byte-a-byte de CSS/JS, com teste provando. Lacuna de
      instrumentação, não de garantia — aceita pelo avaliador;
- [x] evaluator distinto decidiu `approve` em 2026-09-19.

**Task Ready:** n/a — concluída

---

### T-003 — Formas de apresentação e seleção por perfil

**Status:** done
**Objective:** implementar as formas enumeradas e a seleção de rotas por
perfil × domínio, incluindo relação material como nós/arestas.
**Requirement IDs:** FR-004, FR-005, FR-006
**Acceptance criteria IDs:** AC-004, AC-005
**Outcome served:** O-004 (mesma barra para compositor e revisor)
**Demonstrable increment:** SVG acessível gerado de nós/arestas; detecção de
zooms com topologia duplicada; brief `minimal`+`docs` com subconjunto de rotas.
**Expected artifact:** implementação das formas em `scripts/project_brief.py`;
`scripts/test_brief_forms.py`; fixture `minimal`+`docs`.
**Validation method:** V-004, V-005
**Why now:** resolve U-002 e é a mitigação direta de R-001 e IR-003.
**Max subtasks before validation:** 3
**Dependencies:** T-002
**Risk:** medium
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-003.md

#### Scope
`topology`, `sequence`, `matrix`, `footprint`, `risk-chain`, `dossier`, `prose`;
legenda de estados; equivalente textual; seleção de rotas.

**Fechamento de IR-003 (vindo da avaliação de T-001):** construir uma fixture
sintética de domínio **não-software** — `docs` ou `policy` — e validá-la com
`validate_brief_model.py`. Os oito mocks são todos `software`, então nenhum
fecha esse risco empiricamente. É exercício barato e é a única prova
disponível de que o schema não foi otimizado para código.

#### Out of scope
Redesenho visual (NG-003). Cota de cards ou diagramas (NG-002).

#### Outcome linkage
- FR-004/FR-005/FR-006; **entrega** a barra compartilhada entre compositor e revisor.
- Fonte de prioridade: D-001, D-004.

#### Implementation constraints
Calibrar pelo que os briefs existentes **de fato** usam, não por catálogo
especulativo. `prose` é escape sempre disponível (mitigação de R-002).

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| IR-003 — modelo rígido quebra fora de software | Fixture `minimal`+`docs` e inspeção qualitativa de M-006/M-007 | Briefs de `testes/mock-runs/`; `testes/mock-tests/06,07` | Builder | Evaluator distinto | evidence/T-003.md | Falha amplia a enumeração; **nunca** autoriza HTML paralelo |

#### Exit criteria
- [x] formas implementadas e cobertas por teste;
- [x] SVG com `role="img"`, `aria-label` e equivalente textual não vazio;
- [x] zooms com nós idênticos reportados (janela de falso-negativo conhecida e
      aceita quando só `label`/`state` da aresta mudam — registrada, não silenciosa);
- [x] `minimal`+`docs` sem exigir oito disposições `N/A`;
- [x] fixture sintética não-software válida, **reduzindo** IR-003. Não fechando:
      o inventário de fontes continua SDD-shaped (D-028/D-029);
- [x] contradição A-17 corrigida em BC-007, BC-013, **BC-009 e BC-016** — as duas
      últimas só na terceira rodada, e são a doutrina que o revisor executa;
- [x] evaluator distinto decidiu `approve` em 2026-09-19, após três rodadas.

**Task Ready:** n/a — concluída

---

### T-004 — Contrato normativo único e disposição do Anexo A

**Status:** done
**Objective:** criar `.harness/rules/brief-contract.md` como fonte normativa
única e dispor cada item do Anexo A.
**Requirement IDs:** FR-008, FR-009
**Acceptance criteria IDs:** AC-006, AC-007, AC-012
**Outcome served:** O-005, O-006
**Demonstrable increment:** doutrina obrigatória por papel medida; Anexo A com
disposição item a item; lista de invariantes comprovadamente preservada.
**Validation method:** V-006, V-007, V-012
**Expected artifact:** `.harness/rules/brief-contract.md` com regras `BC-NNN`;
reescrita dos consumidores para citação por ID;
`scripts/test_brief_contract_uniqueness.py`; relatório de medição de doutrina
por papel, com os papéis enumerados.
**Why now:** independente de T-001/T-002, e é metade do problema declarado
(§1.2 da spec). Pode correr em paralelo.
**Max subtasks before validation:** 3
**Dependencies:** none
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** approved — owner confirmou AC-012 em 2026-09-21 (D-031).
**Evidence:** evidence/T-004.md

#### Scope
Contrato único; reescrita de `human-visibility.md`, `stakeholder-brief-design.md`,
as 3 SKILLs de brief, `spec-review`, `sdd-lifecycle`, `AGENTS.md` e os 2
arquivos de agente para **referenciar** em vez de reenunciar; A-01 a A-16.
Declarar o **sinal detectável** de "texto normativo de brief" que a segunda
cláusula de AC-007 usa (modal normativo + vocabulário de brief, ou allowlist);
sem esse sinal, essa cláusula não é determinística.

#### Out of scope
Regras de SDD que não são do brief. Alterar qualquer invariante protegida.

#### Implementation constraints
Nenhuma invariante protegida pode desaparecer. Toda remoção registrada no
decision log. Se o contrato não couber em 15.000 chars, renegociar AC-009b
**com evidência**, nunca afrouxar por conveniência (Q-003).

#### Validation IDs and commands
V-006, V-007, V-012 · `python -m pytest scripts/test_brief_contract_uniqueness.py`

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| IR-001 — remove invariante sem perceber | Diff de lista + **leitura humana**; determinístico sozinho é insuficiente para julgar equivalência semântica de regra | `AGENTS.md` §Invariantes antes/depois | Builder | **Humano nomeado** | evidence/T-004.md | Falha reverte a remoção |

#### Exit criteria
- [x] `brief-contract.md` criado; consumidores referenciam;
- [x] A-01…A-16 com correção ou decisão registrada (A-13 permanece `deferred`
      por D-006, o que **é** disposição válida);
- [x] sinal detectável de AC-007 declarado;
- [x] check de reenunciação passa;
- [x] doutrina por papel medida contra AC-009b;
- [x] lista de invariantes idêntica ou ampliada, confirmada por humano nomeado;
- [x] evaluator distinto decidiu `approve`.

**Task Ready:** n/a — concluída

---

### T-005 — Eixo único de versão

**Status:** done
**Objective:** unificar `data-harness-brief-design`, `data-harness-brief-structure`
e `data-brief-shell-contract` em `data-brief-contract`, com mapeamento dos
valores históricos.
**Requirement IDs:** FR-010, FR-015
**Acceptance criteria IDs:** AC-011
**Outcome served:** O-005; resolve A-09
**Demonstrable increment:** eixo único declarado, com tabela de mapeamento dos
três eixos históricos, e brief pinned passando sem alteração de bytes.
**Expected artifact:** eixo em `.harness/templates/stakeholder-brief.html` e no
contrato normativo; tabela de mapeamento; `scripts/test_brief_contract_axis.py`.
**Validation method:** V-011, V-REG-003
**Why now:** resolve U-003; precisa estar estável antes de T-008 remover
camadas que leem os eixos antigos.
**Max subtasks before validation:** 3
**Dependencies:** T-002
**Risk:** medium
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-005.md

#### Scope
Unificar os três eixos em `data-brief-contract`; documentar o mapeamento dos
valores históricos; manter leitura version-aware.

**Reconciliação do vocabulário (D-027, vindo da avaliação):** `project_brief.py`
passa a emitir `data-brief-contract` e para de emitir o eixo legado;
`data-brief-contract-version` é renomeado para `data-brief-model-schema-version`.
T-005 detém o eixo, logo detém a reconciliação — o escopo de T-008 não a cobre e
o gap estava sem dono.

**Checagem por valor (D-030):** `data-brief-contract == "2"`, não mera presença,
em `render_stakeholder_brief.py::candidate_skeleton_inheritance_error` e em
`validate_brief_candidate_inheritance.py`.

#### Out of scope
Reescrever byte de brief histórico (NG-004).

#### Outcome linkage
- FR-010/FR-015; **entrega** a correção de A-09.
- Fonte de prioridade: D-001, D-004.

#### Assurance disposition
**A1 concisa:** teste sobre brief pinned existente + `validate_bundle.py`. Sem
tabela completa: o risco é contido e o oracle é igualdade de bytes.

#### Exit criteria
- [x] eixo único `data-brief-contract` definido, com tabela de mapeamento;
- [x] `project_brief.py` emite o eixo unificado; `data-brief-model-schema-version` renomeado (D-027);
- [x] checagem de estrutura por valor `== "2"`, não por presença (D-030);
- [x] briefs pinned `specs/004` e `specs/010` confirmados por SHA-256 inalterado;
- [x] `validate_bundle.py` passa (315 checks);
- [x] evaluator distinto decidiu `approve` em 2026-09-19, após um ciclo
      `request_revision` e uma auditoria da restauração manual do builder.

**Task Ready:** no

---

### T-006 — Check de suficiência de fontes

**Status:** pending
**Objective:** bloquear composição quando as fontes Markdown não sustentam um
brief útil.
**Requirement IDs:** FR-011
**Acceptance criteria IDs:** AC-008
**Outcome served:** O-004; move a garantia para antes da geração
**Demonstrable increment:** fixture com AC sem validação é bloqueada antes de
qualquer composição.
**Expected artifact:** `scripts/validate_source_sufficiency.py` e seu teste;
fixture positiva e negativa.
**Validation method:** V-008
**Why now:** é o ciclo mais caro do sistema atual (descobrir fonte pobre depois
do HTML). Barato e de alto retorno.
**Max subtasks before validation:** 3
**Dependencies:** T-004
**Risk:** low
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-006.md

#### Scope
AC com caminho de validação; risco material com owner; perfil de arquitetura
declarado; task com exit criteria e destino de evidência.

#### Out of scope
Julgar qualidade de prosa. Score (NG-002).

#### Outcome linkage
- FR-011; **entrega** a antecipação da garantia para antes da geração.
- Fonte de prioridade: D-001, D-004.

#### Assurance disposition
**A1 concisa:** fixtures positiva e negativa; o check é estrutural e o oracle é
binário.

#### Exit criteria
- [x] check implementado e coberto por fixture positiva e negativa;
- [x] bloqueio ocorre **antes** da composição — verificado: nenhum código lê
      `brief-model.yaml` ou `stakeholder-brief.html`;
- [x] **1 ciclo `request_revision`**: falso-negativo em risco↔owner (qualquer
      travessão de prosa era aceito como nome); corrigido endurecendo o
      separador e a forma do nome, com fixture e teste dedicados;
- [x] correção verificada com 15 variações adversariais adicionais na
      segunda rodada; nenhuma quebra na direção perigosa;
- [x] evaluator distinto decidiu `approve` em 2026-09-21.

**Risco residual aceito:** palavra única de prosa capitalizada ainda pode
passar como nome; owners com `/` ou parênteses ficam super-bloqueados
(direção segura). Nenhuma fonte real do bundle exercita nenhum dos dois.

**Task Ready:** n/a — concluída

---

### T-007 — Cadeia de duas revisões com mandatos disjuntos

**Status:** done
**Objective:** redefinir, no contrato normativo, a cadeia de revisão do brief
como exatamente duas passagens com mandatos disjuntos.
**Requirement IDs:** FR-012
**Acceptance criteria IDs:** AC-014
**Outcome served:** O-005; reduz três revisões sobrepostas a duas
**Demonstrable increment:** contrato declarando as duas passagens; nenhum
artefato do bundle instruindo uma terceira.
**Expected artifact:** seção de revisão em `.harness/rules/brief-contract.md`;
`scripts/test_review_chain_contract.py`.
**Validation method:** V-014
**Why now:** é mudança de **doutrina**, não de código. Pertence junto de T-004;
enterrá-la na task destrutiva foi o achado B-7 da revisão independente.
**Max subtasks before validation:** 3
**Dependencies:** T-004
**Risk:** medium
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** not_required
**Evidence:** evidence/T-007.md

#### Scope
Revisão (a) do modelo, antes da projeção, fundindo cobertura e construção;
revisão (b) do HTML servido em loopback, julgando apenas significado e
experiência. Mandatos declarados como disjuntos.

#### Out of scope
Remover arquivo (é T-008). Remover a revisão qualitativa independente (NG-007).

#### Outcome linkage
- FR-012; **entrega** diretamente parte do objetivo de consolidação.
- Fonte de prioridade: D-001, D-004.

#### Expected files and contracts
`.harness/rules/brief-contract.md`, `.harness/workflows/sdd-lifecycle.md`,
SKILLs de brief, `scripts/test_review_chain_contract.py`.

#### Implementation constraints
Duas passagens, não uma. NG-007 proíbe remover a revisão qualitativa
independente; o que muda é **o que ela lê**, não se ela existe.

#### Assurance disposition
**A1 concisa:** check de contrato + fixture. O oráculo é a contagem de
passagens declaradas e a disjunção de mandatos, ambos binários.

#### Validation IDs and commands
V-014 · `python -m pytest scripts/test_review_chain_contract.py`

#### Exit criteria
- [x] duas passagens declaradas com mandatos disjuntos (BC-009, já corretas em T-004);
- [x] nenhum artefato do bundle instrui uma terceira — **achado real**: `.harness/agents/spec-guardian.md`
      ainda instruía o Spec Guardian a executar as duas passagens, contradizendo
      `executive-brief-reviewer.md`. Corrigido: linguagem de execução virou
      linguagem de confirmação, citando BC-009/BC-010;
- [x] revisão qualitativa independente preservada (NG-007) — verificado pelo avaliador;
- [x] detector testado ativamente contra as duas formas de quebra (BC-009
      permissivo; papel reassumindo execução), reproduzido pelo avaliador
      em worktree isolado, não só alegado pelo builder;
- [x] `validate_bundle.py` passa (315 checks);
- [x] evaluator distinto decidiu `approve` em 2026-09-21.

**Risco residual aceito:** detector léxico raso, vulnerável a falso-positivo
em texto histórico futuro. Baixo impacto, registrado na evidência.

**Task Ready:** n/a — concluída

---

### T-008 — Remoção das camadas substituídas

**Status:** done
**Objective:** remover o que perdeu função, com saldo líquido de remoção
comprovado.
**Requirement IDs:** FR-007
**Acceptance criteria IDs:** AC-013
**Outcome served:** R-006 — a iniciativa é subtrativa por contrato
**Demonstrable increment:** dois scripts, seus testes e a §9.1 removidos;
nenhuma referência pendente; saldo de linhas negativo.
**Expected artifact:** remoção de `validate_brief_candidate_inheritance.py`,
`instantiate_brief_skeleton.py`, seus testes e da §9.1 de `plan.md`; redução de
`render_stakeholder_brief.py`; `scripts/test_no_dangling_references.py`.
**Validation method:** V-013, V-REG-004
**Why now:** é a única task destrutiva e só é segura depois que T-001…T-007
provaram a substituição (PD-007).
**Max subtasks before validation:** 3
**Dependencies:** T-001, T-002, T-003, T-004, T-005, T-006, T-007
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** approved — owner autorizou em 2026-09-21 (D-032).
**Evidence:** evidence/T-008.md

#### Scope
Remoção dos dois scripts e seus testes; remoção da §9.1 de `plan.md`; redução
de `render_stakeholder_brief.py` a promoção + projeção; check de referência
pendente.

**Absorção da doutrina residual (vindo da avaliação de T-004):** dissolver
`.harness/rules/human-visibility.md` (4.656 chars) e
`.harness/templates/stakeholder-brief-design.md` (8.279) no contrato normativo,
deixando no máximo um ponteiro. Hoje os dois sobrevivem magros mas ainda
obrigatórios, o que fez o corpus **por papel** subir mesmo com os seis arquivos
da baseline caindo 42%. Sem esta absorção, a iniciativa é aditiva na dimensão
que mais importa — que é o que R-006/IR-006 proíbem.

**Remedir AC-009b depois da absorção** e só então levar a renegociação ao owner
(D-025). O piso previsível é contrato + skill do papel: 18.917 a 23.766.

#### Out of scope
Remover qualquer coisa em consumidor. Reescrever brief histórico (NG-004).
Alterar invariante protegida (NG-005).

#### Outcome linkage
- FR-007; **entrega** o saldo de remoção que R-006 exige.
- Fonte de prioridade: D-001, D-004.

#### Implementation constraints
Reversível por `git revert`. Só ocorre após T-001…T-007 aprovadas.
**Um diff final com saldo positivo de linhas em `.harness/` e `scripts/`
reprova este incremento.**

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| Remoção deixa referência pendente | Check de referência sobre todo o bundle; grep manual não cobre 7.000 arquivos com segurança | `.harness/`, `scripts/`, `docs/` | Builder | Evaluator distinto | evidence/T-008.md | Referência pendente bloqueia |
| IR-006 — iniciativa vira aditiva | `git diff --stat` como **critério de aceite**, não observação | `.harness/` e `scripts/` | Builder | Evaluator distinto | evidence/T-008.md | Saldo positivo replaneja o slice |

#### Validation IDs and commands
V-013, V-REG-004 · `python -m pytest scripts/ -q`, `git diff --stat`

#### Exit criteria
- [ ] os dois scripts, seus testes e a §9.1 não existem mais;
- [ ] `human-visibility.md` e `stakeholder-brief-design.md` absorvidos no contrato;
- [ ] AC-009b remedido após a absorção, com número final para decisão do owner;
- [ ] nenhum artefato do bundle os referencia;
- [ ] saldo líquido de remoção comprovado por `git diff --stat`;
- [ ] `validate_bundle.py` passa;
- [ ] aprovação humana registrada;
- [ ] evaluator distinto decidiu `approve`.

**Task Ready:** n/a — concluída

---

### T-009 — Instrumentação de custo e matriz M-001…M-008

**Status:** done
**Objective:** medir o custo da esteira nova, executar os oito mocks e obter
revisão independente da matriz.
**Requirement IDs:** FR-013, FR-014
**Acceptance criteria IDs:** AC-009a, AC-009b, AC-009c, AC-009d, AC-010
**Outcome served:** O-003, O-007
**Demonstrable increment:** matriz nova com custo medido e convergência
comparada ao histórico (6, 9 e 15 execuções).
**Expected artifact:** nova execução em `testes/mock-runs/`; evidência de custo
por etapa.
**Validation method:** V-009, V-010, V-REG-002
**Why now:** é a verificação final; precisa da esteira já enxuta para que a
medição valha alguma coisa.
**Max subtasks before validation:** 3
**Dependencies:** T-008
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** **pending** — a revisão qualitativa de M-006 e M-007 exige
humano nomeado.
**Evidence:** evidence/T-009.md

#### Scope
Instrumentação de custo por etapa; execução de M-001…M-008; resolução de um
`REVISE` editando só o modelo.

#### Out of scope
Remover arquivo (é T-008). O brief da própria 029 e a liberação dos gates
(é T-010). Mobile e breakpoints (NG-003).

#### Outcome linkage
- FR-013/FR-014; **entrega** a prova do outcome.
- Fonte de prioridade: D-001, D-004, D-009.

#### Implementation constraints
A medição só vale sobre a esteira já enxuta; por isso T-009 depende de T-008.

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| IR-003 — quebra em domínio não-software | Execução real + revisão qualitativa em loopback | `testes/mock-tests/06,07`; referência de M-005 | Builder | Evaluator distinto + **humano nomeado** | evidence/T-009.md | Amplia enumeração; nunca autoriza HTML paralelo |
| IR-004 — HTML à mão reaparece | Byte-reprodutibilidade a partir do modelo | `brief-model.yaml` + `project_brief.py` | Builder | Evaluator distinto | evidence/T-009.md | Não reproduzível bloqueia promoção |

#### Validation IDs and commands
V-009, V-010, V-REG-002 · `python scripts/project_brief.py <initiative>`,
`python -m http.server 4173 --bind 127.0.0.1`

#### Exit criteria
- [x] M-001…M-008 executados; convergência em ~1 tentativa por mock, contra
      6/9/15 do histórico (unidades não diretamente comparáveis, registrado
      com honestidade — sem percentual inventado, D-009);
- [x] custo medido por etapa (tempo real; tokens declarados não medidos, sem
      fingir zero);
- [x] byte-reprodutibilidade confirmada em 4 mocks por duas identidades
      independentes;
- [x] `REVISE` resolvido editando só o modelo (`PROJECTION REFUSED` → 1 edição
      → limpo);
- [x] achado corroborado em uso real: `resolve_locator` recusou ambiguidade
      genuína de "T-002" em M-006 (duas headings na fonte) — a guarda de T-002
      funciona fora de fixture sintética;
- [x] evaluator distinto decidiu `approve` técnico em 2026-09-21;
- [x] **aprovação qualitativa nomeada de M-006/M-007: owner, 2026-09-21
      (D-034)**. M-007 `prose` aceito; M-006 lacuna de fonte genérica aceita
      porque está visível no brief, não escondida — já confirmado no HTML
      projetado (M-006.html:811).

**AC-009b permanece não atingido**, sem afrouxamento silencioso: renegociação
segue adiada por D-025.

**Task Ready:** n/a — concluída

---

### T-010 — Brief da própria 029 e liberação dos gates

**Status:** pending
**Objective:** projetar o brief da SPEC 029 pela esteira nova, obter revisão
independente e resolver os gates suspensos por D-007/D-011/D-012.
**Requirement IDs:** FR-001, FR-002, FR-012
**Acceptance criteria IDs:** AC-009a
**Outcome served:** O-001, O-002 — a 029 é a primeira prova do modelo
**Demonstrable increment:** `stakeholder-brief.html` da 029, projetado e
byte-reproduzível, com `human_visibility_ready`, `brief_coverage_ready` e
`tasks_ready` resolvidos pela primeira vez sob o contrato novo.
**Expected artifact:** `brief-model.yaml` e `stakeholder-brief.html` da 029;
registro de revisão em `evidence/T-010.md`.
**Validation method:** V-009, M-01
**Why now:** é o fechamento do bootstrap. Separada de T-009 porque é governada
por gate próprio e aprovação humana, e não é entregável junto com a medição
(achado de atomicidade da rodada 2).
**Max subtasks before validation:** 3
**Dependencies:** T-009
**Risk:** high
**Builder:** unassigned · **Evaluator:** unassigned
**Human approval:** **pending** — resolve gates suspensos.
**Evidence:** evidence/T-010.md

#### Scope
Modelo da 029; projeção; revisão independente em loopback; transição dos três
gates suspensos.

#### Out of scope
Qualquer brief que não seja o da 029. Reabrir decisão de escopo.

#### Outcome linkage
- FR-001/FR-002/FR-012; **entrega** a prova do bootstrap.
- Fonte de prioridade: D-007, D-011, D-012.

#### Implementation constraints
O brief é gerado pela esteira **nova** (D-007). Os gates foram **deslocados**,
nunca removidos (D-011, D-012): só vão a `true` com o brief projetado e
revisado por identidade distinta. A exceção expira com esta SPEC.

#### Assurance disposition
| Claim/risk | Técnica e porquê | Oracle/dados | Executor | Avaliador | Evidência | Saída/falha |
|---|---|---|---|---|---|---|
| O bootstrap não fecha e a 029 fica sem brief | Projeção + revisão independente em loopback | `brief-model.yaml` da 029; HTTP 127.0.0.1 | Builder | Evaluator distinto + humano nomeado | evidence/T-010.md | Falha devolve ao modelo, nunca ao HTML |

#### Validation IDs and commands
V-009, M-01 · `python scripts/project_brief.py specs/029-...`,
`python -m http.server 4173 --bind 127.0.0.1`

#### Exit criteria
- [x] brief da 029 projetado e byte-reproduzível (3 tentativas; SHA-256
      idêntico em 3 gerações independentes, 69.993 bytes);
- [x] revisão independente `approve` com achados registrados em 2026-09-21:
      bug real de escape HTML em `_verify_fragment_visible` (fragmento com
      `<`/`>` nunca bate com sua versão escapada — falha segura, não
      corrigido aqui, escopo de T-002); lacuna de cobertura de fixture entre
      `decision-log.md` real (tabela plana) e o formato com headings usado
      nos testes de T-001/T-002;
- [x] **autoprova de honestidade passou**: o brief narra sem suavizar a
      colisão de locator (T-002), o achado no Spec Guardian (T-007), os dois
      números conflitantes de D-033, e declara os três gates como `false`;
      nenhuma das 11 ocorrências de "aprovado" no HTML é autoaprovação;
- [ ] `human_visibility_ready`, `brief_coverage_ready` e `tasks_ready` —
      **decisão final do owner, pendente**;
- [ ] aprovação humana registrada — pendente.

**Task Ready:** no

---

## Readiness decision

**Tasks Ready:** no
**Reviewed by:**
**Blocking conditions:** `spec_ready`, `plan_ready` e `validation_ready` ainda
falsos; builder e evaluator não atribuídos; T-004, T-008, T-009 e T-010 exigem
aprovação ou avaliador humano nomeado.

`brief_coverage_ready` e `tasks_ready` permanecem `false` e são resolvidos em
T-010, junto com `human_visibility_ready`. Até lá, a autorização de execução
vem de **D-012**, sob a autoridade de D-007 — não de `tasks_ready`.
