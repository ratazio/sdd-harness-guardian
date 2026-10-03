#!/usr/bin/env python3
"""Guard the narrow autonomous-recovery instruction for executive briefs.

This test does not score prose, generate HTML, or weaken lifecycle evidence.
It protects the operational instruction that a recoverable composition finding
is repaired and re-reviewed by agents in the same run instead of becoming a
routine requester-approval wait.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def require(path: str, *phrases: str) -> None:
    content = (ROOT / path).read_text(encoding="utf-8")
    for phrase in phrases:
        assert phrase in content, f"{path} is missing autonomous-composition instruction: {phrase}"


def main() -> int:
    require(
        ".harness/skills/executive-brief-composition/SKILL.md",
        "## Handoff direto A → B",
        "relato final encerra",
        "Não execute produto",
    )
    require(
        ".harness/skills/executive-brief-experience-review/SKILL.md",
        "Visite as oito abas",
        "Repare diretamente no mesmo HTML",
        "Não confunda esse reviewer histórico com o reparador 3",
    )
    require(
        ".harness/skills/rendered-brief-decision-review/SKILL.md",
        "conclusão factual não é `approve`",
        "nenhum terceiro agente/validador semântico",
        "reparo direto 3",
    )
    require(
        ".harness/workflows/sdd-lifecycle.md",
        "then the same B",
        "Do not add another semantic gate",
        "Relevant legacy re-review remains confined to this branch",
    )
    print("SPEC 028 autonomous composition-recovery instruction contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
