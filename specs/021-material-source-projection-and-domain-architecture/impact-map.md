# Impact Map — SPEC 021

**Status:** draft · **Risk:** high. O escopo é regras/templates/renderer,
validador e laboratório mock; nenhum produto mock será implementado.

| Surface | Change | Risk/control |
|---|---|---|
| Source inventory and coverage | Ratchet vira fonte condicional material e deve registrar estado vazio justificado. | Não tornar ausência irrelevante uma obrigação; V-021-01. |
| Brief composition | Relações materiais usam fluxo, tabela, SVG acessível ou equivalente escolhido pelo domínio. | Não adotar quota visual; V-021-02. |
| Semantic review hook | Agente distinto compara pedido, corpus e candidato antes de promoção/baseline. | Não fixar taxonomia de domínio ou transformar o parecer em score; V-021-02/V-021-04. |
| Renderer/provenance | Novos blocos mantêm fonte, locator, digest e fragmento factual. | Não abrir bypass T-002/T-003; regressão de promoção. |
| Human Visibility | Sete lentes repetem HTML-first e comparação em M-001–M-008. | Baseline só após todos APPROVE; V-021-04. |

| ID | Risk event | Signal | Control/owner | Validation |
|---|---|---|---|---|
| IR-021-01 | Ratchet real desaparece. | Fonte contém regra e HTML/coverage não a recupera. | Inventário condicional; maintainer. | V-021-01 |
| IR-021-02 | Relação material vira texto com setas. | Revisor não decide boundary/falha/rollback só pela página. | Fixture por domínio; review lead. | V-021-02/03 |
| IR-021-03 | Pass determinístico é vendido como aprovação. | Baseline sem sete pareceres. | Gate humano separado. | V-021-04 |
| IR-021-04 | Hook semântico vira checklist de mocks ou selo automático. | Mesmo resultado para corpus materialmente diferente, ou aprovação sem razão/locator. | Prompt corpus-driven, record citado e avaliador distinto. | V-021-02/V-021-04 |
