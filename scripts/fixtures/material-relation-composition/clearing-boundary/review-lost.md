# Corpus semantic composition review

**Review ID:** CSR-T002-clearing-negative
**Composer identity:** spec021_t002_builder
**Reviewer identity:** clearing-architecture-reviewer

## Corpus manifest

| Path | Scope / locator | SHA-256 |
|---|---|---|
| `request.md` | `#Clearing instruction request` | `sha256:fb51b711af5b7b532b10183e71d329ea24243431f450922ab9aeee3ecbe86e0d` |
| `architecture.md` | `#Ledger admission boundary` | `sha256:1916724e0ebaaa0bade93d7ce2a6ea3ca370cef17fbeb31a67fd2fcc2645d954` |
| `candidate-lost.html` | `#summary` | `sha256:16a86926e969d39c80bca7900e9b0ec15c35c3534cc6f52163e110ebf0719581` |

**Decision still impossible from HTML:** whether the order service can write
the regulated ledger directly.

**Finding:** Source: `architecture.md#Ledger admission boundary`; Candidate:
`candidate-lost.html#summary`; lost relation: sole gateway receiver and its
refusal authority; Impact: treasury cannot decide who may admit an instruction;
Repair: recover the boundary handoff from the canonical architecture source,
rerender, then have the clearing architecture reviewer re-review.

**N/A dispositions:** A decorative topology is N/A because it would not state
the approval/refusal authority required by the source.

**Verdict:** REVISE — a material trust-boundary relation was lost.
