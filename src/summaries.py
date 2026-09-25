"""Financial summaries and calculations."""

from . import transactions


def calculate_total_income():
    """Return the sum of all recorded income transactions."""
    total_income = 0

    for transaction in transactions.load_transactions():
        if transaction["Type"].lower() == "income":    
            try:
                total_income += float(transaction["Amount"])
            except ValueError:
                print("Transaction has an invalid amount.")
    return total_income


def calculate_total_expenses():
    """Return the sum of all recorded expense transactions."""
    expenses = 0
    for transaction in transactions.load_transactions():
        if transaction["Type"].lower() == "expense":
            try:
                expenses += float(transaction["Amount"])
            except ValueError:
                print("Invalid expense transaction amount.")
    return expenses

def calculate_net_savings():
    """Return total income minus total expenses."""
    return calculate_total_income() - calculate_total_expenses()


def financial_summary():
    """Print total income, total expenses, and net savings."""
    print("\n--- Financial Summary ---")

    income = calculate_total_income()
    expenses = calculate_total_expenses()
    savings = calculate_net_savings()

    print(f"Total Income:   ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Net Savings:    ${savings:.2f}")

    if savings > 0:
        print("You are currently saving money!")
    elif savings < 0:
        print("You are spending more than you earn.")
    else:
        print("Your income and expenses are equal.")
