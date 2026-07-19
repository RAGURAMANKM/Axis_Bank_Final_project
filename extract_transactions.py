import pdfplumber
import pandas as pd
import os
import re

PDF_FOLDER = "pdf_files"      # Change if your PDFs are elsewhere

transactions = []

# Transaction pattern
pattern = re.compile(
    r"(\d{2}-\d{2}-\d{4})\s+"
    r"(.*?)\s+"
    r"(DR|CR)\s+"
    r"([\d,]+\.\d{2})\s+"
    r"(-?[\d,]+\.\d{2})"
)

for pdf in os.listdir(PDF_FOLDER):

    if not pdf.endswith(".pdf"):
        continue

    path = os.path.join(PDF_FOLDER, pdf)

    print("Reading:", pdf)

    try:

        with pdfplumber.open(path) as pdf_file:

            for page in pdf_file.pages:

                text = page.extract_text()

                if not text:
                    continue

                for line in text.split("\n"):

                    m = pattern.search(line)

                    if m:

                        date = m.group(1)
                        description = m.group(2)
                        trans_type = m.group(3)
                        amount = float(m.group(4).replace(",", ""))
                        balance = float(m.group(5).replace(",", ""))

                        debit = amount if trans_type == "DR" else 0
                        credit = amount if trans_type == "CR" else 0

                        transactions.append({

                            "source_file": pdf,
                            "date": date,
                            "description": description,
                            "type": trans_type,
                            "debit": debit,
                            "credit": credit,
                            "balance": balance

                        })

    except Exception as e:

        print("Error:", pdf, e)

df = pd.DataFrame(transactions)

print(df.head())

print()

print("Rows:", len(df))

df.to_csv("transactions.csv", index=False)

print("Saved transactions.csv")