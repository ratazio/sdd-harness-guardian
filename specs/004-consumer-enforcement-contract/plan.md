# Technical Plan: 004-consumer-enforcement-contract

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-18

## 1. Technical approach

Implement a Python-standard-library CLI in the vendor bundle. It validates a
specified consumer initiative without assuming a CI system. Structural and
gate-state checks are deterministic. Freshness first compares changed source
artifacts to the brief through an optional Git base ref; when that is not
available it uses a local, inspectable hash baseline. A reviewed YAML exception
can document a non-material or offline case. The tool always states that an
independent semantic/rendered review is still required.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | Vendor provides portable validation; consumer/Factory invokes it. | The vendor cannot enforce an uninvoked command. | Make vendor a workflow engine; prompt-only governance. | Adoption wiring remains consumer work. |
| D-002 | Use Git diff with `--base-ref`, then local hash baseline fallback. | Detects source-only changes in CI and works offline. | Git-only; timestamps only. | Baseline needs clear lifecycle docs. |
| D-003 | Require `reason`, `owner` and `status: reviewed` in a local exception file. | Exceptions must be visible and auditable. | Silent CLI bypass. | Adds a small optional artifact. |
| D-004 | Preserve human review as a separate output/gate. | Meaning and rendered legibility are not safely lintable. | LLM judge, prose score, screenshot CI. | Green CLI is not final approval. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** changes a portable script, state contract, documentation and fixture
coverage across the vendor/consumer boundary.  
**Smaller option considered:** structural lint only; insufficient because it
would not detect stale briefs or instruct consumers how to invoke the check.  
**Complexity deliberately excluded:** hosted coordination, CI-provider plugins,
LLM judging and mandatory rendering infrastructure.

## 4. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | CLI and fixture tests | plan/validation ready | executable consumer contract | yes |
| 2 | templates/scaffolder contract as required | CLI behavior defined | new initiatives can record required state | yes |
| 3 | install guide and consumer prompt | command available | consumers/Factory have invocable pattern | yes |
| 4 | bundle validation and smoke tests | all changes landed | regression evidence | yes |

## 5. Contracts, data and compatibility

- API/events: `python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/NNN-slug [--base-ref REF]`.
- Database/storage: local optional baseline JSON and reviewed exception YAML;
  no network or central store.
- External systems: optional Git executable; validator reports fallback/limits.
- Compatibility/migration: old initiatives receive diagnostics and can create a
  baseline only after their Human Visibility gate is marked ready.

## 6. Security, privacy and permissions

- Authentication/authorization: none.
- Secrets/PII: diagnostics expose only paths, identifiers and checks, not file contents.
- Required permission: read-only validation; baseline write is explicit.
- Destructive operations and approvals: none.

## 7. Rollout, observability and rollback

- Rollout: document opt-in local wrapper/CI usage after script release.
- Success/failure signals: non-zero exit and categorized diagnostics; fixture suite.
- Rollback trigger: consumers cannot adopt or validator produces unsound false positives.
- Exact rollback/checkpoint: remove local wrapper/CI call and optional baseline;
  vendor script is additive.

## 8. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Which native invocation point should each Factory template generate? | Factory owner | Decide in Factory follow-up. | no |

## 9. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex acting as Harness Planner  
**Reviewed at:** 2026-08-18  
**Conditions/links:** D-001 through D-004; independent evaluator must review implementation.
