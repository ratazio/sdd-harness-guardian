# Decision Log: build-the-guardian

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-07-13 | accepted | Common lifecycle owns terminal state machine. | Prevent workflow drift. | duplicate ad hoc flows | codex-root | none |
| D-002 | 2026-07-13 | accepted | Python scripts are optional and stdlib-only. | Portability without engine dependency. | external package/engine | codex-root | none |
| D-003 | 2026-07-13 | accepted | Record late source-state scaffolding as ratchet RG-001. | Preserve process truth and prevent recurrence. | omit deviation | codex-root | none |
| D-004 | 2026-07-13 | accepted | No remote tag/publish action in this task. | No remote/authorization supplied; INSTALL documents it. | assume remote and publish | codex-root | none |
| D-005 | 2026-07-13 | accepted | Waive implementation dependency sequencing for the integrated initial-release slice, but preserve evidence/evaluation/terminal ordering. | Bootstrap state and task decomposition were created after edits began; no distinct evaluator was then available. Cycle 2 accepted the waiver and State Keeper closed tasks in dependency order. | falsely backdate transitions; collapse tasks; claim done | codex-root + codex-independent-evaluator-2 | none |
| D-006 | 2026-07-13 | accepted | Use `release_candidate` until checklist and independent evaluation pass. | Readiness must describe actual state; validator now checks checklist when status becomes ready. | premature ready literal | codex-root | none |
