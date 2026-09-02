---
name: rendered-brief-decision-review
description: Review a generated stakeholder brief against its request and canonical sources when a decision-ready rendered HTML claim needs independent evidence; do not use for formatting-only checks.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Rendered Brief Decision Review

## Purpose

Determine whether the rendered HTML preserves the material decisions of the
request and canonical artifacts. This is an independent qualitative review;
structural, provenance and freshness validators remain useful but do not decide
meaning, architecture fitness or visual quality.

## Inputs and independence

Collect locators and SHA-256 digests for: the originating request, applicable
canonical sources, and the exact rendered HTML. Record the artifact locator,
reviewer identity, timestamp and preview environment. For an `APPROVE` that
will be recorded as a post-render review, the evidence must name the exact
`http://127.0.0.1[:port]/...` URL used to inspect the final route surface; a
file-path-only or screenshot-only reading cannot support that claim. Do not
copy request bodies, secrets or PII into review evidence.

Reviewer identities are distinct from the source author and current builder.
Choose only the review lenses that are proportionate to the initiative's
material decisions, risk and domain. A chosen lens may be `not_material` only
with a source-backed reason; `insufficient` or material `REVISE` blocks quality
approval.

## Review method

1. Read the request and canonical artifacts before opening the page. Identify
   the decision that each chosen lens must make without Markdown.
2. Serve and open the rendered HTML through `127.0.0.1` in an appropriate
   available viewer. Check visible content, progressive retrieval,
   keyboard/focus behavior where navigation exists, reduced-motion and print
   fallback where applicable.
3. For each material lens record `APPROVE` or `REVISE`, materiality, source and
   HTML locators, decision impact, and the answer to: “what remains impossible
   without opening Markdown?”
4. For material relationships, require a connected accessible model when
   components, data, trust, state or failure behavior affect the decision. A
   labelled relationship table, semantic flow or accessible SVG can qualify;
   typographic arrows alone cannot. For a concise non-software or low-relation
   case, record why prose or a short ordered handoff is proportional.
5. For material execution, recover workfront, dependency/order, increment,
   risk/authority, validation/evidence and next safe step from the HTML. Do
   not demand a task-card format.

## Repair and disposition

Every material finding names: finding ID; request/source/HTML locators; lost or
weakened fact; decision impact; canonical source recovery action; and the
originating-reviewer re-review required after rerender. When the required fact
already exists in canonical sources, dispatch that correction to the composer,
regenerate the HTML and serve it again in the same run; do not stop to ask the
user for routine approval. Ask externally only for genuinely new authority,
scope, or an absent material fact. Never close a finding by editing HTML alone.

Only a genuinely editorial finding may be promoted under a reviewed editorial
exception. The append-only decision record and its visible HTML projection must
state its ID, finding, source → rendered target, decision impact, residual
risk, accountable owner, decision to proceed, expiry and next action. Preserve
in that record the exact pre-render candidate SHA-256 and composition-manifest
SHA-256 binding; the exception cannot waive integrity, provenance, lifecycle or
security findings. It permits only the named finding to be shown for review and
does not make Human Visibility or Tasks Ready true. Correction, rerender and
originating-reviewer re-review remain the next path; otherwise the finding is
blocking.

## Output

Write the review record inside the initiative `evidence/` directory. State
`Preview URL:` and `Preview environment:` alongside the reviewer and exact
rendered digest. Keep its
metadata compatible with the opt-in `brief_review.quality_review_*` fields.
State separately: deterministic checks PASS/FAIL, qualitative decision review
APPROVE/REVISE, findings, automatic recovery attempted, and the next safe step.
Do not report a deterministic PASS as stakeholder approval, and do not report a
recoverable `REVISE` as a reason no final HTML could be constructed.
