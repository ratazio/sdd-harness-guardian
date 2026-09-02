# Validation plan — SPEC 023

| ID | Afirmação / risco | Método e contexto | Oráculo / evidência | Limite honesto |
|---|---|---|---|---|
| V-023-01 | Rotas são subpáginas reais. | Browser automatizado e inspeção da região principal em todas as rotas. | URL/histórico, rota ativa, conteúdo não ativo oculto/inativo e ausência de `scrollIntoView`; capturas por rota. | Estrutura não prova a qualidade da narrativa. |
| V-023-02 | Experiência é acessível e resiliente. | 320/768/1024/1440, 200%, teclado, no-JS, print e reduced motion. | Sequência de foco, `aria-current`, landmarks, screenshots/PDF e fallback visível. | AT real requer revisão humana complementar. |
| V-023-03 | Narrativa é executiva e fonte-apoiada. | Revisor distinto compara pedido, fontes, mapa editorial e HTML em ao menos três domínios. | Registro APPROVE/REVISE com fonte/locator, impacto e reparo. | Nenhum score ou teste lexical decide compreensão. |
| V-023-04 | Arquitetura material é explicável sem fabricação. | Dois casos materiais e um não software/operacional da suíte. | Macro, change map, unidade de escala, zoom ou N/A justificado, todos ligados às fontes. | Não certifica a arquitetura externa ao corpus. |
| V-023-05 | Mudanças e ausências são honestas. | Fixture negativa: contagem sem unidade, zero falso, frontend inferido, detalhe ausente. | Contrato recusa/flaggea o formato; reviewer exige descoberta. | Código não determina o que é material. |
| V-023-06 | Guia Pearson é seguido como sistema. | Inspeção de origem + browser + visual review em mesmas larguras. | Ativo local/hash, tokens/base shell, contraste/foco, screenshots e parecer visual. | A inspeção automática não substitui julgamento de marca. |
| V-023-07 | A intenção visual foi entendida antes do refactor. | Apresentar M-023-A/B/C ao requester. | Decisão D-023-001 ou feedback de revisão anexado ao log. | Mock de imagem não é implementação nem prova de A11y. |
| V-023-08 | Novo fluxo preserva integridade de Guardian. | Raiz nova M-001–M-008 e regressão do bundle. | Digests, provenance/lifecycle, avaliações independentes e `validate_bundle.py`. | PASS não aprova semântica/estética por si só. |

## Evidência futura

Cada tarefa registra seu pacote correspondente em `evidence/T-001.md`,
`evidence/T-002.md`, `evidence/T-003.md` ou `evidence/T-004.md`; screenshots
e imagens geradas podem ser anexadas como contexto, identificadas como não
canônicas e sem alegar que provam decisão humana.
