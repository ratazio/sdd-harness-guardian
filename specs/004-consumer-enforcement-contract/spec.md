# Spec: 004-consumer-enforcement-contract

**Status:** spec_ready  
**Sequence:** 004  
**Slug:** consumer-enforcement-contract  
**Owner:** platform-engineering  
**Created:** 2026-08-18  
**Last updated:** 2026-08-18  
**Risk:** medium

## 1. Problem

The bundle states that non-trivial work requires a useful
`stakeholder-brief.html` and that Human Visibility must be ready before task
breakdown. In consumer repositories, however, this is presently enforced
mostly by agent instructions and a human review. The bundle's current Python
validator validates the source bundle/template, not the consumer's initiative.

Consequently a scaffold can contain the bundle in `vendor/` yet still let an
agent skip the brief review, retain generic template language, or start tasks
without proving the Human Visibility gate. The Agentic Factory can amplify the
gap when it creates a repository without a local bridge that invokes the
Guardian workflow and its checks.

## 2. Objective

Give consumer projects an installable, runtime-neutral enforcement contract so
that the Guardian's structural gates are actually invoked, while preserving
human judgment for brief meaning, decision usefulness and visual legibility.

## 3. Delivery outcome

- **Product/user outcome:** project teams and stakeholders can trust that a
  non-trivial spec cannot silently advance with a missing, stale or structurally
  invalid stakeholder brief.
- **Demonstrable increment:** the bundle exposes consumer-facing validation
  commands and integration guidance; a scaffold produced by Agentic Factory
  wires those commands into its local agent entrypoint and an appropriate
  repository check.
- **MVP/slice boundary:** enforce presence, structure, source links,
  placeholders, declared gate state and material-source/brief drift where it
  can be detected deterministically. Retain the existing short independent
  semantic/rendered review for quality.
- **Priority source:** human request on 2026-08-18.

The harness validates that these are declared. It does not decide commercial
value or product priority.

Summarize these fields for human review in `stakeholder-brief.html`.

## 4. Users or actors

- Agentic Factory, which creates new consumer repositories/scaffolds.
- Consumer-project maintainer, who chooses local CI, hooks and task runner.
- Agent working in a consumer repository.
- Spec Guardian / independent reviewer.
- Stakeholder making a scope or priority decision.

## 5. Observable outcomes

- **O-001:** a consumer can run one documented command against
  `specs/NNN-slug/` and receive deterministic failures for the supported
  Human Visibility contract.
- **O-002:** task generation or implementation cannot claim readiness when the
  applicable command or the required Human Visibility review is missing.
- **O-003:** an Agentic Factory scaffold produced with Guardian support creates
  a visible local bridge to its entrypoint, validation command and workflow; it
  does not merely copy an HTML template.
- **O-004:** the report distinguishes deterministic structural failures from
  items requiring a human/independent semantic review.
- **O-005:** consumer repositories remain free to choose CI provider, hook
  system and task runner without weakening the protected invariant.

## 6. Non-goals

- **NG-001:** build a hosted workflow engine, centralized service or mandatory
  external account.
- **NG-002:** use word counts, prose-quality scores, an LLM judge or screenshot
  scoring as a default blocking check.
- **NG-003:** make the vendor directory authoritative for project-local policy,
  CI configuration or business decisions.
- **NG-004:** require every consumer to use the Agentic Factory.
- **NG-005:** treat an automated structural pass as approval of semantic or
  visual quality.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN invoked with a consumer root and initiative path, THE BUNDLE SHALL provide a documented validator that checks the rendered `stakeholder-brief.html` contract for a non-trivial initiative. | Moves the existing recommendation from declaration to usable consumer capability. |
