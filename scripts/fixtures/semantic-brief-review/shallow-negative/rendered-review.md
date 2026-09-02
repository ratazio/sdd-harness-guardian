# Post-render review — shallow-negative

**Review ID:** `calibration-negative-001`  
**Reviewer:** independent calibration reviewer  
**Independence:** reviewer is not source author or builder.  
**Request locator:** `spec.md#Outcome` (fixture digest: `negative-request-v1`)  
**Canonical source locators:** `spec.md`, `validation-plan.md`, `decision-log.md`  
**Rendered HTML locator:** `stakeholder-brief.html` (fixture digest: `negative-render-v1`)

| Lens | Reviewer ID | Independence declaration |
|---|---|---|
| Architect | `calibration-architect` | distinct from fixture source author and builder |
| System designer | `calibration-system-designer` | distinct from fixture source author and builder |
| Executive | `calibration-executive` | distinct from fixture source author and builder |
| General stakeholder | `calibration-general-stakeholder` | distinct from fixture source author and builder |
| Delivery manager | `calibration-delivery-manager` | distinct from fixture source author and builder |

This page is deliberately **structurally valid** but decision-poor. The review therefore records a qualitative **REVISE**, not a parser failure.

| Lens | Materiality | Judgment | Source/example | Finding or recovery action |
|---|---|---|---|---|
| Architect | material | `insufficient` / REVISE | **Source:** `spec.md` Risk and decision | **Finding ID:** N-ARC-01. **Lost fact:** cross-tenant boundary and hold condition are invisible. **Recovery action:** project boundary, failure and hold owner from canonical plan. **Re-review:** Architect after rerender. |
| System designer | material | `insufficient` / REVISE | **Source:** `validation-plan.md` | **Finding ID:** N-DES-01. **Lost fact:** a flat service sentence has no recoverable state or relationship. **Recovery action:** render an accessible relationship or justified N/A. **Re-review:** System designer. |
| Executive | material | `insufficient` / REVISE | **Source:** `decision-log.md#D-N1` | **Finding ID:** N-EXE-01. **Lost fact:** who can accept release risk and its consequence. **Recovery action:** render authority, trade-off and hold decision. **Re-review:** Executive. |
| General stakeholder | material | `insufficient` / REVISE | **Source:** `spec.md` Outcome | **Finding ID:** N-STK-01. **Lost fact:** what changes for affected tenants and what remains excluded. **Recovery action:** render outcome/scope and uncertainty. **Re-review:** General stakeholder. |
| Delivery manager | material | `insufficient` / REVISE | **Source:** `validation-plan.md`; `decision-log.md#D-N1` | **Finding ID:** N-DEL-01. **Lost fact:** two-tenant oracle, evidence destination, owner, hold action and notification. **Recovery action:** render workfront, proof and contingency. **Re-review:** Delivery manager. |

**Decision impossible from the brief:** whether a failed probe requires holding the flag and paging incident response. Formal headings and provenance exist, but the material release decision is not recoverable.
