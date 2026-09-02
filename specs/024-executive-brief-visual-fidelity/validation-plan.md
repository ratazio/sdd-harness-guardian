# Validation plan — SPEC 024

| ID | Claim | Method / oracle | Evidence | Class |
|---|---|---|---|---|
| V-024-01 | Rotas são subpáginas e fallback é legível. | Browser `?view=architecture`, histórico, keyboard; no-script/print. | T-001 PNG/PDF/log. | deterministic |
| V-024-02 | Arquitetura tem diagrama, mapa, unidade e zoom factuais. | DOM SVG/legend/labels + inspeção da captura. | T-001 + review. | mixed |
| V-024-03 | Não há frontend ou MySQL direto inventados. | Busca/DOM + revisão contra M-005. | T-001 log. | deterministic + judgment |
| V-024-04 | Pearson é material, não token solto. | asset/CSS/contrast + comparação renderizada por revisor distinto. | T-001 audit + review. | mixed |
| V-024-05 | Fallback textual não passa por visual estruturado. | Fixture negativa e regression de renderer/validator. | T-002. | deterministic |
| V-024-06 | T-004/históricos continuam intocados. | hash/path diff. | T-003. | deterministic |

## Independent qualitative review

O revisor recebe intenção, fontes, screenshot/PDF e HTML. Deve retornar
APPROVE/REVISE com achados sobre clareza C-level, fidelidade Pearson,
existência/legibilidade dos diagramas, correspondência fonte-visual,
limites/N/A e diferenciação referência/corpus. Não aprova o próprio trabalho.
