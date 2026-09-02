# Validation Plan — SPEC 021

**Status:** draft · **Strategy:** integridade determinística e julgamento
independente de sete lentes.

| ID | AC | Method/oracle | Evidence |
|---|---|---|---|
| V-021-01 | AC-021-01 | Fixture de ratchet material projeta gatilho/check/owner; vazio carrega estado/razão. | T-001 |
| V-021-02 | AC-021-02 | Revisor semântico, com corpus completo, aponta relação/decisão omitida em um domínio não codificado e sustenta o REVISE com locator, impacto e reparo. | T-001 |
| V-021-03 | AC-021-03 | Arquiteto/system designer/stakeholder comparam pedido/fontes/HTML de dois domínios; a representação é proporcional e escolhida pelo caso. | T-002 |
| V-021-04 | AC-021-04 | Teste só rejeita identidade, manifesto de entradas declarado pelo revisor, digest ou registro inválido; inspeção independente confirma que não há inferência de materialidade, score, taxonomia de domínio nem aprovação semântica pelo código. | T-003 |
| V-021-05 | AC-021-05 | Em raiz nova, oito consumidores M-001–M-008 guardam digests de request/fonte/HTML e sete pareceres em duas passagens; qualquer REVISE material corrige fontes, rerenderiza e repete os dois passes antes de baseline. | T-004 |

Regressões obrigatórias: `python scripts/test_render_stakeholder_brief.py`,
`python scripts/test_source_render_isolation.py`,
`python scripts/test_validate_human_visibility.py` e
`python scripts/validate_bundle.py`. A camada determinística nunca gradua
prosa, conta elementos visuais, reconhece domínio ou declara aprovação
semântica. O hook de linguagem natural não recebe resposta-modelo: deriva seus
achados do pedido e fontes efetivos, e um avaliador distinto ainda revisa seu
parecer e a evidência.
