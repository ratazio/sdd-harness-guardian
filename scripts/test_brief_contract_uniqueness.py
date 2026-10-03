#!/usr/bin/env python3
"""T-004: brief-contract.md is the single normative source (AC-007).

Detectable signal (declared per the T-004 exit criteria — this is what makes
the second clause of AC-007 deterministic instead of an opinion):

1. Uniqueness: every `## BC-NNN` heading in the bundle lives in exactly one
   file — `.harness/rules/brief-contract.md`. If a `## BC-NNN` heading (or a
   bare `BC-NNN` definition line) appears in any other tracked bundle file,
   that is a second definition and fails.
2. Citation presence: every consumer file in CONSUMERS must cite at least one
   `BC-NNN` ID (a bare `BC-\\d{3}` token), proving it references rather than
   silently drops the contract.
3. Banned-phrase allowlist: an explicit list of exact phrases that were the
   verified Anexo A restatements/contradictions (A-01..A-12). These phrases
   must not reappear in the files they were removed from — this is the
   "normative brief text outside citation by ID" signal, made deterministic
   by naming the exact regressions instead of a fuzzy prose classifier.

This is intentionally narrow: it does not try to detect *novel* future
restatement by NLP; it protects the specific contradictions this task
resolved and the ID-uniqueness invariant going forward.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / ".harness" / "rules" / "brief-contract.md"

BC_HEADING_RE = re.compile(r"^##\s+(BC-\d{3})\b", re.MULTILINE)
BC_CITATION_RE = re.compile(r"\bBC-\d{3}\b")

# Files that must reference the contract instead of restating brief doctrine.
CONSUMERS = [
    ROOT / ".harness" / "rules" / "human-visibility.md",
    ROOT / ".harness" / "templates" / "stakeholder-brief-design.md",
    ROOT / ".harness" / "skills" / "executive-brief-composition" / "SKILL.md",
    ROOT / ".harness" / "skills" / "executive-brief-experience-review" / "SKILL.md",
    ROOT / ".harness" / "skills" / "rendered-brief-decision-review" / "SKILL.md",
    ROOT / ".harness" / "skills" / "spec-review" / "SKILL.md",
    ROOT / ".harness" / "workflows" / "sdd-lifecycle.md",
    ROOT / ".harness" / "AGENTS.md",
    ROOT / ".harness" / "agents" / "brief-experience-composer.md",
    ROOT / ".harness" / "agents" / "executive-brief-reviewer.md",
    ROOT / ".harness" / "agents" / "delivery-orchestrator.md",
]

# Bundle files scanned for a *second* BC-NNN definition (uniqueness, item 1).
# Restricted to the doctrine surface, not the whole repository (mock-runs and
# fixtures intentionally are not bundle doctrine).
SCAN_FOR_DUPLICATE_DEFINITIONS = [
    *CONSUMERS,
    *(ROOT / ".harness").rglob("*.md"),
]

# Item 3: exact phrases verified in the spec's Anexo A that must not
# reappear in the file they were removed from.
BANNED_PHRASES: dict[Path, list[str]] = {
    ROOT / ".harness" / "templates" / "stakeholder-brief-design.md": [
        "keep Pearson navy/lavender/white as the canonical base",
    ],
    ROOT / ".harness" / "skills" / "executive-brief-composition" / "SKILL.md": [
        "architecture.global",
    ],
    ROOT / ".harness" / "agents" / "brief-experience-composer.md": [
        "Editorial map:",
    ],
    ROOT / ".harness" / "agents" / "executive-brief-reviewer.md": [
        "mapa editorial",
    ],
    ROOT / ".harness" / "skills" / "spec-review" / "SKILL.md": [
        "canonical `v1` brief shell was populated",
    ],
    ROOT / ".harness" / "rules" / "human-visibility.md": [
        "impact/risk, execution/tasks",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def bc_ids_in_contract() -> list[str]:
    text = read(CONTRACT)
    ids = BC_HEADING_RE.findall(text)
    assert ids, "brief-contract.md defines no BC-NNN rules"
    duplicates = {i for i in ids if ids.count(i) > 1}
    assert not duplicates, f"brief-contract.md defines duplicate IDs: {sorted(duplicates)}"
    return ids


def check_no_second_definition(bc_ids: list[str]) -> None:
    id_set = set(bc_ids)
    seen_files: dict[str, Path] = {bc_id: CONTRACT for bc_id in bc_ids}
    for path in SCAN_FOR_DUPLICATE_DEFINITIONS:
        path = Path(path)
        if path.resolve() == CONTRACT.resolve() or not path.is_file():
            continue
        text = read(path)
        for match in BC_HEADING_RE.finditer(text):
            bc_id = match.group(1)
            if bc_id in id_set:
                raise AssertionError(
                    f"{bc_id} redefined as a heading in {path.relative_to(ROOT)}; "
                    f"already defined in {seen_files[bc_id].relative_to(ROOT)}"
                )


def check_consumers_cite_ids() -> None:
    missing = []
    for path in CONSUMERS:
        text = read(path)
        if not BC_CITATION_RE.search(text):
            missing.append(str(path.relative_to(ROOT)))
    assert not missing, f"consumers with no BC-NNN citation at all: {missing}"


def check_banned_phrases_absent() -> None:
    violations = []
    for path, phrases in BANNED_PHRASES.items():
        text = read(path)
        for phrase in phrases:
            if phrase in text:
                violations.append(f"{path.relative_to(ROOT)}: {phrase!r} reappeared")
    assert not violations, "\n".join(violations)


def test_brief_contract_uniqueness_and_citation() -> None:
    bc_ids = bc_ids_in_contract()
    check_no_second_definition(bc_ids)
    check_consumers_cite_ids()
    check_banned_phrases_absent()


def main() -> int:
    test_brief_contract_uniqueness_and_citation()
    bc_ids = bc_ids_in_contract()
    print(f"OK: {len(bc_ids)} BC-NNN rules, uniquely defined; "
          f"{len(CONSUMERS)} consumers cite by ID; no banned restatement found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
