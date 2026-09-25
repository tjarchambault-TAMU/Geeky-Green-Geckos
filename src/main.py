"""Personal Finance Tracker - command-line entry point."""

from . import reports
from . import summaries
from . import transactions

def display_menu():
    """Display the main command-line menu."""
    print("\n===================================")
    print("     PERSONAL FINANCE TRACKER")
    print("===================================")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Financial Summary")
    print("4. View Expenses by Category")
    print("5. View Monthly Spending")
    print("6. Exit")


def main():
    """Run the Personal Finance Tracker CLI."""
    try:
        transactions.create_file()
    except OSError as error:
        print(f"Unable to prepare the transaction file: {error}")
        return

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        try:
            if choice == "1":
                transactions.add_transaction()
            elif choice == "2":
                transactions.view_transactions()
            elif choice == "3":
                summaries.financial_summary()
            elif choice == "4":
                reports.category_based_expenses()
            elif choice == "5":
                reports.monthly_spending()
            elif choice == "6":
                print("\nThank you for using Personal Finance Tracker!")
                break
            else:
                print("\nInvalid choice. Please select 1-6.")
        except (OSError, ValueError, KeyError) as error:
            print(f"\nThe requested operation could not be completed: {error}")
            print("Please check the transaction data and try again.")


if __name__ == "__main__":
    main()
