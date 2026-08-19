#!/usr/bin/env python3
"""Deterministic structural checks for the SDD Harness Guardian source bundle."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []
CHECKS = 0


V1_REQUIRED_BRIEF_IDS = (
    "decision-snapshot",
    "scope",
    "validation",
    "decision",
)
V2_REQUIRED_BRIEF_IDS = (
    "decision-snapshot",
    "scope",
    "architecture",
    "impact",
    "execution",
    "validation",
    "evolution",
    "decision",
    "coverage",
)
V1_REQUIRED_BRIEF_SOURCES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "validation-plan.md",
)
V1_BRIEF_TEMPLATE_PLACEHOLDERS = ("<initiative>", "<YYYY-MM-DD>")
V2_BRIEF_TEMPLATE_PLACEHOLDERS = ("{{initiative}}", "{{date}}", "{{risk}}", "{{size}}")
REQUIRED_BRIEF_SHELL_HOOKS = ("brief-shell", "brief-header", "decision-register", "impact-evidence", "decision-actions")


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read(relative: str) -> str:
    path = ROOT / relative
    check(path.is_file(), f"missing required file: {relative}")
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def manifest_list(manifest: str, key: str) -> list[str]:
    match = re.search(
        rf"(?ms)^{re.escape(key)}:\s*\n((?:  - [^\n]+\n?)+)", manifest
    )
    check(match is not None, f"manifest list missing or empty: {key}")
    if not match:
        return []
    return [
        line.removeprefix("  - ").strip()
        for line in match.group(1).splitlines()
        if line.startswith("  - ")
    ]


def manifest_mapping(manifest: str, key: str) -> dict[str, str]:
    match = re.search(
        rf"(?ms)^{re.escape(key)}:\s*\n((?:  [a-z0-9_]+: [^\n]+\n?)+)", manifest
    )
    check(match is not None, f"manifest mapping missing or empty: {key}")
    result: dict[str, str] = {}
    if match:
        for line in match.group(1).splitlines():
            name, value = line.strip().split(":", 1)
            result[name] = value.strip()
    return result


def stakeholder_brief_errors(html: str, *, rendered: bool) -> list[str]:
    """Return stable structural contract failures for a stakeholder brief."""
    errors: list[str] = []
    marker = re.search(r'\bdata-harness-brief-design\s*=\s*["\'](v1|v2)["\']', html)
    if not marker:
        return ["missing stakeholder brief design-lineage marker: data-harness-brief-design=\"v1\" or \"v2\""]
    lineage = marker.group(1)
    for section_id in (V2_REQUIRED_BRIEF_IDS if lineage == "v2" else V1_REQUIRED_BRIEF_IDS):
        pattern = rf'\bid\s*=\s*["\']{re.escape(section_id)}["\']'
        if not re.search(pattern, html):
            errors.append(f"missing stakeholder brief section id: {section_id}")
    if lineage == "v1":
        for source in V1_REQUIRED_BRIEF_SOURCES:
            if not re.search(rf'href\s*=\s*["\']{re.escape(source)}["\']', html):
                errors.append(f"missing stakeholder brief source link: {source}")
    for hook in REQUIRED_BRIEF_SHELL_HOOKS:
        if not re.search(rf'\bclass\s*=\s*["\'][^"\']*\b{re.escape(hook)}\b', html):
            errors.append(f"missing stakeholder brief canonical shell hook: {hook}")

    placeholders = V2_BRIEF_TEMPLATE_PLACEHOLDERS if lineage == "v2" else V1_BRIEF_TEMPLATE_PLACEHOLDERS
    if rendered:
        for placeholder in placeholders:
            if placeholder in html:
                errors.append(f"unresolved stakeholder brief placeholder: {placeholder}")
    else:
        for placeholder in placeholders:
            if placeholder not in html:
                errors.append(f"missing stakeholder brief template placeholder: {placeholder}")
        if lineage == "v2":
            for attribute in ("data-source", "data-source-section", "data-coverage"):
                if attribute not in html:
                    errors.append(f"v2 stakeholder brief template lacks provenance attribute: {attribute}")
    return errors


def main() -> int:
    version = read("VERSION").strip()
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "VERSION is not SemVer")

    manifest = read("manifest.yaml")
    check(f"version: {version}" in manifest, "manifest version differs from VERSION")
    status_match = re.search(r"(?m)^status: ([a-z_]+)$", manifest)
    check(status_match is not None, "manifest status is missing")
    manifest_status = status_match.group(1) if status_match else ""
    check(
        manifest_status in {"draft", "release_candidate", "ready", "deprecated"},
        f"invalid manifest status: {manifest_status}",
    )
    check(f"## {version}" in read("CHANGELOG.md"), "changelog lacks current version")

    for required in (
        "README.md",
        "INSTALL.md",
        ".harness/AGENTS.md",
        "docs/architecture.md",
        "docs/operating-model.md",
        "docs/acceptance-criteria.md",
        "docs/harness-audit-framework.md",
        "prompts/build-the-guardian.md",
        "prompts/use-in-consumer-project.md",
        "scripts/new_initiative.py",
        "scripts/smoke_test_scaffolder.py",
        "scripts/validate_human_visibility.py",
        "scripts/test_validate_human_visibility.py",
        "scripts/test_factory_guardian_fixture.py",
        "docs/consumer-enforcement.md",
        ".harness/templates/stakeholder-brief-design.md",
    ):
        read(required)

    acceptance = read("docs/acceptance-criteria.md")
    if manifest_status == "ready":
        check("**Bundle Ready:** yes" in acceptance, "ready status lacks Bundle Ready: yes")
        check("- [ ]" not in acceptance, "ready status has unchecked release criteria")

    registries = {
        "agents": (".harness/agents", ".md"),
        "skills": (".harness/skills", "/SKILL.md"),
        "workflows": (".harness/workflows", ".md"),
        "rules": (".harness/rules", ".md"),
    }
    for key, (base, suffix) in registries.items():
        names = manifest_list(manifest, key)
        check(len(names) == len(set(names)), f"duplicate manifest entries in {key}")
        for name in names:
            relative = f"{base}/{name}{suffix}"
            read(relative)

    templates = manifest_mapping(manifest, "artifact_templates")
    required_template_keys = {
        "spec",
        "stakeholder_brief",
        "plan",
        "tasks",
        "impact_map",
        "validation_plan",
        "evidence_pack",
        "run_state",
        "progress",
        "handoff",
        "decision_log",
        "ratchet_log",
        "ratchet_entry",
        "reproduction",
        "specs_index",
    }
    check(
        required_template_keys <= templates.keys(),
        "artifact_templates lacks required template keys",
    )
    for relative in templates.values():
        read(relative)

    stakeholder_brief = read(templates["stakeholder_brief"])
    for error in stakeholder_brief_errors(stakeholder_brief, rendered=False):
        check(False, error)

    for rule in manifest_list(manifest, "rules"):
        content = read(f".harness/rules/{rule}.md")
        check("## Soft rule" in content, f"critical rule lacks Soft rule: {rule}")
        check(
            "## Hard mirror recommendation" in content,
            f"critical rule lacks Hard mirror recommendation: {rule}",
        )
        check("Recommended check:" in content, f"rule lacks check name: {rule}")

    terminal_tokens = (
        "evidence",
        "needs_evaluation",
        "approved",
        "done",
        "Evaluator",
    )
    for workflow in ("sdd-lifecycle", "sdd-feature", "sdd-bugfix", "sdd-refactor"):
        content = read(f".harness/workflows/{workflow}.md")
        for token in terminal_tokens:
            check(token in content, f"{workflow} lacks terminal gate token: {token}")

    recovery = read(".harness/workflows/interruption-recovery.md").lower()
    check(
        "common lifecycle" in recovery and "missing evidence" in recovery,
        "interruption recovery must delegate terminal transitions to common lifecycle",
    )
    for workflow in manifest_list(manifest, "workflows"):
        content = read(f".harness/workflows/{workflow}.md")
        check(
            "in_progress -> done" not in content,
            f"workflow contains forbidden direct terminal transition: {workflow}",
        )

    run_state = read(".harness/templates/run-state.yaml")
    check("```" not in run_state, "run-state.yaml must not contain Markdown fences")
    for key in (
        "schema_version:",
        "initiative_id:",
        "initiative_sequence:",
        "initiative_slug:",
        "summary:",
        "quality_gates:",
        "independent_evaluation_done:",
        "evidence_pack_ready:",
        "validation_done:",
        "resume_required:",
        "next_safe_step:",
    ):
        check(key in run_state, f"run-state template lacks key: {key}")

    for skill in manifest_list(manifest, "skills"):
        content = read(f".harness/skills/{skill}/SKILL.md")
        check(content.startswith("---\n"), f"skill lacks frontmatter: {skill}")
        for field in ("name:", "description:", "version:", "maturity:", "risk_level:"):
            check(field in content, f"skill {skill} lacks frontmatter field: {field}")
        check("maturity: stable" in content, f"skill not stable: {skill}")

    if ERRORS:
        print(f"Bundle validation FAILED: {len(ERRORS)} error(s), {CHECKS} checks.")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"Bundle validation passed: {CHECKS} checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
