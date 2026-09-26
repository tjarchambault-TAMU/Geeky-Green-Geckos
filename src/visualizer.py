"""Visualization functions for the Personal Finance Tracker."""

import matplotlib

# Use a non-GUI backend so charts work in GitHub Codespaces.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def category_expense_chart(category_totals):
    """Create and save a bar chart of expenses by category."""

    if not category_totals:
        print("No category data available for visualization.")
        return

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts)

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    filename = "category_expenses.png"
    plt.savefig(filename)
    plt.close()

    print(f"Category expense chart saved as {filename}")


def monthly_spending_chart(monthly_totals):
    """Create and save a bar chart of monthly spending."""

    if not monthly_totals:
        print("No monthly data available for visualization.")
        return

    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(months, amounts)

    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    filename = "monthly_spending.png"
    plt.savefig(filename)
    plt.close()

    print(f"Monthly spending chart saved as {filename}")