# Tasks: 018-derived-brief-completeness-and-delivery-integrity

**Status:** tasks_ready  
**Last updated:** 2026-08-27

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Reproduce and inventory the empty-brief bypass | D-018-03/04, baseline recheck | medium | root | audit_018_root_cause | evidence/T-001.md (approved D-018-T001) |
| T-002 | done | Define the flexible source-to-brief completeness contract | T-001 done | medium | root | audit_018_root_cause | evidence/T-002.md (approved D-018-T002) |
| T-003 | done | Enforce lifecycle and completeness at scaffold and delivery gates | T-002 done | high | root | audit_018_root_cause | evidence/T-003.md (approved D-018-T003) |
| T-004 | done | Prove broad-domain briefs and rendered delivery quality | T-003 done | medium | root | audit_018_root_cause | evidence/T-004.md (approved D-018-T004) |

`pending -> ready -> in_progress -> needs_evaluation -> approved -> done`.
Builder and evaluator must remain distinct; none of these rows may be marked
ready until independent planning review propagates its decision.

## T-001 — Reproduce and inventory the empty-brief bypass

**Objective:** create a minimal, safe reproduction that traces every path by
which a new scaffold or source-only package can look delivered.  
**Requirement IDs:** FR-001, FR-005 | **AC:** AC-001, AC-003  
**Outcome/increment:** turns the observed failure into a fixture-backed
root-cause inventory before policy/code is chosen.  
**Validation:** V-001, V-003, V-REG-001 | **Why now:** prevents a cosmetic fix.

**Scope:** inspect `new_initiative.py`, template, validators, workflow and
fresh fixtures; record paths, expected state and failing evidence.  
**Out of scope:** changing a production consumer brief, inventing content
quality scores, or repairing validator behavior.  
**Expected files/contracts:** focused fixture(s), test assertions and evidence;
no public runtime contract. **Risk:** medium.  
**A2 assurance:** exact entry/exit state, command result and diagnostic
sanitisation recorded; evaluator independently reproduces the failure.  
**Exit criteria:** root cause is code-linked; fresh scaffold is proven unsafe
under the old path; source-only and template-prose negatives are represented;
evidence has a distinct evaluator decision.

## T-002 — Define the flexible source-to-brief completeness contract

**Objective:** implement an additive lifecycle/coverage representation that
states what is present, not applicable, or an owned unknown without dictating
domain, technologies or layout.  
**Requirement IDs:** FR-002, FR-003, FR-004, FR-005 | **AC:** AC-002, AC-003  
**Outcome/increment:** sources and HTML can be compared honestly.  
**Validation:** V-002, V-003, V-REG-002 | **Why now:** T-003 needs a stable
contract rather than ad-hoc strings.

**Scope:** lifecycle semantics, source coverage records/provenance and positive
fixtures spanning unlike domains. **Out of scope:** mandated tabs, diagrams,
specific architecture fields or automatic writing judgment.  
**Expected files/contracts:** source template/workflow documentation and
fixture expectations; old source remains canonical. **Risk:** medium.  
**A2 assurance:** an evaluator selects a non-software/domain variant to prove
the contract does not require a programming shape.  
**Exit criteria:** lifecycle states have transition meaning; material category
rules support `not_applicable`/owned unknown; v1 compatibility is explicit;
distinct evaluator approves evidence.

## T-003 — Enforce lifecycle and completeness at scaffold and delivery gates

**Objective:** update scaffold/template/validators so an unrendered or generic
v2 brief cannot pass Human Visibility, baseline, Tasks Ready or delivery
claims, while a truthful, varied brief can.  
**Requirement IDs:** FR-001–FR-005 | **AC:** AC-001, AC-003, AC-004  
**Outcome/increment:** an empty HTML can no longer be presented as a SPEC.  
**Validation:** V-001, V-003, V-REG-001–003 | **Why now:** contract is approved.

**Scope:** targeted Python/template/workflow changes and regression tests.
**Out of scope:** browser/network services, rewriting legacy packages, forced
visual design, or claiming a validator judges strategy quality.  
**Expected files/contracts:** `scripts/new_initiative.py`, relevant validators,
workflow/rules/template and fixtures. **Risk:** high.  
**A2 assurance:** unit/CLI positives and negatives plus browser-request/manual
HTML check; evaluator verifies failure is actionable and source-safe.  
**Exit criteria:** fresh v2 scaffold fails closed; generic/source-divergent
fixtures fail; complete varied v2 fixture passes; v1 branch is preserved;
distinct evaluator approves evidence.

## T-004 — Prove broad-domain briefs and rendered delivery quality

**Objective:** regenerate the complete mock suite in disposable roots and
review the actual HTML decision packages, not only their Markdown.  
**Requirement IDs:** FR-002–FR-004 | **AC:** AC-002, AC-004  
**Outcome/increment:** demonstrates that the fix is general and that rendered
briefs remain useful for stakeholders.  
**Validation:** V-002, V-004, V-REG-003 | **Why now:** implementation is ready
for adversarial use.

**Scope:** eight mock domains, deterministic commands, local-server rendered
checks and an independent qualitative review. **Out of scope:** treating a
single fixture as proof of all future domains; rewriting a package solely to
make it visually uniform.  
**Expected files/contracts:** disposable mock-run evidence, audit table,
screenshots/reviewer records and synchronized 018 brief/progress. **Risk:** medium.  
**A2 assurance:** deterministic suite reports limits; independent reviewer
judges decision usefulness and identifies residual blind spots.  
**Exit criteria:** all eight packages have HTML inspected; deterministic pass/
fail records are truthful; qualitative findings are dispositioned; the user is
given the HTML-first result; distinct evaluator approves evidence.

## Tasks decision

**Tasks Ready:** approved in D-018-03 after the independently reviewed v2
coverage was refreshed and D-018-04 approved Human Visibility. **Authorized
now:** only T-001. **Blocking conditions for T-002–T-004:** predecessor task
must be done with approved evidence.
