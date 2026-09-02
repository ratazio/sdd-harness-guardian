# Technical Plan: 010-stakeholder-brief-composition-kit

**Status:** approved planning source — execution remains task-gated  
**Spec:** [spec.md](./spec.md)  
**Impact map:** [impact-map.md](./impact-map.md)  
**Validation plan:** [validation-plan.md](./validation-plan.md)  
**Owner:** platform-engineering  
**Last updated:** 2026-08-26

## Technical approach

Extend the existing v2 brief composition path, rather than add an HTML
post-processor. A compact catalogue defines semantic component roles and a
depth ladder. The author selects a pattern only after reading source headings;
the current independent coverage/semantic reviewer evaluates the result. The
template renders accessible patterns with local CSS/SVG and existing provenance.

## Architecture decisions

| ID | Decision | Rationale | Rejected alternative | Consequence |
|---|---|---|---|---|
| D-001 | Put composition guidance in existing author/planner/reviewer/template surfaces selected by T-001. | The agent retains source context. | Mandatory visual-fixer sub-agent after render. | One accountable composition path. |
| D-002 | Limit decomposition to macro plus at most one focused source-backed cut. | Makes internal responsibility visible without diagrams becoming a substitute architecture. | Recursive drill-down/UML. | Rich cases choose, sparse cases omit. |
| D-003 | Model patterns as semantic roles, not a universal UI framework. | Works for software, operations and research. | Code component library/runtime. | Template remains offline/simple. |
| D-004 | Hide optional absent task rows; use owned question only for material absence. | Empty labels and fake detail both harm clarity. | Fixed field quota. | Reviewer judges materiality. |
| D-005 | Keep deterministic tests structural and fixture-based; preserve 008 independent semantic review. | Prose/visual quality is contextual. | A quality score or LLM judge. | Human review remains gate. |
| D-006 | Keep client identity out of this change. | Bundle remains reusable. | Hard-code Pearson style here. | 011 is an opt-in dependent profile. |
| D-007 | Add a source-to-derived-brief parity guard for populated task and validation identifiers, plus an explicit scaffold lifecycle label. | It catches a missing projection deterministically without judging prose quality. | Manual memory/checklist alone. | A brief cannot be shared as generated until sources and projections agree. |
| D-008 | Make `stakeholder-brief-design.md` the single composition catalogue, retain `stakeholder-brief.html` as the generic structural shell, and extend the existing `scripts/fixtures/tabbed-brief-surface/` corpus. | The locations already own author guidance, stable HTML hooks and v2 interaction fixtures. | A post-render agent, new sidecar/schema, or duplicate fixture family. | T-002–T-004 change one guidance home, one shell and one focused fixture/test family. |

## Size and proportionality

**Initiative size:** M.  
**Why:** it changes multiple reusable guidance/template/test surfaces, but no
runtime application or persistent data boundary.  
**Smaller option considered:** document one architecture diagram example only.
It is insufficient because task/impact/coverage consistency and sparse cases
would remain ungoverned.  
**Complexity deliberately excluded:** layout editor, JSON component schema,
renderer service, plugin runtime and automatic quality scoring.

## Architecture readiness

**Profile:** A2-elevated.  
**Rationale:** the change can systematically fabricate detail or regress
accessibility across many future consumer briefs.  
**Reapproval trigger:** any runtime dependency, multi-page output, semantic
automated gate or removal of a v2 fallback.

| Dimension | Current | Target | Proof / N/A |
|---|---|---|---|
| Context | Existing v2 shell, templates, skills and fixtures. | One source-aware composition kit. | spec §5/§8. |
| Components | Generic panels/rows. | Semantic mini-template catalogue and selection guidance. | D-001–D-004. |
| Interfaces | Markdown to derived HTML/provenance. | Same interface, deeper supported projection. | no new API. |
| Data/trust | Canonical Markdown/state. | Unchanged ownership; HTML stays derived. | FR-001, FR-010. |
| Flows | Author then reviewer. | Same flow with selection before render. | D-001. |
| Failure | Unsupported detail can drift. | Reviewer returns canonical correction. | IR-001/IR-002. |
| NFR/access | Tabs/no-script/print exist. | Preserve and extend semantic equivalents. | FR-010. |
| Unknowns | Catalogue home/fixtures/breakpoint. | Bounded discovery tasks. | U-001–U-003. |

