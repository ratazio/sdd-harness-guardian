# Spec: checkout resilience initiative (T-003 forms fixture)

## Functional requirements

FR-010: checkout must retry a failed payment authorization exactly once before failing the order.

## Architecture

The checkout service calls the payment gateway directly; a retry queue sits between them once this change lands.

## Sequence

Order submit triggers authorization; a timeout triggers exactly one retry before the order is marked failed.

## Impact

Affected surfaces: checkout-service, payment-gateway-client, order-status-webhook.

## Risk

A duplicate charge risk exists if the retry queue is not idempotent; consequence is a double debit, control is an idempotency key, owner is Payments.

## Compliance matrix

PCI-DSS scope: checkout-service handles card data; payment-gateway-client is out of PCI scope after tokenization.
