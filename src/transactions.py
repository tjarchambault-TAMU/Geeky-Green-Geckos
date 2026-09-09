"""Transaction management and CSV data storage."""

import csv
import os

import utils

DATA_DIR = "data"
FILE_NAME = "transactions.csv"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)

# --------------------------------------------------------
# Create the transaction file
# --------------------------------------------------------
def create_file():
    """Create the data folder and CSV file (with headers) if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount", "Type"])


# --------------------------------------------------------
# Save a transaction to the CSV file
# --------------------------------------------------------
def save_transaction(date, description, category, amount, transaction_type):
    """save a completed transaction to the CSV file."""

    # make sure the data folder and transaction file exist
    create_file()

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            date,
            description,
            category,
            f"{amount:.2f}",
            transaction_type
        ])



# --------------------------------------------------------
# Add a new transaction
# --------------------------------------------------------
def add_transaction():
    print("\n--- Add Transaction ---")

    # Get the transaction date and description.
    date = utils.get_valid_date()
    description = utils.get_non_empty_string("Enter a description: ")

    # Determine whether the transaction is income or an expense.
    transaction_type = utils.get_valid_transaction_type()

    # Income transactions automatically use the Income category.
    # Expense transactions require the user to select a category.
    if transaction_type == "income":
        category = "Income"
    else:
        category = utils.get_category_choice()

    # Get the transaction amount.
    amount = utils.get_valid_amount()

    # Save the completed transaction.
    save_transaction(
        date,
        description,
        category,
        amount,
        transaction_type
    )

    print("\nTransaction successfully saved!")


# --------------------------------------------------------
# Load transactions from the CSV file
# --------------------------------------------------------
def load_transactions():
    """Return all transactions as a list of dictionaries."""
    create_file()

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# --------------------------------------------------------
# Display all transactions
# --------------------------------------------------------
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
