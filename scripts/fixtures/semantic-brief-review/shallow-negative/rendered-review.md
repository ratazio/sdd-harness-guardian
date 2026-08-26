# Post-render review — shallow-negative

**Reviewer:** independent calibration reviewer

| Lens | Judgment | Source/example | Finding or recovery action |
|---|---|---|---|
| Product | `superficial` | `spec.md` Outcome; header | **Source:** `spec.md` Risk and decision. **Lost fact:** cross-tenant exposure is the reason to hold the release. **Recovery action:** render the risk and hold condition in the decision snapshot. |
| Architecture/operations | `not_applicable` | No architecture source exists in this deliberately small negative. | Justified N/A: the required finding is decision-loss, not invented architecture. |
| Delivery | `absent` | `validation-plan.md`; Validation and Decision | **Source:** `validation-plan.md` and `decision-log.md` D-N1. **Lost fact:** two-tenant oracle, evidence destination, owner, hold action and incident notification vanished. **Recovery action:** render the oracle/evidence and explicit keep-off contingency. |

**Decision impossible from the brief:** whether a failed probe requires holding
the flag and paging incident response. Formal headings and provenance exist, but
the material release decision is not recoverable.
