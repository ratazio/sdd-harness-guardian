# Technical Plan — SPEC 022

## Approach

1. Separar o candidato pré-render do brief renderizado como estados de
   lifecycle, não como duas avaliações semânticas.
2. Declarar uma allowlist/schema fechado: para cada marcador, ID único,
   localização/atributo, fonte canônica, fragmento permitido e valor de
   lifecycle derivável. Marcador desconhecido, duplicado ou tentativa de
   registrar prosa de domínio é recusado.
3. Construir um protocolo de commit recuperável: gerar estado/HTML em arquivos
   temporários, registrar journal de intenção com digests, fazer renames numa
   ordem definida e manter backup do target/estado. A próxima execução detecta
   journal incompleto e restaura o par anterior ou conclui o par validado antes
   de expor qualquer HTML. Artefato histórico existente requer refresh explícito
   e nunca é sobrescrito silenciosamente.
4. Manter revisão humana separada: pre-render aprova a composição; pós-render
   decide suficiência da página atual. O código não infere materialidade.
5. Reproduzir a SPEC 021 em nova tentativa e exigir cinco reviews distintas.

## Bootstrap estritamente limitado

T-001 é a unidade atômica que implementa, e não apenas descreve, o contrato
mínimo acima. Isso é necessário porque a falha do promotor impede que esta
própria SPEC alcance o brief renderizado que normalmente precede tasks prontas.
A autorização explícita do usuário para executar a SPEC 022 só alcança esse
recorte: schema fechado, sincronização lifecycle-only, transação recuperável e
testes. T-001 continua bloqueada até o pacote-fonte receber revisão independente
e só pode ser concluída com evidence e APPROVE distintos do builder. Nenhuma
alteração de prosa de domínio, task posterior ou baseline recebe essa exceção.

| ID | Decision | Consequence |
|---|---|---|
| D-022-01 | Lifecycle é dado canônico sincronizável, não prosa livre. | Schema/allowlist fechado torna o escopo estreito e auditável. |
| D-022-02 | O commit usa temp, journal, backup e recuperação antes de expor o target. | Falha não deixa par HTML/estado contraditório apresentável. |
| D-022-03 | O post-render review é independente do review de composição. | Nenhum APPROVE pré-render libera Tasks Ready. |
| D-022-04 | Determinismo liga bytes/estado; humano decide significado. | Sem score, detector de domínio ou taxonomy. |
| D-022-05 | O bootstrap limita-se a T-001, que contém a implementação mínima inteira. | Evita exceção em cadeia; T-002–T-004 continuam no fluxo normal após o promotor poder renderizar esta SPEC. |

## Modelo de transação e recuperação

Este é um modelo operacional do par, não uma nova taxonomia de qualidade. O
`journal` durável contém os digests pretendidos do novo HTML e do novo
`run-state.yaml`, os digests/existência do par anterior e os dois nomes
temporários de nonce comum. Enquanto há journal, nenhum estado intermediário é
apresentável como brief.

| Estado observável na retomada | Par/journal esperado | Decisão da recuperação | Exposição |
|---|---|---|---|
| Estável anterior | HTML e estado anteriores; sem journal. | Não há promoção pendente. | O par anterior pode continuar visível. |
| Intenção durável | Temps completos e journal com digests do novo e metadados do anterior; backups e renames podem estar parciais. | Não inferir sucesso pela ordem atingida. Comparar os dois destinos aos digests pretendidos. | Bloqueada enquanto o journal existir. |
| Novo par completo | HTML **e** estado batem exatamente com os dois digests de intenção. | Concluir: remover journal, backups e temps. | Liberada somente depois dessa limpeza. |
| Par incompleto | Pelo menos um destino não bate com a intenção. | Restaurar cada membro anterior pelo backup; se ele não existia, removê-lo. Se um backup indispensável faltar e o destino também não corresponder ao digest anterior, recusar recuperação automática. | Bloqueada até restauração íntegra ou intervenção manual. |
| Journal/temps inseguros | Schema, nomes, nonce comum ou metadados não passam validação. | Recusar sem apagar artefatos suspeitos; exigir recuperação manual. | Bloqueada. |

A promoção escreve temps, grava o journal, move HTML anterior para backup,
move estado anterior para backup, instala **primeiro o novo estado** e então o
novo HTML; só depois limpa journal/backups. A retomada roda antes de qualquer
nova promoção. Portanto, o único ponto de exposição do novo brief é o par
completo, com os dois digests confirmados e sem journal pendente.

**Rollback/recovery:** cada ponto de commit injetável deixa journal e backup
suficientes para aplicar a tabela acima. Mudanças são aditivas para novas
promoções; artefatos históricos não são alterados sem refresh explícito.
