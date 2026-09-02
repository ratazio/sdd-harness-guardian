# Ratchet — SPEC 028

## R-028-001 — Nenhum artefato pode contornar o lifecycle oficial

**Baseline observado:** no R2, o M003 declarava `not_rendered` e `REVISE`, mas
possuía skeleton/candidate; a revisão de Human Visibility também falhava por
ausência de final e gate não pronto.

**Novo mínimo proposto:** candidate, final e Human Visibility só avançam quando
run-state, decision log, proveniência/digests e review oficial concordam. Um
PASS de integridade ou de tokens não equivale a aprovação qualitativa.

**Sinal de regressão:** fixture `REVISE` consegue deixar arquivo promovível,
review final não contém URL/digest/revisor/decisão, ou um mock relata Human
Visibility sem final revisado.

**Dono:** Guardian maintainers.  
**Validação:** V-001, V-002, V-005, V-007.
