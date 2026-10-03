# Technical Plan: 029-brief-content-model-and-doctrine-consolidation

**Status:** plan_ready
**Spec:** ./spec.md
**Impact map:** ./impact-map.md
**Validation plan:** ./validation-plan.md
**Owner:** Guardian maintainers + responsável pela experiência do brief
**Last updated:** 2026-09-19

## 1. Technical approach

Nove passos, cada um verificável isoladamente, ordenados para que o risco mais
caro de reverter venha por último.

O princípio de ordem é: **primeiro provar que o modelo representa a realidade,
depois construir o projetor, e só então remover as camadas antigas.** Remover
antes de provar deixaria o bundle sem esteira funcional no meio do caminho.

1. **Schema do modelo**, derivado campo a campo da §9.1 de `plan.md` e validado
   contra os briefs já produzidos em `testes/mock-runs/`. Se um brief existente
   não for representável no schema, o schema está errado — não o brief.
2. **Projetor** modelo → HTML, reusando o shell atual como gabarito.
3. **Formas de apresentação** enumeradas, calibradas pelo que os briefs
   existentes de fato usam.
4. **Contrato normativo único**, absorvendo a doutrina dispersa.
5. **Limpeza do Anexo A**, com disposição registrada item a item.
6. **Cadeia de duas revisões** com mandatos disjuntos (doutrina, não código).
7. **Remoção** das camadas que perderam função — único passo destrutivo.
   Os passos 5a (eixo único, T-005) e 5b (suficiência de fontes, T-006) são
   aditivos e correm em paralelo aos passos 4–6.
8. **Execução da matriz** M-001…M-008, com medição de custo e revisão independente.
9. **Brief da própria 029** projetado pela esteira nova, e liberação dos gates
   suspensos por D-007/D-011/D-012.

A menor abordagem segura é essa porque os passos 1–6 são puramente aditivos e
reversíveis por `git revert`; o passo 7, que é o destrutivo, só acontece depois
que a substituição está provada. A divisão entre os passos 6, 7 e 8 veio do
achado B-7 da revisão independente: doutrina, remoção e medição são entregas
separáveis e não cabem numa task só.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| PD-001 | O modelo é YAML, não JSON | É o formato que o bundle já usa para estado (`run-state.yaml`); permite comentário, que é onde o agente registra a razão da forma escolhida | JSON (sem comentário); TOML (não usado no bundle); Markdown estruturado (é o que falha hoje) | Parser YAML já é dependência do pipeline |
| PD-002 | O modelo vive em `brief-model.yaml` na raiz da iniciativa | Fica ao lado das fontes canônicas que ele referencia; sobrevive a `git revert` do código | Dentro de `plan.md` (não é machine-readable); em `brief-candidates/` (sugere artefato descartável) | Um arquivo novo por iniciativa |
| PD-003 | O projetor lê fonte canônica **apenas** para resolver locator, digest e fragmento | Preserva NG-001: nenhuma síntese semântica em código | Deixar o agente digitar digests (é o que falha hoje); não verificar (perde a garantia) | O projetor precisa de acesso de leitura às fontes |
| PD-004 | O shell atual vira gabarito de projeção, preservando CSS/JS/a11y/print byte a byte quando possível | NG-003 exclui redesenho; a evidência de acessibilidade de 013/014 continua valendo | Reescrever o shell (fora de escopo e descartaria evidência aprovada) | Gabarito e shell precisam ficar sincronizados |
| PD-005 | Eixo único `data-brief-contract="N"`, com mapeamento documentado dos três eixos atuais | FR-010; resolve A-09 | Manter os três eixos (é a contradição); renomear sem mapear (quebra histórico, viola NG-004) | Leitura version-aware precisa conhecer os valores antigos |
| PD-006 | O contrato normativo único é `.harness/rules/brief-contract.md`; skills, agentes e workflows **referenciam** | FR-008; custo de doutrina passa de O(agentes × doutrina) para O(1) | Manter a doutrina distribuída (é a causa); colocar em `templates/` (não é template, é regra) | Toda mudança de regra do brief passa a ter um único ponto |
| PD-007 | Remoção do check de herança e do instanciador de skeleton só no passo 7 | A garantia que eles davam precisa estar provada antes de sumir | Remover no início (deixaria o bundle sem esteira); nunca remover (a iniciativa viraria aditiva, R-006) | Janela em que as duas esteiras coexistem |

