# Impact map — SPEC 024

## Change statement

Trocar a projeção visual insuficiente por uma composição cuja semântica e
geometria sejam verificáveis no render; preservar fontes, laboratório T-004 e
briefs históricos sem alteração.

| Surface | Change | Risk | Evidence |
|---|---|---|---|
| Referência M-005 isolada | HTML, SVGs, navegação query, CSS Pearson e README novos. | Alto: invenção ou falha de a11y. | screenshots, PDF, DOM/no-script, review. |
| Contrato reutilizável | Primitive visual + fallback explícito e validator negativo. | Alto: afeta brief futuro. | regression + casos heterogêneos. |
| Corpus T-004 | Só baseline/reprodução; não sobrescrever. | Médio: confusão de autoridade. | hashes/paths preservados. |
| Briefs históricos | Nenhuma mudança. | Alto: promoção indevida. | diff/path assertion. |

## Material relationships

`pedido M-005 -> fontes -> mapa editorial -> SVG/HTML derivado -> captura/PDF
-> revisão independente -> decisão de promoção ou revise`.

## Rollback

Todo output é novo e isolado. Remover a referência/candidato de uso não altera
autoridade canônica ou histórico; integração futura exige evidence próprio e
reversão por commit, sem apagar evidência.
