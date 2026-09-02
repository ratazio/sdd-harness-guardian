# Reproduction — SPEC 024

**Status:** reproduced  
**Observed in:** `testes/mock-runs/20260831-spec023-t004-r1/m005-ai/t004-candidate.html?view=architecture`  
**Environment:** local file in Codex Browser, 2026-08-31  
**Captured by/date:** requester screenshots and delivery orchestrator, 2026-08-31

## Observed behavior

A rota Arquitetura abre como painel interno, mas o conteúdo visível é lista de
componentes, faixa textual e relações em prosa. Não há macro-diagrama conectado,
mapa gráfico de superfícies/escala ou zoom. A aparência é neutra verde/teal do
corpus, não o perfil Pearson.

## Expected behavior

O exemplo apresentado deve corresponder a M-023-B e `design.md`: identidade
Pearson, relações visíveis, legenda, mudança/preservação, escala honesta e zoom
fonte-apoiado.

## Minimal steps

1. Abrir o URL acima com `?view=architecture`.
2. Comparar com `../023-executive-brief-subpages-and-semantic-architecture/evidence/visual-mocks/M-023-B-architecture.png`.
3. Verificar a ausência dos elementos gráficos e a divergência de identidade.

## Baseline evidence

| Artifact/check | Location/result |
|---|---|
| Candidato técnico | `testes/mock-runs/20260831-spec023-t004-r1/m005-ai/t004-candidate.html` |
| Direção visual | `../023-executive-brief-subpages-and-semantic-architecture/evidence/visual-mocks/M-023-B-architecture.png` |
| Autoridade | `.harness/references/pearson-design.md` |

## Regression check

**Validation ID:** V-024-02 / V-024-04  
**Failing condition before fix:** sem SVG conectado/mapa/zoom e perfil neutro.  
**Expected pass:** captura da referência mostra os elementos e revisor confirma a comparação.
