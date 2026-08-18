# Handoff: 004-consumer-enforcement-contract

**From:** Codex acting as Delivery Orchestrator  
**Intended role/recipient:** Agentic Factory owner  
**Created at:** 2026-08-18  
**Current phase/status:** validation done  
**Current task/status:** none; T-001 through T-003 done  
**Last safe checkpoint:** All evidence packs approved by an independent Terra evaluator.  
**Repository revision/working-tree summary:** Uncommitted implementation and initiative artifacts are ready for normal review/commit.

## 1. Completed and approved work

- Consumer-facing Human Visibility validator with structural, gate/state,
  freshness and human-review categories.
- Git/base-ref freshness with local hash-baseline fallback and reviewed local
  exceptions.
- Consumer guide, prompt and install integration.
- Tested Factory-output contract with real local clone, detached checkout, SHA
  verification and wrapper execution.

## 2. Validations and evidence

See `evidence/T-001.md`, `evidence/T-002.md` and `evidence/T-003.md`.

## 3. Residual risks and next safe step

The bundle does not change Agentic Factory. Its next initiative must turn the
tested contract into each generated project's real pinned bundle, bridge,
wrapper and CI/task-runner invocation; it must retain independent brief review.

## 4. Do not do

- Do not replace semantic/rendered review with a green structural check.
- Do not use an unverified branch or synthetic SHA as a Guardian pin.
- Do not claim the Factory itself was changed by this initiative.
