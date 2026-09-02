# Corpus semantic composition review

**Review ID:** CSR-T002-reservoir-positive
**Composer identity:** spec021_t002_builder
**Reviewer identity:** reservoir-operations-reviewer
**Request locator and digest:** `request.md#Reservoir recovery request` · `sha256:33f937b0bf0197fd68fd574b3c0593ea949310a464b4c52bef9d859957f2e422`
**Candidate HTML locator and digest:** `candidate.html#turbidity-recovery` · `sha256:554ac208071395b43d242a1651d55018bbd64d2fbac5eae17dc2b21934f90887`

## Corpus manifest

| Path | Scope / locator | SHA-256 |
|---|---|---|
| `request.md` | `#Reservoir recovery request` | `sha256:33f937b0bf0197fd68fd574b3c0593ea949310a464b4c52bef9d859957f2e422` |
| `operations.md` | `#Turbidity recovery procedure` | `sha256:09ccf413a0a5b7b92df94e13cfc5f5911a1f7376c31c6dbad2cee535255beba7` |
| `candidate.html` | `#turbidity-recovery` | `sha256:554ac208071395b43d242a1651d55018bbd64d2fbac5eae17dc2b21934f90887` |
| `stakeholder-brief.html` | `#turbidity-recovery` | `sha256:56687d098f9cd693cc029f9723ac37f42927c4272cd317ee68aec99ab08d4644` |

**Disposition:** Represent this relationship as a recovery progression. The
source defines ordered alarm, hold, confirmation and recovery transitions plus
an unsafe timeout; a boundary table would not express when pumping may resume.

**Decision still impossible from HTML:** none. The control-room supervisor can
decide whether recovery is authorized without reopening Markdown.

**N/A dispositions:** A component trust-boundary view is N/A because
`operations.md#Turbidity recovery procedure` describes operating transitions,
not component ownership across a boundary.

**Verdict:** APPROVE — the source-derived recovery relation is recoverable.
