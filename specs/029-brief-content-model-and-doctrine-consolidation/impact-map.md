# Impact Map: 029-brief-content-model-and-doctrine-consolidation

**Status:** reviewed
**Spec:** ./spec.md
**Mapped by:** Guardian maintainers
**Reviewed at:** 2026-09-19
**Overall risk:** high

## 1. Change boundary

**Muda:** a camada de autoria do brief (agente deixa de escrever HTML), a
doutrina normativa do brief (consolidada em contrato único) e a cadeia de
revisão (três passagens → duas).

**Permanece intocado:** as invariantes protegidas de `AGENTS.md`; o shell
visual (CSS/JS/a11y/print) que hoje vive em `.harness/templates/stakeholder-brief.html`;
os briefs já renderizados em `specs/**` e `testes/**`; as regras de SDD que não
são do brief (`sdd-quality`, `outcome-readiness`, `task-readiness`,
`validation-policy`, `evidence-policy`, `state-and-memory`,
`builder-evaluator-separation`, `destructive-operations`,
`instruction-precedence`, `audit-policy`).

Esta é uma iniciativa **subtrativa**: o critério de sucesso inclui remover
artefatos, não só adicionar (R-006 da spec).

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| UI/client | `.harness/templates/stakeholder-brief.html` | direto | CSS/JS/a11y preservados; markup vira gabarito de projeção em vez de arquivo copiado | medium | shell atual + evidência aprovada de 014/023/024 |
| Service/backend | `not_applicable` — o bundle não tem serviço em runtime | — | — | — | — |
| Data/storage | novo `brief-model.yaml` por iniciativa + schema versionado | direto | artefato novo; `plan.md` §9.1 removida em troca | high | spec FR-001, FR-007 |
| Public/API contract | contrato de atributos de proveniência (`data-source`, `data-source-section`, `data-coverage`, `data-source-digest`, `data-source-fragment*`) e eixo de versão do brief | direto | atributos passam a ser emitidos pelo projetor; eixo de versão unificado (FR-010) | high | `stakeholder-brief-design.md`, `validate_human_visibility.py` |
| Auth/security/privacy | política de redação/abstração mínima e ausência de segredo em evidência | indireto | preservada sem alteração; o modelo não cria novo canal de exposição | medium | `human-visibility.md` §arquitetura |
| Build/deploy/infra | `scripts/` do pipeline de brief (4.752 linhas) | direto | `validate_brief_candidate_inheritance.py` e `instantiate_brief_skeleton.py` removidos; `render_stakeholder_brief.py` reduzido a promoção + projeção | high | contagem na spec §1.1 |
| Observability/support | instrumentação de custo por etapa (FR-014) | direto | adição nova; não existe hoje | low | spec FR-013/FR-014 |
| Tests/docs | `scripts/test_*` (4.989 linhas), `.harness/rules/human-visibility.md`, `.harness/templates/stakeholder-brief-design.md`, 3 SKILLs de brief, `spec-review`, `sdd-lifecycle`, `AGENTS.md`, 2 arquivos de agente | direto | consolidação em contrato normativo único; testes de skeleton removidos, testes de projeção adicionados | high | Anexo A da spec |

## 3. Dependency and data flow

Fluxo atual:

```txt
fontes .md -> plan.md 9.1 (registro em prosa) -> revisao -> skeleton copiado
           -> agente autora HTML a mao -> herança check -> renderer -> revisao
```

Fluxo alvo:

```txt
fontes .md -> brief-model.yaml (autorado pelo agente) -> revisao do modelo
           -> projetor determinístico -> stakeholder-brief.html -> revisao renderizada
```

O elo removido é `skeleton copiado -> agente autora HTML -> herança check`.

## 4. Compatibility and migration

- **Backward compatibility:** briefs já renderizados permanecem válidos sob seu
  contrato registrado (FR-015, NG-004). Nenhum byte histórico é reescrito.
- **Data migration:** nenhuma. Iniciativas encerradas não migram; iniciativas
  novas nascem no contrato novo.
- **Rollout:** o contrato novo vale a partir da própria SPEC 029, cujo brief é
  a primeira prova (D-007).
