# DemandPilot AI — Milestone 1 & 2 Audit

Audit date: 2026-10-26 (Africa/Nairobi)
Project root: `/home/alfred/Documents/DemandPilot AI`
Master specification: `DemandPilot AI Master Engineering Prompt v2 (Comprehensive).md`

## 1. Executive summary

- **Milestone 1: MET / COMPLETE.** The package imports in the active project environment; invalid environment and configuration values are rejected; all 11 tests pass; Ruff lint and mypy pass; the CI workflow exists. Additional Ruff format checking fails, but formatting is not an acceptance criterion in the Milestone 1 roadmap row and is not part of the configured CI checks.
- **Milestone 2: NOT MET / INCOMPLETE.** The raw M5 files are available locally and the previously documented baseline metrics reproduce. However, the project has no M5 loader, data validator, data dictionary/data contracts, quality report, EDA notebook, or written EDA findings/plots. M5 provenance and licence acceptance are not documented. These are explicit Milestone 2 deliverables/acceptance requirements.
- **Go/no-go for Milestone 3: NO-GO.** Milestone 2 has multiple demonstrated mandatory failures. The baseline experiment is relevant to Milestone 4, not a substitute for Milestone 2 ingestion and EDA.
- Git branch is `master`, but the repository has **no commits**. All source, tests, configuration, documentation, and CI files are untracked. There is no committed baseline to use for a clean-checkout comparison. M5 files and generated caches are ignored.
- Project virtual environment: Python 3.14.7, pip 26.2.2. The active project virtual environment was used for checks. The master prompt requires Python 3.11+; CI is configured for 3.11.
- All five expected M5 CSVs exist under `data/raw/m5/`; their sizes, row/column counts, and SHA-256 hashes are recorded below. Data source is consistent with M5 but the repository does not document acquisition, competition-rule acceptance, or licence terms.

## 2. Audit methodology and scope

I read the full 64,004-byte master prompt before evaluating the implementation, then reviewed the relevant requirements in sections 3, 4, 6, 7, 10, 11, 20, 21, 22, 24, 25, and 26. The controlling acceptance criteria are the Milestone 1 and 2 rows in section 25. Sections 7, 10, and 11 detail the M5, ingestion, data contract, and EDA requirements. Sections 21 and 22 inform test/reproducibility recommendations.

The implementation is mapped to the actual `src/demandpilot/` package, as requested. I inspected the repository tree, settings, logging, tests, dependencies, README, CI workflow, ignore rules, decision log, M5 data files, and baseline report. I ran the applicable test/lint/type commands and recomputed baseline and subset quality numbers directly from M5 files.

Git commands showed branch `master`, no commits (`git log` returned “fatal: your current branch 'master' does not have any commits yet”), and every project file other than ignored/generated files was untracked. Thus current-working-tree evidence is primary. Committed-checkout reproducibility is not assessable: a committed checkout would contain none of this implementation, and no commit exists. A clean fresh environment was not created because it would require dependency installation, which the audit rules prohibit without authorization. Existing `.venv` import and checks are not represented as a fresh-install test.

The audit did not modify source, tests, data, or existing documents. Two mutation experiments used copies under `/tmp`; only this report was written to the project.

### Specification scope and checklist conflicts

| Topic | Governing master-prompt scope | Audit treatment |
|---|---|---|
| M5 subset loader, provenance, checksums, quality visibility, real data, no fabrication | Milestone 2, section 25; details in section 7 | Formal M2 criteria |
| EDA notebook, real plots, written findings | Milestone 2, section 25; analyses in section 11 | Formal M2 criterion; absent notebook/report is a failure |
| Data contracts | Milestone 2, section 25; details in section 7.3 | Formal M2 criterion; missing `docs/data_dictionary.md` is a failure |
| Baseline forecasts and metric functions | Milestone 4, section 25 | Additional readiness check only; not used to fail M2 |
| PostgreSQL, quarantine tables, idempotent database imports | Milestone 3, section 25 | Later milestone; not assessed as an M1/M2 failure |
| Leakage-safe features and rolling-origin backtesting | Milestone 4, sections 12 and 25 | Later milestone; not assessed as an M1/M2 failure |
| Full configuration list and clean-checkout setup | Section 22, broader reproducibility requirement | Readiness/documentation finding; M1 checks are limited to its section 25 acceptance row |
| README's Ruff format command | README does not include format check | Format check run as extra diagnostic; not substituted for roadmap's tests/lint/type checks |

