# Spec: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** spec_ready  
**Sequence:** 012  
**Kind:** bugfix  
**Owner:** platform-engineering  
**Created / updated:** 2026-08-26  
**Risk:** medium  
**Assurance profile:** A2-elevated — changes a reusable validation contract and its negative fixtures.

## 1. Problem

The consumer fixture `testes/specs/001-news-blog-auth` passed deterministic
Human Visibility validation while a referenced planning-review file did not
exist, one material risk (IR-005) was absent from the rendered brief, and five
API contracts were too abbreviated to support a stakeholder decision. An
independent auditor caught the omissions; the validator did not. This permits
an apparently green v2 package to have unrecoverable evidence or incomplete
projection of material source facts.

## 2. Objective

Make the Guardian reject v2 briefs that reference missing evidence or omit
source-declared material risk/API-contract items, while retaining an explicit
independent semantic review for judgment that parsing cannot establish.

## 3. Delivery outcome

- **Product/user outcome:** maintainers receive actionable failures before a green validation result can mask missing planning evidence or incomplete decision material.
- **Demonstrable increment:** `validate_human_visibility.py` has targeted evidence-reference and projection-completeness checks plus passing and failing regression fixtures.
- **MVP/slice boundary:** local bundle validator, templates/guidance, fixtures and tests only; no consumer application code or hosted service.
- **Priority source:** risk reduction — independent audit of `001-news-blog-auth` on 2026-08-26.

## 4. Users or actors

- **Bundle maintainer:** changes validation behavior and regression suite.
- **Spec author:** receives a path/identifier-specific remediation message.
- **Independent brief reviewer:** confirms semantic and visual decision usefulness that deterministic checks cannot certify.

## 5. Observable outcomes

- **O-001:** a v2 initiative citing a nonexistent local `evidence/*.md` file fails before baseline acceptance and names the source locator.
- **O-002:** a v2 brief missing an `IR-*` row from `impact-map.md` fails with that risk ID and target view.
- **O-003:** a v2 brief omitting a canonical `METHOD /api/...` contract row fails with that route identifier and target view.
- **O-004:** complete source/brief fixtures remain green and an independent reviewer checklist still covers semantic/rendered quality.

## 6. Non-goals

- **NG-001:** score persuasive writing, visual aesthetics or domain correctness automatically.
- **NG-002:** require an API matrix when the plan declares no HTTP/API contract.
- **NG-003:** change task lifecycle, turn deterministic PASS into human approval, or retrofit historic v1/pinned briefs without a material refresh.
- **NG-004:** alter consumer feature behavior or introduce external services, telemetry or network calls.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN a v2 canonical source cites a local `evidence/...` locator, THE validator SHALL resolve it inside the initiative and fail if its file is absent. | A cited evidence record must be recoverable. |
| FR-002 | WHEN `impact-map.md` declares material `IR-*` risks, THE validator SHALL require each identifier in the rendered brief Impact projection. | A represented impact source cannot silently omit a risk. |
| FR-003 | WHEN `plan.md` declares a canonical HTTP method/path contract, THE validator SHALL require the same normalized method/path in the rendered Architecture or Validation projection. | Stakeholders need every public contract, not a summary that drops a route. |
| FR-004 | WHEN a projection check fails, THE validator SHALL report source file, missing identifier/route and expected brief view without scanning outside the initiative. | Repair must be safe and actionable. |
| FR-005 | THE templates and independent-review guidance SHALL distinguish deterministic projection integrity from semantic/rendered review and retain distinct reviewer identity. | Parsing supplements rather than replaces judgment. |
| FR-006 | THE regression suite SHALL contain positive and negative fixtures for missing evidence, risk and API projection, and compatibility cases for no API/no risk and legacy v1. | The guard must not regress or overreach. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A missing cited local evidence file makes the v2 validator non-zero and names the file. | V-001 |
| AC-002 | Every `IR-*` source row missing from an Impact projection makes the v2 validator non-zero and names the ID. | V-002 |
| AC-003 | Every canonical method/path omitted from Architecture or Validation makes the v2 validator non-zero and names the route. | V-003 |
| AC-004 | The repaired `001-news-blog-auth` fixture passes the strengthened validator and baseline recheck. | V-004 |
| AC-005 | Existing valid v2, legacy v1 and source sets with no API/risk entries retain their intended result. | V-005 |
| AC-006 | Errors reject traversal/absolute evidence locators and never read outside the initiative. | V-006 |
| AC-007 | Reviewer/template guidance explicitly requires a distinct semantic/rendered review after deterministic PASS. | V-007 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Evidence locator has a valid file plus an anchor. | Resolve file; anchor is informational unless a future checker owns anchors. |
| EC-002 | A source has no `IR-*` rows or no recognized method/path contract. | Do not create a false completeness obligation. |
| EC-003 | Brief uses a route in code formatting or table text. | Normalize whitespace/HTML encoding, then match exact method/path rather than prose fragments. |
| EC-004 | Locator is absolute, uses `..`, or resolves outside initiative. | Fail closed with a safe diagnostic; never read it. |
| EC-005 | Legacy v1 brief is not materially refreshed. | Preserve current compatibility path; do not impose new v2 projection checks. |

