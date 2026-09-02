# Rich and sparse projection cases

These records are review fixtures, not parser inputs or a second content
schema. `reference-v2.html` exercises the stable eight-tab interaction. The
cases below calibrate how task and validation detail is projected into that
surface.

| Case | Canonical source | Expected rendered decision | Proportionality guard |
|---|---|---|---|
| Rich software planning | `testes/news-blog-spec-sandbox/specs/001-news-blog-auth/{tasks,validation-plan,stakeholder-brief}.md/html` | The Execution panel has one detailed card per task; Validation maps AC, command/context, fixture, oracle, evidence and known limitation. | No task title-only projection; no invented task/action. |
| Non-software manual proof | `scripts/fixtures/semantic-brief-review/field-operations/` | Operating handoff and 14:05 reconciliation prove delivery with workspace/records/oracle/evidence, not fake API or command. | A no-command proof remains concise and source-backed. |
| Sparse material loss | `scripts/fixtures/semantic-brief-review/shallow-negative/` | Architecture may be justified N/A, but missing hold/notification/oracle/evidence must be returned for source correction. | Absence is not filled with a generic card or visual. |

The independent reviewer compares a source fact to its child-level
`data-source`, `data-source-section` and `data-coverage` block in the rich
brief. Passing a structural test does not approve factual fidelity or decide
that a sparse case has enough evidence.
