# Decision Log: 004-consumer-enforcement-contract

Record decisions that change scope, architecture, validation, risk, precedence
or workflow. Do not rewrite prior rows; append a superseding decision.

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-08-18 | accepted | The vendor bundle owns portable validation contracts; the consumer repository or Agentic Factory owns invocation, local instructions and CI/task-runner wiring. | User question; `human-visibility.md`, `soft-hard-rules.md` and `validate_bundle.py` show that the current mirror is declared but not consumer-executed. | Make the vendor a workflow engine; rely on prompts only. | platform-engineering | none |
| D-002 | 2026-08-18 | accepted | Freshness uses Git diff with explicit base ref, then a local SHA-256 baseline fallback; a local exception needs reason, owner and `human_visibility_status: reviewed`. | Independent review identified that a promised fallback must be real and testable offline. | Git-only; timestamps only; silent bypass. | platform-engineering | none |
| D-003 | 2026-08-18 | accepted | Factory integration is represented by a tested output contract that clones, detached-checks-out and verifies a real commit before wrapper execution. | Independent review rejected synthetic pin and injected-validator fixture as insufficient evidence. | Branch tracking; text-only fixture; change Factory in this initiative. | platform-engineering | none |
| D-004 | 2026-08-18 | accepted | Independent Terra evaluator approved AC-001 through AC-008 after remediation; evidence packs are the terminal task proof. | `evidence/T-001.md`, `evidence/T-002.md`, `evidence/T-003.md`. | Self-approval by builder. | Codex acting as Delivery Orchestrator | none |
