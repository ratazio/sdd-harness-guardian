# Plano de validação — SPEC 020

**Status:** completed · **Estratégia:** A2, regressão local e julgamento humano

| ID | AC | Método/oráculo | Comando/passo | Evidence |
|---|---|---|---|---|
| V-001 | AC-001 | scaffold temporário sem HTML/asset | `python scripts/smoke_test_scaffolder.py` | T-001 |
| V-002 | AC-001 | fase e arquivo incompatíveis recusados | `python scripts/test_brief_delivery_integrity_reproduction.py` | T-001 |
| V-003 | AC-002 | promoção, shell/reclassificação/hotlink/overwrite negativos | `python scripts/test_render_stakeholder_brief.py` | T-002 |
| V-004 | AC-002 | browser local, foco/no-script/print/reduced-motion | `python scripts/test_client_identity_profile_render.py` | T-002 |
| V-005 | AC-003 | allowlist, locator/digest e fato estrangeiro negativo | `python scripts/test_source_render_isolation.py` | T-003 |
| V-006 | AC-004/005 | suíte inteira e 7 lentes em duas passagens | mock lab em raiz nova | T-004 |

Regressão obrigatória: `test_validate_human_visibility.py`,
`test_decision_quality_review_contract.py`, `validate_bundle.py`.

Em V-006, cada lente registra veredito e severidade por passagem, decisão que
não era possível tomar apenas pelo HTML, locator recuperado nas fontes e reparo.
REVISE material bloqueia baseline e aprovações do caso; causa sistêmica gera
SPEC corretiva autorizada.

## Execução registrada

| Data | Task | Resultado verificável |
|---|---|---|
| 2026-08-28 | T-002 / V-003–V-004 | Bateria de render, identidade, browser, quality-review, Human Visibility e bundle PASS; a avaliação independente reproduziu dois bypasses de casca e aprovou somente após ambas as regressões fecharem. |
| 2026-08-28 | T-003 / V-005 | Isolamento por origem, digest e fragmento factual visível PASS; dois `REVISE` P1 independentes (locator não verificável e nesting malformado) viraram regressões antes do `APPROVE` final. |
| 2026-08-28 | T-004 / V-006 | M-001–M-008 gerados em r5 e servidos localmente; sete lentes × duas passagens registraram REVISE material em todos os casos. Baselines bloqueados; SPEC 021 criada por duas causas sistêmicas recorrentes. |
| 2026-08-28 | T-004 / V-006 | Auditoria independente `/root/t004_completion_audit` aprovou a completude da execução: manifesto, 24 digests, 56 registros e ausência de baseline; `validate_bundle.py` PASS (272 checks). |
