# Tasks: 019-rendered-brief-decision-quality-gate

**Status:** completed — all evidence packs independently approved  
**Spec:** ./spec.md | **Plan:** ./plan.md | **Validation:** ./validation-plan.md  
**Last updated:** 2026-08-30

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Calibrate five-lens decision-quality review with adaptive fixtures | none | high | codex-root | spec019_t001_evaluation | `evidence/T-001.md` |
| T-002 | done | Enforce review-record integrity and lifecycle blocking without semantic scoring | T-001 | high | codex-root | spec019_t002_evaluation | `evidence/T-002.md` |
| T-003 | done | Publish reusable rendered-review protocol and source-to-HTML repair guidance | T-001, T-002 | medium | codex-root | spec019_t003_evaluation | `evidence/T-003.md` |
| T-004 | done | Execute and independently assess the full mock suite through all five lenses | T-001, T-002, T-003 | high | codex-root | /root/review_t004_arch_system | `evidence/T-004.md` |

## T-001 — Calibrate five-lens decision-quality review with adaptive fixtures

**Status:** done  
**Objective:** Make a decision-poor but structurally valid rendered brief
observable as a qualitative failure, while preserving a valid concise
alternative for unrelated/non-software work.  
**Requirement IDs:** FR-001, FR-002, FR-003, FR-004, FR-005, FR-007  
**Acceptance criteria IDs:** AC-001, AC-002, AC-004  
**Outcome served:** The gate measures recoverable decisions instead of visual
compliance.  
**Increment:** Reusable review schema, negative/positive fixtures and test
wiring that distinguish structural PASS from role evidence.  
**Why now:** The fixture makes later parser and skill work testable without
inventing a universal HTML pattern.  
**Dependencies:** none | **Risk:** high | **Builder:** codex-root | **Evaluator:** spec019_t001_evaluation | **Human approval:** not_required

### Scope

- Add role questions/capabilities with `material`, `not_material` (reason) and
  `insufficient` dispositions.
- Add a structurally valid, fresh decision-poor fixture and a rich varied
  positive fixture with a justified alternative representation.
- Require source→lost fact→recovery action and re-review in fixture evidence.

### Out of scope

- Altering generated mock HTMLs, enforcing tab counts or scoring prose.

### Expected files/contracts

`scripts/fixtures/semantic-brief-review/`, calibration test and concise
documentation necessary to make the fixture executable.

### Validation and evidence

- `python scripts/test_semantic_brief_review_calibration.py`
- `python scripts/validate_bundle.py`
- Evidence names role results, fixture locators, commands and why the positive
  fixture is not a visual exception.

### Exit criteria

- [x] negative fixture remains structurally valid but has at least three
  expected material role revisions;
- [x] positive varied fixture is eligible without tabs/diagram quota;
- [x] evaluator distinct from builder approves evidence;
- [x] sources, brief, ledger and state are synchronized.

## T-002 — Enforce review-record integrity and lifecycle blocking without semantic scoring

**Status:** done  
**Objective:** Reject a claimed decision-quality-ready state unless the
independent five-lens review record is complete, fresh and materially resolved.  
**Requirement IDs:** FR-001, FR-002, FR-006, FR-007, FR-008  
**Acceptance criteria IDs:** AC-002, AC-003  
**Outcome served:** A deterministic PASS cannot masquerade as qualitative
approval.  
**Increment:** Additive state/evidence verification plus regression tests.  
**Why now:** It converts calibrated human judgment into an enforceable
lifecycle claim while retaining human semantic judgment.  
**Dependencies:** T-001 | **Risk:** high | **Builder:** codex-root | **Evaluator:** spec019_t002_evaluation | **Human approval:** not_required

### Scope

- Define an additive review record with identities, role scope, locators/digests,
  materiality, finding disposition and re-review anchor.
- Validate missing/stale/self-approved/unresolved record cases deterministically.
- Preserve existing v1/v2, Pearson and Human Visibility behavior.

### Out of scope

