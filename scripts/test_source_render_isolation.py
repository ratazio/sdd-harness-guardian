#!/usr/bin/env python3
"""Prove source→brief isolation with real mock facts, not keyword filtering."""

from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path

from render_stakeholder_brief import provenance_error


ROOT = Path(__file__).resolve().parents[1]
NEWS_REQUEST = ROOT / "testes" / "spec-mock-test.md"
RECONCILIATION_REQUEST = ROOT / "testes" / "mock-tests" / "02-backend-reconciliation-api.md"
NEWS_FACT = "PATCH /api/v1/admin/posts/:id"
RECONCILIATION_FACT = "SettlementBatch"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(*, source: str, digest: str, fact: str, locator: str) -> str:
    return "<section %s>%s</section>" % (
        provenance_attributes(source=source, digest=digest, fact=fact, locator=locator),
        fact,
    )


def provenance_attributes(*, source: str, digest: str, fact: str, locator: str) -> str:
    fragment_digest = hashlib.sha256(fact.encode("utf-8")).hexdigest()
    return (
        'data-source="%s" data-source-section="%s" '
        'data-coverage="represented" data-source-digest="sha256:%s" '
        'data-source-fragment="%s" data-source-fragment-sha256="sha256:%s"'
    ) % (source, locator, digest, fact, fragment_digest)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    news_request = NEWS_REQUEST.read_text(encoding="utf-8")
    reconciliation_request = RECONCILIATION_REQUEST.read_text(encoding="utf-8")
    require(NEWS_FACT in news_request, "news/blog fixture no longer contains the required PATCH fact")
    require(
        RECONCILIATION_FACT in reconciliation_request,
        "reconciliation fixture no longer contains the required SettlementBatch fact",
    )

    with tempfile.TemporaryDirectory(prefix="source-render-isolation-") as temporary:
        root = Path(temporary)
        target = root / "specs" / "001-reconciliation"
        foreign = root / "specs" / "002-news-blog"
        target.mkdir(parents=True)
        foreign.mkdir(parents=True)
        target_source = target / "spec.md"
        foreign_source = foreign / "spec.md"
        target_source.write_text(reconciliation_request, encoding="utf-8")
        foreign_source.write_text(news_request, encoding="utf-8")

        positive = block(
            source="spec.md",
            digest=digest(target_source),
            fact=RECONCILIATION_FACT,
            locator="Pedido funcional / modelo mínimo",
        )
        require(
            provenance_error(target, positive, "") is None,
            "a target-owned reconciliation fact with its local source digest was rejected",
        )

        foreign_fact = block(
            source="../002-news-blog/spec.md",
            digest=digest(foreign_source),
            fact=NEWS_FACT,
            locator="API concreta / publicação",
        )
        error = provenance_error(target, foreign_fact, "")
        require(
            error == "provenance source is not allowed for this initiative: ../002-news-blog/spec.md",
            f"foreign news/blog fact was not rejected by origin allowlist: {error!r}",
        )
        require(
            NEWS_FACT not in error,
            "isolation error must identify provenance failure, not classify the full foreign fact",
        )

        stale = block(
            source="spec.md",
            digest=digest(foreign_source),
            fact=RECONCILIATION_FACT,
            locator="Pedido funcional / modelo mínimo",
        )
        require(
            provenance_error(target, stale, "") == "provenance digest does not bind the current local source: spec.md",
            "a locally named block with a foreign digest was accepted",
        )

        disguised_foreign = block(
            source="spec.md",
            digest=digest(target_source),
            fact=NEWS_FACT,
            locator="Invented reconciliation locator",
        )
        require(
            provenance_error(target, disguised_foreign, "")
            == "provenance fragment is not present in the current local source: spec.md",
            "a foreign PATCH fact was accepted after being falsely labelled with the local source and digest",
        )

        malformed_visibility = (
            "<section %s><div>fragment deliberately outside the actual block</section>%s"
            % (
                provenance_attributes(
                    source="spec.md",
                    digest=digest(target_source),
                    fact=RECONCILIATION_FACT,
                    locator="Pedido funcional / modelo mínimo",
                ),
                RECONCILIATION_FACT,
            )
        )
        malformed_error = provenance_error(target, malformed_visibility, "")
        require(
            malformed_error
            == "candidate HTML has malformed element nesting: closing element </section> does not match open <div>",
            "a fragment after the effective block close was counted as visible by malformed markup",
        )

    print("RESULT: source-to-brief isolation passed (real PATCH fact rejected by origin, digest, visible fragment and nesting)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
