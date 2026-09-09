"""Input validation, sanitization, and shared helper functions."""

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
    """Keep asking until the user enters a date in MM/DD/YYYY format."""
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%m/%d/%Y")
            return date_str
        except ValueError:
            print("Please enter the date as MM/DD/YYYY.")


def get_valid_amount(prompt="Enter the amount: $"):
    """Keep asking until the user enters a valid, non-negative number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative.")
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
    """Display the category menu and return the chosen category name."""
    print("\nCategories:")
    for key, name in CATEGORIES.items():
        print(f"{key}. {name}")

    choice = input("Choose a category (1-9): ")
    return CATEGORIES.get(choice, "Miscellaneous")