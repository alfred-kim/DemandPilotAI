# DemandPilot AI

Demand forecasting and inventory decision support, developed in milestone order.

## Development setup

Requires Python 3.11 or newer. Create and activate the isolated environment, then
install the package and development tools:

```sh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

Run the foundation checks with:

```sh
pytest --cov=demandpilot --cov-report=term-missing
ruff check .
mypy src
```

Settings are read from `DEMANDPILOT_`-prefixed environment variables and an
optional root `.env` file. See `demandpilot.settings.Settings` for defaults and
validation.
