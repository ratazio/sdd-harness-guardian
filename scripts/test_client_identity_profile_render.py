#!/usr/bin/env python3
"""Browser contracts for neutral briefs and the opt-in Pearson profile.

These checks cover observable local-only identity, focus, fallback and layout
behaviour. They never decide whether a brief is semantically sufficient.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import shutil
import subprocess
import sys
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
NEUTRAL_BRIEF = "/specs/001-render-control/stakeholder-brief.html"
PEARSON_BRIEF = "/pearson-selected.html"
LOGO = "/.harness/assets/brand/pearson-logo-white.png"
TEMPLATE = ROOT / ".harness" / "templates" / "stakeholder-brief.html"
VIEWPORTS = ((320, 700), (390, 844), (768, 900), (1024, 900), (1440, 960))


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evidence-dir",
        type=Path,
        help="optional directory for screenshots, print PDF and review JSON",
    )
    return parser.parse_args()


@contextlib.contextmanager
def local_server(directory: Path) -> str:
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(directory), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


def assert_no_root_overflow(page, width: int) -> None:
    dimensions = page.evaluate("""() => ({
        root: document.documentElement.scrollWidth,
        viewport: window.innerWidth,
        body: document.body.scrollWidth
    })""")
    assert dimensions["root"] <= width, f"root overflow at {width}px: {dimensions}"
    assert dimensions["body"] <= width, f"body overflow at {width}px: {dimensions}"


def rendered_neutral_html() -> str:
    html = TEMPLATE.read_text(encoding="utf-8")
    return html.replace('data-brief-phase="scaffold"', 'data-brief-phase="fixture"', 1).replace(
        "Scaffolded — not ready for review, baseline or delivery",
        "Visual contract fixture — not a stakeholder brief",
        1,
    ).replace(
        "Author canonical sources, then render a decision brief.",
        "Verify vendor-neutral and selected-profile rendering under real browser conditions.",
        1,
    )


def rendered_pearson_html() -> str:
    html = rendered_neutral_html().replace(
        'data-client-identity-profile="vendor-neutral"',
        'data-client-identity-profile="pearson"',
        1,
    ).replace("data-harness-brief-shell", "data-harness-pearson-shell", 1)
    html = html.replace(
        "</style>",
        ".brief-client-logo{display:flex;align-items:center;min-height:5rem;margin-top:16px;"
        "padding:1rem 1.25rem;background:#0b004a;border-radius:18px}.brief-client-logo img"
        "{display:block;width:clamp(8rem,12vw,11rem);max-width:100%;height:auto}"
        ":root{--navy:#0b004a;--lavender:#f3f2fe}</style>",
        1,
    )
    return html.replace(
        "</div>\n<header class=\"brief-header\"",
        "</div><a class=\"brief-client-logo\" href=\"#decision\" aria-label=\"Pearson — decisão da iniciativa\">"
        "<img src=\"../../.harness/assets/brand/pearson-logo-white.png\" width=\"175\" height=\"53\" alt=\"\"></a>"
        "\n<header class=\"brief-header\"",
        1,
    )


def main() -> int:
    args = parse_args()
    evidence_dir = args.evidence_dir.resolve() if args.evidence_dir else None
    if evidence_dir:
        evidence_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="identity-profile-render-consumer-") as temporary:
        consumer_root = Path(temporary)
        scaffold = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "new_initiative.py"), "render-control", "--consumer-root", str(consumer_root)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert scaffold.returncode == 0, scaffold.stderr
        initiative = consumer_root / "specs" / "001-render-control"
        assert not (initiative / "stakeholder-brief.html").exists(), "scaffolding must remain source-only"
        assert TEMPLATE.is_file(), "render test requires the canonical visual fixture"
        (initiative / "stakeholder-brief.html").write_text(rendered_neutral_html(), encoding="utf-8")
        assert not (consumer_root / ".harness" / "assets" / "brand" / "pearson-logo-white.png").exists(), (
            "vendor-neutral fixture must not receive a Pearson asset"
        )
        (consumer_root / "pearson-selected.html").write_text(rendered_pearson_html(), encoding="utf-8")
        logo_destination = consumer_root / ".harness" / "assets" / "brand" / "pearson-logo-white.png"
        logo_destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / ".harness" / "assets" / "brand" / "pearson-logo-white.png", logo_destination)

        with local_server(consumer_root) as base, sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                requests: list[str] = []
                logo_statuses: list[int] = []
                viewport_metrics: list[dict[str, float | int | str]] = []
                context = browser.new_context(viewport={"width": 1440, "height": 960})
                page = context.new_page()
                page.on("request", lambda request: requests.append(request.url))
                page.on(
                    "response",
                    lambda response: logo_statuses.append(response.status)
                    if response.url.endswith(LOGO)
                    else None,
                )

                page.goto(base + NEUTRAL_BRIEF, wait_until="networkidle")
                assert page.locator("html").get_attribute("data-client-identity-profile") == "vendor-neutral"
                assert page.locator(".brief-client-logo").count() == 0
                assert not any(url.endswith(LOGO) for url in requests), requests
                assert page.locator("[role=tabpanel]").evaluate_all(
                    "nodes => nodes.filter(node => !node.hidden && getComputedStyle(node).display !== 'none').length"
                ) == 1, "only the selected route may be visibly rendered after enhancement"

                requests.clear()
                page.goto(base + PEARSON_BRIEF, wait_until="networkidle")
                assert page.locator("html").get_attribute("data-client-identity-profile") == "pearson"
                logo_link = page.locator(".brief-client-logo")
                assert logo_link.get_attribute("role") is None
                assert logo_link.get_attribute("aria-label") == "Pearson — decisão da iniciativa"
                image = logo_link.locator("img")
                assert image.get_attribute("src") == "../../.harness/assets/brand/pearson-logo-white.png"
                assert image.get_attribute("width") == "175"
                assert image.get_attribute("height") == "53"
                assert image.get_attribute("alt") == ""
                assert all(url.startswith(base) for url in requests), requests
                assert any(url.endswith(LOGO) for url in requests), requests
                assert logo_statuses == [200], logo_statuses

                for width, height in VIEWPORTS:
                    page.set_viewport_size({"width": width, "height": height})
                    assert_no_root_overflow(page, width)
                    metrics = page.evaluate(
                        """() => ({
                            h1_font_size_px: Number.parseFloat(getComputedStyle(document.querySelector('h1')).fontSize),
                            logo_width_px: Number.parseFloat(getComputedStyle(document.querySelector('.brief-client-logo img')).width),
                            root_scroll_width: document.documentElement.scrollWidth,
                            body_scroll_width: document.body.scrollWidth
                        })"""
                    )
                    viewport_metrics.append({"viewport": f"{width}x{height}", **metrics})
                    if width in (320, 390):
                        assert 128 <= metrics["logo_width_px"] <= 176, metrics
                        assert metrics["h1_font_size_px"] >= 40, metrics
                    if evidence_dir:
                        page.screenshot(path=str(evidence_dir / f"pearson-{width}x{height}.png"))

                page.evaluate("document.body.style.zoom = '2'")
                assert_no_root_overflow(page, 1440)
                page.evaluate("document.body.style.zoom = ''")
                page.locator("#tab-impact").click()
                assert page.locator("#impact").is_visible()
                assert "view=impact" in page.url
                page.locator("#tab-impact").focus()
                page.keyboard.press("ArrowRight")
                assert page.locator("#tab-execution").get_attribute("aria-selected") == "true"
                assert page.locator("#execution").is_visible()
                assert page.locator("#execution").get_attribute("aria-current") is None
                assert page.locator("#tab-execution").get_attribute("aria-current") == "page"
                assert "view=execution" in page.url
                assert page.locator("[role=tabpanel]").evaluate_all(
                    "nodes => nodes.filter(node => !node.hidden && getComputedStyle(node).display !== 'none').length"
                ) == 1
                page.go_back(wait_until="networkidle")
                assert page.locator("#impact").is_visible()
                assert "view=impact" in page.url
                page.emulate_media(reduced_motion="reduce", media="screen")
                assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")

                print_path = evidence_dir / "pearson-print.pdf" if evidence_dir else consumer_root / "pearson-print.pdf"
                page.pdf(path=str(print_path), print_background=True)
                assert print_path.is_file() and print_path.stat().st_size > 1_000, "print PDF was not produced"
                context.close()

                no_script_context = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
                no_script = no_script_context.new_page()
                no_script.goto(base + PEARSON_BRIEF, wait_until="networkidle")
                notice = no_script.locator('[data-noscript-fallback="continuous-reading"]')
                assert notice.is_visible(), "no-script fallback must disclose that continuous reading is not tab navigation"
                assert "não equivale" in notice.inner_text(), notice.inner_text()
                assert no_script.locator("[role=tabpanel]").count() == 8
                assert no_script.locator("[role=tabpanel]").evaluate_all("nodes => nodes.every(node => !node.hidden)")
                assert_no_root_overflow(no_script, 390)
                no_script_context.close()
            finally:
                browser.close()

        if evidence_dir:
            (evidence_dir / "render-review.json").write_text(
                json.dumps(
                    {
                        "consumer": "fresh source-only scaffold with separate neutral and explicitly selected Pearson fixtures",
                        "neutral": "no Pearson logo request or DOM hook",
                        "pearson": "same-origin approved local logo; focus, responsive, no-script, print and reduced-motion checks passed",
                        "viewports": [f"{width}x{height}" for width, height in VIEWPORTS],
                        "viewport_metrics": viewport_metrics,
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )

    print("Client identity profile render: PASS (neutral default has no Pearson asset; selected Pearson is local, accessible and resilient)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
