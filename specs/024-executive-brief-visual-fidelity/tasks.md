# Tasks — SPEC 024

**Status:** complete  
**Spec:** `./spec.md`  
**Plan:** `./plan.md`  
**Validation plan:** `./validation-plan.md`  
**Last updated:** 2026-08-31

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Construir referência visual M-005 renderizada e offline | spec ready | high | `/root/spec024_visual_reference_builder` | `/root/spec024_visual_reference_reviewer` | `evidence/T-001.md` |
| T-002 | done | Integrar contrato reutilizável de visual material e teste negativo | T-001 approve | high | `/root/spec024_visual_contract_builder` | `/root/spec024_visual_contract_reviewer` | `evidence/T-002.md` |
| T-003 | done | Revalidar aplicação heterogênea e preservar corpus/históricos | T-002 approve | high | `/root/spec024_visual_heterogeneous_builder` | `/root/spec024_visual_heterogeneous_reviewer` | `evidence/T-003.md` |

## T-001 — Referência visual M-005 renderizada e offline

**Status:** done  
**Requirement IDs:** FR-024-01…FR-024-07  
**Acceptance criteria IDs:** AC-024-01…AC-024-04  
**Outcome served:** referência correta substitui o artefato técnico mostrado indevidamente.  
**Demonstrable increment:** HTML isolado + SVGs + PNG desktop/mobile + PDF + audit.  
**Why now:** reproduz a divergência antes de generalizar contrato.  
**Builder:** `/root/spec024_visual_reference_builder`  
**Evaluator:** `/root/spec024_visual_reference_reviewer` — APPROVE sobre os bytes congelados.  
**Human approval:** requester autorizou execução e avaliação agêntica; revisão independente obrigatória.  
**Evidence:** `evidence/T-001.md`

### Scope

Raiz nova `testes/visual-reference-runs/20260831-m005-executive-reference/`;
HTML único, rotas, SVG arquitetural/assurance, CSS Pearson e evidência renderizada.

### Out of scope

Alterar T-004, brief histórico, fontes M-005 ou implementar produto.

### Assurance disposition

| Claim/risk | Technique | Oracle/data | Builder | Evaluator | Evidence | Exit/failure |
|---|---|---|---|---|---|---|
| Fatos/limites corretos | fonte→visual review | M-005 + plan | builder | independent reviewer | audit + review | REVISE bloqueia T-002 |
| Rota/a11y | browser/no-script/print | HTML local | builder | reviewer spot-check | PNG/PDF/log | falha volta ao builder |
| Fidelidade | render comparison | design.md + M-023-B | builder | independent reviewer | screenshot/review | ausência de gráfico = REVISE |

### Exit criteria

- [x] output isolado/offline/não canônico;
- [x] SVG/topologia/mapa/zoom/assurance visíveis;
- [x] render desktop/mobile/PDF registrado;
- [x] revisor independente decidiu APPROVE;
- [x] evidence e run-state sincronizados.

## T-002 — Contrato reutilizável de visual material

**Status:** done. Implementação e regressões, inclusive as duas
correções de REVISE, foram aprovadas por avaliador distinto. Extrai somente primitives
necessários, com proveniência, fallback/N/A e teste negativo; não padroniza
todo layout.

## T-003 — Aplicação heterogênea e preservação

**Status:** done. O builder recompôs e capturou oito cópias descartáveis
heterogêneas; avaliador distinto aprovou os renders exatos. Nenhuma promoção
de T-004 ou de histórico foi autorizada.
