# Technical Plan: 001-build-the-guardian

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** Codex / Delivery Orchestrator role  
**Last updated:** 2026-07-13

## 1. Technical approach

Harden the passive file contracts first, then canonical templates and optional
stdlib tooling, then consumer/release documentation. Validate registries and
scaffolding deterministically; finish with independent evaluation.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | Add common lifecycle and terminal state machine | prevents divergent workflows | repeat gates ad hoc | one canonical dependency |
| D-002 | Keep direct YAML plus Markdown contract | copyable and explainable | fenced YAML only | two files must stay aligned |
| D-003 | Use Python stdlib for optional tools | cross-platform, no dependencies | mandatory engine/package | manual copy still supported |
| D-004 | Keep state project-local | submodule stays immutable | state under vendor | consumer owns history |

## 3. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | manifest, entrypoint, roles/rules/workflows | Spec Ready | governance contract | yes |
| 2 | templates and scripts | contract stable | copy/scaffold/validate | yes |
| 3 | README, INSTALL, docs, prompts | paths stable | operational docs | yes |
| 4 | checklist, evidence, evaluator | validations pass | release decision | yes before tag |

## 4. Contracts, data and compatibility

No API/database/event changes. Public contract is the file/path layout in
`manifest.yaml` and `.harness/AGENTS.md`.

## 5. Security, privacy and permissions

No secrets or external writes. Publishing/tagging is outside this execution and
requires maintainer authorization.

## 6. Rollout, observability and rollback

Roll out as tag `v0.1.0` only after evaluator approval. Structural validator and
consumer smoke tests are success signals. Before publication, rollback is file
revision; after publication, release a new SemVer tag.

## 7. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Real consumer ergonomics | maintainer | post-release pilot | no |

## 8. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex / Harness Planner role  
**Reviewed at:** 2026-07-13  
**Conditions/links:** validation-plan.md
