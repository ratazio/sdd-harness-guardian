# Post-render review — software-release

**Review ID:** `calibration-release-001`  
**Reviewer:** independent calibration reviewer  
**Independence:** reviewer is not source author or builder.  
**Request locator:** `spec.md#Outcome` (fixture digest: `release-request-v1`)  
**Canonical source locators:** `spec.md`, `plan.md`, `validation-plan.md`, `decision-log.md`  
**Rendered HTML locator:** `stakeholder-brief.html` (fixture digest: `release-render-v1`)

| Lens | Reviewer ID | Independence declaration |
|---|---|---|
| Architect | `calibration-architect` | distinct from fixture source author and builder |
| System designer | `calibration-system-designer` | distinct from fixture source author and builder |
| Executive | `calibration-executive` | distinct from fixture source author and builder |
| General stakeholder | `calibration-general-stakeholder` | distinct from fixture source author and builder |
| Delivery manager | `calibration-delivery-manager` | distinct from fixture source author and builder |

| Lens | Materiality | Judgment | Source/example | Finding or recovery action |
|---|---|---|---|---|
| Architect | material | APPROVE | **Source:** `plan.md`; Architecture and trust | Session boundary, filter chain and flag rollback remain visible. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| System designer | material | APPROVE | **Source:** `plan.md`; Architecture | The accessible From/responsibility/To relationship table makes direction, owner and tenant boundary recoverable; it is not prose with typographic arrows. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| Executive | material | APPROVE | **Source:** `decision-log.md` | Enable/hold trade-off, owner and release consequence are visible. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| General stakeholder | material | APPROVE | **Source:** `spec.md` Outcome | Beneficiary, outcome and release boundary are visible without jargon. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |
| Delivery manager | material | APPROVE | **Source:** `validation-plan.md`; Proof and Decision | Owner, two-tenant oracle, evidence destination and next step remain visible. **Finding ID:** none. **Recovery action:** none. **Re-review:** not required. |

**Decision impossible from the brief:** none material; the release operator can decide enable versus hold without opening Markdown.
