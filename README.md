
#DemandPilot AI

DemandPilot AI is a demand forecasting and inventory decision-support project designed to learn from historical sales data, generate forecasts, and support better business decisions as new data becomes available.

The project is being developed incrementally, with emphasis on reproducibility, data quality, leakage prevention, evaluation, and reliable data ingestion.

## Project Goals

- Analyze historical sales and demand patterns.
- Build and evaluate time-series forecasting baselines.
- Develop reliable data ingestion and validation pipelines.
- Design a PostgreSQL data model for sales, products, stores, and ingestion history.
- Support future inventory and business decision recommendations.
- Establish a foundation for learning from new data and evaluating model performance over time.

## Current Status

The project is under active development.

| Area | Status |
|---|---|
| Python project foundation | Established |
| Settings and logging | Implemented |
| Automated foundation tests | Passing at the last recorded check |
| M5 Forecasting dataset | Downloaded and explored |
| Baseline forecasting evaluation | Completed for a deterministic sample |
| Database schema | Proposed; migration approval pending |
| Production ingestion pipeline | Still to be completed |
| Production forecasting and decision agent | Still to be completed |

See [docs/audit_m1_m2.md](docs/audit_m1_m2.md) for the milestone audit, and [docs/decisions.md](docs/decisions.md) for recorded design decisions.

## Dataset

The project uses the [M5 Forecasting Accuracy dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy) for demand forecasting research.

The dataset includes daily sales histories, calendar information, and prices for products across stores.

Expected local dataset directory:

```text
data/raw/m5/
├── sales_train_validation.csv
├── sales_train_evaluation.csv
├── calendar.csv
└── sell_prices.csv
```

**Data handling:** Dataset files are local inputs and should not be committed to Git. Review the competition's terms and dataset licensing conditions before redistribution.

## Baseline Forecasting

An initial baseline evaluation was conducted using a deterministic sample of 100 product-store series.

Evaluation configuration:

- Historical window: `d_1907`–`d_1913`
- Forecast horizon: 28 days, `d_1914`–`d_1941`
- Sample random state: `42`

Recorded baseline results:

| Model | MAE | WAPE |
|---|---:|---:|
| Weekly seasonal naive | 1.1614 | 83.04% |
| Seven-day mean | 1.0227 | 73.12% |

The seven-day mean performed better on this particular sample and evaluation window. These results are preliminary and do not establish production forecasting accuracy or general performance across all series.

WAPE is calculated as:

`WAPE = sum(abs(actual - forecast)) / sum(abs(actual)) × 100`

## Technology Stack

- Python 3.11+
- pandas and NumPy for data analysis
- pytest and pytest-cov for testing
- Ruff for linting
- mypy for static type checking
- PostgreSQL for the planned relational data store
- SQLAlchemy, Alembic, and psycopg are candidates for the future database implementation

The database integration stack and production architecture are not yet complete.

## Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/alfred-kim/DemandPilotAI.git
cd DemandPilotAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

### 3. Install the project and development dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

### 4. Run the checks

```bash
python -m pytest --cov=demandpilot --cov-report=term-missing
ruff check .
mypy src
```

Run these commands from the project root with the virtual environment activated.

## Configuration

Settings use environment variables prefixed with `DEMANDPILOT_` and can also be loaded from an optional root `.env` file.

See `src/demandpilot/settings.py` for the available settings and validation rules.

Do not commit `.env` files, credentials, API tokens, or other secrets.

## Documentation

- [`README.md`](README.md) — project overview and development setup
- [`docs/decisions.md`](docs/decisions.md) — recorded design decisions
- [`docs/database.md`](docs/database.md) — proposed database schema and implementation safeguards
- [`docs/audit_m1_m2.md`](docs/audit_m1_m2.md) — milestone audit
- [`docs/eda-baseline-results.md`](docs/eda-baseline-results.md) — baseline exploratory analysis
- [`DemandPilot AI Master Engineering Prompt v2 (Comprehensive).md`](<DemandPilot AI Master Engineering Prompt v2 (Comprehensive).md>) — engineering specification

## Development Principles

- Keep data ingestion reproducible and idempotent.
- Preserve source provenance and data-quality information.
- Prevent future information from leaking into historical model training.
- Evaluate forecasts against explicit baselines.
- Test failure handling and recovery paths.
- Keep proposed designs separate from implemented and verified functionality.

## License

No license has been specified yet. All rights to the project remain subject to the applicable ownership and third-party dataset terms until a license is added.
