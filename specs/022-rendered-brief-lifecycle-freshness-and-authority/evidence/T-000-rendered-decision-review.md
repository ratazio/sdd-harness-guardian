# Rendered-decision review — D-022-011

**Artifact reviewed:** `stakeholder-brief.html`  
**SHA-256:** `cbf53371bcff9b33c35646b6ec3931362a4d5a385ffae456fb01684dfdb427d2`  
**Serving check:** `http://127.0.0.1:8878/specs/022-rendered-brief-lifecycle-freshness-and-authority/stakeholder-brief.html` returned HTTP 200.  
**Outcome:** REVISE P1. This is not a Human Visibility or Tasks Ready approval.

## Independent reviewers

| Lens | Reviewer | HTML-alone result | Comparison/result | Material decision blocked |
|---|---|---|---|---|
| Architect | `spec022_render_architect` | REVISE P1 | Current state is semantically contradictory even though source digest bindings are byte-fresh. | Whether lifecycle is rendered-and-awaiting-review or still awaiting refresh. |
| System designer | `spec022_render_system` | REVISE P1 | Canonical state contradiction plus missing transaction/recovery decision model. | Whether an interrupted promotion can expose a stale or split pair. |

## Findings and repair

| ID | Severity | Source/HTML locator | Finding | Required repair |
|---|---|---|---|---|
| AR-022-01 / SD-022-01 | P1 | `run-state.yaml:9-12,62,93`; `progress.md`; `handoffs/latest-handoff.md`; HTML lifecycle/progress bindings | `brief_phase: rendered` conflicted with `render_pending`, “awaits refresh,” and “no rendered brief.” | Reconcile canonical sources before composing a replacement. |
| SD-022-02 | P1 | `plan.md`; HTML `#architecture`, `#validation` | Commit steps were visible, but the old/new pair, journal-digest recovery choice, refusal and exposure point were not decision-readable. | Add a source-bound transaction/recovery model and project it structurally. |
| AR-022-02 | P2 | HTML introduction | “not delivered HTML” could be read as “not rendered.” | State explicitly that it is rendered but not approved/deliverable. |

## Deterministic context

`python scripts/validate_human_visibility.py` reported no structural failures
for this artifact. Its overall failure was expected: Human Visibility, Tasks
Ready, the required rendered-review metadata and the freshness baseline were
not yet recorded. Deterministic structure did not override these human P1
findings.

## Replacement-candidate composition review r5

**Reviewer:** `spec022_prerender_r5` (Terra, medium; distinct from the
replacement composer). **Artifact version:** pre-authority-repair candidate
(not a promotion binding). **Outcome:** REVISE P1.

The reviewer approved the decision-readable transaction model and the honest
candidate/authority boundaries, but found that its root and decision section
still named D-022-008 as an approved review for this new candidate. D-022-008
binds the older candidate, while the new page truthfully also said a fresh
review was required. The repair is to show D-022-008 only as history, declare
that no composition approval binds the replacement yet, and bind D-022-012
only after an independent review of the exact candidate. This finding blocks
promotion but does not create a new quality rule.
