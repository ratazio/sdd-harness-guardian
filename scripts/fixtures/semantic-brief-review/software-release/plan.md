# Plan — fictional software fixture

The web client calls `GET /api/v1/invoices/export`; the route handler resolves
the signed session tenant, Prisma filters by that tenant, and PostgreSQL enforces
the tenant-indexed query. The trust boundary is the signed session-to-route
handler transition. Rollback is disabling `invoice_export_enabled`; no data
migration occurs.
