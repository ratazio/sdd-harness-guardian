# Technical Plan: <initiative>

**Status:** draft | plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:**  
**Last updated:**

## 1. Technical approach

Describe sequence, boundaries and why this is the smallest safe approach.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | | | | |

## 3. Size and proportionality

**Initiative size:** S | M | L.  
**Why:** one sentence on the affected boundaries and risk; this is not an effort estimate.  
**Smaller option considered:** state the smaller approach and why it is sufficient or insufficient.  
**Complexity deliberately excluded:** state infrastructure, process or scope not justified by the outcome.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** unknown | A1-local | A2-elevated | A3-critical-local-policy  
**Rationale and trigger evidence:**  
**A2/A3 source links/headings (or A1 N/A reason):**  
**Reapproval trigger:** profile change, envelope breach, new trust/data/public
boundary, or an assurance failure/waiver.

### Architecture scope/size profile (separate from assurance profile)

State the architecture scope/size profile (`localized/S`, `M`, `L`, `high` or `unknown`) and
complete every applicable row before Plan Ready. An omission needs a source-backed
reason. Missing material information becomes a named unknown with owner and
resolution path; block Plan Ready or create a bounded discovery task rather
than inventing a diagram or contract.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | | | |
| Components/responsibilities | | | |
| Interfaces/events/contracts | | | |
| Data ownership/lifecycle | | | |
| Security/trust boundaries | | | |
| Critical runtime flows | | | |
| Failure behavior | | | |
| NFRs | | | |
| Compatibility/migration | | | |
| Observability | | | |
| Rollout/rollback | | | |
| Alternatives/trade-offs | | | |
| Unknowns | | | |

### Current → target → delta and complexity envelope

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Architecture/method | | | | |
| Modules/classes/APIs/data/contracts | | | | |
| Process/tooling | | | | |

Use bounded counts or `not_applicable` with reason when meaningful. This is a
decision envelope, not a speculative implementation inventory.

| Architecture scope/size profile | Minimum architecture decision surface |
|---|---|
| localized/S | Concise text or one boundary view only when it improves a decision. |
| M | Context, changed components/contracts and applicable critical flow. |
| L, high or unknown | Applicable context, responsibilities, data/trust and success/failure/rollback views; source-backed omissions only. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | | | | |

## 6. Contracts, data and compatibility

- API/events:
- Database/storage:
- External systems:
- Compatibility/migration:

## 7. Security, privacy and permissions

- Authentication/authorization:
- Secrets/PII:
- Required permission:
- Destructive operations and approvals:

## 8. Rollout, observability and rollback

- Rollout:
- Success/failure signals:
- Rollback trigger:
- Exact rollback/checkpoint:

## 9. Brief coverage composition (v2 when applicable)

Before final rendering, inventory the applicable sources and principal headings
in this existing plan. For each, record source locator, coverage disposition,
rendered target and any required reason. Do not create an embedded JSON index
or coverage sidecar. Core material headings may not be `link_only`.

| Source locator | Coverage (`represented`/`synthesized`/`not_applicable`/`link_only`) | Rendered target | Reason when required |
|---|---|---|---|
| | | | |

Record the author, distinct coverage reviewer, review date, findings status and
the `decision-log.md` row that records the review. The review must precede
`brief_coverage_ready`; a named human reviewer is required if an independent
agent is unavailable.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | | | | yes/no |

## 11. Plan decision

**Plan Ready:** no  
**Reviewer:**  
**Reviewed at:**  
**Conditions/links:**
