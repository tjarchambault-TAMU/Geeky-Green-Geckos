""" Financial reports and visualizations."""
import transactions

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
            month_year = date.split("/")[0] + "/" + date.split("/"[2])
            amount = float(transaction["Amount"])

            if month  in monthly_totals:
                monthly_totals[month] += amount
            else:
                monthly_totals[month] = amount
    print("\n--- Monthly Spending ---")

    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")

if __name__ == "__main__":
    category_based_expenses()
    monthly_spending()
    
              
