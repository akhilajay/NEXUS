import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer


BACKEND_DIR = Path(__file__).resolve().parents[2]
CHUNKS_FILE = BACKEND_DIR / "data" / "output" / "brd_chunks.json"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def read_chunks() -> list[dict]:
    if not CHUNKS_FILE.is_file():
        raise SystemExit(f"Chunk file not found: {CHUNKS_FILE}")

    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    if not chunks:
        raise SystemExit(f"No chunks found in {CHUNKS_FILE}")

    return chunks


def embed(model: SentenceTransformer, text: str, label: str) -> list[float]:
    token_ids = model.tokenizer(text, truncation=False)["input_ids"]
    limit = model.max_seq_length

    if len(token_ids) > limit:
        raise SystemExit(
            f"{label} has {len(token_ids)} tokens, but the model limit is {limit}. "
            "Shorten the input before embedding it."
        )

    return model.encode(text).tolist()


def embed_chunk(model: SentenceTransformer, chunk: dict) -> list[float]:
    text = f"{chunk['heading']}\n\n{chunk['text']}"
    return embed(model, text, label=chunk["chunk_id"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed and search NEXUS BRD chunks.")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("preview", help="Embed the first chunk and print a sample.")
    commands.add_parser("upload", help="Embed all chunks and store them in Neo4j.")
    search = commands.add_parser("search", help="Find passages relevant to a question.")
    search.add_argument("question")
    args = parser.parse_args()

    model = SentenceTransformer(MODEL_NAME, device="cpu")

    if args.command == "preview":
        chunk = read_chunks()[0]
        vector = embed_chunk(model, chunk)

        print(f"Chunk: {chunk['chunk_id']} | {chunk['heading']}")
        print(f"Dimensions: {len(vector)}")
        print(f"First five values: {vector[:5]}")
        return

    load_dotenv(BACKEND_DIR / ".env")
    database = os.getenv("NEO4J_DATABASE", "neo4j")
    auth = (os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"])

    with GraphDatabase.driver(os.environ["NEO4J_URI"], auth=auth) as driver:
        if args.command == "upload":
            rows = []
            for chunk in read_chunks():
                print(f"Embedding {chunk['chunk_id']}")
                rows.append({**chunk, "embedding": embed_chunk(model, chunk)})

            records, _, _ = driver.execute_query(
                """
                UNWIND $rows AS row
                MERGE (c:NexusChunk {
                    source: row.source,
                    chunk_id: row.chunk_id
                })
                SET c.heading = row.heading,
                    c.text = row.text,
                    c.embedding = row.embedding,
                    c.embedding_model = $model
                RETURN count(c) AS stored
                """,
                rows=rows,
                model=MODEL_NAME,
                database_=database,
            )
            print(f"Stored {records[0]['stored']} chunks in Neo4j")
            return

        vector = embed(model, args.question, label="Search question")
        records, _, _ = driver.execute_query(
            """
            CYPHER 25
            MATCH (c:NexusChunk)
            SEARCH c IN (
                VECTOR INDEX nexus_brd_embeddings
                FOR $embedding
                LIMIT 3
            ) SCORE AS score
            RETURN c.chunk_id AS chunk_id, c.source AS source,
                   c.heading AS heading, c.text AS text, score
            ORDER BY score DESC
            """,
            embedding=vector,
            database_=database,
        )

        if not records:
            print("No indexed chunks found.")
            return

        for record in records:
            print(
                f"\n{record['score']:.3f} | {record['source']} | "
                f"{record['chunk_id']} | {record['heading']}"
            )
            print(record["text"])


if __name__ == "__main__":
    main()