## 3. Requirement traceability matrix

| Requirement | Master prompt reference | Implementation/evidence | Status | Notes |
|---|---|---|---|---|
| Package imports | §25, M1 | `src/demandpilot/__init__.py`; import command succeeded from `.venv` | PASS | Actual package is `demandpilot`, not `app`. |
| Configuration rejects invalid values | §25, M1; §22 | `src/demandpilot/settings.py:11-47`; tests in `tests/test_settings.py:23-41`; direct mutation experiments | PASS | Environment is a restricted `Literal`; log level, URL, pool bounds validated. |
| Unit tests pass with counts | §25, M1; §21 | `.venv/bin/python -m pytest --cov=demandpilot --cov-report=term-missing`: 11 passed, 0 failed, 0 skipped | PASS | Coverage 94% (52 statements, 3 missed). |
| Lint and type check pass | §25, M1; §21 | Ruff check: pass; mypy `src`: pass | PASS | Required CI checks are green in the active environment. |
| M1 project foundation deliverables: environment, packaging, settings, logging, Git hygiene, tests, CI skeleton | §25, M1 | `.venv`, `pyproject.toml`, `src/demandpilot/`, `tests/`, `.gitignore`, `.github/workflows/ci.yml` | PASS | Files exist in working tree but are not committed. Fresh setup and committed baseline are not verified. |
| M5 source/licence documented and real data loaded | §7.1, §7.4; §25, M2 | Five local CSVs found and read; no provenance/licence documentation or loader | FAIL | File presence alone does not demonstrate source/licence record or project ingestion. |
| M5 subset loader and quality issues visible | §7.1; §10; §25, M2 | No loader, validation module, or quality report exists in `src/`/`docs/` | FAIL | Direct mandatory implementation gap. |
| EDA notebook and written findings from real data | §11; §25, M2 | No notebook, EDA document, or figures; only `docs/eda-baseline-results.md` with overview and baseline claims | FAIL | The baseline report is not the required EDA notebook/findings. |
| Data contracts | §7.3; §25, M2 | `docs/data_dictionary.md` absent; no contracts found | FAIL | Direct mandatory deliverable gap. |
| No fabricated M5 records/results | §1 honesty; §7.4; §25, M2 | Local dataset exists; independently recomputed reported baseline metrics agree to stated precision | PASS | This does not validate missing data-pipeline deliverables. |
| Baseline metrics and model selection | §25, M4 | `docs/eda-baseline-results.md`; independent re-run matches | PASS (additional, not M2) | Historical one-window comparison is explicitly provisional and limited. |

## 4. Milestone 1 results

### A1. Reproducibility and installation — NOT VERIFIABLE

- README documents `python -m venv .venv`, editable install with `python -m pip install -e '.[dev]'`, then pytest/Ruff/mypy (`README.md:5-23`).
- The currently activated project environment has installed metadata `demandpilot-ai==0.1.0`; import succeeded and resolved to `src/demandpilot/__init__.py`.
- Exact command: `.venv/bin/python -c 'import demandpilot, demandpilot.settings, demandpilot.logging_config; print(demandpilot.__version__, demandpilot.__file__)'` → exit 0; output `0.1.0 /home/alfred/Documents/DemandPilot AI/src/demandpilot/__init__.py`.
- A fresh venv/editable installation was not attempted: it would install dependencies, disallowed by the audit instructions. Therefore current environment import is verified, but fresh-environment README reproducibility is not.
- Committed-checkout reproducibility is unavailable because there are no commits and all implementation files are untracked. This is a limitation, not evidence that current working-tree imports fail.
- `pyproject.toml` declares `requires-python = ">=3.11"`; active Python is 3.14.7. CI uses Python 3.11. No test was run under 3.11 in this audit.

