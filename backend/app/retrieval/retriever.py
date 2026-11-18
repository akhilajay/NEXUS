import argparse
from pathlib import Path

from dotenv import load_dotenv

from app.embeddings.embedding_service import EmbeddingService
from app.storage.neo4j_store import Neo4jStore


BACKEND_DIR = Path(__file__).resolve().parents[2]


class Retriever:
    def __init__(self):
        load_dotenv(BACKEND_DIR / ".env", override=True)
        self.embeddings = EmbeddingService()
        self.store = Neo4jStore()

    def retrieve_chunks(
        self,
        question: str,
        top_k: int = 3,
    ) -> list[dict]:
        question = question.strip()

        if not question:
            raise ValueError("Enter a question.")

        if not 1 <= top_k <= 10:
            raise ValueError("top_k must be between 1 and 10.")

        vector = self.embeddings.embed(question)
        return self.store.search(vector, top_k)

    def close(self):
        self.store.close()


def main():
    parser = argparse.ArgumentParser(description="Search document passages.")
    parser.add_argument("question")
    parser.add_argument("--top-k", type=int, default=3)
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
        print("No passages found.")

    for chunk in chunks:
        print(
            f"\n{chunk['score']:.3f} | {chunk['source']} | "
            f"{chunk['chunk_id']} | {chunk['heading']}"
        )
        print(chunk["text"])


if __name__ == "__main__":
    main()