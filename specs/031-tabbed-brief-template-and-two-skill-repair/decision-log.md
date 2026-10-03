# Decision Log — 031

Registros de planejamento e execução. A autorização humana expressa é D-010;
conclusão de um brief não constitui autorização de produto.

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-10-02 | accepted | Tratar MD existentes como corretos/read-only; focar o trabalho no HTML. | Pedido direto do owner nesta conversa. | Reabrir autoria/corrigir fixtures, rejeitado por ampliação de escopo. | Owner | none |
| D-002 | 2026-10-02 | accepted | Entregar planejamento MD/YAML sem HTML031 e aguardar OK posterior antes de desenvolvimento. | Owner dispensou HTML desta spec explicitamente. | Gerar HTML pelo pipeline reconhecidamente insuficiente, rejeitado. | Owner | none |
| D-003 | 2026-10-02 | accepted | Nova autoria agêntica sobre template substitui a proposta draft de transposição literal da 030. | Direção explícita desta conversa; preservar 030 como histórico. | Continuar literal/modelo obrigatório, rejeitado. | Owner / registro por Codex | 030 proposta draft |
| D-004 | 2026-10-02 | accepted | A compõe; B distinto executa conteúdo e visual sequencialmente, ambas high/xhigh; corrige e relata, sem terceira validação/reaprovação. | Owner pede mesmo agente reparando na própria skill. B será papel de reparo, não evaluator das edições. | Reviews devolutivos e loop de aprovação, rejeitado. | Owner | Mandato proposto do brief 2 para novo caminho 3 |
| D-005 | 2026-10-02 | accepted | Reaproveitar compositor e duas skills existentes; descriptions/mandatos ajustados no bundle em T-002/T-003. | Evidências aprovadas T-002/T-003. | Instalar skills globais/duplicar caminhos, descartado no MVP. | Guardian maintainers / evaluator root | none |
| D-006 | 2026-10-02 | accepted | Checks aceitam a implementação do bundle uma vez; não entram como terceira etapa por brief. | Contrato/integração aceitos T-001/T-004; aceitação dos oito casos em T-005. | Remover evidence/evaluation de tasks, fora do pedido. | Guardian maintainers / evaluator root | none |
| D-007 | 2026-10-02 | accepted | Snapshot dos paths locais antes da implementação; rollback só nesses paths, pois HEAD não contém a 029. | Snapshot pré-031 registrado em D-010; R-029-001 preservado. | Restaurar HEAD em massa, rejeitado. | Guardian maintainers | none |
| D-008 | 2026-10-02 | accepted | Contrato 3: template único inline com oito abas, mesma identidade; históricos 1/2 preservados, legado mantido. | T-001/T-002/T-004 aceitas, leitura histórica e hashes preservados. | Alterar sem versão/remover legado, rejeitado. | Guardian maintainers / evaluator root | none |

## Scope and governance disposition

A escolha do owner de correção sem reaprovação é normativa para o novo
processo e será implementada como papel reparador, com skills que editam.
Não se chamará isso de avaliação independente das próprias edições.

As regras atuais que proíbem reviewer editar e exigem review pré-render
serão adaptadas para composição do contrato 3; não podem permanecer
obrigatórias por baixo do fluxo. A adaptação foi implementada e aceita em
T-001..004; aceitação dos oito casos segue em T-005.

Avaliação independente das tasks do bundle/produto, evidence packs,
autorização humana e veracidade do estado permanecem. A conclusão do HTML
pode ser completed, completed_with_source_limitations ou incomplete,
conforme saída real das skills; nenhuma dessas disposições autoriza produto.

## D-009 — Revisão independente do planejamento

**Status:** accepted — approve do planejamento em 2026-10-02
**Reviewer:** /root/review_spec031 — agente independente da autoria, esforço high
**Scope:** spec, impact, plan, validation, tasks, decisões e dispensa HTML031
**Outcome/Spec/Plan/Validation Ready:** yes; nenhum bloqueador material
**Evidence:** evidence/planning-review.md
**Non-blocking suggestions:** prova explícita das identidades em V-012 e
entrypoint spec-review em impact-map/T-001; incorporadas sem mudança de escopo.
**Human Visibility Ready:** N/A pela dispensa explícita D-002; nenhum gate de
renderização concedido. Tasks Ready permanece false.
**Execution approval:** não concedida; owner dará OK em próximo turno.

## D-010 — Autorização de execução integral

**Date:** 2026-10-02
**Status:** accepted
**Owner:** owner do bundle
**Evidence:** pedido direto: "Perfeito pode iniciar a execução na íntegra."
**Decision:** executar T-001..T-005 da SPEC 031; preservar a dispensa de HTML031 de D-002 e fontes mockadas imutáveis.
**Checkpoint:** testes/mock-runs/20261002-spec031-baseline/snapshot.json, snapshot dos bytes locais antes da implementação; sem reset/stash/clean.

## D-011 — Seleção de modelos e esforço

**Status:** accepted, 2026-10-02. Owner orienta não seguir recomendações antigas de modelo da skill Spec Execution nem tentar Terra. Orquestrador escolhe gpt-6.1-sol/high para mudanças acopladas de contrato, UI, habilidades e compatibilidade; B usa high efetivo obrigatório pela spec. Nenhum modelo antigo foi chamado.