### A2. Quality gates — PASS

| Exact command | Exit | Result | Scope |
|---|---:|---|---|
| `.venv/bin/python -m pytest --cov=demandpilot --cov-report=term-missing` | 0 | 11 passed; 0 failed; 0 skipped; 94% coverage | M1 required |
| `.venv/bin/python -m ruff check .` | 0 | “All checks passed!” | M1 lint required |
| `.venv/bin/python -m mypy src` | 0 | “Success: no issues found in 3 source files” | M1 type check required; actual layout target used |
| `.venv/bin/python -m ruff format --check .` | 1 | Five files would be reformatted | Extra diagnostic; not configured/documented as a required M1 gate |

CI at `.github/workflows/ci.yml:7-19` runs editable installation, pytest with coverage, Ruff lint, and mypy on Python 3.11. No project-level `make check` or equivalent task runner was found. The README and CI do not claim or run format check.

### A3. Dependency management — PASS

`pyproject.toml:1-28` defines package metadata (`demandpilot-ai`), Python `>=3.11`, runtime dependencies `pydantic` and `pydantic-settings`, and a `dev` extra for mypy, pytest, pytest-cov, and Ruff. Runtime and development dependencies are separated; ranges have lower and upper bounds. Heavy dependencies such as LightGBM, XGBoost, MLflow, FastAPI, Streamlit, and Docker tooling are absent, consistent with the current milestone. No lock file exists. The master prompt says to commit a lockfile if the chosen tool produces one; absence is not a demonstrated violation. CI does not pin resolved versions, so reproducibility is limited. pandas and NumPy happen to be installed in `.venv` but are not declared runtime/development dependencies; this does not break M1, but prevents treating those packages as reproducibly available for M2 work.

### A4. Configuration — PASS

`src/demandpilot/settings.py:11-54` uses Pydantic Settings, an environment prefix, documented defaults, Literal validation for development/test/staging/production, bounded DB pool settings, and explicit validation for log level and non-empty URL. `tests/test_settings.py:9-41` covers defaults and invalid environment, level, pool, and URL values. M1 validation is demonstrated. The broad configuration set in section 22 is intended for the whole system and later milestones; missing horizons, training windows, MLflow, and monitoring settings are not M1 failures.

### A5. Logging — PASS

`src/demandpilot/logging_config.py:11-42` provides text and JSON formatting, UTC timestamps in JSON, exception formatting, configured levels, and resets root handlers before installing one handler. `tests/test_logging_config.py:10-27` verifies JSON fields and configured level/handler. No fake secret was passed to the logger. No secret-redaction filter or redaction test exists; section 20 calls for secret protection system-wide, but this foundation does not currently accept or log settings, and M1's section 25 row does not make redaction a separate gate. Repeated-configuration behavior is implemented via handler clearing but lacks a dedicated assertion.

### A6. Git hygiene and sensitive files — PASS (working-tree rules); committed-state verification unavailable

- `git check-ignore -v` confirmed ignore matches for `.venv/`, `.env`, `data/`, `artifacts/`, and Python bytecode. `.gitignore` also covers caches, local artifacts, and MLflow output (`.gitignore:1-31`).
- The entire `data/` directory is ignored; `git ls-files -s` returned no tracked files. Thus no M5 CSV is committed, but the files are present locally and currently ignored.
- No `.env` or `.env.example` file was present. No credential file was found in the listed project tree. There are no commits to inspect for historical secrets or large artifacts; historical scanning is therefore not possible.
- No secret scanner was installed/configured in CI. The repository has zero tracked files, so “no tracked secret” is not evidence of a meaningful committed history.

### A7. Documentation and development process — NOT VERIFIABLE

