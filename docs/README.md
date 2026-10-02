# Geeky Green Geckos: Personal Finance Tracker

ITSM 601 team project. This repository contains a modular Python application for recording income and expenses, validating user input, generating financial reports, and visualizing spending information.

## Features

* Add financial transactions through a command-line interface (CLI)
* Store transaction data using a CSV file
* Categorize expense transactions
* Calculate total income and expenses
* Calculate net savings
* Access financial reports through a dedicated Reports submenu
* Generate an **Expenses by Category** report
* Generate a **Monthly Spending** report
* Generate graphical financial reports using Matplotlib
* Save generated report charts to the `images/` directory
* Validate dates, descriptions, amounts, transaction types, and categories
* Reject future transaction dates and dates outside the current year
* Detect duplicate transactions and allow the user to confirm or cancel saving
* Handle common input, CSV, and file errors without unexpectedly terminating

## Project Layout

```text
personal-finance-tracker/
├── data/
│   └── transactions.csv
├── docs/
│   ├── README.md
│   └── requirements-dev.txt
├── images/
│   ├── category_expenses.png
│   └── monthly_spending.png
├── src/
│   ├── main.py
│   ├── transactions.py
│   ├── summaries.py
│   ├── reports.py
│   ├── visualizer.py
│   └── utils.py
├── tests/
│   └── test_finance_tracker.py
├── .gitignore
├── poetry.lock
└── pyproject.toml
```

## Module Responsibilities

| Module | Responsibility |
| ----------------- | ------------------------------------------------------------------------- |
| `main.py`         | Program entry point, main menu, and Reports submenu                       |
| `transactions.py` | Transaction input, duplicate detection, CSV storage, loading, and display |
| `summaries.py`    | Income, expense, and net-savings calculations                             |
| `reports.py`      | Expense-by-category and monthly-spending report calculations              |
| `visualizer.py`   | Generates and saves graphical financial reports using Matplotlib          |
| `utils.py`        | Input validation and shared helper functions                              |
|-------------------|---------------------------------------------------------------------------|

## Reporting

Financial reports are available by selecting **4. View Reports** from the main menu.

### Expenses by Category

Groups expense transactions by category and calculates the total amount spent in each category. A bar chart is generated to provide a graphical representation of category spending.

The generated chart is saved as:

```text
images/category_expenses.png
```

### Monthly Spending

Groups expense transactions by calendar month and calculates the total amount spent during each month. Months are displayed by name and arranged in chronological order.

The generated chart is saved as:

```text
images/monthly_spending.png
```

Both reports use transaction data stored in `data/transactions.csv`.

## Generated Output

Financial visualizations are generated as PNG files and stored in the `images/` directory. Existing report images are replaced when a new report of the same type is generated.

## Data Validation

The application validates user input before saving a transaction:

* Dates must use `MM/DD/YYYY` format.
* Transaction dates cannot be in the future.
* Transaction dates must be within the current year.
* Descriptions cannot be blank.
* Amounts must be numeric and greater than zero.
* Transaction type must be income or expense.
* Expense categories must be selected from the available list.
* Invalid menu choices are rejected.
* Duplicate transactions are detected and require confirmation before being saved.

## Exception Handling

The application handles common anticipated issues, including:

* Invalid numeric input
* Invalid or improperly formatted dates
* Missing or inaccessible transaction files
* CSV formatting errors
* Invalid transaction data encountered during reporting
* Invalid menu choices

Invalid report rows are skipped with a warning rather than causing the application to terminate unexpectedly.

## Setup

Python 3.10 or newer is required.

Install the development dependencies listed in `docs/requirements-dev.txt`.

### Windows

```powershell
py -m pip install -r docs/requirements-dev.txt
```

### macOS/Linux

```bash
python3 -m pip install -r docs/requirements-dev.txt
```

## Run

Run the application from the repository root.

### Windows

```powershell
py -m src.main
```

### macOS/Linux

```bash
python3 -m src.main
```

Transactions are saved to:

```text
data/transactions.csv
```

Enter dates using `MM/DD/YYYY` format and amounts as positive numeric values.

## Testing

Automated tests are located in the `tests/` directory.

### Windows

Run the automated test suite with:

```powershell
py -m pytest
```

Check that all Python source files compile successfully with:

```powershell
py -m compileall src
```

### macOS/Linux

Run the automated test suite with:

```bash
python3 -m pytest
```

Check that all Python source files compile successfully with:

```bash
python3 -m compileall src
```

## Generative AI Disclosure

Generative AI may be used as a collaborative coding assistant for brainstorming, implementation, debugging, and documentation. The team is responsible for reviewing, explaining, testing, verifying, and adapting all generated code before submission.