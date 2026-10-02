# PROGRAM:    Personal Finance Tracker - Visualizer
# PURPOSE:    Create graphical visualizations of recorded financial data.
# INPUT:      Aggregated category and monthly expense data.
# PROCESS:    Uses Matplotlib to create bar charts from calculated financial totals.
# OUTPUT:     Saves graphical financial reports as PNG image files.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received
#             unauthorized aid on this academic work.
# Gen AI:     In keeping with my commitment to leverage advanced technology
#             for enhanced efficiency and accuracy in my work, I use
#             generative artificial intelligence tools to assist in writing
#             my Python code.

import matplotlib
import os

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

    os.makedirs("images", exist_ok=True)
    filename = os.path.join("images", "category_expenses.png")
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

    os.makedirs("images", exist_ok=True)
    filename = os.path.join("images", "monthly_spending.png")
    plt.savefig(filename)
    plt.close()

    print(f"Monthly spending chart saved as {filename}")