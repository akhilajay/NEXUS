import argparse

from app.rag.rag_service import RAGService


def main():
    parser = argparse.ArgumentParser(
        description="Answer using BRD and NFR evidence."
    )
    parser.add_argument("question")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    service = RAGService()
    try:
        result = service.ask(
            args.question,
            top_k=args.top_k,
        )
    finally:
        service.close()

    print("\nRetrieved evidence:")
    for chunk in result["evidence"]:
        print(
            f"- {chunk['chunk_id']} | {chunk['heading']} | "
            f"score={chunk['score']:.3f}"
        )

    print("\nAnswer:")
    print(result["answer"])
    print(f"\nInput tokens: {result['input_tokens']}")
    print(f"Output tokens: {result['output_tokens']}")
    print(f"Stop reason: {result['stop_reason']}")

    if result["stop_reason"] == "max_tokens":
        print("The answer reached its output limit and may be incomplete.")


if __name__ == "__main__":
    main()