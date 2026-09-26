"""Financial reports for the Personal Finance Tracker."""

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
    """Return total expenses grouped by month and year."""

    records = transactions.load_transactions()
    monthly_totals = {}

    for transaction in records:
        if transaction["Type"].lower() == "expense":
            try:
                date = transaction["Date"]
                amount = float(transaction["Amount"])

                parts = date.split("/")
                month = int(parts[0])
                year = parts[2]

                month_year = f"{month:02d}/{year}"

                if month_year in monthly_totals:
                    monthly_totals[month_year] += amount
                else:
                    monthly_totals[month_year] = amount

            except (ValueError, KeyError, IndexError):
                print("Warning: invalid transaction skipped.")

    return monthly_totals


def monthly_spending():
    """Display monthly spending and provide a visualization."""

    monthly_totals = get_monthly_spending()

    print("\n--- Monthly Spending ---")

    if not monthly_totals:
        print("No expense transactions found.")
        return

    for month_year, total in sorted(monthly_totals.items()):
        print(f"{month_year}: ${total:.2f}")

    print("\nOpening the Monthly Spending visualization...")

    visualizer.monthly_spending_chart(monthly_totals)


if __name__ == "__main__":
    category_based_expenses()
    monthly_spending()