# Technical plan — SPEC 024

## Strategy

1. Construir referência isolada M-005 que transforma fatos existentes em
   visuais nativos SVG/HTML; HTML não recebe fatos de imagem gerada.
2. Renderizar as rotas completas e registrar PNG/PDF reais da Arquitetura.
3. Pedir revisão a identidade distinta com pedido, `design.md`, M-023-B e
   captura como entradas — nunca apenas o código.
4. Somente após T-001 APPROVE extrair contrato/checagem reutilizável sem impor
   SVG decorativo a caso sem arquitetura material.

## M-005 composition map

| Elemento derivado | Fato/limite | Fonte |
|---|---|---|
| Macro-topologia | API parceira → FastAPI/estado/fila → modelo local → política/revisão → API destino; MySQL só por API. | `testes/mock-tests/05-local-ai-exam-scoring.md` |
| Zoom | minimização/pseudônimo, chamada local, schema/faixa/confiança, bloqueio humano, outbox/retry. | M-005 limites/contratos. |
| Escala | cinco superfícies declaradas no fluxo; contagem de superfícies, não de arquivos/linhas. | composição marcada. |
| Assurance | contratos/invariantes vs qualidade/viés/explicabilidade. | M-005 separa determinístico/probabilístico. |
| N/A frontend | pedido declara serviço/API; não define frontend. | ausência material M-005. |

## Design implementation

- tokens: navy `#0B004A`, violet `#4C30A5`, lavender `#C1BFFA`, canvas
  `#EDECF5`, superfície branca;
- `Plus Jakarta Sans, Segoe UI, Arial, sans-serif`, sem font remote;
- logo Pearson local em navy; sem avatar/login;
- SVG com `<title>`, `<desc>`, rótulos e legenda; texto+forma além de cor;
- preservar impressão, no-script, reduced motion e 320px.

## Promotion guard

O exemplo não promove template nem T-004. T-002 só extrai contrato depois de
T-001 APPROVE sobre o render real.
