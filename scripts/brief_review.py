"""Closed parsing helpers for structured stakeholder-brief review fields."""

from __future__ import annotations


# `brief_review.findings_status` is structured lifecycle input, not reviewer
# prose. Keep this vocabulary small and its spelling canonical so descriptive
# text cannot grant pre-render or Human Visibility readiness.
REVIEW_FINDING_OUTCOMES = frozenset({"not_started", "pending", "pass", "revise"})


def review_finding_outcome(value: str | None) -> str | None:
    """Return one exact canonical outcome, refusing free-text values."""
    if value is None:
        return None
    if value not in REVIEW_FINDING_OUTCOMES:
        allowed = ", ".join(sorted(REVIEW_FINDING_OUTCOMES))
        raise ValueError(
            "brief_review.findings_status must be exactly one of "
            f"{allowed} (lowercase canonical spelling)"
        )
    return value


def yaml_review_finding_outcome(raw_value: str | None) -> str | None:
    """Parse one tiny YAML scalar without normalizing its semantic content.

    Normal YAML quote delimiters are accepted, but embedded quotes and
    whitespace remain part of the value and therefore cannot become ``pass``.
    """
    if raw_value is None:
        return None
    value = raw_value
    if value[:1] in {"\"", "'"} and value[-1:] == value[:1]:
        value = value[1:-1]
    return review_finding_outcome(value)
