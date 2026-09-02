#!/usr/bin/env python3
"""Contract checks for reviewed editorial-exception promotion semantics."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

from editorial_exceptions import composition_editorial_findings, reviewed_editorial_exception_error
from render_stakeholder_brief import canonical_composition_manifest, decision_record_digest, review_record_content
from test_render_stakeholder_brief import SCAFFOLDER, RENDERER, candidate_with_block_digests, ready_to_render, valid_candidate_html, with_lifecycle_markers


def candidate(exception_markup: str = "") -> str:
    return """<!doctype html><html data-composition-contract=\"v3\"><body>
<section id=\"execution\">T-001</section><section id=\"validation\"></section>
<section id=\"composition-exceptions\">%s</section></body></html>""" % exception_markup


def exception(identifier: str, finding: str, *, expires: str = "2099-01-01") -> str:
    return f"""### Editorial exception {identifier}
Finding: {finding}
Source: tasks.md#T-002
Target: #execution
Decision impact: A reunião não vê a segunda tarefa no resumo de execução.
Residual risk: O decisor pode subestimar o trabalho pendente.
Owner: brief-experience-owner
Decision: proceed
Expires: {expires}
Next action: Recompor a projeção antes do próximo refresh.
"""


def visible(identifier: str, finding: str) -> str:
    return f"""<article data-composition-exception-id=\"{identifier}\">
<p>{finding}</p><p>tasks.md#T-002</p><p>#execution</p>
<p>A reunião não vê a segunda tarefa no resumo de execução.</p>
<p>O decisor pode subestimar o trabalho pendente.</p>
<p>brief-experience-owner</p><p>Recompor a projeção antes do próximo refresh.</p>
</article>"""


def cli_integration() -> None:
    """The real renderer must reject by default and promote only with the flag."""
    with tempfile.TemporaryDirectory(prefix="sdd-editorial-cli-") as directory:
        root = Path(directory)
        created = subprocess.run([sys.executable, str(SCAFFOLDER), "editorial-exception", "--sequence", "901", "--consumer-root", str(root)], text=True, capture_output=True, check=False)
        assert created.returncode == 0, created.stderr
        initiative = root / "specs" / "901-editorial-exception"
        ready_to_render(initiative / "run-state.yaml")
        (initiative / "tasks.md").write_text("Task inventory\n\n## T-901\n", encoding="utf-8")
        (initiative / "validation-plan.md").write_text("Proof inventory\n\n| V-901 | claim |\n", encoding="utf-8")
        html = valid_candidate_html().replace("<html ", '<html data-composition-contract="v3" ', 1)
        raw_findings = composition_editorial_findings(initiative, html)
        assert len(raw_findings) == 2 and raw_findings[0].startswith("missing task projection:") and raw_findings[1].startswith("missing validation projection:"), raw_findings
        findings = raw_findings
        html = html.replace("</body>", '<section id="composition-exceptions">' + visible("EX-901", findings[0]) + visible("EX-902", findings[1]) + "</section></body>", 1)
        candidate_html = candidate_with_block_digests(initiative, with_lifecycle_markers(html))
        candidate_html = candidate_html.replace(">candidate</p>", ">Authored candidate; exact pre-render review has passed; ready only for guarded refresh; not rendered/deliverable; Human Visibility and Tasks Ready false.</p>", 1)
        record = "# Decision Log\n\n## D-900 — reviewed candidate composition\n\nAuthor: fixture-author\nReviewer: fixture-reviewer\nReview outcome: approve\nComposition provenance: verified\nHuman attestation: confirmed\n"
        record += f"Composition manifest SHA-256: {canonical_composition_manifest(initiative)}\nCandidate SHA-256: pending\n\n" + exception("EX-901", findings[0]) + "\n" + exception("EX-902", findings[1])
        decision = initiative / "decision-log.md"
        decision.write_text(record, encoding="utf-8")
        initial_digest = decision_record_digest(review_record_content(record, "D-900") or "")
        candidate_html = candidate_html.replace("decision-record-sha256:PENDING", "decision-record-sha256:" + initial_digest, 1)
        signed = record.replace("Candidate SHA-256: pending", "Candidate SHA-256: " + hashlib.sha256(candidate_html.encode("utf-8")).hexdigest(), 1)
        final_digest = decision_record_digest(review_record_content(signed, "D-900") or "")
        candidate_html = candidate_html.replace("decision-record-sha256:" + initial_digest, "decision-record-sha256:" + final_digest, 1)
        signed = record.replace("Candidate SHA-256: pending", "Candidate SHA-256: " + hashlib.sha256(candidate_html.encode("utf-8")).hexdigest(), 1)
        assert decision_record_digest(review_record_content(signed, "D-900") or "") == final_digest, "candidate signature changed stable decision context"
        decision.write_text(signed, encoding="utf-8")
        resolved = review_record_content(signed, "D-900") or ""
        assert decision_record_digest(resolved) == final_digest, "review-record resolver lost nested exception context"
        assert "decision-record-sha256:" + final_digest in candidate_html, "candidate did not bind final decision record digest"
        candidate = initiative / "candidate.html"
        candidate.write_text(candidate_html, encoding="utf-8")
        assert composition_editorial_findings(initiative, candidate_html) == findings, (findings, composition_editorial_findings(initiative, candidate_html))
        refused = subprocess.run([sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate)], text=True, capture_output=True, check=False)
        assert refused.returncode != 0 and "--allow-reviewed-editorial-exceptions" in refused.stderr, refused.stderr
        promoted = subprocess.run([sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate), "--allow-reviewed-editorial-exceptions"], text=True, capture_output=True, check=False)
        assert promoted.returncode == 0, promoted.stderr


