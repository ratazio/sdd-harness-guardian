# Technical Plan: 003-stakeholder-brief-enrichment

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-12

## 1. Technical approach

Evolve the existing passive bundle in place. Enrich the canonical HTML template,
place one checklist in existing human-visibility/agent/skill guidance, strengthen
the existing agent responsibilities, then add narrow structural
checks to the current validator and smoke test. Keep semantic and visual judgment
with the Spec Guardian at the existing gate.

This is the smallest safe approach because it reuses the current scaffold,
artifact, roles, workflow transition and test entrypoints.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | Keep HTML derived from the four canonical source artifacts. | Preserves a single source of truth while making the brief the primary meeting surface. | Make HTML canonical; add structured data model. | Refresh is required after material source changes. |
| D-002 | Reuse existing rules, roles and skills for generation/refresh. | Makes authorship explicit without adding a capability to discover or maintain. | New skill or agent role; leave authorship implicit. | Guidance must stay synchronized across a small set of existing surfaces. |
| D-003 | Use conditional HTML/CSS/inline SVG patterns. | Portable, offline and accessible without runtime dependencies. | Mermaid/JS/CDN; generated images. | Authors need simple SVG guidance and text equivalents. |
| D-004 | Use static checks plus one short visual review. | Machines catch stable structure; humans/agents judge meaning. | Screenshot CI; LLM scoring; no validation. | Visual quality depends on the reviewer but avoids false precision. |
| D-005 | Size initiatives as S/M/L with a one-line rationale. | Exposes proportionality without turning the brief into estimation. | Story points, dates or detailed complexity scoring. | Size is comparative guidance, not a commitment. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** coordinated changes span a template, existing guidance, two agent
contracts, lifecycle wording and existing test scripts, but add no runtime,
service or data model.  
**Smaller option considered:** update only the HTML template. Rejected because
agents would still lack explicit authoring responsibility and meaningful review
criteria.  
**Complexity deliberately excluded:** new schema/state, workflow engine, new
skill or permanent agent, mandatory screenshot CI, semantic scoring and external
diagram tooling.

## 4. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Template + existing author/reviewer guidance | Approved source contract | A scaffolded brief contains useful decision and conditional visual patterns. | yes |
| 2 | Rule + Spec Guardian + Orchestrator + lifecycle | Step 1 | Authoring, refresh and review are explicit at the existing gate. | yes |
| 3 | Plan template + architecture/operating docs | Steps 1–2 | Sizing/proportionality has a canonical source and the boundary is documented. | yes |
| 4 | Validator + smoke assertions | Stable IDs from steps 1–3 | Cheap regressions catch missing structure/placeholders without scoring prose. | yes |
| 5 | Rendered review + existing validations | All changes | Desktop/narrow layouts and the 60-second decision test are verified. | yes |

## 5. Contracts, data and compatibility

- **API/events:** none.
- **Database/storage:** none.
- **External systems:** none; static HTML must work offline.
- **Compatibility/migration:** prospective template evolution. Do not rewrite
  consumer briefs automatically. Preserve the existing scaffold command and
  artifact paths.

## 6. Security, privacy and permissions

- **Authentication/authorization:** not applicable.
- **Secrets/PII:** author guidance must prohibit copying secrets or sensitive
  production values into diagrams.
- **Required permission:** ordinary repository edits only.
- **Destructive operations and approvals:** none planned.

## 7. Rollout, observability and rollback

- **Rollout:** implement and validate in this source bundle; release a versioned
  tag for consumers to pin deliberately.
- **Success signals:** scaffold contains the enriched contract; static and visual
  checks pass; a reviewer can use this initiative's brief alone for the decision.
- **Failure signals:** new files/states become required, the brief repeats source
  documents, diagrams are decorative or brief creation dominates delivery cost.
- **Rollback trigger:** existing scaffold/validator fails or the new contract
  cannot support a concise localized-change example.
- **Exact rollback/checkpoint:** revert the initiative implementation commit or
  pin the previous bundle tag; do not rewrite consumer initiative state.

## 8. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Should the normal word range remain 600–900 after real adoption? | bundle maintainer | Treat as guidance and revisit from feedback. | no |

## 9. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex  
**Reviewed at:** 2026-08-12  
**Conditions/links:** implement only the lean slice described here; see
`impact-map.md` and `validation-plan.md`.
