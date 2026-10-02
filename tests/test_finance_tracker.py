"""Automated tests for the Personal Finance Tracker."""

from src import reports


def test_category_expenses():
    """Verify that expenses are correctly totaled by category."""

    test_transactions = [
        {
            "Date": "01/10/2026",
            "Description": "Groceries",
            "Category": "Groceries",
            "Amount": "100.00",
            "Type": "expense",
        },
        {
            "Date": "01/15/2026",
            "Description": "More Groceries",
            "Category": "Groceries",
            "Amount": "50.00",
            "Type": "expense",
        },
        {
            "Date": "01/20/2026",
            "Description": "Gas",
            "Category": "Transportation",
            "Amount": "40.00",
            "Type": "expense",
        },
    ]

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: test_transactions

        totals = reports.get_category_expenses()

        assert totals["Groceries"] == 150.00
        assert totals["Transportation"] == 40.00

    finally:
        reports.transactions.load_transactions = original_load


def test_income_not_in_category_expenses():
    """Verify that income is not included in expense reports."""

    test_transactions = [
        {
            "Date": "01/15/2026",
            "Description": "Paycheck",
            "Category": "Income",
            "Amount": "3000.00",
            "Type": "income",
        },
        {
            "Date": "01/20/2026",
            "Description": "Groceries",
            "Category": "Groceries",
            "Amount": "150.00",
            "Type": "expense",
        },
    ]

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: test_transactions

        totals = reports.get_category_expenses()

        assert "Income" not in totals
        assert totals["Groceries"] == 150.00

    finally:
        reports.transactions.load_transactions = original_load


def test_monthly_spending():
    """Verify that expenses are correctly totaled by month."""

    test_transactions = [
        {
            "Date": "01/10/2026",
            "Description": "Groceries",
            "Category": "Groceries",
            "Amount": "100.00",
            "Type": "expense",
        },
        {
            "Date": "01/20/2026",
            "Description": "Gas",
            "Category": "Transportation",
            "Amount": "50.00",
            "Type": "expense",
        },
        {
            "Date": "03/10/2026",
            "Description": "Restaurant",
            "Category": "Dining",
            "Amount": "75.00",
            "Type": "expense",
        },
    ]

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: test_transactions

        totals = reports.get_monthly_spending()

        assert totals["January"] == 150.00
        assert totals["March"] == 75.00

    finally:
        reports.transactions.load_transactions = original_load


def test_months_are_chronological():
    """Verify that monthly report results remain in calendar order."""

    test_transactions = [
        {
            "Date": "09/10/2026",
            "Description": "September Expense",
            "Category": "Miscellaneous",
            "Amount": "100.00",
            "Type": "expense",
        },
        {
            "Date": "01/10/2026",
            "Description": "January Expense",
            "Category": "Miscellaneous",
            "Amount": "100.00",
            "Type": "expense",
        },
        {
            "Date": "06/10/2026",
            "Description": "June Expense",
            "Category": "Miscellaneous",
            "Amount": "100.00",
            "Type": "expense",
        },
    ]

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: test_transactions

        totals = reports.get_monthly_spending()

        assert list(totals.keys()) == ["January", "June", "September"]

    finally:
        reports.transactions.load_transactions = original_load


def test_empty_category_report():
    """Verify that an empty transaction list returns an empty category report."""

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: []

        totals = reports.get_category_expenses()

        assert totals == {}

    finally:
        reports.transactions.load_transactions = original_load


def test_empty_monthly_report():
    """Verify that an empty transaction list returns an empty monthly report."""

    original_load = reports.transactions.load_transactions

    try:
        reports.transactions.load_transactions = lambda: []

        totals = reports.get_monthly_spending()

        assert totals == {}

    finally:
        reports.transactions.load_transactions = original_load