# M-002 — API de conciliação de repasses

## Pedido funcional

Criar a SPEC de um serviço backend para conciliar, diariamente, repasses recebidos de três adquirentes de pagamento com pedidos de uma plataforma de cursos. Cada adquirente entrega um arquivo CSV por SFTP e pode reenviar um lote corrigido. O serviço importa os lotes, valida o esquema, normaliza moeda e fuso horário, correlaciona cada linha ao pedido interno e expõe divergências para correção por operadores financeiros.

O serviço deve usar Node.js 22, TypeScript strict, PostgreSQL 16, fila RabbitMQ e uma API REST JSON sob `/api/v1`. A importação é assíncrona, idempotente por adquirente/data/hash do arquivo e deve preservar o arquivo original em armazenamento compatível com S3. Não há UI de consumidor: existe somente API, jobs e uma tela administrativa interna mínima para acompanhar lotes e divergências.

Definir contratos concretos para envio de lote, consulta de status, lista de divergências, resolução manual e reprocessamento. Descrever autenticação de operador, autorização por papel, paginação, erros, idempotency key, webhooks de conclusão e política para lote inválido ou duplicado. O modelo mínimo inclui `SettlementBatch`, `SettlementLine`, `Order`, `ReconciliationMatch`, `Discrepancy` e trilha de auditoria.

## Limites e decisões obrigatórias

- Não chamar bancos ou APIs reais; SFTP, armazenamento e adquirentes são adaptadores simulados em desenvolvimento e testes.
- Tratar valores monetários em centavos, sem `float`; definir timezone canônico e regra de arredondamento.
- Um lote corrigido não apaga o anterior: substitui sua visão operacional e mantém proveniência/auditoria.
- Explicitar política de retry, DLQ, ordenação, duplicidade, falha parcial e recuperação após queda durante processamento.
- Incluir migração, retenção de arquivos, mascaramento de identificadores de cartão e logs sem segredos.

## O que a SPEC e o brief devem demonstrar

O pacote deve decompor contratos, invariantes de conciliação, estados do job, limites de confiança e riscos de dinheiro/dados. O stakeholder brief deve deixar legíveis o fluxo arquivo → fila → conciliação → divergência, a consistência/rollback e uma matriz de decisões e validações. Tasks não devem implementar o produto.
