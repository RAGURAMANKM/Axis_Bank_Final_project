import os
import pandas as pd

from parser.customer_parser import extract_customer
from parser.transaction_parser import extract_transactions


PDF_FOLDER = "pdf_files"


customers = []
transactions = []


pdf_files = sorted([
    file
    for file in os.listdir(PDF_FOLDER)
    if file.lower().endswith(".pdf")
])


print("=" * 60)
print("Axis Bank PDF Dataset Builder")
print("=" * 60)
print()


total = len(pdf_files)

for index, file in enumerate(pdf_files, start=1):

    print(f"[{index}/{total}] Processing {file}")

    path = os.path.join(PDF_FOLDER, file)

    try:

        customer = extract_customer(path)

        customers.append(customer)

        txn_df = extract_transactions(path)

        if not txn_df.empty:

            txn_df["account_number"] = customer["account_number"]

            transactions.append(txn_df)

    except Exception as e:

        print("ERROR :", file)

        print(e)

        print()


print()
print("=" * 60)

customers_df = pd.DataFrame(customers)

customers_df = customers_df[
    [
        "account_number",
        "customer_name",
        "account_type",
        "branch",
        "ifsc",
        "currency",
        "statement_start",
        "statement_end",
        "source_file"
    ]
]

customers_df.to_csv(
    "customers_extracted.csv",
    index=False
)

print("Customers Saved :", len(customers_df))


if len(transactions):

    transactions_df = pd.concat(
        transactions,
        ignore_index=True
    )

else:

    transactions_df = pd.DataFrame()


transactions_df.to_csv(
    "transactions.csv",
    index=False
)

print("Transactions Saved :", len(transactions_df))

print()

print("Finished Successfully.")