"""Personal Finance Tracker - command-line entry point."""

from src import transactions
from src import summaries
from src import visualizer


def display_menu():
    print("\n===================================")
    print("     PERSONAL FINANCE TRACKER")
    print("===================================")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Financial Summary")
    print("4. Manage Budgets")
    print("5. View Budget Status")
    print("6. View Expenses-by-Category Chart")
    print("7. Exit")


def main():
    transactions.create_file()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            transactions.add_transaction()
        elif choice == "2":
            transactions.view_transactions()
        elif choice == "3":
            summaries.financial_summary()
        elif choice == "4":
            print("\nBudget management is coming in a future phase.")
        elif choice == "5":
            print("\nBudget status tracking is coming in a future phase.")
        elif choice == "6":
            visualizer.show_category_chart()
        elif choice == "7":
            print("\nThank you for using Personal Finance Tracker!")
            break
        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()