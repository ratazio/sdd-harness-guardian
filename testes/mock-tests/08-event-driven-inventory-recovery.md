# M-008 — Recuperação de estoque orientada a eventos

## Pedido funcional

Criar a SPEC de um serviço que consolida eventos de estoque de centros de distribuição e lojas. Eventos `received`, `reserved`, `shipped`, `returned` e `adjusted` chegam por Kafka a partir de sistemas existentes, podem estar duplicados ou fora de ordem e precisam formar uma visão consultável de saldo por SKU/local. Quando a reconciliação detecta saldo negativo ou lacuna de sequência, abre um incidente para o time operacional e permite reprocessar uma partição/intervalo de eventos.

Stack fixa: Java 21, Spring Boot, Kafka, PostgreSQL, Redis para leitura em cache, API REST somente de consulta/administração e OpenTelemetry. Não criar interface de e-commerce, ERP, app de inventário manual ou integração com fornecedores novos.

## Limites e decisões obrigatórias

- Definir contrato de evento, chave de idempotência, versão, ordenação por SKU/local, retenção, esquema compatível e estratégia para evento atrasado/venenoso.
- Declarar o modelo de consistência eventual, projeção de saldo, watermark, SLA de atualização e como o operador distingue dado atrasado de erro real.
- Reprocessamento deve ser auditável, limitado e não pode corromper a projeção ativa; definir rollback/snapshot e autorização operacional.
- Especificar métricas, traces e alertas que permitam detectar lag, DLQ, divergência e falha de projeção sem vazar dados comerciais sensíveis.
- Incluir testes de contrato, propriedades/invariantes, integração Kafka/PostgreSQL e cenários de caos/recovery em ambiente isolado.

## O que a SPEC e o brief devem demonstrar

O brief deve tornar compreensíveis o fluxo de eventos, a origem da verdade, os limites de consistência e os controles de recuperação. Não deve fingir transação distribuída nem prometer saldo em tempo real sem uma decisão explícita.
