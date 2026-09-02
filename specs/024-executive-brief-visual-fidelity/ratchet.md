# Ratchet Log: 024-executive-brief-visual-fidelity

Serious first-time or recurring preventable failures are appended here using
`ratchet-entry.md`. An entry is `implemented` only after its prevention and
regression check are verified.

## Index

| ID | Failure type | Severity | Status | Owner | Regression check |
|---|---|---|---|---|---|
| R-024-001 | Material architecture visual silently degraded to text or decorative graph | high | implemented | Guardian maintainers | `python scripts/test_architecture_visual_contract.py` |

## Entries

## R-024-001 — Material architecture requires structural and rendered proof

**Failure:** a technical candidate was presented as an executive visual example;
its architecture could be textual while the approved direction showed diagrams.
Early guards also allowed loose, empty or partially invalid graph primitives.

**Prevention:** material is explicit; the reusable guard enforces scoped,
connected and named topology/legend/surface/zoom contracts, with regressions
for text-only, empty/disconnected and invalid-endpoint bypasses. Independent
render review checks visibility, fidelity, print and mobile legibility.

**Regression check:** `python scripts/test_architecture_visual_contract.py`.
