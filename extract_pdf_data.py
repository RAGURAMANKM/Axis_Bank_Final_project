import fitz
import pandas as pd
import os

PDF_FOLDER = "pdf_files"

customers = []


def get_next_value(lines, label):
    for i, line in enumerate(lines):
        if line.strip() == label:
            if i + 1 < len(lines):
                return lines[i + 1].strip()
    return None


def extract_pdf(file_path):

    doc = fitz.open(file_path)

    text = ""

    for page in doc:
        text += page.get_text()

    lines = [x.strip() for x in text.split("\n") if x.strip()]

    data = {}

    # --------------------------------
    # Customer Name (from text blocks)
    # --------------------------------
    customer_name = None

    blocks = doc[0].get_text("blocks")

    for block in blocks:

        block_text = block[4].strip()

        block_lines = [
            line.strip()
            for line in block_text.split("\n")
            if line.strip()
        ]

        # Example:
        # Thiyagarajan Subbu
        # Thiyagarajan Subbu
        if (
            len(block_lines) >= 2
            and block_lines[0] == block_lines[1]
            and "Account" not in block_lines[0]
            and "Statement" not in block_lines[0]
            and len(block_lines[0]) > 3
        ):
            customer_name = block_lines[0]
            break

    data["customer_name"] = customer_name

    # --------------------------------
    # Other Fields
    # --------------------------------
    data["account_number"] = get_next_value(lines, "Account Number:")
    data["account_type"] = get_next_value(lines, "Account Type:")
    data["ifsc"] = get_next_value(lines, "IFSC Code:")
    data["branch"] = get_next_value(lines, "Branch:")
    data["currency"] = get_next_value(lines, "Currency:")

    # --------------------------------
    # Statement Period
    # --------------------------------
    data["statement_start"] = None
    data["statement_end"] = None

    for i, line in enumerate(lines):

        if line == "Statement Period:":

            if i + 1 < len(lines):

                period = lines[i + 1]

                if "to" in period:

                    start, end = period.split("to")

                    data["statement_start"] = start.strip()
                    data["statement_end"] = end.strip()

            break

    data["source_file"] = os.path.basename(file_path)

    doc.close()

    return data


for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        print("Processing:", file)

        customers.append(
            extract_pdf(
                os.path.join(PDF_FOLDER, file)
            )
        )

df = pd.DataFrame(customers)

print("\nColumns:")
print(df.columns)

print("\nSample Data:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv(
    "customers_extracted.csv",
    index=False
)

print("\nSaved: customers_extracted.csv")
print("Total Customers:", len(df))