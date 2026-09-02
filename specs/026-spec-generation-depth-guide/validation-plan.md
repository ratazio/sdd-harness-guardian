# Plano de validação — SPEC 026

**Status:** draft  
**Spec:** [spec.md](./spec.md) | **Plan:** [plan.md](./plan.md)

## Estratégia

Validação proporcional e majoritariamente por leitura: verificar que o guia é utilizável, que o revisor é independente e que ambos preservam limites de fonte. Não há teste de volume, score ou verificação automática da qualidade semântica.

| ID | AC | Método | Resultado esperado | Evidência |
|---|---|---|---|---|
| V-026-01 | AC-026-01 | Revisão do guia e de seu destino Markdown | Perguntas mínimas, classificação de fonte e artefatos canônicos aparecem uma vez, de forma condicional. | evidence/T-001.md |
| V-026-02 | AC-026-02 | Cenários de leitura: caminho/localizador inequívoco, ausente e contraditório | Só o localizador inequívoco permite inspeção; os demais levam a limite declarado ou descoberta, nunca a busca semântica ou caminho inventado. | evidence/T-001.md |
| V-026-03 | AC-026-03 | Revisão por identidade distinta sobre pedido, SPEC e plano | Saída `PASS` ou `REVISE`; achado `REVISE` contém fonte → perda → decisão → correção. | evidence/T-003.md |
| V-026-04 | AC-026-04 | Dois exemplos curtos de Markdown: M005 e caso sem localizador | M005 recupera relações arquiteturais/executáveis/provas; o segundo declara incerteza sem fabricar estrutura. Não há novo mock, SPEC completa ou HTML. | evidence/T-004.md |
| V-026-05 | AC-026-05 | Inspeção de diff e instruções alteradas | Não há parser, gerador automático de narrativa/HTML, schema de conteúdo ou score introduzidos. | evidence/T-002.md |
| V-026-06 | AC-026-06 | Regeração e revisão independente de M-001, M-004 e M-006, seguida da suíte heterogênea | Fatos materiais desses pedidos chegam a SPEC/impacto/tasks/validação; discoveries ficam restritas aos detalhes realmente ausentes. | evidence/T-005.md |

## Regressão e avaliação humana

| Risco | Check | Oráculo | Falha |
|---|---|---|---|
| Checklist mecânico | Revisor verifica se ausência é justificada e se a narrativa preserva decisão | julgamento humano/agentivo com fontes | `REVISE` |
| Invenção de código | Exercitar caso sem localizador e contraditório | nenhum caminho/fato técnico sem fonte; sem busca para eleger superfície | `REVISE` |
| Complexidade indevida | Inspecionar superfícies e diffs | documentação/papel apenas; sem runtime novo | bloquear T-002/T-003 |
| Reviewer superficial | Exercitar ao menos uma perda deliberada em calibração | achado liga fonte a decisão e correção | `REVISE` |
| Não invenção virar omissão | Comparar pedido rico com cada artefato canônico aplicável | entrega/limite/prova material fornecido não some sob uma discovery | `REVISE` |

## Decisão de validação

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** `spec-depth-reviewer`, [parecer](./evidence/spec-depth-review.md)  
**Sem comandos obrigatórios:** trata-se de mudança de orientação e gate qualitativo; a evidência é revisão rastreável e calibração.
