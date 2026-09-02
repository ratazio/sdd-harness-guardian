# Tasks: 011-stakeholder-brief-client-identity-profile

**Status:** validation done — T-001–T-004 done  
**Spec:** [spec.md](./spec.md)  
**Plan:** [plan.md](./plan.md)  
**Validation plan:** [validation-plan.md](./validation-plan.md)  
**Last updated:** 2026-08-26

## Task ledger

| ID | Status | Title | Dependencies | Risk | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|---|
| T-001 | done | Define opt-in selection, reference boundary and approval record | none | high | platform-engineering | identity_gate_review | evidence/T-001.md |
| T-002 | done | Package local Pearson assets and foundation tokens safely | T-001 done | high | platform-engineering | identity_gate_review | evidence/T-002.md |
| T-003 | done | Apply semantic operational variants to brief components | T-002 done | medium | t003_builder | t003_visual_review | evidence/T-003.md |
| T-004 | done | Prove accessibility, offline fallback and profile isolation | T-001–T-003 done | high | platform-engineering | t004_release_review | evidence/T-004.md |

### T-001 — Define opt-in selection, reference boundary and approval record

**Status:** done — independently approved in D-009  
**Objective:** choose the smallest canonical profile-selection location and
record that design.md is visual reference only, with explicit brand owner and
U-001/U-003 disposition.  
**FR/AC:** FR-001, FR-009–FR-011; AC-001, AC-008–AC-009.  
**Outcome/increment:** generic consumers cannot accidentally acquire Pearson
identity, and selected release knows its owner/approval boundary.  
**Scope:** inventory current consumer/template metadata; select one source;
define selected/unselected fixture contract and approval record.  
**Out of scope:** download asset, modify CSS/HTML, claim legal permission or
style a brief.  
**Contracts/dependencies:** none; output is canonical decision/guidance only.  
**Risk/assurance:** high/A2; profile leakage or fake legal authority is
cross-consumer harm.  
**Validation/evidence:** V-001, V-008, E-002; selection matrix, source
decision and independent evaluator result in evidence/T-001.md.  
**Why now:** asset/CSS work must not begin before its opt-in and authority
boundary is recoverable.  
**Exit:** U-003 resolved; U-001 owner/path explicit; negative fixture defined;
no implementation claimed. Independent evaluation approved in D-009.

### T-002 — Package local Pearson assets and foundation tokens safely

**Status:** done — independently approved in D-011  
**Objective:** implement local approved asset workflow, navy/lavender token
layer, typography fallback and protected brand header.  
**FR/AC:** FR-002, FR-003, FR-006–FR-008; AC-002, AC-003, AC-006–AC-009.  
**Outcome/increment:** selected fixture loads no remote brand resource and
renders readable Pearson foundation; generic fixture remains untouched.  
**Scope:** local logo/font path/checksum/source record, token CSS, header/base
components, focus/reduced motion and safe fallback.  
**Out of scope:** marketing hero/photo, impact/coverage redesign, runtime
theme picker, legal approval inference.  
**Contracts/dependencies:** T-001 approved; selected profile record plus
brand-owner U-001/U-004 evidence.  
**Risk/assurance:** high/A2; logo/contrast/offline failures are blocking.  
**Validation/evidence:** V-002, V-003, V-006, V-009, M-001/M-002; asset scan,
contrast/focus notes and evaluator decision in evidence/T-002.md.  
**Why now:** semantic component styling needs a safe foundation, not ad hoc
colours.  
**Exit:** local asset/ratio/header verified; no hotlink/filter; fallback
works; evaluator accepted evidence in D-011.

### T-003 — Apply semantic operational variants to brief components

**Status:** done — independently approved in D-014  
**Objective:** turn existing/010 semantic roles into coherent Pearson
operational cards and differentiated impact/coverage/proof/decision views.  
**FR/AC:** FR-004–FR-007, FR-011; AC-004–AC-007, AC-010.  
**Outcome/increment:** brief has hierarchy/variation that explains
relationships without losing provenance, table equivalent or task density.  
**Scope:** component variants for tab/snapshot/diagram/task/impact/risk/
validation/decision/coverage; responsive card transformations.  
**Out of scope:** change source facts/gates, introduce image-only visual,
customer data, hero photography or remote dependency.  
**Contracts/dependencies:** T-002 approved; consume 010 role catalogue when
available, otherwise current v2 hooks.  
**Risk/assurance:** medium/A2; visual improvement must remain operational and
accessible.  
**Validation/evidence:** V-004, V-005, V-006, M-003/M-006, E-001; selected
render comparisons and reviewer decision in evidence/T-003.md.  
**Why now:** component semantics need foundation and selection safety first.  
**Exit:** all material views have appropriate variant; impact/coverage retain
semantic equivalents; reviewer accepted fidelity/proportionality in D-014.

### T-004 — Prove accessibility, offline fallback and profile isolation

**Status:** done — D-018 approval, refreshed baseline and terminal synchronization recorded in D-019  
**Objective:** make release evidence show selected style does not regress
accessibility/offline behavior or contaminate unselected consumers.  
**FR/AC:** FR-001, FR-006–FR-010; AC-001, AC-006–AC-010.  
**Outcome/increment:** commands/manual checks/evaluators produce a recoverable
profile evidence pack and rollback/deselection path.  
**Scope:** negative fixture, no-network scan, browser modes, grayscale/zoom/
print, existing v2 checks, brand/semantic review and ratchet.  
**Out of scope:** deploy to client, actual legal decision, application
rebranding or replacing independent semantic review.  
**Contracts/dependencies:** T-001–T-003 approved; U-001/U-004 need brand owner
record before selected release evidence can be accepted.  
**Risk/assurance:** high/A2; final release gate.  
**Validation/evidence:** V-001, V-006–V-009, M-004/M-005, E-002/E-003 and
validate_bundle; transcripts, review decisions and rollback in evidence/T-004.md.  
**Why now:** only final after the selected and generic variants actually exist.  
**Exit:** selected/unselected isolation, offline/access modes and owner record
proved; independent evaluator approved; state/progress/ratchet and final
Human Visibility baseline are synchronized in D-019.