def main() -> int:
    template = (Path(__file__).resolve().parent.parent / ".harness" / "templates" / "decision-log.md").read_text(encoding="utf-8")
    for required in ("### Editorial exception EE-001", "Finding:", "Source:", "Target:", "Decision impact:", "Residual risk:", "Owner:", "Decision: proceed", "Expires:", "Next action:"):
        assert required in template, f"decision-log template drifted from exception parser: {required}"
    with tempfile.TemporaryDirectory() as directory:
        initiative = Path(directory)
        (initiative / "tasks.md").write_text("## T-001\n## T-002\n", encoding="utf-8")
        (initiative / "validation-plan.md").write_text("| V-025-01 | claim |\n", encoding="utf-8")
        html = candidate()
        findings = composition_editorial_findings(initiative, html)
        assert findings == [
            "missing task projection: T-002",
            "missing validation projection: V-025-01",
        ], findings
        assert "normal correction" in (reviewed_editorial_exception_error(html, "", findings, False) or "")

        task_finding, validation_finding = findings
        reviewed = exception("EX-001", task_finding) + "\n" + exception("EX-002", validation_finding)
        disclosed = candidate(visible("EX-001", task_finding) + visible("EX-002", validation_finding))
        assert reviewed_editorial_exception_error(disclosed, reviewed, findings, True) is None

        missing_owner = reviewed.replace("Owner: brief-experience-owner\n", "", 1)
        assert "missing reviewed field(s): Owner" in (reviewed_editorial_exception_error(disclosed, missing_owner, findings, True) or "")
        expired = reviewed.replace("2099-01-01", "2000-01-01", 1)
        assert "EX-001 is expired" in (reviewed_editorial_exception_error(disclosed, expired, findings, True) or "")
        invisible = candidate(visible("EX-001", task_finding))
        assert "exactly match" in (reviewed_editorial_exception_error(invisible, reviewed, findings, True) or "")
        hidden = candidate('<article hidden data-composition-exception-id="EX-001">hidden</article>' + visible("EX-002", validation_finding))
        assert "rendered visibly" in (reviewed_editorial_exception_error(hidden, reviewed, findings, True) or "")
    cli_integration()
    print("Reviewed editorial-exception contracts passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
