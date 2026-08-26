# Release safety summary — fictional software fixture

## Outcome

Operators can enable the invoice-export release without exposing another
tenant's data. The demonstrable increment is a bounded release decision with a
named rollback and proof path.

## Decision and acceptance

The release owner may enable the flag only after tenant-isolation integration
tests pass. AC-S1: an export request returns only records owned by its session
tenant. AC-S2: a failed isolation probe keeps the flag off and pages the
release owner.
