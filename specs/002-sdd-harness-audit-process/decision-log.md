# Decision Log: 002-sdd-harness-audit-process

| ID | Date | Decision | Rationale | Consequence |
|---|---|---|---|---|
| D-2026-07-25-001 | 2026-07-25 | Create audit as skill + workflow + agents + HTML template. | User requested a complete process that is agentic but repeatable. | Audits have stable structure without becoming script-only output. |
| D-2026-07-25-002 | 2026-07-25 | Store distilled source knowledge in docs, not in the skill body. | Skills should carry method while living/project knowledge stays external. | `docs/harness-audit-framework.md` becomes the stable audit baseline. |
| D-2026-07-25-003 | 2026-07-25 | Keep T-001 at `needs_evaluation`. | Builder cannot approve own work under Guardian invariants. | Independent evaluator must review before terminal done. |
| D-2026-08-25-004 | 2026-08-25 | Independent Evaluator-002-T001 approved T-001 after reviewing the original implementation, current maintained artifacts and regression results. | AC-001 through AC-006 and all exit criteria are met; graph parsing remains explicitly out of scope. | State Keeper may transition `needs_evaluation -> approved -> done` and close validation. |
