# Decision Log: 005-stakeholder-brief-meeting-standard

Record decisions that change scope, architecture, validation, risk, precedence
or workflow. Do not rewrite prior rows; append a superseding decision.

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-08-18 | accepted | The 004 regression is caused by bypassing the existing canonical template and by missing brief-specific design/lineage enforcement; it is not caused by a missing HTML template. | Template (17 KB), 003 brief (25 KB), 004 brief (4 KB), current validator and design-file inventory. | Treat 004 as acceptable local variation; redesign all artifacts. | Codex acting as Spec Guardian | none |
| D-002 | 2026-08-18 | accepted | Canonical briefs use `data-harness-brief-design="v1"`; a material custom layout needs a reviewed exception recorded in this decision log with rationale, owner, retained decision surfaces and review date. | User approved both recommendations after reviewing the populated 005 brief. | Stylesheet checksum; separate exception sidecar. | platform-engineering | none |
