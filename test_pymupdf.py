import fitz

doc = fitz.open("pdf_files/0001_Thiyagarajan_Subbu_Statement.pdf")

page = doc[0]

blocks = page.get_text("blocks")

for i, block in enumerate(blocks):
    print("=" * 60)
    print(f"BLOCK {i}")
    print(repr(block[4]))