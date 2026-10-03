# Spec: support docs taxonomy migration (T-003 non-software fixture)

## Scope

The support knowledge base moves from a flat wiki of 240 articles to a three-tier taxonomy; article content is reorganized and re-linked, not rewritten.

## Impact

Affected audiences: support agents who link articles in tickets, self-serve customers who search the KB directly, and docs maintainers who own the article backlog.

## Migration sequence

An old URL resolves through a 301 redirect to its new taxonomy page for six months before the redirect table is retired.

## Risk

A broken inbound link from a third-party integration or a search engine result loses a customer mid-task; the control is a permanent redirect table checked before every publish.

## Content inventory

Getting-started articles move to the Onboarding category; billing articles move to the Billing category; the remaining long tail moves to a single Reference category pending a second pass.