The README gives setup and M1 check instructions, and `docs/decisions.md:3-14` records foundation choices. CI skeleton exists. `docs/progress.md` is absent despite section 24 defining it as the handoff record after each milestone; no milestone completion report with actual evidence exists before this audit. The only data-related document is `docs/eda-baseline-results.md`; it does not establish M2 requirements. Documentation claims in the baseline report were checked independently in section 6. Fresh setup instructions and Git history cannot be reconciled against a clean checkout because the files are untracked and no commit exists.

### A8. Mutation testing — PASS (two foundation safeguards)

Experiments ran in disposable `/tmp/demandpilot-audit-mutations.*` copies; the project files were not modified.

1. Changed `environment` from the allowed `Literal` to unrestricted `str`; ran `PYTHONPATH=<copy>/src .venv/bin/python -m pytest -q <copy>/tests`. Result: **1 failed, 10 passed**; `test_invalid_environment_is_rejected` failed because validation no longer raised.
2. Removed log-level normalization/validation; same command in an independent copy. Result: **2 failed, 9 passed**; log-level normalization and invalid-level rejection failed.

These spot checks show tests detect these specific regressions; they are not comprehensive mutation coverage.

## 5. Milestone 2 results

### B1. M5 dataset availability and provenance — FAIL

All expected files exist at `data/raw/m5/`. Inventory follows in section 6. All files were readable as CSV and hashes were computed. CSV dimensions are consistent with the documented competition data. However, there is no project documentation stating the acquisition method, source URL, licence/competition-rule review or acceptance, attribution, or redistribution constraints. Local availability is verified; documented provenance/licence compliance is not. No loader/import record or batch timestamp exists.

### B2. Loader and wide-to-long transformation — FAIL

The actual project tree contains only `src/demandpilot/__init__.py`, `settings.py`, and `logging_config.py`. There is no M5 loader, mapping logic, subset configuration, memory estimate, dtype policy, deterministic subset implementation, import metadata, or transformation test. The independent audit script read selected columns for verification, but it is not project implementation and does not satisfy the loader criterion.

### B3. Data validation — FAIL

No data-validation module, schema contract, row-level diagnostics, quarantine behavior, or valid/invalid M5 fixture tests exist. M5 files were structurally inspected for CSV readability and row counts only. The master requires contracts and ingestion rejection/quarantine details; these are not present. Validation mutation experiments could not be performed against nonexistent project safeguards.

### B4. Data-quality report — FAIL

`docs/data_quality_report.md` and equivalent quality report are absent. There are no documented run dates, subset definition, import checksums, validation warnings, missing-value policy, or reproducible report command. This audit independently computed a subset profile from the dataset (section 6); that audit calculation does not replace the missing deliverable.

### B5. Exploratory data analysis — FAIL

No EDA notebook, `docs/eda.md`, or figure directory exists. Section 11 requires real-data plots and written analysis covering hierarchy, sales/zero/intermittency, seasonality/events/SNAP, prices, gaps, launches/discontinuations, anomalies, cold starts, and limitations/decisions. The baseline results note contains a short dataset overview and one forecast comparison, not the required EDA. No figures were available to inspect. The EDA evidence requirement is therefore unmet.

### B6. Data dictionary and completeness policies — FAIL

`docs/data_dictionary.md` and `docs/data_pipeline.md` are absent. File headers were read, but there are no documented types, units, keys, ranges, null policies, date semantics, provenance, or missing product-day/price policy. No pipeline code exists to assess `fillna`, interpolation, or reindexing behavior. Missing price rows in M5 must remain distinguishable from zero prices; no application behavior currently handles them.

### B7. Baseline experiment — PASS as additional readiness check; not an M2 acceptance criterion

The report's exact 100-series seed, history (`d_1907`–`d_1913`), horizon (`d_1914`–`d_1941`), matching by `(item_id, store_id)`, and two formulas were independently reproduced from current CSVs. Results are detailed in section 6. No experiment script or baseline package implementation exists; the independent calculation is a one-off verification, not a maintained workflow. The report correctly labels mean-demand as a provisional benchmark and notes the limited sample/window. One 28-day historical window does not demonstrate generalization. Per the master roadmap, baseline implementation/evaluation belongs to Milestone 4, so this absence does not fail M2.

