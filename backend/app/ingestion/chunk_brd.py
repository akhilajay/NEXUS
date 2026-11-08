import json
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


def chunk_document(path: Path) -> list[dict]:
    document = Document(str(path))
    chunks = []
    heading = "Introduction"
    content = []

    def save_section():
        if content:
            chunks.append({
                "chunk_id": f"{path.stem}-{len(chunks) + 1:03d}",
                "source": path.name,
                "heading": heading,
                "text": "\n\n".join(content),
            })

    for block in document.iter_inner_content():
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text:
                continue

            style = block.style.name if block.style else ""
            if style.startswith("Heading "):
                save_section()
                heading = text
                content = []
            else:
                content.append(text)

        elif isinstance(block, Table):
            rows = [
                " | ".join(cell.text.strip() for cell in row.cells)
                for row in block.rows
            ]
            content.append("\n".join(rows))

    save_section()
    return chunks


if __name__ == "__main__":
    backend_dir = Path(__file__).resolve().parents[2]
    source = backend_dir / "data" / "documents" / "XATA_TODO_BRD.docx"
    output = backend_dir / "data" / "output" / "brd_chunks.json"

    chunks = chunk_document(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote {len(chunks)} chunks to {output}")