# Tasks: 010-stakeholder-brief-composition-kit

**Status:** execution in progress — only T-004 is authorized  
**Spec:** [spec.md](./spec.md)  
**Plan:** [plan.md](./plan.md)  
**Validation plan:** [validation-plan.md](./validation-plan.md)  
**Last updated:** 2026-08-26

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Locate the integrated composition entrypoint and fixture baseline | none | medium | platform-engineering | sandbox_coverage_review | evidence/T-001.md |
| T-002 | done | Define depth ladder and source-aware architecture/task/proof mini-templates | T-001 done | high | platform-engineering | sandbox_coverage_review | evidence/T-002.md |
| T-003 | done | Compose impact, coverage and responsive semantic variants | T-002 done | high | platform-engineering | sandbox_coverage_review | evidence/T-003.md |
| T-004 | done | Prove projection parity regression behavior and publish reviewer guidance | T-001–T-003 done | high | platform-engineering | sandbox_coverage_review | evidence/T-004.md |

### T-001 — Locate the integrated composition entrypoint and fixture baseline

**Status:** done — independent evaluator approved D-010 on 2026-08-26.  
**Objective:** inventory existing template, author/planner/reviewer guidance and
fixtures to choose one catalogue home and minimal calibration corpus.  
**FR/AC:** FR-001, FR-010–FR-012; AC-001, AC-007, AC-010.  
**Outcome/increment:** a recorded decision removes U-001/U-002 without adding
a new agent, sidecar or duplicate fixture family.  
**Scope:** read current v2 surfaces; map rich/sparse/non-software examples;
record selected locations and rejected options.  
**Out of scope:** modify HTML/CSS, create components, style client brand or
declare any quality gate.  
**Contracts/dependencies:** none; output is plan/decision/evidence only.  
**Risk/assurance:** medium/A2; source-entrypoint choice controls all later work.  
**Validation/evidence:** V-001, V-007, V-009, E-001; inventory, decision,
fixture matrix and independent evaluator result in evidence/T-001.md.  
**Why now:** prevents a second “polisher” process before any presentation
pattern is defined.  
**Exit:** one minimal home/fixture baseline selected; U-001/U-002 disposition
recorded; evaluator distinct; no implementation claimed.

### T-002 — Define depth ladder and source-aware architecture/task/proof mini-templates

**Status:** done — independent evaluator approved on 2026-08-26.  
**Objective:** create the vendor-neutral catalogue that maps source sufficiency
to orientation, macro relation, focused cut, complete task card and proof card.  
**FR/AC:** FR-002–FR-006, FR-009–FR-012; AC-002–AC-004, AC-006, AC-009–AC-010.  
**Outcome/increment:** rich, sparse and non-software source records select
different truthful projections rather than one generic layout.  
**Scope:** guidance/template hooks/fixtures for depth ladder, textual
equivalents, task fields and material-gap behavior.  
**Out of scope:** impact/coverage visual treatment, brand/profile, runtime
component system or semantic score.  
**Contracts/dependencies:** T-001 approved; existing provenance and task
sources stay canonical.  
**Risk/assurance:** high/A2; reviewer must trace focused cuts and task details
to source sections.  
**Validation/evidence:** V-002–V-004, V-006, E-002/E-003; source-to-view
matrix, rich/sparse render notes and independent decision in evidence/T-002.md.  
**Why now:** establishes truthful semantic roles before styling other views.  
**Exit:** all mini-template fields source-aware; focused cut limited to one
level; no empty placeholders or forced technical diagram; evaluator approves.

### T-003 — Compose impact, coverage and responsive semantic variants

**Status:** done — independent evaluator approved on 2026-08-26.  
**Objective:** make impact and coverage relationships scannable and visually
distinct while preserving table/equivalent, provenance and access modes.  
**FR/AC:** FR-007–FR-010; AC-005–AC-007.  
**Outcome/increment:** reference brief shows surface/risk/control and grouped
source/view/disposition compositions that reflow truthfully.  
**Scope:** semantic patterns, CSS/template variants, local SVG/HTML where
needed and 320/390/print/no-script behavior.  
**Out of scope:** change task/architecture source model, client branding,
remote assets or hide a complete table merely for aesthetics.  
**Contracts/dependencies:** T-002 approved; impact/coverage sources and
existing coverage-register stay recoverable.  
**Risk/assurance:** high/A2; accessibility evaluator validates order,
non-colour cues and print.  
**Validation/evidence:** V-005–V-007, M-003/M-004; browser observation,
semantic equivalent and evaluator result in evidence/T-003.md.  
**Why now:** applies the established semantic roles to the surfaces the user
identified as visually monotonous.  
**Exit:** impact/coverage no longer rely on a single flat table; accessibility
modes pass; evaluator approves.

### T-004 — Prove projection parity regression behavior and publish reviewer guidance

**Status:** done — independent evaluator approved on 2026-08-26.  
**Objective:** complete fixture/check/reviewer guidance and verify that richer
composition did not create automatic semantic judgement or profile coupling.  
**FR/AC:** FR-001, FR-008, FR-010–FR-014; AC-001, AC-007–AC-012.  
**Outcome/increment:** maintainers can regenerate rich/sparse/non-software
examples, and a populated source ledger cannot silently become a generic
Execution/Validation scaffold.  
**Scope:** focused deterministic parity check, explicit scaffold lifecycle
label, reviewer rubric examples, ratchet and release evidence.  
**Out of scope:** production deployment, client profile implementation,
application code or replacing independent evaluation.  
**Contracts/dependencies:** T-001–T-003 approved; checks assert structure
only.  
**Risk/assurance:** medium/A2; release evaluator verifies no semantic score.  
**Validation/evidence:** V-007–V-012, M-005, E-004/E-005 and validate_bundle;
command transcript, source-to-render fixture comparison and decision in
evidence/T-004.md.  
**Why now:** it is the safe final gate after real patterns exist.  
**Exit:** all commands/reviews pass or approved exception exists; rich fixture
projects every populated task/AC, scaffold-negative fixture fails, reviewer
accepts evidence, and state/progress/ratchet are synchronized.