### B8. Baseline comparison and model-selection discipline — PASS (additional documentation check)

`docs/eda-baseline-results.md:13-32,45-60` identifies dataset overview, sample size/seed, periods/horizon, metrics/results, provisional status, limitations, and further validation needs. It does not give an exact reproduction command or dependency versions/data hashes, and category table only reports seasonal-naive results. The provisional-vs-production distinction is clear. This is not the formal M2 deliverable set.

### B9. Fabrication and integrity — PASS (limited scope)

Searched all current source/tests/docs for reported claims. No synthetic generator or hard-coded statistics in application/tests exists. The only result table is `docs/eda-baseline-results.md`; independently recomputed core and category metrics match its numbers (details below). The report openly identifies the sample and one-window limitation. There are no plots whose provenance can be examined. This supports the accuracy of those listed numbers, not the completeness of M2 EDA.

### B10. Milestone 2 test coverage — FAIL

The only tests are settings and logging tests (`tests/test_settings.py`, `tests/test_logging_config.py`); 11 total. No tests cover date mapping, wide-to-long conversion, deterministic sampling, missing versus zero prices/sales, validation, duplicate keys, intermittent demand, memory bounds, forecast metrics, or category aggregation. No Milestone 2 safeguards exist to mutate. This is consistent with the missing loader/validation implementation and directly leaves the M2 deliverables untested.

## 6. Dataset inventory and reported-versus-recomputed values

### M5 file inventory

| File | Bytes | CSV data rows | Columns | SHA-256 |
|---|---:|---:|---:|---|
| `calendar.csv` | 103,469 | 1,969 | 14 | `d12b5914ef03e66649adf5dd9e996e6602251c22b7a6af8f1f7e3aa12f8860f5` |
| `sales_train_validation.csv` | 120,007,726 | 30,490 | 1,919 | `f368e66ed1dbecb48b2cc8fc589bf68b3deddbbb36bf5c88b4d6d0a09b9b6724` |
| `sales_train_evaluation.csv` | 121,736,518 | 30,490 | 1,947 | `4b4a47c44c38380d2a9168216fea8c9ff2f31b1ddb772f8a0995952a038b8aa0` |
| `sample_submission.csv` | 5,228,786 | 60,980 | 29 | `eb7597afbec367475ef25dc6dbbc009b8faa47fa2107252a029e3cdf72343` |
| `sell_prices.csv` | 203,395,785 | 6,841,121 | 4 | `9da3ad1f8b8ccacdbdc70612191dd375ec24a4ac6625c24b75b3bc60b0bed2ef` |

Counts include the header separately as one column row, not as a data row. Hashes are from `sha256sum data/raw/m5/*.csv`. The M5 files were read locally; no network acquisition was performed. Calendar check found 1,969 rows, no duplicate `d` values, no duplicate dates, and date range 2011-01-29 through 2016-06-19.

### Independently recomputed data quality profile

This profile uses **only the deterministic 100-series sample** selected from `sales_train_validation.csv` with pandas `sample(n=100, random_state=42)`; sales observations are `d_1`–`d_1913`. The observed period is 2011-01-29 through 2016-04-24. Price completeness checks align those 100 `(store_id,item_id)` series to calendar `wm_yr_wk` values and count missing applicable series-day price lookup rows. This is a sample profile, not a full M5 transformation or full-dataset quality report.

