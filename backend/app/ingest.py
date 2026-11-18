import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from app.embeddings.embedding_service import (
    MODEL_NAME,
    EmbeddingService,
)
from app.ingestion.chunker import create_chunks
from app.ingestion.document_reader import read_document
from app.storage.neo4j_store import Neo4jStore


BACKEND_DIR = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description="Ingest a Word document.")
    parser.add_argument("--file", required=True)
    parser.add_argument("--type", required=True, choices=["BRD", "NFR"])
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Save chunks for inspection without uploading.",
    )
    args = parser.parse_args()

    load_dotenv(BACKEND_DIR / ".env", override=True)

    source_path = Path(args.file).resolve()
    blocks = read_document(source_path)

    embeddings = EmbeddingService()

    if embeddings.dimension != 384:
        raise ValueError("The current Neo4j index expects 384 dimensions.")

    chunks = create_chunks(
        blocks=blocks,
        source=source_path.name,
        document_type=args.type,
        embeddings=embeddings,
    )

    if not chunks:
        raise ValueError("No content was extracted from the document.")

    output = (
        BACKEND_DIR
        / "data"
        / "output"
        / f"{source_path.stem}_chunks.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Created {len(chunks)} chunks.")
    print(f"Inspection file: {output}")

    if args.preview:
        return

    rows = []

    for chunk in chunks:
        print(f"Embedding {chunk['chunk_id']}")
        vector = embeddings.embed(
            embeddings.passage_text(chunk)
        )
        rows.append({
            **chunk,
            "embedding": vector,
            "embedding_model": MODEL_NAME,
        })

    store = Neo4jStore()
    try:
        store.ensure_schema()
        store.replace_document(source_path.name, rows)
    finally:
        store.close()

    print(f"Stored {len(rows)} chunks for {source_path.name}.")


if __name__ == "__main__":
    main()