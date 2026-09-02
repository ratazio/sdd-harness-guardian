# Reproduction evidence — SPEC 020 T-004 systemic findings

**Run:** `testes/mock-runs/20260828-spec020-t004-r5` · **Bundle revision:**
`1568928e5f973a8b3c0602c26c4f22caf72dc450` · **Date:** 2026-08-28.

## Method and deterministic boundary

All eight cases were scaffolded into newly unused consumer roots, canonical
sources were recomposed, and each candidate was promoted through the current
source/review/provenance guard. The r5 HTMLs were served on local HTTP
`127.0.0.1:8877`; each reviewer first read only that HTML and then compared the
original request, all canonical Markdown sources and the HTML. No previous
baseline, review outcome or approval was copied.

Before review, each `validate_human_visibility.py` run had no structural
failure, but correctly failed its ten pending gates: Human Visibility/Tasks
Ready, quality-review metadata and baseline were absent. This is an expected
pre-review result, not a deterministic approval. No `--write-baseline` command
was run because every case later received at least one material `REVISE`.

Legend for the matrix: `A/A` is Pass 1 APPROVE / Pass 2 APPROVE; `A/R1` is
Pass 1 APPROVE / Pass 2 REVISE severity P1; `R1/R1` is both passes REVISE P1.
Reviewers are independent from builder `mock-builder-spec020`: architect,
system designer and developer = `/root/t004_architecture_reviews`; delivery
manager, director and C-level = `/root/t004_delivery_exec_reviews`; general
stakeholder = `/root/t004_stakeholder_reviews`.

## Per-mock matrix

| Mock | Request SHA-256 | Markdown-source-set SHA-256 | HTML SHA-256 | Deterministic result | Architect | System designer | Developer | Delivery | Director | C-level | Stakeholder | Baseline/final |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M-001 | `972ac91c76f1b9f0eb5772add7730ff32214aab83badab7cd18f1edea2bb079a` | `66b6d6bc8bc895b5ce95f19798a357ac81909a77394930bf9cf4c59b74afa79a` | `c3ab365ae587638ec7633fcca9471d354d555e0b360136dbef27a7570b0fd4a5` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/R1 | A/R2 | A/R2 | R1/R1 | blocked / REVISE |
| M-002 | `562d990a02817ef21d1c8ab6a8d46cd05c82d308b3293e05205592206ca006d7` | `01eeb075edf76ebc4465a320acd050fcd47977851eb58b81038814f46a07dab0` | `fc430350e8daae7118b4b52f87b128688d39a4de0f7c0e2f73aca4413239714b` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/R1 | A/R1 | A/R1 | R1/R1 | blocked / REVISE |
| M-003 | `034c0ef6d96c9363408c0059446bed787409e774f4d7f9b1a70e5a993204f2f4` | `9b27b8eb94e437d72bd9dcff6fa56440e4c3be74d4e751a785e7e56129e22078` | `7a293c0a884565a1f7acf66202eb5f99c81b9d72efe35846511238e353017e19` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/R1 | A/R1 | A/R1 | R1/R1 | blocked / REVISE |
| M-004 | `11cee48da98d3c13a5b9dfa62577ee10daffcb5d119ea95e35937aba693b3fbc` | `353da7df2ca2529e539020d8b21cbb5637922b529df183435b60533f0e31cd16` | `c465c34db96bb773425f32149c8ce4afd205ab82f6fb1870216ba236e9ebfa84` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/A | A/A | A/A | R1/R1 | blocked / REVISE |
| M-005 | `98b33a0b6e58ef5b09a89547a03275b73c7fe91a18bbf971ce5a8e5e2de32744` | `0f3ee0049c57d983875d910157c7cb82aea27c9bb7fe42a771ae757077c4e656` | `695c83cee3840786ef1092d5e8c8fcc831bbcb9fc735f1f0de64e9ef01eb49a9` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/A | A/A | A/A | R1/R1 | blocked / REVISE |
| M-006 | `6bdce7ba03415cb3bcb235d3b5d3dd378ef995b8a52f9e7773c15c0e9ca52eb5` | `ab73937fd8ee0f837a4dcff2cba257c70eab2f315055a7453762ba95edc90aa3` | `832942f973e643f2aeafc8d72239668af596d1c9a59ced3cfdb311784faccae8` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/A | A/A | A/A | R1/R1 | blocked / REVISE |
| M-007 | `7de393484416d3d99df329c62e3ecc2ef84c81d25bc5579a4d7246dd743d5be6` | `1c0b938e062e8a3315bb90411a0c40a49b1f344ece7deff71ffd6c536de8b9b7` | `e0291d453e0f089d8cb77b77725b8296dbd18803fc69573fbf89d4dd883ebfbb` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/A | A/A | A/A | R1/R1 | blocked / REVISE |
| M-008 | `9c0b6f600ec7be8582d7022c020f7a1ca2eb72812c987ce4c650f8eff2d7c6c6` | `fe45b495c1185ff14be2d015a6dc56ee37357cfb652059c27ac64c77d6f3bab1` | `813d8d22552e5ab5832cf537aad1a0c7b2e28628a437c5f2aef047a6d483ce57` | promotion PASS; HV pending gates | R1/R1 | R1/R1 | R1/R1 | A/A | A/A | A/A | R1/R1 | blocked / REVISE |

## Material findings and required repair

| ID | Recurrence and locator | Impact | Required repair / re-review |
|---|---|---|---|
| F-020-T004-01 | Architect/system/developer: M-001–M-003 `ratchet.md#Ratchet` contains mandatory V-01–V-08/V-01–V-07 and independent review; M-004–M-008 `ratchet.md#Entries` says no entries. Neither state appears in HTML provenance or coverage. | A stakeholder cannot decide post-change regression/governance obligations or know that none exists. | SPEC 021 FR-021-01: inventory conditional material source, project rule or reasoned empty state, add positive/negative regression, rerender then repeat both passes. |
| F-020-T004-02 | Stakeholder: all M-001–M-008 `#architecture` uses four generic nodes and a textual arrow sentence while each request/`plan.md` defines domain-specific relations. Examples: M-002 file/outbox/RabbitMQ/DLQ/revision; M-003 offline state machine/chunk recovery; M-005 PII/local-model/human block/API destination; M-008 Kafka/watermark/DLQ/snapshot promotion. | HTML-first reader cannot approve trust boundaries, recovery, data ownership or operational safety, despite complete source extracts. | SPEC 021 FR-021-02: compose source-driven structured relation appropriate to the domain, add relation-loss negative and cross-domain review, rerender then repeat both passes. |

The two findings recur across materially different domains and are therefore a
systemic Guardian gap, not eight isolated source edits. SPEC 021 was created
as the authorized corrective initiative. Its execution is subsequent work;
these r5 packages remain preserved as failed evidence and must not be modified
into cosmetic passes.