| FR-002 | THE validator SHALL report separately: structural contract failures, gate/state inconsistencies and checks that remain human-review responsibilities. | Prevents a green machine check from being mistaken for semantic approval. |
| FR-003 | THE validator SHALL reject missing required brief sections/source links, unresolved canonical placeholders and missing required source artifacts. | These are stable facts suitable for deterministic enforcement. |
| FR-004 | WHEN tracked source artifacts materially change, THE integration contract SHALL provide a deterministic way to require a brief refresh or an explicit reviewed exception. | Addresses stale derived briefs without inventing source content. |
| FR-005 | THE bundle SHALL document a consumer integration pattern for local agent instructions plus a repository command/CI gate, including failure behavior before task breakdown or implementation. | A vendor bundle cannot force execution unless the consumer invokes it. |
| FR-006 | Agentic Factory scaffolds that opt into the Guardian SHALL install or pin the bundle, create a root-level instruction bridge, expose the validation command, and configure a project-native pre-task or CI check. | Makes correct adoption the generated default. |
| FR-007 | THE Factory-generated bridge SHALL instruct agents to read the Guardian entrypoint and run the validator, then require an independent short semantic/rendered review for non-trivial initiatives. | Preserves the quality component automation cannot determine. |
| FR-008 | The contract SHALL support documented local exceptions only with a reason, owner and explicit Human Visibility status; it SHALL not permit disabling a protected invariant silently. | Keeps vendor neutrality without bypasses. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A clean consumer fixture with a valid initiative passes the consumer-facing Human Visibility validator. | V-001 |
| AC-002 | Fixtures fail deterministically for an absent brief, unresolved placeholder, missing base section, missing source link and missing source artifact. | V-002 |
| AC-003 | A fixture with a material source change and no brief refresh/approved exception fails through the selected freshness mechanism. | V-003 |
| AC-004 | Validator output identifies which concerns require the independent semantic/rendered review rather than implying that it performed that review. | V-004 |
| AC-005 | The install guide and consumer prompt explain an executable integration pattern for a generic task runner and CI, without requiring a particular vendor. | V-005 |
| AC-006 | A Factory fixture produced with Guardian support contains a pinned/installable bundle, root instruction bridge, validation command and configured invocation point. | V-006 |
| AC-007 | The Factory prompt explicitly blocks task breakdown/implementation when the relevant validator or Human Visibility review has not passed. | V-007 |
| AC-008 | Existing bundle validation and scaffolder smoke tests continue to pass. | V-008 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Formatting-only or release-administrative initiative. | Validator accepts the existing `not_applicable` exception only when reason and reviewer/status are recorded. |
| EC-002 | Consumer does not have Git metadata or runs from an exported archive. | Structural validation remains available; freshness validation reports its limitation and requires a documented explicit review instead of silently passing. |
| EC-003 | Consumer uses a CI/task runner unknown to the bundle. | It calls the documented bundle command through a thin local wrapper; no CI vendor integration is assumed. |
| EC-004 | A brief passes every structural check but is generic or visually misleading. | Independent Spec Guardian/human review fails Human Visibility Ready and blocks task progression. |
| EC-005 | A source change is non-material. | A reviewer records the explicit exception/reason; the brief is not needlessly regenerated. |

## 10. Constraints and non-functional requirements

- **Architecture:** the vendor delivers portable scripts, contracts and
  fixtures; consumers supply invocation and local-policy wiring.
- **Security/privacy:** validators must not log source contents, secrets or
  production data beyond paths and safe diagnostic identifiers.
- **Data:** no centralized collection; any freshness baseline must be local,
  inspectable and reviewable.
- **Performance/reliability:** local, deterministic and cheap enough for a
  pre-task or CI check; it must degrade with a clear diagnostic, not a false
  pass.
- **Compatibility/accessibility:** Python standard library unless a documented
  optional renderer is available; CI/task-runner neutral.
- **Operational:** maintain versioned fixtures, a consumer command and an
  adoption/migration guide; the Factory owns generated-project wiring.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| The Agentic Factory can safely create a root instruction bridge and invoke a project-local command. | Confirm against the Factory's scaffold conventions; Factory owner. |
| A material source change can be determined from paths plus Git diff or a local manifest without semantic change detection. | Prototype against fixtures; bundle maintainer. |
| Independent semantic review remains feasible in the target agent environments. | Confirm during first adoption; consumer owner. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Structural validation creates a false sense of full quality. | medium | high | Label human-review responsibilities in output and retain the blocking gate; bundle maintainer. |
| R-002 | Freshness check flags harmless edits or misses semantic changes. | medium | medium | Use conservative paths, explicit reviewed exceptions and fixtures; bundle maintainer. |
| R-003 | Factory-generated wiring is ignored or diverges from the bundle version. | medium | high | Pin/version the bundle and add a generated-project self-check; Factory owner. |
| R-004 | Mandatory tooling makes lightweight repos costly to bootstrap. | low | medium | Keep command stdlib-only and make CI adapter thin/local; bundle maintainer. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Guardian consumer validator and fixture contract | delivered and independently approved | bundle maintainer | no — see D-004 and `evidence/T-001.md` / `evidence/T-002.md` |
| Local task-runner/CI convention for each consumer template | varies | consumer/Factory owner | yes |
| Freshness baseline and approved-exception format | decided: Git diff plus local hash baseline; reviewed YAML exception | platform-engineering | no |

## 14. Validation notes

The implementation uses Git diff with an explicit base ref and a local hash
baseline fallback. The minimum Factory contract is a pinned bundle, root
instruction bridge, invocable command and native invocation point; its specific
CI/task-runner adapter is intentionally deferred to the Factory. The validation
plan must include isolated consumer fixtures and a representative Factory-output
fixture, not only bundle-source tests.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Codex acting as Spec Guardian  
**Reviewed at:** 2026-08-18  
**Blocking issues:** none. D-002 selects Git diff plus local hash-baseline
fallback; the Factory's exact native invocation remains a non-blocking follow-up.  
**Required revisions:** none before implementation.  
**Decision evidence/link:** user request on 2026-08-18; existing
`.harness/rules/human-visibility.md`, `soft-hard-rules.md` and
`scripts/validate_bundle.py`.