| Statistic | Independently recomputed | Definition / denominator |
|---|---:|---|
| Observation rows | 191,300 | 100 series × 1,913 validation days; wide-cell count, not a materialized project long table |
| Product-store series | 100 | Selected sample rows; duplicate `(item_id,store_id)` keys: 0 |
| Date range | 2011-01-29–2016-04-24 | Calendar mapping for `d_1`–`d_1913` |
| Zero-sales share | 69.5849% | Zero daily units / 191,300 sampled daily observations |
| Series with no sales in evaluated period | 0 | Series with sum 0 over all `d_1`–`d_1913`; differs from forecast target-only meaning |
| Missing-price series-day rows | 42,896 | Missing `(store,item,week)` price lookup / 191,300 sampled series-days; no missing `sell_price` values among the fetched subset price rows |
| Total sales | 173,201 units | Sum over all 191,300 sampled validation daily observations |
| Duplicate series keys | 0 | Duplicate `(item_id,store_id)` in 100 sampled source rows |
| Sample products / stores | 98 / 10 | Distinct `item_id` and `store_id` in sample |

The audit did not compute full-dataset long-form statistics, full price-join coverage, active-window/intermittency classification, or all quality checks. No report values existed for direct comparison.

### Baseline reproduction

Command was a temporary inline Python audit script run with `.venv/bin/python`; it read only six identifiers plus 7 history columns and the 28 evaluation-target columns. Validation sample used pandas `DataFrame.sample(n=100, random_state=42)`. Evaluation targets were joined by `item_id` and `store_id`, with `validate="one_to_one"`. Weekly seasonal-naive repeats the last seven observed values four times. Seven-day mean repeats each series’ trailing seven-day arithmetic mean 28 times. MAE is mean absolute error across 2,800 series-days; WAPE is total absolute error divided by total absolute actuals for those same series-days.

| Statistic or metric | Previously reported | Independently recomputed | Difference | Scope/definition | Status |
|---|---:|---:|---:|---|---|
| Weekly seasonal-naive MAE | 1.1614 | 1.16142857 | +0.00002857 | 2,800 points; 100 sampled series × 28 forecast days | PASS |
| Weekly seasonal-naive WAPE | 83.04% | 83.04392237% | +0.00392237 pp | Same numerator/denominator scope; absolute error / absolute actual | PASS |
| Weekly seasonal-naive forecast total | 4,252 | 4,252 | 0 | Forecast units over 2,800 points | PASS |
| Seven-day mean MAE | 1.0227 | 1.02265306 | -0.00004694 | Overall point-weighted MAE, not mean per-series MAE | PASS |
| Seven-day mean WAPE | 73.12% | 73.12126076% | +0.00126076 pp | Same numerator/denominator scope | PASS |
| Seven-day mean forecast total | 4,252 | 4,252 | 0 | Forecast units over 2,800 points | PASS |
| Actual total | 3,916 | 3,916 | 0 | Evaluation target units over 2,800 points | PASS |
| MAE reduction, mean vs seasonal-naive | ~11.9% | 11.935% | ~+0.035 pp | Relative reduction from recomputed overall MAEs | PASS |
| WAPE reduction, mean vs seasonal-naive | ~11.9% | 11.950% | ~+0.050 pp | Relative reduction from recomputed WAPEs | PASS |
| FOODS seasonal-naive actual/forecast/mean series MAE/WAPE | 2,617 / 2,960 / 1.42 / 71.34% | 2,617 / 2,960 / 1.418693 / 71.341230% | Rounding only | 47 sampled series, 1,316 points | PASS |
| HOBBIES seasonal-naive actual/forecast/mean series MAE/WAPE | 572 / 640 / 0.99 / 120.98% | 572 / 640 / 0.988571 / 120.979021% | Rounding only | 25 sampled series, 700 points | PASS |
| HOUSEHOLD seasonal-naive actual/forecast/mean series MAE/WAPE | 727 / 652 / 0.88 / 95.32% | 727 / 652 / 0.883929 / 95.323246% | Rounding only | 28 sampled series, 784 points | PASS |

The matching evaluation file has the same item/store universe, but identifiers use different suffixes; matching by item/store was successful for all selected series. The selected sample contained 47 FOODS, 25 HOBBIES, and 28 HOUSEHOLD series. No category-specific mean-demand table is in the source report; recomputed values are not treated as previously claimed. These results verify one historical window only and do not justify universal superiority.

## 7. Findings by severity

