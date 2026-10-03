#!/usr/bin/env python3
"""Guard FR-012 / AC-014: the brief review chain has exactly two passes.

This test is doctrine, not code. It does not render anything, does not
compose a brief and does not replace the qualitative review itself (NG-007).
It proves two things:

1. The normative contract (`.harness/rules/brief-contract.md`, BC-009)
   declares exactly two independent passes with disjoint mandates: (a) a
   merged model/construction review before projection, and (b) a
   meaning-and-experience review of the HTML served over loopback.
2. No *operative* bundle artifact (agents, skills, workflows, rules other
   than the contract itself) instructs, reintroduces or reassigns a third
   pass — either by re-splitting the merged pass (a) back into a separate
   "coverage review" and "construction review", or by assigning execution of
   either pass to a role other than the Executive Brief Reviewer.

`.harness/templates/plan.md` §9.1 (`#### Independent construction review`)
was the legacy pre-model construction-record review. T-008 removed that
section along with the skeleton/candidate mechanism it described; the
construction record now lives in `brief-model.yaml` and its review is BC-009
pass (a), as declared below. `.harness/templates/**` remains excluded from
the split-detector (`BUNDLE_GLOBS` below) because a template is scaffolding
text, not an operative instruction.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTRACT_PATH = ROOT / ".harness" / "rules" / "brief-contract.md"

# Files that carry operative instructions and must not, on their own, instruct
# a third pass or reassign pass (a)/(b) execution. Excludes brief-contract.md
# (the declaration itself) and .harness/templates/** (scaffolding text, not an
# operative instruction).
BUNDLE_GLOBS = [
    ".harness/agents/*.md",
    ".harness/skills/**/SKILL.md",
    ".harness/workflows/*.md",
    ".harness/rules/*.md",
]

COVERAGE_SIGNAL = re.compile(r"coverage review|revis(?:ã|a)o de cobertura", re.IGNORECASE)
CONSTRUCTION_SIGNAL = re.compile(
    r"construction[- ]review|construction-plan review|revis(?:ã|a)o de constru", re.IGNORECASE
)
FUSION_SIGNAL = re.compile(r"BC-009|pass \(a\)|pass a\b", re.IGNORECASE)

# Verbs that mean "this role performs/executes the review", as opposed to
# merely confirming, citing or referencing that it happened.
PERFORM_VERB = r"(conduzir|realizar|executar|perform|conducts?|runs?|carries? out)"
REVIEW_NOUN = r"(revis(?:ã|a)o de cobertura|revis(?:ã|a)o p[oó]s-render|pass \(a\)|pass \(b\)|coverage review|post-render review|rendered[- ]html review)"
REASSIGNMENT_PATTERN = re.compile(PERFORM_VERB + r".{0,80}" + REVIEW_NOUN, re.IGNORECASE)


def _bundle_files() -> list[Path]:
    files: list[Path] = []
    for pattern in BUNDLE_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def find_split_pass_violation(text: str) -> str | None:
    """Detect the pre-FR-012 pattern: coverage review and construction review
    named as two separate things, without citing the BC-009 fusion."""
    if COVERAGE_SIGNAL.search(text) and CONSTRUCTION_SIGNAL.search(text):
        if not FUSION_SIGNAL.search(text):
            return "mentions coverage review and construction review as separate items without citing BC-009/pass (a)"
    return None


def find_reassignment_violation(text: str, *, is_reviewer_agent: bool) -> str | None:
    """Detect a non-reviewer role instructed to itself perform pass (a)/(b)."""
    if is_reviewer_agent:
        return None
    match = REASSIGNMENT_PATTERN.search(text)
    if match:
        return f"assigns execution of a review pass to a non-reviewer role: {match.group(0)!r}"
    return None


def test_contract_declares_exactly_two_disjoint_passes() -> None:
    content = CONTRACT_PATH.read_text(encoding="utf-8")
    marker = "## BC-009"
    start = content.index(marker)
    end = content.index("\n## BC-010", start)
    section = re.sub(r"\s+", " ", content[start:end])

    direct, legacy = section.split("**v2 historical only:**", 1)
    assert "**v3 default:**" in direct
    sequence = ["executive-brief-composition", "rendered-brief-decision-review", "executive-brief-experience-review", "report."]
    positions = [direct.index(token) for token in sequence]
    assert positions == sorted(positions), "v3 authorship/content/visual/report order regressed"
    assert "same B" in direct and "same HTML" in direct
    assert "No pre-render review" in direct and "third validation" in direct
    assert "independent pass (a)" in legacy and "pass (b)" in legacy
    assert "brief_coverage_ready" in legacy and "human_visibility_ready" in legacy
    assert "No third pass and no Spec Guardian rendered review" in legacy
    assert "qualitative, not a semantic score" in legacy
    # T-008 removed the transitional skeleton-inheritance structural check
    # this used to carve out; BC-009 no longer needs to name it.


def test_no_bundle_artifact_splits_the_merged_pass() -> None:
    violations = []
    for path in _bundle_files():
        if path == CONTRACT_PATH:
            continue
        text = path.read_text(encoding="utf-8")
        problem = find_split_pass_violation(text)
        if problem:
            violations.append(f"{path.relative_to(ROOT)}: {problem}")
    assert not violations, "third-pass split reintroduced:\n" + "\n".join(violations)


def test_no_bundle_artifact_reassigns_a_pass_to_a_non_reviewer_role() -> None:
    # The reviewer's own agent file and the two skills it operates
    # (BC-009's named implementation of pass a/b) are the sole permitted
    # place where "perform pass (a)/(b)" language belongs.
    reviewer_owned = {
        ROOT / ".harness" / "agents" / "executive-brief-reviewer.md",
        ROOT / ".harness" / "skills" / "executive-brief-experience-review" / "SKILL.md",
        ROOT / ".harness" / "skills" / "rendered-brief-decision-review" / "SKILL.md",
    }
    violations = []
    for path in _bundle_files():
        if path == CONTRACT_PATH:
            continue
        text = path.read_text(encoding="utf-8")
        problem = find_reassignment_violation(text, is_reviewer_agent=(path in reviewer_owned))
        if problem:
            violations.append(f"{path.relative_to(ROOT)}: {problem}")
    assert not violations, "review pass reassigned outside the Executive Brief Reviewer:\n" + "\n".join(violations)


def test_spec_guardian_confirms_but_does_not_perform_either_pass() -> None:
    text = (ROOT / ".harness" / "agents" / "spec-guardian.md").read_text(encoding="utf-8")
    assert "conduzir a revisão de cobertura" not in text
    assert "realizar uma leitura pós-render" not in text
    assert "BC-009" in text
    assert "sem executar" in text or "não repete" in text or "não performa" in text


def test_detector_catches_a_reintroduced_third_pass_fixture() -> None:
    """Prove the detector is not a no-op: feed it synthetic pre-029 doctrine
    that reintroduces three overlapping reviews, and confirm it fires."""
    split_fixture = (
        "## Responsabilidades\n\n"
        "- conduzir a revisão de cobertura comparando fontes e headings;\n"
        "- conduzir a revisão de construção antes do skeleton;\n"
        "- realizar a revisão do HTML renderizado após o build.\n"
    )
    assert find_split_pass_violation(split_fixture) is not None, (
        "detector failed to catch a fixture that names coverage review and "
        "construction review as two separate passes"
    )

    reassignment_fixture = (
        "## Agent: Spec Guardian\n\n"
        "## Responsabilidades\n\n"
        "- conduct the coverage review independently before the skeleton is copied;\n"
    )
    assert (
        find_reassignment_violation(reassignment_fixture, is_reviewer_agent=False) is not None
    ), "detector failed to catch a non-reviewer role instructed to perform a pass"

    # Sanity: the same fixture must NOT fire when it is the reviewer agent's
    # own file, or when BC-009 fusion is cited alongside the two nouns.
    assert find_reassignment_violation(reassignment_fixture, is_reviewer_agent=True) is None
    fused_fixture = split_fixture + "\nBoth are merged into BC-009 pass (a).\n"
    assert find_split_pass_violation(fused_fixture) is None


def main() -> int:
    test_contract_declares_exactly_two_disjoint_passes()
    test_no_bundle_artifact_splits_the_merged_pass()
    test_no_bundle_artifact_reassigns_a_pass_to_a_non_reviewer_role()
    test_spec_guardian_confirms_but_does_not_perform_either_pass()
    test_detector_catches_a_reintroduced_third_pass_fixture()
    print("Review chain contract (FR-012/AC-014/NG-007) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
