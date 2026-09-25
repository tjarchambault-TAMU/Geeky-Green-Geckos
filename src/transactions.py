"""Transaction management and CSV data storage."""

import csv
import os

from . import utils

DATA_DIR = "data"
FILE_NAME = "transactions.csv"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)
HEADERS = ["Date", "Description", "Category", "Amount", "Type"]

def create_file():
    """Create the data folder and CSV file with headers if needed."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(HEADERS)

def save_transaction(date, description, category, amount, transaction_type):
    """Save a completed transaction to the CSV file."""
    create_file()
    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([date, description, category, f"{amount:.2f}", transaction_type])

def add_transaction():
    """Prompt for and save a new transaction."""
    print("\n--- Add Transaction ---")
    date = utils.get_valid_date()
    description = utils.get_non_empty_string("Enter a description: ")
    transaction_type = utils.get_valid_transaction_type()
    category = "Income" if transaction_type == "income" else utils.get_category_choice()
    amount = utils.get_valid_amount()
    try:
        save_transaction(date, description, category, amount, transaction_type)
        print("\nTransaction successfully saved!")
    except OSError as error:
        print(f"\nUnable to save the transaction: {error}")

def load_transactions():
    """Return valid transaction rows from the CSV file."""
    try:
        create_file()
        with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != HEADERS:
                raise ValueError("transactions.csv has an unexpected header or format.")
            records = []
            for row_number, row in enumerate(reader, start=2):
                if any(value is None for value in row.values()):
                    print(f"Warning: row {row_number} contains missing fields and will be skipped.")
                    continue
                records.append(row)
            return records
    except FileNotFoundError:
        print("Transaction file could not be found.")
        return []
    except (OSError, csv.Error, ValueError) as error:
        print(f"Unable to read transaction data: {error}")
        return []

def view_transactions():
    """Print every recorded transaction."""
    print("\n--- All Transactions ---")
    records = load_transactions()
    if not records:
        print("No valid transactions have been recorded yet.")
        return
    for row in records:
        print(f"Date: {row['Date']} | Description: {row['Description']} | Category: {row['Category']} | Amount: ${row['Amount']} | Type: {row['Type']}")