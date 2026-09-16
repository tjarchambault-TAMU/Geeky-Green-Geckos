""" Financial reports and visualizations."""
import transactions

def expenses_by_category():
    """Display total expenses for each category."""
    records = transactions.load_transactions()
    category_totals = {}

    for record in records:
        if record["Type"].lower() == "expense":
            category = record["Category"]
            amount = float(record["Amount"])

            if category in category_totals:
              category_totals[category] += amount
            else:
              category_totals[category] = amount
print("\n--- Expenses by Category ---")

for category, total in category_totals.items():
  print(f"{category}: ${total:.2f}")

if __name__ == "__main__":
  expenses_by_category()
              
