# Geeky Green Geckos: Personal Finance Tracker

ITSM 601 team project. This repository contains a modular Python application for recording income and expenses, validating user input, generating financial reports, and displaying spending information.

## Features

* Add financial transactions through a command-line interface (CLI)
* Store transaction data using a CSV file
* Categorize expense transactions
* Calculate total income and expenses
* Calculate net savings
* Generate an **Expenses by Category** report
* Generate a **Monthly Spending** report
* Validate dates, descriptions, amounts, transaction types, and categories
* Handle common input, CSV, and file errors without unexpectedly terminating

## Project Layout

```text
personal-finance-tracker/
├── data/
│   └── transactions.csv
├── src/
│   ├── main.py
│   ├── transactions.py
│   ├── summaries.py
│   ├── reports.py
│   ├── visualizer.py
│   └── utils.py
├── tests/
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## Module Responsibilities

| Module            | Responsibility                                                  |
| ----------------- | --------------------------------------------------------------- |
| `main.py`         | Program entry point and command-line interface                  |
| `transactions.py` | Transaction input, CSV storage, loading, and display            |
| `summaries.py`    | Income, expense, and net-savings calculations                   |
| `reports.py`      | Phase 2 financial reports                                       |
| `visualizer.py`   | Reserved for financial visualizations in the next project phase |
| `utils.py`        | Input validation and shared helper functions                    |

## Reporting

### Expenses by Category

Groups expense transactions by category and totals the amount spent in each category. Access it from the CLI with **4. View Expenses by Category**.

### Monthly Spending

Groups expense transactions by month and totals spending for each month. Access it from the CLI with **5. View Monthly Spending**.

Both reports use `data/transactions.csv`.

## Data Validation

The application validates user input before saving a transaction:

* Dates must use `MM/DD/YYYY` format.
* Descriptions cannot be blank.
* Amounts must be numeric and greater than zero.
* Transaction type must be income or expense.
* Expense categories must be selected from the available list.
* Invalid menu choices are rejected.

## Exception Handling

The application handles common anticipated issues, including:

* Invalid numeric input
* Invalid dates
* Missing or inaccessible transaction files
* CSV formatting errors
* Invalid transaction data encountered by reports
* Invalid menu choices

Invalid report rows are skipped with a warning rather than causing the application to crash.

## Setup

Python 3.10 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

## Run

From the repository root:

```bash
python3 -m src.main
```

Transactions are saved to:

```text
data/transactions.csv
```

Enter dates using `MM/DD/YYYY` format and amounts as positive numeric values.

## Test

Run the automated tests with:

```bash
python3 -m pytest
```

You can also check that all Python files compile successfully with:

```bash
python3 -m compileall src
```

## Phase 2 Requirements Addressed

### Reports

* Expenses by Category
* Monthly Spending

### Validation

* Date validation
* Description validation
* Positive amount validation
* Transaction type validation
* Category validation
* Menu-choice validation

### Error Handling

* Invalid user input
* Missing transaction file
* File access errors
* CSV errors
* Invalid transaction data during reporting

## Generative AI Disclosure

Generative AI may be used as a collaborative coding assistant for brainstorming, implementation, debugging, and documentation. The team is responsible for reviewing, explaining, testing, and adapting all generated code before submission.
