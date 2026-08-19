# T-002 rendered checks

These artifacts were generated from `../../../stakeholder-brief.html` with local
Microsoft Edge through Playwright on 2026-08-19:

```powershell
@'
from pathlib import Path
from playwright.sync_api import sync_playwright
brief = Path('specs/006-stakeholder-brief-complete-decision-surface/stakeholder-brief.html').resolve()
out = Path('specs/006-stakeholder-brief-complete-decision-surface/evidence/rendered/T-002')
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    for name, width in [('desktop', 1440), ('narrow', 390)]:
        page = browser.new_page(viewport={'width': width, 'height': 900})
        page.goto(brief.as_uri())
        assert page.evaluate('innerWidth == document.documentElement.scrollWidth')
        page.screenshot(path=str(out / f'{name}.png'), full_page=True)
        if name == 'desktop': page.pdf(path=str(out / 'print.pdf'), print_background=True)
        page.close()
    page = browser.new_page(viewport={'width': 390, 'height': 900}, java_script_enabled=False)
    page.goto(brief.as_uri())
    assert page.evaluate('innerWidth == document.documentElement.scrollWidth')
    page.screenshot(path=str(out / 'no-script-narrow.png'), full_page=True)
    browser.close()
'@ | python -
```

- `desktop.png`: JavaScript-enabled 1440px rendering.
- `narrow.png`: JavaScript-enabled 390px rendering.
- `no-script-narrow.png`: 390px rendering with JavaScript disabled.
- `print.pdf`: print-media rendering; collapsed details are forced visible by
  CSS.

The script asserted `scrollWidth == innerWidth` at 1440px and 390px, collapsed
details with JavaScript, open details without it, native keyboard focus, and
print visibility of deep content.