### High

**M2-01 — No M5 loader or transformation.** Requirement: §7.1 and §25 M2. Evidence: no ingestion/loader file exists under `src/`; project tree contains only settings/logging/package initializer. Impact: the project cannot perform the required configurable, memory-aware subset import or record batch provenance. Remediation: implement and test the specified subset loader, calendar mapping, dtypes, measured memory estimate, and checksums/import metadata. **Blocks M2 acceptance: yes.**

**M2-02 — Data contracts, validation, and quality report are absent.** Requirement: §7.3, §10, §25 M2. Evidence: `docs/data_dictionary.md`, `docs/data_pipeline.md`, validation code, and `docs/data_quality_report.md` are missing. Impact: schema/range/null behavior and actual data issues are not reproducibly defined or surfaced. Remediation: document contracts and completeness policy, implement diagnostics, and generate a report from real subset data with reproducible commands. **Blocks M2 acceptance: yes.**

**M2-03 — EDA deliverables are absent.** Requirement: §11 and §25 M2. Evidence: no EDA notebook, written EDA analysis, or plots; `docs/eda-baseline-results.md` only reports overview and a baseline comparison. Impact: required analysis and decisions about data limitations are not demonstrated. Remediation: produce real-data notebook/findings and labeled plots covering the required analyses and limitations. **Blocks M2 acceptance: yes.**

### Medium

**M1-01 — No committed baseline.** Requirement: §3.1 (small commits), §22 clean-checkout reproducibility, and audit reproducibility procedures. Evidence: `git log` reports no commits; `git ls-files -s` is empty; all source/config/docs/CI are untracked. Impact: current work cannot be recreated from Git or audited against a committed state. Remediation: after project-owner review, commit the intended project baseline and verify a clean-checkout setup; no commit was created during this read-only audit. **Blocks M1 acceptance under §25 row: not by itself; it materially limits reproducibility evidence.**

**M2-04 — Dataset source/licence and acquisition method are undocumented.** Requirement: §7.1 and §25 M2. Evidence: no source/licence section or attribution in `README.md` or `docs/`; data files are ignored. Impact: compliance/provenance and redistribution status cannot be established from repository evidence. Remediation: document Kaggle source, acquisition, competition-rule/licence review, attribution, and non-redistribution constraints as applicable. **Blocks M2 acceptance: yes.**

**M1-02 — Ruff formatter check fails (additional gate).** Evidence: `.venv/bin/python -m ruff format --check .` exited 1 and identified five files. Impact: formatting differs from current Ruff formatter output; current CI and README do not run this check. Remediation: format the files and add the check if it is intended to be a quality gate. **Blocks M1 acceptance: no under the section 25 M1 acceptance row.**

**M1-03 — Fresh-install and Python 3.11 runs were not verified.** Requirement: §6, §22. Evidence: active Python 3.14.7 environment passed; CI declares 3.11 but was not executed here; fresh venv install prohibited by audit dependency-install rule. Impact: compatibility/reproducibility outside current environment remains unproven. Remediation: run the documented setup and CI checks in a clean Python 3.11+ environment when authorized. **Blocks M1 acceptance: no demonstrated failure; evidence limitation.**

### Low

**M2-05 — Baseline report lacks exact reproduction command and run metadata.** Requirement: useful reproducibility practice; baseline is a Milestone 4 deliverable, not M2. Evidence: `docs/eda-baseline-results.md:13-32` provides design and values but no runnable command, version snapshot, or input hashes. Impact: another engineer must reconstruct the experiment. Remediation: retain a script/command and environment/data snapshot metadata with the future M4 baseline. **Blocks M2 acceptance: no.**

### Informational

**I-01 — Baseline values and category figures reproduce.** Evidence: section 6 calculations from real local M5 files match all documented values to rounding precision. Impact: supports integrity of reported baseline numbers for the documented sample and window only. **Blocks acceptance: no.**

