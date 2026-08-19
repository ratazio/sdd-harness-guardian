# T-005 rendered validation artifacts

**Current result:** PASS after D-018. The pre-rerun F-005-01 screenshots remain
for history only; the final acceptance artifacts are the `*-final.*` files.

Generated locally on 2026-08-19 from the current initiative brief with local
Microsoft Edge through Playwright.

| Artifact | Mode | Result |
|---|---|---|
| `desktop-final.png` | JavaScript enabled, 1440×900 | PASS: no page-wide overflow; seven progressive details collapse after load; keyboard navigation verified. |
| `narrow-final.png` | JavaScript enabled, 390×844 | PASS: no page-wide overflow; both dense tables provide local horizontal scroll. |
| `no-script-narrow-final.png` | JavaScript disabled, 390×844 | PASS: no page-wide overflow; all seven progressive details remain open; both dense tables provide local horizontal scroll. |
| `print-final.pdf` | Print media, A4 | PASS: CSS makes progressive detail content visible. |
| `desktop.png`, `narrow.png`, `no-script-narrow.png`, `print.pdf` | pre-D-018 | Historical evidence of resolved F-005-01; not the final judgment artifacts. |

Keyboard script checks: all eight navigation anchors received focus and activated;
a native details `summary` received focus and toggled. Print-media computed-style
checks confirmed each progressive detail paragraph is visible. The final narrow
checks asserted local scrolling for both `decision-ledger` and `coverage-register`.

This is captured manual evidence, not screenshot CI or an automated semantic
approval.
