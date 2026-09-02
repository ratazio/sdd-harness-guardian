# Conditional Source & Corpus Semantic Review Record

Use this record when a source can be materially relevant only in the effective
case (for example, a ratchet with an active preventive rule, or an explicitly
empty ratchet whose absence changes governance). This is a **human-review
hook**, not a classifier, score, visual quota, or automatic approval.

## Reviewer-declared inputs

- **Review ID:** `CSR-...`
- **Reviewer identity:** `<independent identity; must differ from composer>`
- **Request locator and digest:** `<path/locator>` · `sha256:<digest>`
- **Candidate HTML locator and digest:** `<path/locator>` · `sha256:<digest>`
- **Corpus manifest:** every input the reviewer actually considered, as
  `<path> | <locator or whole-file scope> | sha256:<digest>`.

The reviewer, not code, decides which sources or relations are material. A
deterministic consumer may only preserve this declared manifest, identity,
digest, and record scope; it must not infer missing sources, domain labels,
prose quality, visual counts, or semantic sufficiency.

## Conditional source inventory

For each conditional source considered, record one case-specific disposition.

| Source | State in this corpus | Locator and provenance | Recoverable brief location | Human rationale |
|---|---|---|---|---|
| `ratchet.md` | `material_rule` / `empty_with_reason` / `not_applicable` | `<source locator + digest>` | `<candidate locator>` | `<why this state changes or does not change a decision>` |

`material_rule` must make the source fact recoverable: **trigger, check,
owner, consequence, and provenance**. `empty_with_reason` must make both the
empty state and its reason recoverable. `not_applicable` is valid only with a
source-backed reason; it is never a silent omission.

## Corpus-driven decision review

Answer from the request, declared corpus, and candidate—not from a fixed
domain taxonomy:

1. **Decision still impossible from HTML:** `<none, or a concrete decision>`.
2. **Finding (when non-none):** source path + locator, candidate locator,
   lost/weakened fact or relation, decision impact, concrete source repair,
   rerender, and re-review owner.
3. **N/A dispositions:** for every source or relation the reviewer declines
   to require, provide a cited source locator and a case-specific reason.
4. **Verdict:** `APPROVE` or `REVISE`, with rationale. `REVISE` remains
   blocking until repair, rerender, and a new independent review.

Passing structural checks around this record never approves the candidate.
Only an independent reviewer can make its semantic verdict.

## Optional machine-readable integrity envelope

Where a consumer needs a deterministic handoff, it may attach a separate
`semantic-review-integrity/v1` JSON envelope. It carries only the distinct
composer/reviewer identities, `candidate_and_rendered_artifact` record scope,
candidate and rendered `{path, locator, sha256}` bindings, the reviewer-declared
corpus manifest with the same fields, and the human `APPROVE` or `REVISE`
verdict. `scripts/validate_semantic_review_record.py` verifies that bounded
envelope. It must not be used to infer materiality, classify the case, count
text or visuals, or convert an `APPROVE` token into automatic approval.
