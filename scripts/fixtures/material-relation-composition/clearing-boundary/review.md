# Corpus semantic composition review

**Review ID:** CSR-T002-clearing-positive
**Composer identity:** spec021_t002_builder
**Reviewer identity:** clearing-architecture-reviewer
**Request locator and digest:** `request.md#Clearing instruction request` · `sha256:fb51b711af5b7b532b10183e71d329ea24243431f450922ab9aeee3ecbe86e0d`
**Candidate HTML locator and digest:** `candidate.html#ledger-boundary` · `sha256:ba4ae82744c6f20a900646bf27a57ac5520bec9a711c85d1caa951354a171356`

## Corpus manifest

| Path | Scope / locator | SHA-256 |
|---|---|---|
| `request.md` | `#Clearing instruction request` | `sha256:fb51b711af5b7b532b10183e71d329ea24243431f450922ab9aeee3ecbe86e0d` |
| `architecture.md` | `#Ledger admission boundary` | `sha256:1916724e0ebaaa0bade93d7ce2a6ea3ca370cef17fbeb31a67fd2fcc2645d954` |
| `candidate.html` | `#ledger-boundary` | `sha256:ba4ae82744c6f20a900646bf27a57ac5520bec9a711c85d1caa951354a171356` |
| `stakeholder-brief.html` | `#ledger-boundary` | `sha256:96dea27f009867408dee7f835472d039a04ab71af37e3b0630cac8131c178983` |

**Disposition:** Represent the admission relationship as a boundary handoff
table. This follows the source's sender, sole receiver, required payload,
refusal, owner and proof; a state progression would hide the regulated trust
boundary.

**Decision still impossible from HTML:** none. The treasury lead can decide
whether ledger admission is allowed without reopening Markdown.

**N/A dispositions:** A recovery-state diagram is N/A because
`architecture.md#Ledger admission boundary` defines a one-way authority
boundary, not lifecycle transitions.

**Verdict:** APPROVE — the source-derived boundary relation is recoverable.
