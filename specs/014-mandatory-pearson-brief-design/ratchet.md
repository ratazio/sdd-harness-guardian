# Ratchet Log: 014-mandatory-pearson-brief-design

Serious first-time or recurring preventable failures are appended here using
`ratchet-entry.md`. An entry is `implemented` only after its prevention and
regression check are verified.

## Index

| ID | Failure type | Severity | Status | Owner | Regression check |
|---|---|---|---|---|---|
| R-001 | Consumer-local asset absent after scaffold | high | implemented | platform-engineering | fresh-consumer smoke + Playwright same-origin logo request |

## Entries

### R-001 — provision the official consumer-local logo

**Failure:** a fresh consumer brief referenced the official local logo but the scaffold did not copy the asset, leaving the relative URL unresolved.

**Prevention:** `new_initiative.py` hash-preflights source and destination, provisions the official PNG only when absent, and refuses divergent bytes before target creation.

**Regression proof:** fresh feature/bugfix scaffold proves SHA-256 and 175 × 53 dimensions; divergent destination remains untouched; real consumer Playwright observes same-origin HTTP 200. Independently reproduced in D-019.
