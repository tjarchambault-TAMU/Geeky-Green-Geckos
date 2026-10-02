# PROGRAM:    Personal Finance Tracker - Utilities
# PURPOSE:    Provide shared input validation and helper functions.
# INPUT:      User-entered dates, descriptions, amounts, categories, and menu selections.
# PROCESS:    Validates and sanitizes user input before it is used by other modules.
# OUTPUT:     Validated values or appropriate error messages for invalid input.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received
#             unauthorized aid on this academic work.
# Gen AI:     In keeping with my commitment to leverage advanced technology
#             for enhanced efficiency and accuracy in my work, I use
#             generative artificial intelligence tools to assist in writing
#             my Python code.

from datetime import datetime

CATEGORIES = {
    "1": "Housing",
    "2": "Utilities",
    "3": "Groceries",
    "4": "Transportation",
    "5": "Dining",
    "6": "Entertainment",
    "7": "Education",
    "8": "Healthcare",
    "9": "Miscellaneous",
}


def get_non_empty_string(prompt):
    """Keep asking until the user enters non-blank text, then return it stripped."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_valid_date(prompt="Enter the date (MM/DD/YYYY): "):
    """Keep asking until the user enters a valid date."""
    while True:
        date_str = input(prompt).strip()

        try:
            entered_date = datetime.strptime(date_str, "%m/%d/%Y")
            current_date = datetime.now()

            if entered_date > current_date:
                print("Transaction date cannot be in the future.")
                continue

            if entered_date.year < current_date.year:
                print("Transaction date must be within the current year.")
                continue

            return date_str

        except ValueError:
            print("Please enter the date as MM/DD/YYYY.")


def get_valid_amount(prompt="Enter the amount: $"):
    """Keep asking until the user enters a valid, positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_valid_transaction_type():
    """Prompt the user to select either income or expense."""

    while True:
        print("\nTransaction Type:")
        print("1. Income")
        print("2. Expense")

        choice = input("Choose a transaction type (1-2): ")

        if choice == "1":
            return "income"
        elif choice == "2":
            return "expense"
        else:
            print("Invalid choice. Please select 1 or 2.")


def get_category_choice():
    """Display the category menu and keep asking until a valid category is selected."""

    while True:
        print("\nCategories:")

        for key, name in CATEGORIES.items():
            print(f"{key}. {name}")

        choice = input("Choose a category (1-9): ").strip()

        if choice in CATEGORIES:
            return CATEGORIES[choice]

        print("Invalid choice. Please select a category from 1-9.")
