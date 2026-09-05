"""Financial calculations and period-based summaries."""

from src import transactions


def calculate_total_income():
    """Return the sum of all recorded income transactions."""
    return sum(
        float(row["Amount"])
        for row in transactions.load_transactions()
        if row["Type"].lower() == "income"
    )


def calculate_total_expenses():
    """Return the sum of all recorded expense transactions."""
    return sum(
        float(row["Amount"])
        for row in transactions.load_transactions()
        if row["Type"].lower() == "expense"
    )


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