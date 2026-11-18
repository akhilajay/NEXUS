from pathlib import Path


from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


def read_document(path: Path) -> list[dict]:
    if not path.is_file():
        raise FileNotFoundError(f"Document not found: {path}")

    if path.suffix.lower() != ".docx":
        raise ValueError("This reader supports .docx files.")

    document = Document(str(path))
    blocks = []
    heading = "Introduction"

    for position, block in enumerate(document.iter_inner_content(), start=1):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text:
                continue

            style = block.style.name if block.style else ""
            if style.startswith("Heading "):
                heading = text
                continue

            blocks.append({
                "heading": heading,
                "text": text,
                "location": f"body-block-{position}",
            })

        elif isinstance(block, Table):
            rows = [
                " | ".join(cell.text.strip() for cell in row.cells)
                for row in block.rows
            ]

            if not rows:
                continue

            header = rows[0]

            for row_number, row in enumerate(rows[1:], start=2):
                if not row.replace("|", "").strip():
                    continue

                blocks.append({
                    "heading": heading,
                    "text": f"{header}\n{row}",
                    "location": f"body-block-{position}-row-{row_number}",
                })

            # Preserve a table containing only one row.
            if len(rows) == 1:
                blocks.append({
                    "heading": heading,
                    "text": header,
                    "location": f"body-block-{position}-row-1",
                })

    return blocks