import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer

from app.embeddings.brd_vectors import embed


BACKEND_DIR = Path(__file__).resolve().parents[2]
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_MODEL_DIR = BACKEND_DIR / "models" / "all-MiniLM-L6-v2"


class Retriever:
    def __init__(self):
        load_dotenv(BACKEND_DIR / ".env",override=True)

        configured_path = os.getenv("EMBEDDING_MODEL_PATH")
        model_path = (
            Path(configured_path)
            if configured_path
            else DEFAULT_MODEL_DIR
        )

        # Relative configured paths are resolved from backend/.
        if not model_path.is_absolute():
            model_path = BACKEND_DIR / model_path

        if model_path.is_dir():
            self.model = SentenceTransformer(
                str(model_path),
                device="cpu",
                local_files_only=True,
            )
        elif configured_path:
            raise FileNotFoundError(
                f"Configured embedding model folder not found: {model_path}"
            )
        else:
            # Uses the existing Hugging Face cache where possible.
            self.model = SentenceTransformer(
                MODEL_NAME,
                device="cpu",
                local_files_only=True,
            )

        self.database = os.environ["NEO4J_DATABASE"]
        self.driver = GraphDatabase.driver(
            os.environ["NEO4J_URI"],
            auth=(
                os.environ["NEO4J_USERNAME"],
                os.environ["NEO4J_PASSWORD"],
            ),
        )

    def retrieve_chunks(
        self,
        question: str,
        top_k: int = 10,
    ) -> list[dict]:
        question = question.strip()

        if not question:
            raise ValueError("Enter a question.")

        if not 1 <= top_k <= 10:
            raise ValueError("top_k must be between 1 and 10.")

        vector = embed(
            self.model,
            question,
            label="Search question",
        )

        records, _, _ = self.driver.execute_query(
            """
            CYPHER 25
            MATCH (c:NexusChunk)
            SEARCH c IN (
                VECTOR INDEX nexus_brd_embeddings
                FOR $embedding
                LIMIT $top_k
            ) SCORE AS score
            RETURN
                c.chunk_id AS chunk_id,
                c.source AS source,
                c.heading AS heading,
                c.text AS text,
                score
            ORDER BY score DESC
            """,
            embedding=vector,
            top_k=top_k,
            database_=self.database,
        )

        return [dict(record) for record in records]

    def close(self):
        self.driver.close()


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve BRD passages from Neo4j."
    )
    parser.add_argument("question")
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()

    retriever = Retriever()
    try:
        chunks = retriever.retrieve_chunks(
            args.question,
            top_k=args.top_k,
        )
    finally:
        retriever.close()

    if not chunks:
        print("No indexed chunks found.")
        return

    for chunk in chunks:
        print(
            f"\n{chunk['score']:.3f} | {chunk['source']} | "
            f"{chunk['chunk_id']} | {chunk['heading']}"
        )
        print(chunk["text"])


if __name__ == "__main__":
    main()