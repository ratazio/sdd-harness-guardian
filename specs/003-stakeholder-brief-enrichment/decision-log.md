# Decision Log: 003-stakeholder-brief-enrichment

| ID | Date | Status | Decision | Rationale/evidence | Alternatives | Owner/approver | Supersedes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-08-12 | accepted | Make the HTML the primary meeting/decision surface while keeping Markdown artifacts canonical. | User request and existing derived-artifact architecture. | Make HTML canonical; keep current textual brief. | user | none |
| D-002 | 2026-08-12 | accepted | Use conditional visuals and qualitative S/M/L proportionality. | Reveals complexity without making diagrams or estimates ritualistic. | Mandatory diagrams; detailed effort scoring. | user/Codex | none |
| D-003 | 2026-08-12 | superseded | Add one authoring skill and reuse current roles/gate. | Initial option before independent simplicity review. | Permanent new agent; implicit authorship. | Codex | none |
| D-005 | 2026-08-12 | accepted | Reuse existing rules, skills and roles for authorship/checklist; do not add a new skill in the MVP. | Independent review found the extra capability unnecessary before adoption evidence. | New authoring skill. | Codex | D-003 |
| D-004 | 2026-08-12 | accepted | Keep hard validation structural and visual/semantic validation agentual. | Avoids brittle semantic scoring and screenshot bureaucracy. | LLM judge; screenshot CI; no validation. | user/Codex | none |
