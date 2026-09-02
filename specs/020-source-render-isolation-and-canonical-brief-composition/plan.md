# Plano técnico — SPEC 020

**Status:** in_review · **Profile:** A2 · **Escopo:** M/high

## Abordagem e fluxo

Separar scaffold, promoção e julgamento humano. O scaffold cria fontes; o
promotor aceita apenas candidato revisado/digerido; o mock lab usa raiz por
caso e revisa pedido→fontes→HTML.

```txt
pedido + fontes permitidas ──► candidato com provenance/digest
            │ revisão distinta                 │ policy + lifecycle
            ▼                                  ▼
       registro canônico ───────────────► brief renderizado ─► duas revisões
```

## Decisões

| ID | Decisão | Consequência |
|---|---|---|
| D-020-01 | Nenhum HTML no scaffold. | Elimina casca clicável. |
| D-020-02 | Promoção exige origem, revisão e digest. | Impede troca e mistura após revisão. |
| D-020-03 | Cada bloco tem allowlist/locator/digest. | Detecta origem estrangeira sem score semântico. |
| D-020-04 | Rubrica humana em duas passagens. | Mede autonomia do HTML e perda frente a pedido/fontes. |

## Composição e proporcionalidade

Arquitetura material expõe responsabilidade, relação/direção, dados/contratos,
sucesso/falha, operação e prova; cada dimensão ausente recebe N/A baseado na
fonte. A representação pode ser tabela, fluxo, SVG acessível ou texto
estruturado. Não há quota de abas, cards ou diagramas.

## Sequência, rollback e cobertura

T-001→T-002→T-003→T-004. As mudanças são locais e reversíveis; reverter só com
decisão humana porque reintroduz a falha. A cobertura do brief representa
`spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md` e
`decision-log.md` nos painéis de escopo, arquitetura, impacto, execução,
validação e decisão, com provenance por bloco.
