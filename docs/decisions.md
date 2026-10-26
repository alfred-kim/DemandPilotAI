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