## D-012 — Aceite do incremento T-001

**Status:** accepted, 2026-10-02. Evaluator /root distinto do builder /root/contract031 aprova incremento normativo em evidence/T-001.md. Transição needs_evaluation → approved → done; T-002 inicia. Dois regressores textuais antigos e proof runtime seguem pendentes de T-003/T-004/T-005, obrigatórios antes do aceite final.

## D-013 — Aceite T-002 e paralelismo de implementação

**Status:** accepted, 2026-10-02. Evaluator /root aprova T-002 em
evidence/T-002.md; fontes e interfaces HTML/brief_repair estão estáveis.
T-003 inicia com /root/presentation031; T-004 pode implementar com
/root/integration031 em paralelo às skills, após T-001/T-002 done.
Aceite final de T-004 continua condicionado a T-003 done e regressão completa.
É ajuste de sequência autorizado pela execução integral e autonomia de
orquestração do owner; não remove requisito, avaliação nem validação.
T-005 permanece após T-001..004 done. Ambos builders têm /root como
evaluator distinto; B do ensaio será /root/contract031 high efetivo,
distinto de A e mantendo identidade nas duas skills.

## D-014 — Aceite das skills e da integração

**Status:** accepted, 2026-10-02. /root, evaluator distinto dos builders,
aprova T-003 e depois T-004 nos respectivos evidence packs; ambas done.
O suplemento do template T-002 foi aceito pelas provas do ensaio: abertura
do próprio details e componentes/cobertura adaptativos. Não houve edição
da implementação pelo evaluator. A interface mecânica nativa operada por
root sob solicitação de B não emitiu julgamento semântico adicional; B
interpretou imagens e editou HTML, com high efetivo em ambos os mandatos.
O teste medium é somente metadata negativo; nenhum executor medium usado.
T-005 inicia agora nos oito pacotes copiados/hash: autoria A presentation031,
reparos B contract031 e aceite único da implementação por root. MD
read-only; YAML somente campos operacionais de brief, sem gates de produto.

## D-015 — Paralelismo entre casos no laboratório T-005

**Status:** accepted, 2026-10-02. Orquestrador /root usa a autonomia expressa
do owner em D-011 para distribuir casos, preservando A distinto de B e o
mesmo B/high nas duas skills de cada HTML. Após liberação explícita de
contract031 e confirmação dos hashes A intactos, repair_offline031 assume
exclusivamente M003/M004, com dispatch nativo gpt-6.1-sol/high/fork:none.
Contract031 mantém M001/M002/M005/M006/M007/M008. Root mantém a interface
mecânica de browser e o aceite único da implementação; nenhuma terceira
skill, etapa normal ou aprovação própria foi introduzida. Fontes, autoridade,
ordem conteúdo → visual → relato e todos os aceites permanecem os mesmos.

## D-016 — Aceite e encerramento integral da SPEC031

**Status:** accepted, 2026-10-02. **Evaluator:** /root, distinto dos builders
e editores de código/skills/HTML. Aprova T-005/evidence/T-005.md após relatos
B finais, leitura material dos oito domínios, inspeção de SVG/experiência e
confirmação independente de integridade. AC-001..017 satisfeitos; transição
needs_evaluation → approved → done. T-001..005 e suas evidências aprovadas;
status complete, current_phase validation_done, current_task null.

**Provas:** 256 seleções nativas, 128 imagens primárias e recapturas
interpretadas por B; root-final-integrity.json sem erros (23 históricos,
72 originais, 64 MD copiados e campos de produto dos oito YAML intactos);
oito PASS mecânicos de contrato 3, sem concessão de autoridade. Regressão
aceita T-004: 319 checks, 89 pytest, 27 standalones. Produção não mudou em
T-005. Os ajustes pontuais de targets/BC-005 foram feitos somente pelo B
responsável; texto, CSS, JS, SVG e IDs dos seis patches de provenance são
iguais aos preimages. Esta aceitação não cria terceira etapa de brief.

**Limites:** fontes e ambientes incompletos continuam explícitos, métricas
de custo/tempo não medidas; nenhum produto mockado executado. Sem HTML031
por D-002, brief_phase not_rendered e gates de brief false preservados.
Working tree preexistente preservada; nenhuma instalação global, remoção
de legado, operação destrutiva, commit ou push. Modelo das delegações:
gpt-6.1-sol/high nativo, sem Terra ou executor medium.

## D-017 — Publicação Git autorizada pelo owner

**Status:** accepted, 2026-10-02. O owner solicita diretamente: "primeiro,
você deve já comitar e dar push no que você fez". Autoriza a publicação
da implementação aceita; a condição de ausência de commit/push em D-016
descreve aquele encerramento, sem bloquear esta instrução posterior.

Publicar em origin/main o conjunto canônico coerente: base SPEC029 ainda
local e necessária aos leitores/validators legados, draft 030 substituído
e SPEC031 implementada/aceita. Não incluir tmp nem forçar os laboratórios
ignorados. Conferir o diff staged e a coincidência do HEAD remoto após o
push. Nenhum gate, evidência de aceite ou dispensa de HTML031 é alterado.

A explicação de custo será qualitativa: não há contagem de tokens por fase.
Separar implementação/migração única, testes automáticos e revisão visual
dos oito casos; não converter tempos de log em tokens ou economia medida.
