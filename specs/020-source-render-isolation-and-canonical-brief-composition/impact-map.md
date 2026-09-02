# Impact map — SPEC 020

**Status:** in_review · **Risk:** high

| Superfície | Mudança | Risco/controle |
|---|---|---|
| Scaffolder | Não cria HTML ou asset. | Fixture temporário prova ausência. |
| Lifecycle/HV | Cruza `brief_phase`, fonte, revisão e baseline. | Contrato v1 preservado; v2 estrito. |
| Renderização/brand | Promoção local com política Pearson. | Hotlink, filtro, role e overwrite recusados. |
| Composição | Origem por bloco allowlisted. | Fato estrangeiro negativo e digest. |
| Mock lab | Raiz isolada e matriz de lentes. | REVISE bloqueia baseline e abre corretivo. |

```txt
fonte A + candidato A ─► brief A
fonte B + candidato B ─► brief B
qualquer bloco A em B ─► falha de proveniência, sem promoção/aprovação
```

**Compatibilidade:** v1 histórico não ganha fase retroativamente; v2 renderizado
exige fase e review. **Operação:** sem rede, banco, segredo ou migração.
**Rollback:** decisão humana; reverter restauraria a superfície insegura.
