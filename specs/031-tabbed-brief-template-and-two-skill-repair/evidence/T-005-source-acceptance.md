# T-005 — leitura material dos oito casos

**Evaluator:** /root, distinto de A e dos reparadores B. **Data:** 2026-10-02.
Esta leitura integra o aceite único da implementação SPEC031. Não cria
skill, reviewer, aprovação ou etapa obrigatória depois de B em futuras
gerações. A decisão formal e os digests finais estão em T-005.md e no
manifesto root-final-integrity.json do laboratório.

Foram usadas as fontes congeladas e a matriz de validation-plan.md §3,
com inputs read-only de acceptance031 (M001..004/M007/M008) e integration031
(M005/M006), depois do término das duas skills e dos relatos B. Root
examinou os relatos, alvos materiais, SVGs finais e registros de operação.
Nenhuma fonte foi corrigida para favorecer o resultado.

| Caso | Fatos materiais recuperáveis | Destinos reais no HTML | Limites preservados |
|---|---|---|---|
| M001 blog | Draft/publicação, RBAC/sessão/cookies, User/Session/Post e FKs/índices, cinco APIs com envelopes/status/conflito/idempotência, projeção pública restrita, recuperação e provas por task. | scope-requirements; architecture-flow/contracts; impact; execution; validation; evolution-source-state. | Paths atuais/hosting/tráfego ausentes; p95 local planejado não prova produção; divergência MD false/pending versus YAML true/approve não adjudicada. |
| M002 conciliação | Três adquirentes, API preserva original em S3 antes RabbitMQ, worker/checkpoint/PG, centavos/half-up/ordem, lote corrigido conserva auditoria, restart sem duplicação, retry/DLQ e webhook terminal. | scope/architecture inclusive migração; architecture-contracts/recovery; impact; execution; validation. | Timezone/política de retenção sem valores inventados; Q001/Q002/D004 conservados; nenhuma reconciliação real executada. |
| M003 mobile offline | Sete estados/transições, Room cifrado separado de token/chave, edição offline versus envio bloqueado por token expirado, multipart/ack, conflito com escolha explícita, remoção conserva rascunho, novo aparelho não reutiliza segredos. | scope-requirements; architecture-contracts/recovery; impact-risks; task-T-001..007-details; proof-V-001..009; evolution-history. | Android10+/48dp/TalkBack e permissões mantidos; localização ativa/30 dias é sandbox; schemas/códigos externos bloqueiam T003/T005; YAML histórico true/revise exposto sem mudar gates. |
| M004 multiplataforma | Domínio sem runtime, adaptadores mobile/web, grafo web isolado de módulos nativos, GraphQL existente, cache stale/timestamp, pendência com base revision/key até confirmação, conflito conserva intenção sem overwrite/retry automático. | architecture-flow/contracts/critical-flows; execution/details; proof-V-001..007; decision-discoveries; evolution-history. | Donos/bloqueios de conflito/contratos/retention/assistência preservados; V002-C não tem dossiê próprio na fonte e não foi equiparado a V002; CI planejado não é distribuição executada. |
| M005 IA local | Grafo R2 ativo T005..008/V006..013, lote/version/rubrica/idioma validado antes fila, minimização/mapping segregado, modelo local sugere, regra determinística/gate humano decidem, destino somente via API/MySQL, timeout/retry/ambiguidade não publicam, reprocesso conserva auditoria. | architecture-flow/contracts/source-failures; impact; execution; validation; evolution-source-state. | Limiar U003 pertence Educação+Segurança; acurácia/viés/SLA não medidos; nenhuma arquitetura direta modelo→MySQL ou treino externo inventada. |
| M006 documentos | Quarentena/scan antes parser/modelo, custódia MinIO/hash/versões, proposta local separada de totais determinísticos, job normal versus revisão de exceção, isolamento containers/Redis/Celery/PG, cancel/retry/DLQ sem duplicar, saída HTML/PDF por job. | architecture-flow/contracts/states/source-failures; impact; execution/details; validation; evolution-source-state. | Breakdown já está no R2 e foi recuperado; retenção/recursos/rede/SLA desconhecidos mantidos; sem signing/banco/investimento/posting; ledger anterior versus cinco dossiês R2 é histórico explícito. |
| M007 quiosque | Quinze FR, quatorze AC e V006..020 com oráculos distintos, mapa/texto equivalente, cache versionado/aviso offline, sem resultado separado de impressora sem papel, rota preservada na falha, reset limpa estado, acessibilidade específica. | scope-requirements; architecture-contracts; impact-risks; execution; validation-matrix/proofs; evolution-source-state. | NoJS é informacional, sem prometer busca dinâmica; limiares/viewport/impressora/reset sem valores inventados; V006/AC006 e V020/all verificados em pixels da tabela final inteira. |
| M008 estoque | Cinco famílias de eventos, contrato/versão/chave/ordem, saldo eventual/watermark, delayed separado de poison/erro/DLQ/negativo/gap, replay autorizado/bounded, snapshot ativo/candidato isolado, comparação antes de promover/rollback, Redis atualizável não autoritativo. | architecture-contracts/states/recovery; impact-signals; execution; validation-proofs; decision-discoveries; evolution-source-state. | U003..006 ativos com donos/bloqueios, U001/002 supersedidos; nenhuma garantia exactly-once/realtime/SLA inventada; sinais/redaction são provas planejadas, não certificação de produção. |

Não foram identificadas omissões, contradições ou invenções materiais
remanescentes na matriz de aceite. Não é certificação universal de qualquer
fato ou de futuras gerações; demonstra estes oito domínios e fontes.
Objetivo, beneficiários, transformação/benefício observável, anti-escopo,
responsabilidades, tarefas, validação e autoridade aparecem no HTML.

O aceite localizou alvos coarse de coverage em M001, M002 e M006 que
apontavam apenas parte do fato composto. O B responsável corrigiu somente
essas linhas; inputs read-only confirmaram o fechamento. Na conferência
mecânica final, atributos data-source compostos em seis casos contrariavam
BC-005: múltiplos locators devem usar children/blocos próprios. A correção
pontual de provenance pertence ao mesmo B, preserva conteúdo/visual e
metadados/digests, sem rerun factual ou terceira skill normal.

Lacunas reais das fontes, políticas ausentes e divergência histórica entre
MD e YAML ficaram visíveis. Nenhuma task/gate/approvação do produto foi
adjudicada pela entrega HTML. Evidências planejadas não foram declaradas
executadas. Este evaluator não editou o HTML ou o código que julgou.