## 3. Size and proportionality

**Initiative size:** L.
**Why:** toca o contrato público de proveniência, a doutrina normativa do
bundle inteiro e ~9.700 linhas de Python entre pipeline e testes; e seu modo de
falha (IR-001, remover invariante sem perceber) é crítico.
**Smaller option considered:** fazer só a consolidação da doutrina (Anexo A),
sem o modelo de conteúdo. **Insuficiente:** resolveria a variância de qualidade
mas não o custo, que é a causa declarada em §1.1 da spec. O inverso — só o
modelo, sem consolidar a doutrina — também foi rejeitado: o agente continuaria
recebendo instrução contraditória sobre como preencher o modelo.
**Complexity deliberately excluded:** redesenho visual, mobile, migração de
briefs históricos, geração determinística de conteúdo, score de qualidade.

### Client visual profile selection (conditional)

| Field | Required record |
|---|---|
| Default profile | `vendor-neutral`. Esta iniciativa não seleciona perfil de cliente. |
| Pearson selection | `not_applicable` — nenhuma fonte canônica desta iniciativa seleciona Pearson. |
| Brand authority | `not_applicable` |
| Asset | `not_applicable` — nenhum asset de marca é referenciado. |
| Asset distribution | `not_applicable` |
| Font boundary | `not_applicable` |
| Exception | Nenhuma. A contradição A-01 (`vendor-neutral by default` vs `Pearson as canonical base`) é **escopo de correção** desta iniciativa, não uma seleção de perfil. |

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** A2-elevated
**Rationale and trigger evidence:** altera contrato público de proveniência
(`data-source*`), toca fronteira de confiança do lifecycle (o que autoriza
promoção) e é trabalho de UI material. Qualquer um desses gatilhos já exigiria
A2 por `.harness/rules/validation-policy.md`.
**A2/A3 source links/headings:** spec §10 (Restrições), impact-map §2 (linhas
`Public/API contract` e `Build/deploy/infra`), impact-map §5 (IR-001, IR-002).
**Reapproval trigger:** mudança de perfil, nova fronteira de confiança,
descoberta de que o modelo não representa um domínio dos oito mocks, ou falha
de asseguramento no passo 8 ou 9.

### Architecture scope/size profile

**Profile:** L

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Bundle instalado como submódulo em consumidor; agentes leem `.harness/`, escrevem em `specs/NNN-slug/` | Inalterado | `.harness/AGENTS.md` §Bootstrap |
| Components/responsibilities | Agente autora HTML; scripts validam e promovem | Agente autora modelo; projetor gera HTML; scripts validam e promovem | spec FR-001/FR-002; PD-003 |
| Interfaces/events/contracts | Atributos `data-source*` digitados pelo agente; três eixos de versão | Atributos emitidos pelo projetor; eixo único `data-brief-contract` | PD-005; FR-010 |
| Data ownership/lifecycle | Markdown canônico = fatos; HTML = derivado, mas na prática guarda a única cópia da prosa editorial | Markdown = fatos; `brief-model.yaml` = editorial canônico; HTML = estritamente derivado | spec §10 (Dados). **Isto reforça a invariante "HTML não é fonte": hoje ela é violada de facto, porque a prosa só existe no HTML.** |
| Security/trust boundaries | Promoção guardada por attestation SHA-256 + lifecycle | Inalterada. O modelo entra **antes** da attestation, não a substitui | `render_stakeholder_brief.py` §attestation |
| Critical runtime flows | fontes → plan §9.1 → revisão → skeleton → HTML à mão → herança → render → revisão | fontes → modelo → revisão → projeção → render → revisão | impact-map §3 |
| Failure behavior | Falha tardia: o erro aparece depois do HTML existir | Falha antecipada: locator irresolvível ou fragmento ausente barram a projeção (FR-003) | spec FR-003, EC-001 |
| NFRs | Custo por brief não medido | Custo medido (FR-014); doutrina por papel ≤15.000 chars (AC-009b) | spec §8 |
| Compatibility/migration | Version-aware v1/v2 | Version-aware com mapeamento explícito dos valores históricos | PD-005; FR-015; NG-004 |
| Observability | Inexistente para custo | Instrumentação por etapa na esteira nova | FR-014 |
| Rollout/rollback | Release por tag | Idem; rollback é `git revert` da release. Nenhum artefato de consumidor é reescrito, então o revert não corrompe iniciativa existente | impact-map §4 |
| Alternatives/trade-offs | — | Ver §3 (opções menores rejeitadas) e PD-001…PD-007 | — |
| Unknowns | — | U-001 a U-004 | impact-map §6 |

