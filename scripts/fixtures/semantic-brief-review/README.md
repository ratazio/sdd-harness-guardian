# Semantic brief-review calibration fixtures

These fictional, static examples calibrate an independent reviewer; they are
not inputs to a semantic scorer or a production validator. Each case includes
canonical sources, a rendered stakeholder brief and a post-render review.
The record lists request/source/render locators and fixture digests, never the
source bodies. An initiative may add decision lenses that suit its context and
risk; the bundle does not require a fixed persona set or review count.

| Fixture | Domain | Expected review result | Calibration point |
|---|---|---|---|
| `software-release` | Software delivery | pass | Architecture, trust and validation must survive synthesis. |
| `field-operations` | Non-software operations | pass | Contextual lenses use handoffs, controls and operating state—not fake APIs. |
| `shallow-negative` | Software delivery | request revision | A structurally valid v2 brief still fails when material relation, authority and proof are lost. |

For every applicable capability, the reviewer records `material`,
`not_material` with a reason, or `insufficient`; `insufficient` is a blocking
REVISE. Every material finding is request/source locator → fact lost in HTML →
decision impact → canonical recovery action → rerender → originating-role
re-review. An accountable acceptance names the finding, authority, scope,
residual risk and expiry. The post-render question is: **which material
decision remains impossible without opening Markdown?**

The field-operations positive intentionally has neither tabs nor a diagram.
It calibrates decision recovery in an unfamiliar/non-software case, not a
fixed information architecture.

Run `python scripts/test_semantic_brief_review_calibration.py` from the bundle
root to check fixture wiring. Passing that command does not approve semantic
quality; a distinct reviewer must make and record that judgment.
