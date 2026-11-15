import argparse

from app.llm_client import LLMClient
from app.retrieval.retriever import Retriever


def main():
    parser = argparse.ArgumentParser(
        description="Answer a question using retrieved BRD evidence."
    )
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
        print("No passages found. Add documents before asking questions.")
        return

    # Show exactly which evidence will be sent to Claude.
    print("\nRetrieved evidence:")
    for chunk in chunks:
        print(
            f"- {chunk['chunk_id']} | {chunk['heading']} | "
            f"score={chunk['score']:.3f}"
        )

    result = LLMClient().answer(args.question, chunks)

    print("\nAnswer:")
    print(result["answer"])

    print(f"\nInput tokens: {result['input_tokens']}")
    print(f"Output tokens: {result['output_tokens']}")
    print(f"Stop reason: {result['stop_reason']}")

    if result["stop_reason"] == "max_tokens":
        print("The answer reached its output limit and may be incomplete.")


if __name__ == "__main__":
    main()