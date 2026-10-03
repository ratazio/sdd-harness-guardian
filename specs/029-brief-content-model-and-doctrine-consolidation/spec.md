# SPEC 029 — Modelo de conteúdo do brief e consolidação da doutrina

**Status:** spec_ready
**Sequência:** 029
**Slug:** brief-content-model-and-doctrine-consolidation
**Tipo:** refactor
**Owner:** Guardian maintainers + responsável pela experiência do brief
**Criada em:** 2026-09-19
**Última atualização:** 2026-09-19
**Risco:** high
**Assurance profile:** A2-elevated

## 1. Problema

O bundle acumulou, entre 0.1.2 e 0.4.0, oito ciclos de correção sobre a mesma
esteira de stakeholder brief. O resultado tem dois defeitos estruturais
distintos, e nenhum deles é falta de regra.

### 1.1 O agente autora HTML, e por isso o custo é desproporcional

Medições sobre este repositório:

| Item | Medida |
|---|---|
| Doutrina `.harness/**/*.md` | 35.338 palavras |
| Subconjunto obrigatório para compor um brief | 61.786 chars, relido por **cada** agente da cadeia |
| Skeleton v3 `.harness/templates/stakeholder-brief.html` | 50 KB (18 KB CSS + 3,5 KB JS + 28 KB markup), 27 slots |
| Briefs produzidos | 45–84 KB; `specs/023/stakeholder-brief.html` tem 79 KB de markup para 3 KB de CSS |
| Pipeline de brief em Python | 4.752 linhas de renderer/validators + 4.989 linhas de teste |

A cadeia atual executa no mínimo três passagens de contexto completo sobre o
mesmo material (compositor, revisor de construção, revisor renderizado), cada
uma carregando doutrina + fontes canônicas, multiplicadas pelos ciclos
`REVISE`. A maior parte dos bytes que o agente emite — wrappers, classes,
atributos estruturais, repetição de casca — não carrega nenhuma decisão.

O ponto crítico é que **o modelo de conteúdo já existe**: a seção 9.1 de
`.harness/templates/plan.md` ("Brief construction record") já obriga o autor a
registrar, por rota e por componente repetido, a pergunta executiva, o arco
narrativo, os fatos e relações a recuperar, a forma visual escolhida e sua
razão, os campos de repetição, a ausência/discovery, o alvo renderizado e a
ação de fechamento. Esse registro é revisado e aprovado — e então **descartado**:
o agente reescreve tudo em HTML à mão, de memória. É exatamente aí que nasce a
divergência entre o `.md` e o HTML, e é aí que o token é queimado.

### 1.2 A doutrina se contradiz, e o agente decide sem referência comum

A mesma regra é reenunciada em `human-visibility.md`, em
`stakeholder-brief-design.md`, em três SKILLs, em `spec-review`, no
`sdd-lifecycle` e nos arquivos de agente. Onde há reenunciação há divergência.
As contradições verificadas estão no anexo A. As mais graves:

- o mesmo documento declara o shell "vendor-neutral by default" e, 200 linhas
  depois, manda "keep Pearson navy/lavender/white as the canonical base";
- a SKILL de composição manda emitir a rota `architecture.global`; o validator
  e os testes exigem `architecture`; um terceiro script usa um conjunto de oito
  rotas completamente diferente;
- o agente `brief-experience-composer` deve entregar um "Editorial map"; a SKILL
  que ele é obrigado a usar proíbe "producing a sidecar map";
- `AGENTS.md`, que é o arquivo de bootstrap lido por todo agente, descreve um
  fluxo de 17 passos que **omite a etapa de skeleton** presente no
  `sdd-lifecycle`;
- `human-visibility.md` enumera sete visões; todo o resto do sistema exige oito.

