"""Closed, ordered source inventory for v2 stakeholder-brief contracts."""

from __future__ import annotations


V2_EVIDENCE_REFERENCE_SOURCES = (
    "spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md",
    "decision-log.md", "progress.md", "run-state.yaml",
)
V2_SUPPORT_SOURCES = ("ratchet.md",)
V2_REQUIRED_SOURCES = V2_EVIDENCE_REFERENCE_SOURCES + V2_SUPPORT_SOURCES