### Current → target → delta e envelope de complexidade

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Arquitetura/método | Agente autora HTML a partir de doutrina dispersa | Agente autora modelo a partir de contrato único | **Saldo líquido de remoção obrigatório** em `.harness/` e `scripts/` (R-006, IR-006) | Saldo positivo no diff final |
| Módulos/APIs/contratos | 9 scripts de brief (4.752 linhas) + 4.989 de teste; 3 eixos de versão; 8 rotas fixas | Projetor + schema; 1 eixo de versão; rotas selecionadas por perfil × domínio | Remover `validate_brief_candidate_inheritance.py`, `instantiate_brief_skeleton.py` e seus testes | Necessidade de manter qualquer um dos dois |
| Processo/ferramental | 3 revisões sobrepostas; doutrina em 8+ arquivos | 2 revisões disjuntas; 1 contrato normativo | Doutrina obrigatória por papel: 61.786 → ≤15.000 chars | Não caber em 15.000 chars (renegociar com evidência, não afrouxar) |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | `schemas/brief-model.schema.*`, derivado de `.harness/templates/plan.md` §9.1 | Spec Ready | Schema que representa os briefs existentes de `testes/mock-runs/` | sim — aditivo |
| 2 | novo `scripts/project_brief.py`; `.harness/templates/stakeholder-brief.html` como gabarito | passo 1 | Projeção modelo → HTML com proveniência computada | sim — aditivo |
| 3 | formas enumeradas dentro do projetor | passo 2 | Cobertura das formas que os briefs existentes usam | sim — aditivo |
| 4 | novo `.harness/rules/brief-contract.md` | — | Contrato normativo único | sim — aditivo |
| 5 | `human-visibility.md`, `stakeholder-brief-design.md`, 3 SKILLs, `spec-review`, `sdd-lifecycle`, `AGENTS.md`, 2 agentes | passo 4 | Anexo A disposto item a item; reenunciação removida (T-004) | sim — `git revert` |
| 5a | eixo `data-brief-contract` em `.harness/templates/stakeholder-brief.html` + tabela de mapeamento | passo 2 | Eixo único de versão (T-005) | sim — aditivo |
| 5b | novo `scripts/validate_source_sufficiency.py` | passo 4 | Check de suficiência de fontes antes da composição (T-006) | sim — aditivo |
| 6 | `.harness/rules/brief-contract.md` §revisão; `sdd-lifecycle.md`; SKILLs | passo 4 | Cadeia de duas revisões com mandatos disjuntos (T-007) | sim — aditivo |
| 7 | remover `validate_brief_candidate_inheritance.py`, `instantiate_brief_skeleton.py`, `plan.md` §9.1 e testes correspondentes | passos 1–6 provados | Saldo líquido de remoção (T-008) | **sim, mas é o passo destrutivo** — só após prova |
| 8 | `testes/mock-runs/` nova execução | passo 7 | Matriz M-001…M-008 + custo medido + revisão independente (T-009) | n/a — é verificação |
| 9 | `brief-model.yaml` e `stakeholder-brief.html` da 029 | passo 8 | Brief da própria 029 + liberação dos gates suspensos (T-010) | n/a — é verificação |

## 6. Contracts, data and compatibility

- **API/events:** contrato de atributos de proveniência preservado em
  significado; muda o emissor (agente → projetor). Eixo de versão unificado com
  mapeamento documentado.
