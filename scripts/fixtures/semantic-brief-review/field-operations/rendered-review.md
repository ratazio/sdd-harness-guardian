# Post-render review — field-operations

**Review ID:** `calibration-operations-001`  
**Reviewer:** independent calibration reviewer  
**Independence:** reviewer is not source author or builder.  
**Request locator:** `spec.md#Outcome` (fixture digest: `operations-request-v1`)  
**Canonical source locators:** `spec.md`, `plan.md`, `validation-plan.md`, `decision-log.md`  
**Rendered HTML locator:** `stakeholder-brief.html` (fixture digest: `operations-render-v1`)

| Lens | Reviewer ID | Independence declaration |
|---|---|---|
| Architect | `calibration-architect` | distinct from fixture source author and builder |
| System designer | `calibration-system-designer` | distinct from fixture source author and builder |
| Executive | `calibration-executive` | distinct from fixture source author and builder |
| General stakeholder | `calibration-general-stakeholder` | distinct from fixture source author and builder |
| Delivery manager | `calibration-delivery-manager` | distinct from fixture source author and builder |

| Lens | Materiality | Judgment | Source/example | Finding or recovery action |
|---|---|---|---|---|
| Architect | not_material — no software boundary is requested | APPROVE | **Source:** `plan.md`; operating flow | A managed workspace boundary, handoff and rollback are visible without inventing APIs. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| System designer | material | APPROVE | **Source:** `plan.md`; operating control | The ordered semantic handoff is a justified alternative: one linear owned procedure, with no material component/trust/failure graph that calls for a diagram. Tabs are not needed for this concise control. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| Executive | material | APPROVE | **Source:** `decision-log.md#D-O1` | Deadline, managed-workspace choice, supervisor authority and fallback are visible. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| General stakeholder | material | APPROVE | **Source:** `spec.md` Outcome | High-risk residents, the expected contact result and time boundary are plain. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| Delivery manager | material | APPROVE | **Source:** `validation-plan.md`; Proof and Decision | Owner, 14:05 reconciliation oracle, evidence and next step are visible. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |

**Decision impossible from the brief:** none material; the supervisor can decide whether the controlled shift may start without opening Markdown.