## 10. Constraints and non-functional requirements

- **Architecture:** extend the existing local Python validator and its established fixture/test conventions; no second validator or sidecar schema.
- **Security/privacy:** evidence path resolution must stay under the selected consumer initiative and report paths without opening arbitrary files.
- **Data:** no persistent data/migration; fixtures are synthetic and must not contain credentials.
- **Performance/reliability:** checks are deterministic, offline and proportionate to current test-suite runtime.
- **Compatibility/accessibility:** retain v1 behavior and the v2 no-script, tabs, print, responsive and provenance contracts.
- **Operational:** baseline write/recheck remains explicit; a deterministic PASS message continues to say independent review is required.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| Material risks retain `IR-` identifiers in the impact-map risk table. | T-002 fixtures / validation maintainer. |
| Canonical HTTP contracts are stated as method + `/api/...` route in plan tables or bullets. | T-003 parser tests / validation maintainer. |
| Referenced planning evidence uses initiative-relative `evidence/...` locators. | T-001 negative fixtures / security reviewer. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Overmatching prose causes valid briefs to fail. | medium | medium | Narrow parsers to risk-table IDs and normalized method/path tokens; negative and compatibility fixtures / validation maintainer. |
| R-002 | Evidence resolution escapes a consumer root. | low | high | Reject absolute/traversal paths before resolution; security review / security reviewer. |
| R-003 | Automation is misrepresented as semantic approval. | medium | high | Preserve warning and require distinct reviewer checklist / workflow owner. |
| R-004 | Fixture drift masks a regression. | medium | medium | Keep a repaired real-world-inspired fixture plus purpose-built negative fixtures / test maintainer. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| `scripts/validate_human_visibility.py` and its test conventions | available | platform-engineering | yes |
| v2 template/design guidance | available | platform-engineering | yes |
| `001-news-blog-auth` repaired fixture | available | fixture maintainer | no |
| Independent security/semantic reviewer | required before task completion | platform-engineering | yes |

## 14. Validation notes

Validation is local Python/unit-fixture based, plus the existing bundle and
Human Visibility baseline/recheck commands. An independent reviewer checks
that diagnostics and projections remain decision-useful; it does not implement
the task it evaluates.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** Spec Guardian / user-authorized corrective scope  
**Reviewed at:** 2026-08-26  
**Blocking issues:** none for planning; implementation waits for plan, tasks and independent evaluation gates.  
**Decision evidence/link:** `testes/specs/001-news-blog-auth/evidence/planning-review.md#final-independent-approval`.