- DOM/content quality score, mandatory layout/diagram or replacement of human
review.

### Validation and evidence

- `python scripts/test_validate_human_visibility.py`
- focused new review-record contract test
- `python scripts/validate_bundle.py`
- Evidence includes failure and success fixture outputs and evaluator decision.

### Exit criteria

- [x] unresolved material finding blocks a quality-ready assertion;
- [x] finding-specific accountable resolution needs corrected-render and
originating-role re-review;
- [x] parser only verifies record/state, never semantic quality;
- [x] distinct evaluator approves evidence and synchronized state.

## T-003 — Publish reusable rendered-review protocol and source-to-HTML repair guidance

**Status:** done  
**Objective:** Give builders and reviewers a repeatable local serving,
multi-role inspection and canonical-source repair workflow.  
**Requirement IDs:** FR-001, FR-003, FR-004, FR-005, FR-007  
**Acceptance criteria IDs:** AC-003, AC-004  
**Outcome served:** Agents genuinely inspect rendered HTML against its request
and sources rather than reporting a script-only pass.  
**Increment:** Bundle skill/protocol and updated reviewer guidance.  
**Why now:** The gate record is only useful when agents can collect honest,
safe, accessible observations.  
**Dependencies:** T-001, T-002 | **Risk:** medium | **Human approval:** not_required

### Scope

- Document local-server/rendered inspection, five role lenses, evidence
template, redaction and HTML regeneration from canonical-source repair.
- Update the Human Visibility/Spec Guardian path where necessary.
- Demonstrate keyboard/local inspection on fixtures.

### Out of scope

- Installing a browser automation product, changing profile/logo policy, or
requiring any fixed visual layout.

### Validation and evidence

- serve fixture over `127.0.0.1`; inspect browser-visible HTML and focus flow
- `python scripts/validate_bundle.py`
- Evaluator verifies instructions remain adaptive and source-backed.

### Exit criteria

- [x] reviewers receive request, sources and served HTML locators;
- [x] every material loss leads to source repair—not HTML-only patch;
- [x] evidence contains no copied source bodies;
- [x] distinct evaluator approves evidence/state sync.

## T-004 — Execute and independently assess the full mock suite through all five lenses

**Status:** done  
**Objective:** Demonstrate the gate on eight varied requests and identify
generator/system gaps honestly.  
**Requirement IDs:** FR-001–FR-008  
**Acceptance criteria IDs:** AC-001–AC-005  
**Outcome served:** The Guardian can be trusted across diverse work, not one
fixture.  
**Increment:** Disposable complete mock run, 8×5 role matrix, source repair /
rerender/re-review trace and executive conclusion.  
**Why now:** This is the end-to-end proof that the new process catches the
failure reported by the user.  
**Dependencies:** T-001, T-002, T-003 | **Risk:** high | **Human approval:** not_required

### Scope

- Generate all mock specs into a new disposable root.
- Serve each HTML locally; each role receives original request, canonical
sources and page.
- Repair source-backed system/generator issues when found; regenerate and
re-review; report residual gaps honestly.

### Out of scope

- Altering fixture requests to force a pass, treating a structural command as
qualitative approval, or presenting Markdown as the primary deliverable.

### Validation and evidence

- full mock-lab command and local server logs
- 8×5 matrix, per-finding source/HTML locators and correction/re-review chain
- `python scripts/test_semantic_brief_review_calibration.py`
- `python scripts/test_validate_human_visibility.py`
- `python scripts/validate_bundle.py`

### Exit criteria

- [x] all eight have separately stated structural and qualitative results;
- [x] no material `REVISE` is hidden; each is corrected/re-reviewed or has a
finding-specific accountable residual disposition;
- [x] final reviewed surfaces point to rendered HTML, not Markdown;
- [x] distinct evaluator approves evidence and final state reflects reality.

## Allowed transitions

`pending → ready → in_progress → needs_evaluation → approved → done`; a
revision returns to `in_progress`. No task is done without approved evidence,
distinct identities and state synchronization.