- **Rollback:** o bundle é versionado por tag. Um rollback é `git revert` da
  release + retorno ao contrato anterior. Como nenhum artefato de consumidor é
  reescrito, o rollback não corrompe iniciativa existente. Esse é o motivo pelo
  qual NG-004 é invariante e não preferência.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-001 | Consolidação da doutrina remove uma invariante protegida sem perceber | diff de `.harness/rules/` e `AGENTS.md` tocando lista de invariantes | média / crítico | Check que compara a lista de invariantes antes/depois | Reverter a remoção e registrar no decision log — Guardian maintainers | V-012 |
| IR-002 | Projetor emite HTML que passa nos checks mas perde uma garantia que o pipeline antigo dava | fixture negativa existente deixa de falhar | média / alto | Rodar todas as fixtures de `scripts/fixtures/**` contra a esteira nova | Restaurar o check equivalente antes de prosseguir — Guardian maintainers | V-002 |
| IR-003 | Modelo rígido demais quebra em domínio não-software. **ABERTO, rebaixado para médio (D-029):** o modelo de conteúdo generaliza; o inventário de fontes não (D-028) | fixture não-software precisa fabricar artefato de SDD sem uso orgânico | média / médio | Bloco `prose` como escape sempre disponível; perfil × domínio seleciona rotas | Ampliar a enumeração de formas, nunca autorizar HTML paralelo — responsável pela experiência do brief | V-005, M-02 |
| IR-004 | Remoção do check de herança abre espaço para HTML autorado à mão reaparecer | diff de iniciativa contendo markup de brief | média / alto | AC-009a: todo brief byte-reproduzível a partir do seu modelo | Bloquear a promoção — Guardian maintainers | V-009, V-REG-002 |
| IR-005 | Eixo único de versão (FR-010) quebra leitura de brief histórico | validator falha em `specs/00*/stakeholder-brief.html` | média / alto | Mapeamento documentado dos valores históricos; teste sobre brief pinned | Manter leitura version-aware dos valores antigos — Guardian maintainers | V-011 |
| IR-007 | Tasks em paralelo produzem vocabulários divergentes para conceitos que se sobrepõem | dois atributos de nome quase idêntico, ou um consumidor ainda emitindo o eixo que outra task eliminou | **ocorrido** / alto | Reconciliação explícita antes de T-008 remover o fallback legado | Atribuir a reconciliação a uma task nomeada; nunca deixar os dois vocabulários coexistirem em release — Guardian maintainers | avaliação de T-005 |
| IR-006 | A iniciativa vira aditiva e repete o padrão histórico do repositório | diff final com saldo de linhas positivo em `.harness/` e `scripts/` | média / crítico | Saldo líquido de remoção como critério explícito (R-006) | Replanejar o slice — Guardian maintainers | V-REG-004 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Se a §9.1 de `plan.md` cobre campo a campo o que o modelo precisa carregar | Se não cobrir, o schema nasce incompleto e a primeira execução da matriz falha por falta de campo | T-001 (desenho do schema) — Guardian maintainers | não — é a primeira task |
| U-002 | Quantas formas de apresentação o projetor precisa implementar para cobrir os oito domínios | Determina o tamanho do projetor e o risco IR-003 | T-003, calibrado contra os briefs já produzidos em `testes/mock-runs/` | não |
| U-003 | Se o eixo único de versão consegue representar os três eixos atuais sem perda | Determina se FR-010 é renomeação ou mudança de contrato | T-005 — Guardian maintainers | não |
| U-004 | Qual o tamanho mínimo viável do contrato normativo único (AC-009b exige ≤15.000 chars por papel) e quais papéis são contados | Se não couber, AC-009b precisa ser renegociado com evidência, não afrouxado por conveniência | T-004 — Guardian maintainers | não |

## 7. Recommended reviewers and checks

- **Especialista/humano:** responsável pela experiência do brief, para
  IR-003 e para a comparação com `testes/visual-reference-runs/20260831-m005-executive-reference`.
- **Determinísticos:** fixtures negativas existentes de `scripts/fixtures/**`;
  novo teste de projeção; teste de invariantes preservadas; teste sobre brief
  histórico pinned.
- **Manual/operacional:** revisão renderizada independente sobre a matriz
  M-001…M-008 servida em loopback.

## 8. Impact decision

**Impact mapped:** yes
**Human review required:** yes — IR-001 e IR-006 são críticos e não têm
controle puramente determinístico.
**Approval/evidence:** decision-log D-001 a D-012
**Conditions before implementation:** Spec Ready por identidade distinta;
`validation-plan.md` cobrindo todos os ACs; `tasks.md` com exit criteria e
destino de evidência por task.
