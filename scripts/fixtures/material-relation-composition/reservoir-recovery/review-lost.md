# Corpus semantic composition review

**Review ID:** CSR-T002-reservoir-negative
**Composer identity:** spec021_t002_builder
**Reviewer identity:** reservoir-operations-reviewer

## Corpus manifest

| Path | Scope / locator | SHA-256 |
|---|---|---|
| `request.md` | `#Reservoir recovery request` | `sha256:33f937b0bf0197fd68fd574b3c0593ea949310a464b4c52bef9d859957f2e422` |
| `operations.md` | `#Turbidity recovery procedure` | `sha256:09ccf413a0a5b7b92df94e13cfc5f5911a1f7376c31c6dbad2cee535255beba7` |
| `candidate-lost.html` | `#summary` | `sha256:06c69bde145d615184c5bf973696f0a193fe4f965e362603a6471d4d301b967b` |

**Decision still impossible from HTML:** whether pumping may restart when the
first high-turbidity alarm clears.

**Finding:** Source: `operations.md#Turbidity recovery procedure`; Candidate:
`candidate-lost.html#summary`; lost relation: hold → second-sample confirmation
→ supervisor recovery and timeout escalation; Impact: the supervisor could
restart unsafely; Repair: recover the operation's state progression from the
canonical source, rerender, then have the reservoir operations reviewer re-review.

**N/A dispositions:** A generic pipeline is N/A because it would lose the
source's no-restart-on-timeout safety condition.

**Verdict:** REVISE — a material failure/recovery relation was lost.
