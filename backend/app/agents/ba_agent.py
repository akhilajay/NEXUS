import argparse
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

from app.storage.neo4j_store import Neo4jStore


BACKEND_DIR = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Load source evidence for the Business Analyst agent."
    )
    parser.add_argument(
        "--source",
        nargs="+",
        required=True,
        help="One or more source filenames as stored in Neo4j.",
    )
    args = parser.parse_args()

    load_dotenv(BACKEND_DIR / ".env", override=True)

    store = Neo4jStore()
    try:
        chunks = store.load_chunks_by_source(args.source)
    finally:
        store.close()

    counts = Counter(chunk["source"] for chunk in chunks)
    print(f"Loaded {len(chunks)} chunks.")
    for source, count in sorted(counts.items()):
        print(f"  {source}: {count} chunks")

    for chunk in chunks:
        print(
            f"\n[{chunk['chunk_id']}] "
            f"{chunk['document_type']} | {chunk['heading']}"
        )
        locations = ", ".join(chunk["locations"] or [])
        print(f"Locations: {locations or '(none recorded)'}")
        print(chunk["text"])


if __name__ == "__main__":
    main()