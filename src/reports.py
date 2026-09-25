"""Financial reports and visualizations."""

from collections import defaultdict
from datetime import datetime

from . import transactions
def category_based_expenses():
    """Display total expenses for each category."""
    records = transactions.load_transactions()
    category_totals = {}

    for transaction in records:
        if transaction["Type"].lower() == "expense":
            category = transaction["Category"]
            amount = float(transaction["Amount"])

            if category in category_totals:
              category_totals[category] += amount
            else:
              category_totals[category] = amount
    print("\n--- Category Based Expenses ---")

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def monthly_spending():
    """Display total expenses for each month."""
    records = transactions.load_transactions()
    monthly_totals = {}

    for transaction in records:
        if transaction["Type"].lower()== "expense":
            date = transaction["Date"]
            month_year = date.split("/")[0] + "/" + date.split("/")[2]
            amount = float(transaction["Amount"])

            if month_year in monthly_totals:
                monthly_totals[month_year] += amount
            else:
                monthly_totals[month_year] = amount
    print("\n--- Monthly Spending ---")

    for month_year, total in monthly_totals.items():
        print(f"{month_year}: ${total:.2f}")

if __name__ == "__main__":
    category_based_expenses()
    monthly_spending()
    
              