## Change sequence

| Step | Surface | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Inventory current authoring/design/review surfaces and fixtures. | T-001 ready. | Select minimal catalogue home and fixtures. | yes |
| 2 | Add depth ladder, selection rules and task/proof/architecture patterns. | T-001 evidence. | Source-aware component contract. | yes |
| 3 | Apply impact/coverage patterns and responsive semantic equivalents. | T-002 evidence. | Differentiated but accessible views. | yes |
| 4 | Add parity fixture/check, lifecycle label and complete independent review. | T-002/T-003 evidence. | Release evidence prevents scaffold-as-brief regression. | yes |

## Contracts and compatibility

- **Input:** existing spec, plan, impact map, tasks, validation plan, decision,
  progress and state headings; no new sidecar.
- **Output:** same one-file HTML, existing v2 data-source/provenance and
  coverage register; optional semantic visual blocks. A populated task ledger
  and AC trace are mechanically compared with Execution/Validation projections
  before the file is presented as generated.
- **Compatibility:** v1 stays legacy; v2 does not require all patterns.
- **External system:** none. 011 may consume semantic role names but does not
  block 010.

## T-001 inventory result

| Concern | Selected existing home | Why it is the smallest coherent extension |
|---|---|---|
| Author/reviewer composition rules | `.harness/templates/stakeholder-brief-design.md` | Already contains per-tab missions, source-sufficiency rules and the independent rendered-review contract. |
| Stable rendered shell and semantic hooks | `.harness/templates/stakeholder-brief.html` | Already owns the one-file v2 tabs, provenance, no-script and print fallback. |
| Rich/sparse/non-software calibration | `scripts/fixtures/tabbed-brief-surface/` plus the referenced 008 semantic fixtures | Existing baseline distinguishes interaction wiring from semantic review; extend it rather than create an alternate renderer corpus. |
| Deterministic guard location | `scripts/test_brief_composition_contract.py` (new focused sibling) | Tests stable source/fixture/projection IDs only and does not turn semantic review into a prose score. |

U-001 and U-002 are resolved by D-008. U-003 remains for T-003 and must be
chosen from actual content reflow, not a universal breakpoint rule.

## Security, privacy and permissions

No new authentication, PII or network. Avoid copying sensitive source detail
into a visual cut. Existing human approval rules apply to any sensitive content
shown in a consumer brief.

## Rollout, observability and rollback

- Run focused tests plus existing bundle checks; inspect rich/sparse/non-software
  reference briefs in browser modes.
- Failure signal: missing fallback, source/provenance mismatch, unsupported
  detail, populated task/AC absent from projection, generic scaffold presented
  as derived, or inaccessible reflow.
- Rollback: revert the catalogue, template and fixtures as one bounded bundle
  change; do not edit consumer sources to hide the regression.

## Brief coverage composition

This initiative already has a **derived pre-review candidate** at
`stakeholder-brief.html`. It projects populated tasks and validation trace, but
is not a Human Visibility approval and does not authorize a task. After the
coverage correction is independently accepted, the same derived file is
refreshed from these sources; it is never an unrendered scaffold masquerading
as a generated brief.

## Open questions

| ID | Question | Owner | Resolution | Blocks? |
|---|---|---|---|---|
| Q-001 | Which current file is the single catalogue home? | T-001 / template owner | Inventory and select; record D-007. | no |
| Q-002 | Which existing fixtures can be extended without duplicate corpus? | T-001 / test owner | Compare 009 and sandbox fixtures. | no |
| Q-003 | Is a specific focus-cut SVG helper needed? | T-002 / accessibility owner | Prefer structured HTML/SVG only if decision relation needs it. | no |

## Plan decision

**Plan Ready:** yes — D-006 records the user's explicit authorization to
execute this initiative under the normal v2 gates.  
**Remaining condition:** independent coverage review must accept the corrected
candidate and a propagated decision must set a truthful `tasks_ready` state
before T-001 becomes ready.
