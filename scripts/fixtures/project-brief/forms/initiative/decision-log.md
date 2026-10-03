# Decision log

### D-002 — retry queue is idempotent by construction

The retry queue keys every attempt by order id plus attempt number, so a duplicate publish cannot cause a duplicate charge.
