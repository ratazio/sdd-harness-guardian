# Handoff — SPEC 028

**From:** Codex  
**Intended recipient:** próximo mantenedor  
**Created at:** 2026-09-02  
**Current phase/status:** `completed` / `completed`  
**Current task/status:** nenhuma; T-001…T-005 `done`  
**Last safe checkpoint:** evidências T-001…T-005 e avaliações independentes registradas.

## 1. Trabalho concluído e aprovado

- T-001 e T-004 consolidaram lifecycle, herança de skeleton e binding de review
  HTTP sem adicionar um gerador de narrativa/diagramas.
- T-002 e T-003 provaram a composição agente com M003 R4 e a superfície HTTP
  local, registrada em `evidence/T-002.md` e `evidence/T-003.md`.
- T-005 executou a matriz M001–M008, com 64/64 rotas verificadas e recuperações
  transparentes; ver `evidence/T-005.md` e o `matrix-evidence.md` da run.

## 2. Trabalho parcial ou não verificado

- Nenhuma task desta iniciativa permanece parcial.
- Nenhum mock recebeu Human Visibility ou Tasks Ready; esse limite é
  intencional e não representa pendência desta SPEC.

## 3. Arquivos relevantes nesta iniciativa

| Arquivo | Estado | Motivo |
|---|---|---|
| `evidence/T-002.md` | approved | M003 source-backed skeleton composition. |
| `evidence/T-003.md` | approved | servidor HTTP e auditoria 64/64. |
| `evidence/T-005.md` | approved | matriz heterogênea e limites. |
| `decision-log.md` | accepted | D-011: autoria de toda a superfície editorial. |

## 4. Validações e evidências

| Check | Resultado | Evidência |
|---|---|---|
| 10 contratos/regressões de composition/render | PASS | `evidence/T-002.md`, `T-003.md`, `T-005.md` |
| Candidate inheritance M001–M008 | 8/8 PASS | `evidence/T-005.md` |
| Navegador local por rota | 64/64 PASS | `evidence/T-003.md` |
| Bundle validation | PASS, 315 checks | `evidence/T-005.md` |

## 5. Decisões e aprovações

Ler `decision-log.md`. D-001…D-011 estão aceitas. A aprovação das tasks é
interna a esta iniciativa e não muda os gates dos mocks.

## 6. Bloqueios, incógnitas e riscos

- Não transformar os controles em Markdown→HTML ou um score de design.
- Não tratar candidate/herança ou auditoria de matriz como Human Visibility.
- Não editar a run R2 histórica para fazer a reprodução parecer resolvida.

## 7. Próximo passo seguro

Para uma nova SPEC consumidora, usar fontes canônicas → construction review →
skeleton local → composição agente → inheritance/render → revisão HTTP. Um
`REVISE` recuperável retorna ao compositor no mesmo run; falta material vira
discovery explícito. Aprovação de entrega continua uma decisão per-initiative.

## 8. Não fazer

- Não criar Markdown→HTML, gerador de diagramas, score de beleza ou exceção
  específica para M003.
- Não tratar candidate, preview ou check estático como Human Visibility, nem
  usar um review pendente para suprimir o HTML final.
