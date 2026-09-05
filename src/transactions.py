"""Transaction management and CSV data storage."""

import csv
import os

from src import utils

DATA_DIR = "data"
FILE_NAME = "transactions.csv"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)


def create_file():
    """Create the data folder and CSV file (with headers) if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount", "Type"])


def add_transaction():
    """Prompt the user for transaction details and append it to the CSV file."""
    print("\n--- Add Transaction ---")

    date = utils.get_valid_date()
    description = utils.get_non_empty_string("Enter a description: ")
    category = utils.get_category_choice()
    amount = utils.get_valid_amount()
    transaction_type = utils.get_valid_transaction_type()

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, f"{amount:.2f}", transaction_type])

    print("\nTransaction successfully saved!")


def load_transactions():
    """Return all transactions as a list of dictionaries."""
    create_file()

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def view_transactions():
    """Print every recorded transaction."""
    print("\n--- All Transactions ---")

    records = load_transactions()

    if not records:
        print("No transactions have been recorded yet.")
        return

    for row in records:
        print(
            f"Date: {row['Date']} | "
            f"Description: {row['Description']} | "
            f"Category: {row['Category']} | "
            f"Amount: ${row['Amount']} | "
            f"Type: {row['Type']}"
        )