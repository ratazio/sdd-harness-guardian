# SDD/Harness Audit Action Backlog

Use this template when an audit should produce actionable spec candidates from
its findings. The file belongs in the same human-approved audit output package
as the HTML report and raw artifacts.

## Purpose

Convert audit findings into candidate SDD initiatives. This is not a substitute
for creating formal specs; it is the handoff from audit to spec creation.

## Required Structure

```txt
# SDD/Harness Audit Action Backlog

Audit ID:
Source report:
Purpose:

## Recommended Sequence

| Order | Candidate Spec | Priority | Main Findings | Why First |

## Epic N: <Name>

Suggested slug:

### Outcome
### Why This Exists
### Suggested Prompt
### Suggested Tasks
### Acceptance Signals

## Cross-Epic Dependencies
## Suggested First Command
## Notes For The Spec Creator
```

## Epic Rules

- Each epic should be scoped as a future `specs/NNN-slug/` initiative.
- Each epic should map back to one or more audit findings.
- P0 epics address contradictory state, false readiness, missing evidence or
  blocked release posture.
- P1 epics harden behavior through validators, hooks, CI, graph checks,
  normalized agent contracts or normalized skill contracts.
- P2 epics improve release hygiene, polish, readability or lower-risk process
  quality.
- Suggested tasks are seed tasks, not final implementation tasks.
- Acceptance signals must be testable and evidence-oriented.

## Prompt Guidance

Every epic should include a prompt that a future user can paste into the SDD
Harness Guardian flow to create the formal spec. The prompt should name the
target outcome, major constraints and the audit finding class it resolves.

## Dependency Guidance

Prefer this sequence when applicable:

```txt
state/evaluation/release truth
state consistency validators
hard mirrors through hooks/CI
graph reachability validators
agent and skill contract normalization
audit package completeness checks
release evidence/versioning cleanup
low-risk readability polish
```
