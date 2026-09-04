# Geeky Green Geckos: Personal Finance Tracker

ITSM 601 team project. This repository contains a modular Python application
for recording income and expenses, generating financial reports, and displaying
an expenses-by-category chart with Turtle Graphics.

## Features

- Add, edit, and delete financial transactions
- Categorize income and expenses
- Store transaction data using CSV files
- Calculate total income and expenses
- Calculate net savings
- Generate weekly and monthly financial summaries
- Create visual representations of spending patterns using Turtle Graphics
- Validate and sanitize user input
- Provide error handling for invalid entries

## Project Layout

```text
personal-finance-tracker/
│
├── data/
│   ├── transactions.csv
│   └── categories.csv
│
├── docs/
│   ├── Phase-1-Project-Proposal.pdf
│   ├── Phase-2-Project-Report.pdf
│   ├── Phase-3-Project-Report.pdf
│   ├── Phase-4-Project-Report.pdf
│   └── architecture_diagram.png
│
├── images/
│   └── bar-chart.png
│
├── src/
│   ├── main.py
│   ├── transactions.py
│   ├── summaries.py
│   ├── visualizer.py
│   └── utils.py
│
└── README.md

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Program entry point and primary user interface |
| `transactions.py` | Transaction management and CSV data storage |
| `summaries.py` | Financial calculations and period-based summaries |
| `visualizer.py` | Turtle Graphics visualizations |
| `utils.py` | Input validation, sanitization, and shared helper functions |

## Setup

Python 3.10 or newer is required. A virtual environment is recommended:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"

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
