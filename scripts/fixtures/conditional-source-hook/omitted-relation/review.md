# Conditional Source Review

**Review ID:** CSR-revise-001
**Reviewer identity:** independent-reviewer-revise
**Request locator and digest:** `request.md#Shift handoff request` · `sha256:db7e877dd7c892f12d2604a8acc9fd6d2cfb6c985419132d5b1fd2eae4b7dcd8`
**Candidate HTML locator and digest:** `stakeholder-brief.html#summary` · `sha256:54ebd99047faeeae61f65d4fd977bdcdbefb526683f0cf531f7981fb75bad4de`

## Corpus manifest

| Path | Scope / locator | SHA-256 |
|---|---|---|
| `request.md` | `#Shift handoff request` | `sha256:db7e877dd7c892f12d2604a8acc9fd6d2cfb6c985419132d5b1fd2eae4b7dcd8` |
| `plan.md` | `#Reconciliation` | `sha256:6c2993293f13852dddc6f1aeb23788367bb88f91cba91a51cf54544cdde4ae24` |
| `stakeholder-brief.html` | `#summary` | `sha256:54ebd99047faeeae61f65d4fd977bdcdbefb526683f0cf531f7981fb75bad4de` |

**Decision still impossible from HTML:** whether the supervisor may start a shift when the reconciliation oracle fails.
**Finding:** Source: `plan.md#Reconciliation`; Candidate: `stakeholder-brief.html#summary`; Impact: the supervisor cannot decide hold versus start; Repair: project the oracle, hold owner, notification, and recovery into the brief, rerender, then have the operations reviewer re-review.
**N/A dispositions:** API diagram is N/A because `plan.md#Reconciliation` defines an operating handoff rather than a software interface.
**Verdict:** REVISE — the material operating decision is omitted.
