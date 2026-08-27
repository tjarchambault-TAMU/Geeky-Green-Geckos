# Geeky Green Geckos: Personal Finance Tracker

ITSM 601 team project. This repository contains a modular Python application
for recording income and expenses, generating financial reports, and displaying
an expenses-by-category chart with Turtle Graphics.

## Project Layout

- `src/models.py`: validated transaction data model
- `src/storage.py`: CSV loading and saving
- `src/finance.py`: input validation and financial calculations
- `src/reports.py`: period, category, and monthly reports
- `src/visualization.py`: Turtle chart generation
- `src/main.py`: command-line interface and `main()` entry point
- `tests/`: automated tests for the core functionality
- `data/`: application data, including the generated `transactions.csv`

## Setup

Python 3.10 or newer is required. A virtual environment is recommended:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

No runtime libraries outside the Python standard library are required.

## Run

```bash
python3 -m src.main
```

Transactions are saved to `data/transactions.csv`. Enter dates as `YYYY-MM-DD`,
positive amounts as currency values, and transaction types as `income` or
`expense`. The chart option requires a desktop environment that supports Tk.

## Test

```bash
python3 -m pytest
```

The application separates input, processing, storage, reports, and output so
team members can work on individual modules without changing the CLI.

## Generative AI Disclosure

Generative AI may be used as a collaborative coding assistant for brainstorming,
implementation, debugging, and documentation. The team is responsible for
reviewing, explaining, testing, and adapting all generated code before
submission.
