from parser.pdf_reader import read_pdf

pdf = "pdf_files/0001_Thiyagarajan_Subbu_Statement.pdf"

text = read_pdf(pdf)

print(text[:3000])