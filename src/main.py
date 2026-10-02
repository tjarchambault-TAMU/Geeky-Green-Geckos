# PROGRAM:    Personal Finance Tracker - Main
# PURPOSE:    Provide the main command-line interface for the Personal Finance Tracker.
# INPUT:      User menu selections.
# PROCESS:    Displays program options and directs user selections to the appropriate
#             transaction, summary, and reporting functions.
# OUTPUT:     Displays menus, program results, and status messages to the user.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received
#             unauthorized aid on this academic work.
# Gen AI:     In keeping with my commitment to leverage advanced technology
#             for enhanced efficiency and accuracy in my work, I use
#             generative artificial intelligence tools to assist in writing
#             my Python code.

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
    print("4. View Reports")
    print("5. Exit")

def reports_menu():
    """Display and process the financial reports menu."""

    while True:
        print("\n--- Financial Reports ---")
        print("1. Expenses by Category")
        print("2. Monthly Spending")
        print("3. Return to Main Menu")

        choice = input("\nChoose a report (1-3): ").strip()

        if choice == "1":
            reports.category_based_expenses()

        elif choice == "2":
            reports.monthly_spending()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please select 1-3.")

def main():
    """Run the Personal Finance Tracker CLI."""
    try:
        transactions.create_file()
    except OSError as error:
        print(f"Unable to prepare the transaction file: {error}")
        return

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        try:
            if choice == "1":
                transactions.add_transaction()
            elif choice == "2":
                transactions.view_transactions()
            elif choice == "3":
                summaries.financial_summary()

            elif choice == "4":
                reports_menu()

            elif choice == "5":
                print("\nThank you for using Personal Finance Tracker!")
                break

            else:
                print("\nInvalid choice. Please select 1-5.")
        except (OSError, ValueError, KeyError) as error:
            print(f"\nThe requested operation could not be completed: {error}")
            print("Please check the transaction data and try again.")


if __name__ == "__main__":
    main()