**I-02 — Python 3.14/pandas 3.1 are installed in `.venv` but absent from project dependencies.** Impact: these tools were available for audit computations, but they are not reproducibly provisioned by the project configuration. This is not an M1 failure; it matters when implementing M2 data work.

## 8. Acceptance criteria

### Milestone 1

- **Acceptance decision: MET.** Package import, invalid configuration rejection, tests, lint, type check, and the foundation structure are directly verified. All 11 tests passed. Current-tree reproducibility limitations and the additional formatting failure are documented; neither demonstrates failure of the Milestone 1 section 25 acceptance row.
- **Overall verdict: COMPLETE WITH MINOR ISSUES.** Fresh environment and clean committed-checkout behavior remain unverified; formatter check is not clean. These do not overturn the mandatory criteria that were executed and passed.

### Milestone 2

- **Acceptance decision: NOT MET.** Loader, quality report, EDA notebook/written findings/plots, and data contracts are mandatory and absent; provenance/licence documentation is also missing. These are demonstrated failures, not merely unavailable evidence.
- **Overall verdict: INCOMPLETE.** The raw files and baseline computation are available, but they do not satisfy the required M2 implementation/documentation deliverables.

## 9. Prioritized remediation plan

### Mandatory blockers for Milestone 1

No demonstrated mandatory acceptance failure. For stronger reproducibility, commit the reviewed intended baseline and run the documented setup in a clean Python 3.11+ environment. Evidence: clean checkout, editable installation, import, test counts, Ruff lint, and mypy all succeed. The format-check issue is an optional quality improvement under the current roadmap row.

### Mandatory blockers for Milestone 2

1. **Implement the M5 subset loader** with deterministic configuration, memory estimate before transformation, chunked/typed processing, complete unique contiguous `d_N` to date mapping, and import metadata/checksums. Evidence: reproducible run on a documented subset, row counts/checksums, and tests for mapping, deterministic selection, dtypes, and memory-safe behavior.
2. **Document source and licence/provenance.** Evidence: M5 source, acquisition method, competition-rule/licence review, attribution, and data use/redistribution constraints written in project docs.
3. **Define data contracts and validation/completeness policies.** Evidence: `docs/data_dictionary.md` covers all source files/fields and null/key/range/date policies; tests demonstrate invalid inputs are rejected or quarantined with reasons and that unknown/missing prices remain distinct from zero.
4. **Generate a reproducible data-quality report** from actual loaded M5 subset. Evidence: run date, file hashes, subset/seed, row and series counts, dates, missingness, validation diagnostics, and exact command are present and independently recomputable.
5. **Complete EDA notebook and written findings with real figures.** Evidence: required hierarchy, sales/intermittency, calendar/event/SNAP, price, gaps, launches, anomalies/cold starts and limitations are covered; plots identify scope, axes, units, aggregation and dates; conclusions avoid causal claims and list decisions.
6. **Add Milestone 2 tests.** Evidence: test output for loader, calendar, data contracts/validation and missing-vs-zero cases; mutation tests show key safeguards are detected.

### Additional quality improvements

- Add reproducible dependency resolution (lockfile if adopted tooling creates it) and document Python versions tested.
- Add Ruff format check if formatting is intended to be a required gate.
- Add a documented baseline reproduction command and version/data snapshot metadata when baseline work is formalized in Milestone 4.
- Add `docs/progress.md` handoff evidence following section 24.

### Later milestones

PostgreSQL schema/migrations/idempotent persistence and quarantine tables belong to Milestone 3. Leak-safe features and maintained baseline metric functions/backtesting belong to Milestone 4. Do not treat their current absence as an M1/M2 failure.

## 10. Go/no-go recommendation for Milestone 3

**NO-GO.** Milestone 2 is not met because its required data loader, data contracts, quality report, and EDA deliverables are missing, and provenance/licence evidence is undocumented. The local dataset and reproduced historical baseline do not substitute for those acceptance requirements. Complete and verify Milestone 2 first; preserve the M5 hashes/subset configuration and provide reproducible quality/EDA evidence before beginning Milestone 3.
