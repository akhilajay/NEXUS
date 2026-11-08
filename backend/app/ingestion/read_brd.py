from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph



def print_document(path):
    document = Document(path)

    for block in document.iter_inner_content():
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if text:
                style = block.style.name if block.style else "Paragraph"
                print(f"[{style}] {text}")

        elif isinstance(block, Table):
            print("[Table]")
            for row in block.rows:
                cells = [cell.text.strip() for cell in row.cells]
                print(" | ".join(cells))


if __name__ == "__main__":
    print_document("data/documents/XATA_TODO_BRD.docx")