O efeito combinado é o sintoma relatado: o mesmo pipeline produz ora um brief
denso, ora um brief pobre, porque compositor e revisor não compartilham uma
barra — cada um a reconstrói a partir de prosa normativa ambígua ("isto não é
cota", "isto não é score", "use julgamento"), e cada divergência custa um ciclo
`REVISE` inteiro.

## 2. Objetivo

Fazer com que o agente autore **decisão editorial**, não HTML, e que a doutrina
que o instrui seja **uma única fonte normativa não contraditória** — reduzindo
o custo por brief segundo os indicadores verificáveis de AC-009a/b/c, sem
reivindicar percentual contra linha de base não medida (R-005, D-009), sem
reduzir nenhuma invariante protegida e sem introduzir geração determinística de
conteúdo.

## 3. Resultado de entrega

- **Resultado para usuário:** um brief de qualidade previsível e visualmente
  consistente por um custo que não inviabiliza o uso do harness; e um bundle em
  que um agente não recebe duas instruções conflitantes para a mesma ação.
- **Incremento demonstrável:** a matriz M001–M008 recomposta sob o novo modelo,
  com custo medido por brief comparado à linha de base atual, e um relatório de
  consolidação mostrando cada contradição do anexo A resolvida.
- **Limite da entrega (MVP/slice):** o modelo de conteúdo, o projetor
  determinístico, o contrato normativo único e a limpeza das contradições
  verificadas. **Não** inclui redesenho visual do shell, nem mobile, nem
  reescrita retroativa de briefs históricos.
- **Fonte de prioridade:** decisão humana registrada em `decision-log.md`
  D-001, D-004 e D-009 (custo insustentável + variância de qualidade).

## 4. Atores

| Ator | Necessidade |
|---|---|
| Agente compositor | Registrar tese, rotas, fatos, relações e forma escolhida uma única vez, em um artefato pequeno. |
| Revisor independente | Julgar decisão editorial sem precisar ler 60 KB de markup nem reconciliar doutrina divergente. |
| Maintainer do harness | Ter uma fonte normativa única e verificável; alterar uma regra em um lugar só. |
| Stakeholder | Abrir um HTML consistente, legível e verdadeiro, com a mesma barra em toda iniciativa. |
| Operador/pagador | Custo por brief previsível e medido. |

## 5. Resultados observáveis

- **O-001:** o agente não escreve markup de brief. Ele autora um modelo de
  conteúdo; layout, CSS, abas, atributos de proveniência, digests, fragmentos,
  tabela de cobertura, fallback sem script, print e acessibilidade são
  projetados deterministicamente.
- **O-002:** a divergência `.md` ↔ HTML deixa de ser possível nas partes
  projetadas: locator, digest e fragmento são computados a partir da fonte, não
  digitados.
- **O-003:** um achado `REVISE` custa editar um nó do modelo, não reautorar a
  página.
- **O-004:** compositor e revisor operam sob a mesma barra declarada
  (perfil + rotas selecionadas), o que torna a qualidade reprodutível em vez de
  dependente do agente que calhou de executar.
- **O-005:** toda regra material do brief existe em exatamente um lugar
  normativo; skills, agentes e workflows referenciam, não reenunciam.
- **O-006:** cada contradição listada no anexo A está resolvida ou
  explicitamente declarada como decisão consciente no `decision-log.md`.
- **O-007:** o custo da esteira **nova** é medido por etapa e registrado como
  linha de base futura; a esteira antiga é caracterizada por proxies estáticos
  declarados (FR-013), sem reivindicação de percentual.

## 6. Não objetivos

- **NG-001:** gerar narrativa, escolher diagrama, resumir spec ou decidir
  materialidade por código. A autoria de conteúdo permanece agêntica. O
  projetor recebe conteúdo já decidido e apenas o posiciona.
- **NG-002:** introduzir score de qualidade, cota de cards, cota de diagramas ou
  contagem de palavras como gate.
- **NG-003:** redesenhar a identidade visual, tratar responsividade mobile ou
  trocar a paleta. O shell atual é insumo, não escopo.
- **NG-004:** reescrever, reprocessar ou invalidar briefs históricos já
  renderizados e revisados.
- **NG-005:** reduzir qualquer invariante protegida de `AGENTS.md` — identidades
  distintas, evidência antes de `done`, renderizar ≠ aprovar, HTML não é fonte.
- **NG-006:** transformar o usuário final em aprovador operacional de modelo,
  render ou remediação.
- **NG-007:** remover a revisão qualitativa independente. Ela permanece; o que
  muda é o que ela lê.
- **NG-008:** usar a exceção de bootstrap (D-007) como precedente. Ela suspende
  **apenas a ordenação** do gate `human_visibility_ready` para esta iniciativa,
  deslocando-o para a task que projeta o brief da própria 029 (D-011). D-012
  estende a mesma suspensão de ordenação a `brief_coverage_ready` e à
  dependência de brief em `tasks_ready`. Nenhum gate é removido, e a exceção
  expira com a SPEC 029. Identidades
  distintas, evidência aprovada antes de `done`, revisão independente,
  renderizar ≠ aprovar e HTML não é fonte permanecem integrais (D-008).

## 7. Requisitos funcionais

| ID | Requisito | Racional |
|---|---|---|
| FR-001 | O sistema deve definir um **modelo de conteúdo de brief** (`brief-model.yaml`) com schema versionado, que é o único artefato editorial que um agente autora para o brief. Cada bloco declara texto autoral, `source`, `source_section` e `coverage`. | Move o esforço do agente de markup para decisão. |
| FR-002 | Um projetor determinístico deve transformar o modelo no HTML final: casca, CSS, abas, ordem de origem sem script, print, foco, tabela de cobertura humana, tuplas de proveniência, `data-source-digest`, `data-source-fragment` e seu SHA-256. | Elimina 80% dos bytes autorados e torna a proveniência não falsificável. |
| FR-003 | O projetor deve recusar a projeção quando um `source`/`source_section` não resolve na fonte canônica, ou quando o `fragment` declarado não ocorre literalmente na fonte **e** no bloco visível. | Mantém o contrato de proveniência atual sem exigir que o agente o digite. |
| FR-004 | Relações materiais devem ser declaradas no modelo como lista de nós e arestas com rótulo, estado (`proposed`/`preserved`/`out-of-scope`/`discovery`) e origem; o projetor desenha o SVG acessível e seu equivalente textual. | O contrato `data-architecture-node/relation` já é um modelo de conteúdo disfarçado de HTML; extraí-lo remove autoria de SVG à mão e permite detectar topologias duplicadas por diff de conjuntos. |
| FR-005 | O modelo deve declarar `profile` (`minimal`/`standard`/`deep`) e `domain` (`software`/`ops`/`docs`/`policy`/`research`), e o par deve **selecionar quais rotas existem**. Uma rota não selecionada não precisa de disposição `N/A`. | Substitui 8 disposições + 8 justificativas por uma decisão antecipada, e dá ao revisor a mesma barra do compositor. |
| FR-006 | A forma de apresentação de cada bloco deve ser uma enumeração declarada pelo agente com razão (`topology`, `sequence`, `matrix`, `footprint`, `risk-chain`, `dossier`, `prose`), e o projetor deve ter implementação própria de cada uma. | Preserva variedade visual onde ela carrega significado, sem que o agente reimplemente CSS por iniciativa. |
| FR-007 | A seção 9.1 de `plan.md` deve ser substituída por referência ao modelo. O registro de construção e o modelo não podem coexistir como dois artefatos. | Hoje o mesmo conteúdo é escrito duas vezes, em prosa e em HTML. |
| FR-008 | Deve existir um **contrato normativo único** do brief. `human-visibility.md`, `stakeholder-brief-design.md`, as três SKILLs de brief, `spec-review` e `sdd-lifecycle` devem referenciá-lo; nenhum deles pode reenunciar uma regra material. | Custo de doutrina passa de O(agentes × doutrina) para O(1). |
| FR-009 | Cada contradição verificada no anexo A deve ter resolução registrada: correção aplicada, ou decisão consciente com razão no `decision-log.md`. Nenhuma pode ser deixada sem disposição. | É a limpeza do campo minado pedida. |
| FR-010 | O vocabulário de versão deve ser unificado em **um** eixo declarado. Os eixos concorrentes atuais (`data-harness-brief-design`, `data-harness-brief-structure`, `data-brief-shell-contract`) devem ser reduzidos a um contrato explícito, com mapeamento documentado para os valores históricos. | Hoje o mesmo arquivo diz v2, v3 e v1 simultaneamente; nenhum agente consegue reconciliar. |
| FR-011 | Deve existir um check determinístico barato sobre as **fontes Markdown**, executado antes da composição, verificando: todo AC com caminho de validação, todo risco material com owner, perfil de arquitetura declarado, toda task com exit criteria e destino de evidência. | A causa real de um brief pobre é uma fonte pobre; descobrir isso após o HTML é o ciclo mais caro do sistema. |
| FR-012 | A cadeia de revisão deve ter duas passagens: (a) revisão independente do **modelo**, antes da projeção, fundindo as atuais revisões de cobertura e de construção; (b) revisão independente do **HTML servido em loopback**, julgando apenas significado e experiência. A checagem de herança de skeleton deve ser removida. | Três revisões com mandatos sobrepostos viram duas com mandatos disjuntos; herança não pode quebrar se ninguém autora a casca. |
| FR-013 | A linha de base de custo deve ser **derivada estaticamente dos artefatos já versionados** em `testes/` e `specs/`, sem reexecutar a esteira antiga. Os indicadores são: (a) bytes de markup autorados por agente por brief; (b) bytes de doutrina obrigatória por papel; (c) número de execuções da matriz registradas até um resultado aceito. | Reexecutar a esteira antiga só para medir custaria exatamente o que se quer evitar. O histórico já está em disco, contado pelo **maior sufixo `-rN` registrado**, nunca pelo número de diretórios retidos: `spec021-t004` exigiu 15 execuções (`r1`…`r15`, com apenas 10 diretórios retidos), `spec025-t004` 9, `spec020-t004` 6. |
| FR-014 | A esteira nova deve registrar o custo real por etapa quando executada sobre os mesmos pedidos M-001…M-008 de `testes/mock-tests/`. Esse número é medido, não estimado, e passa a ser a linha de base futura. | Só o lado novo precisa de instrumentação; o lado antigo já deixou rastro suficiente. |
| FR-015 | Briefs históricos já renderizados permanecem válidos sob seu contrato registrado. Um refresh material segue o caminho de migração explícito. | Preserva NG-004 e o princípio version-aware já existente. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-001 | Para uma iniciativa fixture, o agente produz apenas `brief-model.yaml`; nenhum markup de brief aparece em diff autorado por agente. | V-001 |
| AC-002 | O projetor gera HTML que passa os checks de proveniência, lifecycle, a11y, no-script e print hoje exigidos, a partir de um modelo válido, sem edição manual. | V-002 |
| AC-003 | Um modelo cujo `fragment` não ocorre na fonte canônica é recusado pela projeção com mensagem acionável. | V-003 |
| AC-004 | Um modelo com relação material produz SVG acessível com equivalente textual; dois zooms com o mesmo conjunto de nós/arestas são detectados e reportados. | V-004 |
| AC-005 | `profile: minimal` + `domain: docs` produz um brief com subconjunto de rotas, sem exigir oito disposições `N/A`, e o revisor recebe a mesma lista de rotas que o compositor. | V-005 |
| AC-006 | Cada item do anexo A tem, no `decision-log.md`, correção aplicada ou decisão consciente com razão; um check enumera os itens e falha se algum ficar sem disposição. | V-006 |
| AC-007 | Cada regra do contrato tem ID estável `BC-NNN` com **exatamente uma** definição normativa em `.harness/rules/brief-contract.md`. Skills, agentes e workflows só citam o ID. O check falha se um `BC-NNN` for definido em mais de um arquivo, ou se um consumidor contiver texto normativo de brief fora de citação por ID. Oráculo binário. | V-007 |
| AC-008 | O check de suficiência de fontes (FR-011) bloqueia uma iniciativa fixture com AC sem validação **antes** de qualquer composição. | V-008 |
| AC-009a | **Mecanismo:** todo `stakeholder-brief.html` da iniciativa é **byte-reproduzível** a partir de `brief-model.yaml` + `project_brief.py` na revisão registrada. HTML de brief não reproduzível caracteriza markup autorado e reprova o incremento. Oráculo determinístico; não depende de julgar autoria em diff. | V-009 |
| AC-009b | **Doutrina:** o corpus normativo obrigatório por papel cai de 61.786 chars para no máximo 15.000 chars, medido por arquivo. | V-009 |
| AC-009c | **Convergência:** a matriz M-001…M-008 atinge PASS determinístico + `APPROVE` qualitativo em no máximo **duas** execuções, contra 6, 9 e 15 registradas no histórico de `testes/mock-runs/`. O `APPROVE` só conta como convergência quando vem de identidade distinta e registra achados; um `APPROVE` sem achados não é evidência. | V-010 |
| AC-009d | **Custo absoluto:** o custo real da execução nova é medido por etapa e registrado como linha de base futura. Nenhum percentual de redução é reivindicado contra um número que nunca foi medido. | V-010 |
| AC-010 | Uma revisão `REVISE` sobre o modelo é resolvida editando o modelo e reprojetando, sem reautorar HTML, e a evidência registra a diferença de custo em relação ao ciclo antigo. | V-010 |
| AC-011 | Um brief histórico pinned continua passando seus checks sem alteração de bytes. | V-011 |
| AC-012 | O conjunto de invariantes protegidas de `AGENTS.md` é **semanticamente preservado**, confirmado por humano nomeado. Igualdade textual não é exigida, porque FR-008 converte a invariante de brief em citação por ID. | V-012 |
| AC-013 | Após T-008, `validate_brief_candidate_inheritance.py`, `instantiate_brief_skeleton.py`, seus testes e a §9.1 de `plan.md` não existem no repositório, e nenhum artefato do bundle os referencia. Um check de referência pendente falha. | V-013 |
| AC-014 | A cadeia de revisão do brief tem exatamente **duas** passagens, com mandatos disjuntos declarados no contrato normativo. Nenhum artefato do bundle instrui uma terceira. | V-014 |

## 9. Casos de borda e comportamento em falha

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-001 | Fonte canônica muda depois do modelo autorado | Digest/fragmento divergem; a projeção falha e aponta o bloco e a fonte. Nunca projeta conteúdo stale silenciosamente. |
| EC-002 | O agente quer uma forma visual que o projetor não implementa | O modelo declara `form: prose` com razão, ou abre discovery. Não autora HTML paralelo. |
| EC-003 | Iniciativa não-software com zero relação material | `profile: minimal`; rota de arquitetura não é selecionada; nenhuma ausência precisa ser justificada. |
| EC-004 | Fonte genuinamente ausente e material | Vira discovery com fato faltante, impacto decisório e caminho, projetada como ausência visível. Não vira filler nem pergunta ao usuário durante construção normal. |
| EC-005 | Modelo válido mas editorialmente genérico | A revisão independente do modelo devolve `REVISE`. Nenhum check determinístico tenta julgar isso. |
| EC-006 | Consumidor pinned em contrato antigo | Continua no seu contrato; o novo só se aplica a partir do próximo refresh material ou migração explícita. |

## 10. Restrições e requisitos não funcionais

- **Arquitetura:** o projetor é um passo de projeção puro, sem leitura semântica
  de Markdown para síntese. Ele lê fonte apenas para resolver locator, digest e
  fragmento.
- **Segurança/privacidade:** nenhuma fonte, segredo ou PII é copiada para
  evidência de revisão; abstração mínima útil permanece a regra.
- **Dados:** o modelo é a fonte editorial; o Markdown canônico permanece fonte
  dos fatos. O HTML permanece estritamente derivado.
- **Performance:** o custo por brief é um requisito verificável (AC-009), não
  uma aspiração.
- **Compatibilidade:** version-aware por contrato declarado; nenhum byte
  histórico é reescrito.
- **Operacional:** a esteira continua autônoma — um `REVISE` recuperável das
  fontes não aguarda aprovação rotineira do usuário.
- **Precedência de enxugamento (D-004):** em conflito entre riqueza do
  resultado e limpeza da base, prevalece a limpeza. Um brief um pouco mais
  enxuto é um resultado **aceito** desta SPEC. Enriquecimento é trabalho
  posterior, sobre a base limpa — nunca justificativa para manter uma camada
  atual porque ela produz mais volume.

## 11. Premissas

| Premissa | Validação/owner |
|---|---|
| A seção 9.1 de `plan.md` cobre, em prosa, substancialmente o que o modelo precisa carregar | Verificar campo a campo durante o desenho do schema — Guardian maintainers |
| O shell atual (CSS/JS/a11y/print) é adequado e pode ser reusado sem redesenho | Confirmar contra a evidência renderizada de 014/023/024 — responsável pela experiência do brief |
| Uma barra declarada (perfil × domínio) reduz variância entre agentes | Medir em fixtures heterogêneas M001–M008 — Guardian maintainers |

## 12. Riscos

| ID | Risco | Prob. | Impacto | Mitigação/owner |
|---|---|---|---|---|
| R-001 | Projeção determinística uniformiza demais e o brief fica visualmente pobre | média | médio | **Risco aceito e rebaixado por D-004.** Formas enumeradas com implementação própria (FR-006) e revisão renderizada com poder de `REVISE` são a mitigação; um resultado mais enxuto não é regressão nesta SPEC — responsável pela experiência do brief |
| R-002 | O schema vira uma camisa de força para domínios não previstos | média | alto | Perfis × domínio (FR-005) + bloco `prose` genérico como escape sempre disponível — Guardian maintainers |
| R-003 | A consolidação da doutrina remove sem querer uma invariante protegida | média | crítico | AC-012 com check explícito antes/depois; toda remoção registrada no decision log — Guardian maintainers |
| R-004 | O esforço de migração excede o ganho | média | médio | Slice: novo contrato só para iniciativas novas; históricos pinned (FR-015, NG-004) — Guardian maintainers |
| R-005 | Os indicadores estáticos de FR-013 são proxies e não capturam todo o custo real da esteira antiga | alta | baixo | **Aceito e declarado.** São proxies, e a SPEC não reivindica percentual contra número não medido: AC-009a/b/c comparam grandezas verificáveis nos artefatos existentes, e AC-009d mede o lado novo em absoluto — Guardian maintainers |
| R-006 | Esta SPEC repete o padrão histórico: mais uma camada sobre as anteriores | média | crítico | **Métrica redefinida por D-033 (2026-09-21):** o critério real não é LOC estático, é custo operacional recorrente por brief (convergência, retrabalho). Código novo de investimento único (schema, projetor, checks) é aceitável quando reduz esse custo recorrente — medido em AC-009c/AC-009d, não em `git diff --stat`. V-REG-004 permanece como sinal de alerta, não gate — Guardian maintainers |

## 13. Dependências

| Dependência | Status | Owner | Bloqueante? |
|---|---|---|---|
| SPEC 028 | `superseded` por D-002 (2026-09-19) | owner | Não — resolvida. Requisitos absorvidos: proveniência do candidate, revisão em HTTP loopback, separação PASS determinístico × decisão qualitativa |
| SPECs 010, 015, 016, 017, 018, 019, 021, 022 | `superseded` por D-003 (2026-09-19), sem retrabalho | owner | Não — resolvidas. Encerradas como passado nos três registros (`spec.md`, `run-state.yaml`, `INDEX.md`) |
| SPECs 025 e 027 | `superseded` por D-005 (2026-09-19) | owner | Não — resolvidas. Tratavam do handoff e da integridade do skeleton, que FR-012 remove |
| SPECs 013 e 023 | `validation_done` desde 2026-08-27 e 2026-08-31 | — | Não — **não estão em execução**. As linhas `executing` no `INDEX.md` eram registro obsoleto (A-16), sincronizadas por D-010. Nenhuma coordenação de merge é necessária |
| Linha de base de custo | derivável estaticamente de `testes/mock-runs/` e `specs/` (FR-013) | Guardian maintainers | Não — resolvida. Nenhuma reexecução da esteira antiga é necessária |

## 14. Notas de validação

### Ordem de execução

A SPEC 029 é dispensada de produzir seu brief pela esteira antiga (D-007). O
brief dela é gerado pela esteira nova, ao final, e é a primeira prova do
modelo. A validação acontece **depois** da implementação, não antes. Gerar um brief de
exemplo com a esteira atual, só para servir de linha de base, custaria
exatamente o que esta SPEC existe para eliminar. Decisão do owner, 2026-09-19.

### Material de teste já disponível

| Artefato | O que é | Custo |
|---|---|---|
| `testes/mock-tests/0N-*.md` + `testes/spec-mock-test.md` | Os oito pedidos funcionais originais M-001…M-008, em domínios distintos: web full-stack, backend transacional, mobile offline, React Native, IA local, agentes, quiosque acessível, event-driven | zero — são a entrada |
| `testes/mock-runs/**` | 41 execuções da esteira antiga, com fontes canônicas completas e briefs produzidos por mock | zero — já versionado |
| `testes/visual-reference-runs/**` | Referências visuais aprovadas, incluindo a de M-005 | zero — já versionado |
| `scripts/fixtures/**` | Fixtures negativas dos validators atuais | zero — já versionado |

A cobertura de domínio dos oito mocks é o que impede a esteira nova de ser
otimizada para software: M-006 e M-007 exercitam casos que não são
desenvolvimento convencional, e é neles que um modelo rígido demais quebra
primeiro.

### O que a validação precisa provar

1. **Equivalência de garantia:** tudo que os validators atuais bloqueiam
   continua bloqueado. Rodar as fixtures negativas de `scripts/fixtures/**`
   contra a esteira nova é a prova mais barata disponível.
2. **Geração funciona nos oito domínios:** cada mock produz um brief projetado,
   sem markup autorado, sem detalhe técnico inventado nos casos não-software, e
   com as rotas selecionadas pelo perfil.
3. **Convergência:** quantas execuções a matriz precisa até PASS determinístico
   + `APPROVE` qualitativo. O histórico registrado (6, 9 e 15 execuções) é o
   comparativo, e ele é gratuito.
4. **Não regressão de qualidade:** revisão independente renderizada sobre a
   matriz nova, comparada com a evidência aprovada de 024 e com
   `testes/visual-reference-runs/20260831-m005-executive-reference`. Um PASS
   determinístico não prova qualidade e não pode ser reportado como tal.

O `validation-plan.md` é autoritativo para execução.

## 15. Decisão do Spec Guardian

**Outcome Ready:** yes
**Spec Ready:** yes
**Reviewer:** Spec Guardian independente (identidade distinta do autor dos
artefatos; não editou arquivo nem executou comando de escrita)
**Reviewed at:** 2026-09-19 — rodada 1
**Blocking issues (rodada 1):** B-1 objetivo sem AC; B-2 AC-009a sem oráculo;
B-3 AC-007 opinião rotulada de determinística; B-4 parte subtrativa sem AC;
B-5 D-007 sem nomear o gate; B-6 divergência de estado interna; B-7 T-007 não
atômica; B-8 A-13/A-15 em buraco de escopo; B-9 contagem histórica errada;
B-10 coordenação com 013/023.
**Required revisions:** todas aplicadas nesta rodada. B-9 era erro factual do
autor: `spec021-t004` chegou a `r15`, não a 10 execuções; a contagem por
diretórios retidos subcontava em 5. B-10 partia de premissa falsa: 013 e 023
já estavam `validation_done` e suas linhas no `INDEX.md` é que estavam
obsoletas (D-010). B-8 foi resolvido por `deferred` explícito (D-006), não por
inclusão de escopo.
**Reviewed at (rodada 2):** 2026-09-19 — Outcome Ready `yes`; Spec Ready `no`
com N-1 (pré-condição errada da operação destrutiva), N-2 (A-16 sem task),
N-3a/b/c (divergências entre spec, decision log e registros de estado) e N-4
(gates `brief_coverage_ready`/`tasks_ready` sem caminho). Todos corrigidos.
N-4 originou D-012.

**Reviewed at (rodada 3):** 2026-09-19 — **Outcome Ready `yes`, Spec Ready
`yes`.** O revisor verificou N-1…N-4 contra o repositório, julgou D-012
legítima (é consequência já contida em D-007, e aperta em vez de afrouxar: ata
os três gates a T-010, com aprovação humana pendente e expiração junto da
SPEC) e registrou seis achados não bloqueantes, todos aplicados.

**Decision evidence/link:** `decision-log.md` D-001…D-012. Plan Ready e
Validation Ready continuam exigindo suas próprias revisões independentes.

---

## Anexo A — Contradições verificadas na doutrina

Cada item foi confirmado por leitura direta. Este anexo é o insumo de FR-009 e
AC-006.

| ID | Contradição | Evidência |
|---|---|---|
| A-01 | Perfil visual: shell declarado "vendor-neutral by default" e, no mesmo documento, "keep Pearson navy/lavender/white as the canonical base" | `.harness/templates/stakeholder-brief-design.md:7` vs `:206` |
| A-02 | ID de rota de arquitetura: SKILL manda `architecture.global`; validator e testes exigem `architecture` | `.harness/skills/executive-brief-composition/SKILL.md:34` e `.harness/templates/plan.md:166` vs `scripts/validate_brief_candidate_inheritance.py:19`, `scripts/test_spec025_visual_skeleton.py:19` |
| A-03 | Terceiro vocabulário de rotas (`overview`…`trust`) vivo em script de referência | `scripts/build_spec024_heterogeneous_references.py:14` |
| A-04 | "Editorial map": exigido como entrega do agente e proibido como sidecar pela SKILL que ele deve usar | `.harness/agents/brief-experience-composer.md:38` e `.harness/agents/executive-brief-reviewer.md:22` vs `.harness/skills/executive-brief-composition/SKILL.md:92`; fixtures ativas em `scripts/fixtures/executive-brief-editorial-contract/*/editorial-map.md` |
| A-05 | Fluxo de bootstrap omite a etapa de skeleton presente no lifecycle | `.harness/AGENTS.md:96-116` (17 passos) vs `.harness/workflows/sdd-lifecycle.md:28-102` (20 passos, skeleton no 10) |
| A-06 | Número de visões: sete na regra, oito em todo o resto | `.harness/rules/human-visibility.md:75` vs `stakeholder-brief-design.md:121`, `executive-brief-composition/SKILL.md:34`, `validate_brief_candidate_inheritance.py:19` |
| A-07 | Numeração do lifecycle repete o passo 16 | `.harness/workflows/sdd-lifecycle.md:93` e `:95` |
| A-08 | `spec-review` ainda instrui a confirmar que "the canonical `v1` brief shell was populated" | `.harness/skills/spec-review/SKILL.md:45` |
| A-09 | Três eixos de versão simultâneos no mesmo arquivo: `design="v2"`, `structure="executive-brief-v3"`, `shell-contract="v1"` | `.harness/templates/stakeholder-brief.html:4-9` |
| A-10 | Local do registro de construção: "existing technical plan **or decision log**" vs "`plan.md` as the **only** composition record" | `.harness/rules/human-visibility.md` (§ coverage) vs `.harness/skills/executive-brief-composition/SKILL.md:28` |
| A-11 | Revisão pós-render atribuída simultaneamente ao Spec Guardian (via `spec-review`) e ao Executive Brief Reviewer (via `rendered-brief-decision-review`) | `.harness/skills/spec-review/SKILL.md:45-75` vs `.harness/workflows/sdd-lifecycle.md:74-83` e `.harness/AGENTS.md:92` |
| A-12 | `delivery-orchestrator` descreve a sequência de brief sem a etapa de skeleton nem a revisão pré-skeleton distinta da revisão de cobertura | `.harness/agents/delivery-orchestrator.md:28-30` |

| A-13 | Vocabulário de status do `INDEX.md` sem enum: `complete`, `completed`, `closed` e `validation_done` coexistem como se fossem estados distintos | `specs/INDEX.md`, coluna Status |
| A-14 | Status divergente entre as três fontes da mesma iniciativa: SPEC 010 declarava `approved for gated execution` no `spec.md`, `validation_done` no `run-state.yaml` e `draft` no `INDEX.md` | verificado em 2026-09-19, antes do encerramento por D-003 |
| A-14b | Mesma divergência em 025 (`spec ready` / `awaiting_human_visibility` / `spec_ready`) e 027 (`spec_ready` / `validation_done` / `spec_ready`) | verificado em 2026-09-19, antes do encerramento por D-005 |
| A-15 | SPECs 015, 016 e 017 carregavam o placeholder não preenchido do template (`draft \| outcome_ready \| spec_ready \| superseded`) como linha de Status | verificado em 2026-09-19, antes do encerramento por D-003 |
| A-16 | SPECs 013 e 023 apareciam como `executing` no `INDEX.md` enquanto seus `run-state.yaml` declaravam `validation_done: true` com todas as tasks `done` | verificado em 2026-09-19; sincronizado por D-010 |
| A-17 | **Contradição criada pela própria consolidação.** `brief-contract.md` BC-007 ("exactly **eight** canonical routes") e BC-013 ("Eight decision-view content contracts") afirmam oito rotas universais, enquanto BC-022 declara que rotas são **selecionadas** e a ausência é normal. `scripts/validate_brief_candidate_inheritance.py:234` ainda impõe as oito por código. | `brief-contract.md:98`, `:176`, `:269`; `validate_brief_candidate_inheritance.py:234` — achado da avaliação de T-003 |

Itens adicionais podem ser acrescentados durante a execução; nenhum pode ser
removido sem disposição registrada.

**Disposição (satisfaz FR-009/AC-006):**

| Item | Disposição |
|---|---|
| A-01 | **Corrigido (D-014).** Vendor-neutral por padrão; Pearson é opt-in explícito. Regra única em `.harness/rules/brief-contract.md` BC-011. |
| A-02, A-03 | **Corrigido/registrado (D-015).** ID canônico `architecture` (BC-007); SKILL de composição corrigida. Terceiro vocabulário de `build_spec024_heterogeneous_references.py` é divergência registrada, não corrigida (script histórico). |
| A-04 | **Corrigido (D-016).** "Editorial map" removido dos agentes; registro de construção vive só em `plan.md`/modelo (BC-008). |
| A-05 | **Corrigido (D-017).** Fluxo de `AGENTS.md` alinhado ao alvo pós-029 (duas passagens nomeadas, sem etapa de skeleton doutrinária). |
| A-06 | **Corrigido (D-018).** Confirmadas oito rotas/visões (BC-007); `human-visibility.md` cita BC-007 em vez de repetir um número. |
| A-07 | **Corrigido (D-019).** Numeração de `sdd-lifecycle.md` sequencial até 21. |
| A-08 | **Corrigido (D-020).** `spec-review` cita BC-002/BC-011 em vez de "canonical `v1` brief shell". |
| A-09 | **Registrado (D-021).** Eixo único `data-brief-contract` declarado em BC-002 como alvo; mapeamento de valores históricos é escopo de T-005. |
| A-10 | **Corrigido (D-022).** Registro de construção exclusivamente em `plan.md`/modelo (BC-008); resolvido junto com A-04. |
| A-11 | **Corrigido (D-023).** Revisão pós-render (pass b) atribuída exclusivamente ao Executive Brief Reviewer (BC-009); Spec Guardian só confirma que ocorreu. |
| A-12 | **Corrigido (D-024).** `delivery-orchestrator.md` nomeia as duas passagens (pass a antes da síntese, pass b depois do refresh). |
| A-14, A-14b, A-15, A-16 | **Corrigidos.** D-003 e D-005 alinharam as três fontes das iniciativas encerradas; D-010 sincronizou 013 e 023. |
| A-17 | **Corrigir em T-003 (doutrina) + T-008 (código).** BC-007/BC-013 passam a declarar as oito como **conjunto canônico de IDs**, não como obrigatoriedade de presença; o enforcement por código sai com o check de herança em T-008. Sem isso, um agente lendo o contrato isoladamente continua achando que oito rotas são obrigatórias, o que anula BC-022 na prática. |
| A-13 | **`deferred` (D-006).** O vocabulário misto de status do `INDEX.md` (`closed`, `complete`, `completed`, `validation_done`) **continua vivo** e não é corrigido por esta SPEC. Normalizá-lo exige o enum que D-006 adiou. |

A **causa** comum de A-13 a A-16 — ausência de enum de status e de check de
coerência entre `spec.md`, `run-state.yaml` e `INDEX.md` — é **decisão
consciente de ficar fora do MVP**, registrada em D-006 como `deferred`: não é
regra de brief, logo não cabe no contrato normativo de T-004, e D-004 manda
preferir escopo enxuto. A causa fica reconhecida e rastreada, não esquecida.

## Anexo B — Relação com a SPEC 028

A SPEC 028 diagnostica corretamente os sintomas (candidate com texto de
scaffold, topologia repetida entre zooms, tasks viradas em cartões-título,
estado incoerente). Sua resposta, porém, é **mais orquestração, mais gates e
mais contratos sobre a mesma arquitetura de autoria de HTML**. Executada como
está, ela aumenta o custo por brief e não remove a causa.

Esta SPEC trata a causa. **Decisão tomada (D-002, 2026-09-19): a SPEC 028 é
`superseded` por esta.** Os requisitos ainda válidos de 028 são absorvidos aqui:

| 028 | Absorvido por |
|---|---|
| FR-002 — proveniência do candidate ligada a plano e decisão | FR-001/FR-003: o modelo é a proveniência, e a projeção recusa locator irresolvível |
| FR-004 — revisão do HTML final em URL HTTP local por revisor distinto | FR-012 (b) |
| FR-007 — reportar separadamente check determinístico e decisão qualitativa | FR-012 e seção 14 |
| FR-005 — arquitetura material declara disposição visual | FR-004/FR-005 |
| FR-006 — execução e validação recuperam dossiers, não só IDs | FR-006 (`dossier` como forma enumerada) |

O que **não** foi absorvido, por decisão: as camadas adicionais de orquestração e
de gate que a 028 acrescentaria sobre a autoria de HTML. Elas deixam de fazer
sentido quando não há HTML autorado por agente.
