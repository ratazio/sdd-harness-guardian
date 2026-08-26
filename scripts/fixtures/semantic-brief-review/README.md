# Semantic brief-review calibration fixtures

These fictional, static examples calibrate an independent reviewer; they are
not inputs to a semantic scorer or a production validator. Each case includes
canonical sources, a rendered stakeholder brief and a post-render review.

| Fixture | Domain | Expected review result | Calibration point |
|---|---|---|---|
| `software-release` | Software delivery | pass | Architecture, trust and validation must survive synthesis. |
| `field-operations` | Non-software operations | pass | The same lenses use handoffs, controls and operating state—not fake APIs. |
| `shallow-negative` | Software delivery | request revision | Formal provenance and headings still fail when a material decision is lost. |

The reviewer records product, architecture/operations and delivery as
`recoverable`, `superficial`, `absent` or justified `N/A`; every material
finding is source → lost fact → recovery action. The post-render question is:
**which material decision remains impossible without opening Markdown?**

Run `python scripts/test_semantic_brief_review_calibration.py` from the bundle
root to check fixture wiring. Passing that command does not approve semantic
quality; a distinct reviewer must make and record that judgment.
