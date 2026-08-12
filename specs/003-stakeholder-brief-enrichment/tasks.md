# Tasks: 003-stakeholder-brief-enrichment

**Status:** complete  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Validation plan:** ./validation-plan.md  
**Last updated:** 2026-08-12

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Deliver the enriched decision-surface contract | none | medium | terra-t001-builder | terra-independent-evaluator | evidence/T-001.md |
| T-002 | done | Add lightweight structural regression checks | T-001 | low | terra-t002-builder | terra-independent-evaluator | evidence/T-002.md |

## Allowed statuses and transitions

```txt
pending -> ready -> in_progress -> needs_evaluation
needs_evaluation -> needs_revision -> in_progress
needs_evaluation -> approved -> done
any non-terminal state -> blocked
```

`done` requires approved evidence and distinct builder/evaluator identities.

## T-001 — Deliver the enriched decision-surface contract

**Status:** done  
**Objective:** make the default brief useful for a short spec decision meeting.  
**Requirement IDs:** FR-001–FR-008, FR-010–FR-011  
**Acceptance criteria IDs:** AC-002–AC-007, AC-010  
**Outcome served:** stakeholders understand value, boundary, implementation shape
and proportionality from one rendered page.  
**Demonstrable increment:** updated template and existing author/reviewer
governance contracts work together without a new skill, state or gate.  
**Expected artifact/behavior:** a newly authored non-trivial brief contains only
the relevant decision content and visual explanations.  
**Validation method:** V-002–V-005, V-008 and V-REG-001–V-REG-003.  
**Why now:** it establishes the contract before deterministic checks encode IDs.  
**Dependencies:** none  
**Risk:** medium  
**Builder:** terra-t001-builder  
**Evaluator:** terra-independent-evaluator  
**Human approval:** approved by explicit request  
**Evidence:** evidence/T-001.md

### Scope

- Update the canonical HTML template.
- Add the conditional checklist to existing author/reviewer guidance.
- Update human-visibility, Spec Guardian, Orchestrator and lifecycle guidance.
- Add proportionality to the plan source and update the smallest necessary docs.
- Visually review a rendered non-trivial example and a concise localized path.

### Out of scope

- New agent, state, gate, YAML/JSON, external diagram engine, screenshot CI or
  semantic scoring.

### Expected files and contracts

Only the surfaces listed in `impact-map.md`; expanding beyond them requires a
recorded reason and impact review.

### Exit criteria

- [x] one conditional checklist guides authorship without a new artifact;
- [x] relevance triggers govern architecture, impact and flow visuals;
- [x] size/proportionality and a smaller-option decision are visible;
- [x] Spec Guardian rejects contradiction, filler and unreadable visuals;
- [x] rendered desktop and narrow views pass the 60-second decision test;
- [x] evidence draft is independently evaluated.

#### Readiness decision

**Task Ready:** yes  
**Reviewed by:** Codex  
**Blocking conditions:** none.

## T-002 — Add lightweight structural regression checks

**Status:** done  
**Objective:** protect the stable brief contract without automating subjective judgment.  
**Requirement IDs:** FR-009  
**Acceptance criteria IDs:** AC-001, AC-008, AC-009  
**Outcome served:** consumers keep receiving a structurally usable default brief.  
**Demonstrable increment:** validator/smoke fail on missing base IDs, unresolved
canonical placeholders or missing source references and pass on the valid template.  
**Expected artifact/behavior:** narrow assertions in existing scripts; no new validation service.  
**Validation method:** V-001, V-006, V-007 and V-REG-004.  
**Why now:** stable IDs are known only after T-001.  
**Dependencies:** T-001  
**Risk:** low  
**Builder:** terra-t002-builder  
**Evaluator:** terra-independent-evaluator  
**Human approval:** not_required  
**Evidence:** evidence/T-002.md

### Scope

- Extend the existing bundle validator and scaffolder smoke assertions.
- Exercise precise negative structural cases without scoring prose.

### Out of scope

- Screenshot comparison, cross-file hash state, word-count blocking or LLM judge.

### Exit criteria

- [x] enriched scaffold assertions pass;
- [x] each structural negative case fails for a precise reason;
- [x] existing validate and smoke commands exit 0;
- [x] no new runtime dependency or per-initiative artifact exists;
- [x] evidence draft is independently evaluated.

#### Readiness decision

**Builder handoff:** complete and independently approved.  
**Evaluator:** terra-independent-evaluator  
**Blocking conditions:** none.
