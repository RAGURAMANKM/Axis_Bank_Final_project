import pdfplumber

pdf_file = "pdf_files/0001_Thiyagarajan_Subbu_Statement.pdf"

with pdfplumber.open(pdf_file) as pdf:

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

print(text[:4000])