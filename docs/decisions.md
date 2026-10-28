# Decision log

## 2026-10-26 — Milestone 1 foundation

- Use a `src` package layout named `demandpilot` to keep importable application
  code separate from repository-level tools and tests.
- Use `pyproject.toml` with compatible-release dependency ranges and one `dev`
  extra. Pydantic Settings is the only application dependency at this stage;
  database, data, API, and ML libraries are deferred until their milestones.
- Keep initial settings limited to environment, logging, data path, and database
  connection-pool foundations. Validate values at startup and never log settings.
- Configure standard-library logging centrally, supporting readable text and
  structured JSON output.
- Use pytest, Ruff, and mypy as the initial local and CI checks.
## 2026-10-27 — Milestone 3 database design direction

The following design decisions are approved as the direction for the database schema. Final migration approval remains pending until the schema specifies the required enforcement and recovery safeguards.

- Use the provisional M5 active-window rule: the earlier of the first positive sale and first applicable sell-price week. This is a modeling boundary, not proof of actual product availability.
- Use canonical upserts for corrected source deliveries, immutable source-file checksum references, and audit events recording corrections.
- Use PostgreSQL `jsonb` for quarantine payloads and regional SNAP flags, with payload-size limits and strict exclusion of credentials, secrets, and unnecessary sensitive information.
- Set the initial M5 business timezone to `America/New_York`. Preserve source business dates as `date` values.
- Defer row-level security (RLS), table partitioning, and price-interval exclusion constraints pending operational evidence. Tenant-scoped queries and tenant-scoped foreign keys remain required. Price-overlap protection under concurrent writes must be resolved before accepting price imports.
- Use a dedicated, disposable `demandpilot_test` database and restricted test role for integration tests. Existing development databases must not be used for destructive tests.

### Required safeguards before migration approval

- Define null-safe database constraints for `daily_sales.data_status` and `units`.
- Specify source-file retention and record-level correction provenance.
- Define concurrency-safe import idempotency and retry behavior.
- Define recovery for interrupted `RUNNING` batches.
- Prevent overlapping price intervals under concurrent writes.
- Enforce and test audit-log append-only permissions.

**Status:** Design direction approved; schema and migrations not yet approved.