- **Database/storage:** `not_applicable` — sem banco.
- **External systems:** `not_applicable` — o bundle é offline por contrato;
  nenhum asset remoto, fonte de rede ou serviço externo é introduzido.
- **Compatibility/migration:** nenhuma migração. Briefs históricos pinned;
  contrato novo vale a partir da 029.

## 7. Security, privacy and permissions

- **Authentication/authorization:** `not_applicable`.
- **Secrets/PII:** inalterado. O modelo não cria novo canal de exposição; a
  regra de abstração mínima e redação registrada continua valendo, agora em um
  único lugar normativo.
- **Required permission:** escrita em `.harness/`, `scripts/`, `specs/` e
  `testes/` do próprio bundle.
- **Destructive operations and approvals:** o **passo 7** (T-008) é a única
  operação destrutiva: remove arquivos versionados. É reversível por
  `git revert` e só ocorre após os passos **1–6** estarem provados, o que
  inclui a cadeia de duas revisões do passo 6. Exige aprovação humana
  registrada. Nenhuma remoção em consumidor.

## 8. Rollout, observability and rollback

- **Rollout:** release por tag do bundle, como toda alteração deste repositório.
- **Success/failure signals:** matriz M-001…M-008 convergindo em ≤2 execuções
  (AC-009c); fixtures negativas existentes continuando a falhar (V-002);
  saldo líquido de remoção (V-REG-004).
- **Rollback trigger:** qualquer fixture negativa deixando de falhar; qualquer
  invariante protegida ausente no check de V-012; matriz não convergindo.
- **Exact rollback/checkpoint:** `git revert` até a tag 0.4.0. Os passos 1–6
  são aditivos e podem ser revertidos isoladamente; o passo 7 é o único que
  exige revert conjunto com 1–6.

## 9. Brief coverage composition

`not_applicable` por **D-007**: esta iniciativa está dispensada de produzir seu
stakeholder brief pela esteira antiga. Seu brief será gerado pela esteira nova
no passo 9 e serve como primeira prova do modelo. D-011 delimita que a
dispensa é de **ordenação** do gate `human_visibility_ready`, nunca de sua
existência: o gate só vai a `true` com o brief projetado e revisado por
identidade distinta, e a exceção expira com esta SPEC. **D-012** estende a
mesma suspensão de ordenação a `brief_coverage_ready` e à dependência de brief
em `tasks_ready`; os três gates são resolvidos juntos no passo 9.

O escopo dessa dispensa é estrito (**D-008**): ela cobre apenas o caminho de
produção do brief. Continuam integrais identidades distintas, evidência
aprovada antes de `done`, revisão independente, renderizar ≠ aprovar, HTML não
é fonte canônica, e a proibição de `done` a partir de `in_progress` ou
`needs_evaluation`.

A seção 9.1 do template (`Brief construction record`) é **objeto de remoção**
por FR-007, não um campo a preencher aqui.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | A §9.1 cobre campo a campo o que o modelo precisa? | Guardian maintainers | T-001 valida contra `testes/mock-runs/` | no |
| Q-002 | Quantas formas de apresentação cobrem os oito domínios? | responsável pela experiência do brief | T-003 calibra pelos briefs existentes | no |
| Q-003 | O contrato normativo único cabe em ≤15.000 chars por papel, e quais papéis são contados? | Guardian maintainers | T-004; se não couber, renegociar AC-009b **com evidência**, nunca afrouxar por conveniência | no |
| Q-004 | O eixo único representa os três atuais sem perda? | Guardian maintainers | T-005 testa contra brief histórico pinned | no |

## 11. Plan decision

**Plan Ready:** yes
**Reviewer:** revisor independente de Plan/Validation Ready (identidade distinta do autor)
**Reviewed at:** 2026-09-19
**Conditions/links:** aprovado. O revisor confirmou as 13 dimensões de arquitetura
preenchidas com fato e fonte, rollback compatível com risco `high`, pré-condições
corretas da operação destrutiva (T-008 depende de T-001…T-007) e PD-001…PD-007 com
alternativa rejeitada e consequência real. F-5 verificado como já resolvido pelos
passos 5a e 5b.
