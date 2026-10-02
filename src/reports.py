# PROGRAM:    Personal Finance Tracker - Reports
# PURPOSE:    Generate category-based and monthly financial reports.
# INPUT:      Stored expense transaction records.
# PROCESS:    Groups and totals expenses by category or calendar month and
#             sends the calculated results to the visualization functions.
# OUTPUT:     Displays report totals and generates graphical financial reports.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received
#             unauthorized aid on this academic work.
# Gen AI:     In keeping with my commitment to leverage advanced technology
#             for enhanced efficiency and accuracy in my work, I use
#             generative artificial intelligence tools to assist in writing
#             my Python code.

import calendar
from datetime import datetime

from . import transactions
from . import visualizer


def get_category_expenses():
    """Return total expenses grouped by category."""

    records = transactions.load_transactions()
    category_totals = {}

    for transaction in records:
        if transaction["Type"].lower() == "expense":
            try:
                category = transaction["Category"]
                amount = float(transaction["Amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            except (ValueError, KeyError):
                print("Warning: invalid expense transaction skipped.")

    return category_totals


def category_based_expenses():
    """Display expenses by category and provide a visualization."""

    category_totals = get_category_expenses()

    print("\n--- Category Based Expenses ---")

    if not category_totals:
        print("No expense transactions found.")
        return

    for category, total in sorted(category_totals.items()):
        print(f"{category}: ${total:.2f}")

    print("\nOpening the Expenses by Category visualization...")

    visualizer.category_expense_chart(category_totals)


def get_monthly_spending():
    """Return total expenses grouped by month."""

    records = transactions.load_transactions()
    monthly_totals = {}

    for transaction in records:
        if transaction["Type"].lower() == "expense":
            try:
                date = datetime.strptime(transaction["Date"], "%m/%d/%Y")
                amount = float(transaction["Amount"])

                month = date.month

                if month in monthly_totals:
                    monthly_totals[month] += amount
                else:
                    monthly_totals[month] = amount

            except (ValueError, KeyError):
                print("Warning: invalid transaction skipped.")
# Convert numeric months to names while preserving chronological order.
    sorted_totals = {}

    for month in sorted(monthly_totals):
        month_name = calendar.month_name[month]
        sorted_totals[month_name] = monthly_totals[month]

    return sorted_totals

def monthly_spending():
    """Display monthly spending and provide a visualization."""

    monthly_totals = get_monthly_spending()

    print("\n--- Monthly Spending ---")

    if not monthly_totals:
        print("No expense transactions found.")
        return

    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")

    print("\nOpening the Monthly Spending visualization...")

    visualizer.monthly_spending_chart(monthly_totals)


if __name__ == "__main__":
    category_based_expenses()
    monthly_spending()