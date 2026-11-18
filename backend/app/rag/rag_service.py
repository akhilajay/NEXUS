from app.llm_client import LLMClient
from app.retrieval.retriever import Retriever


class RAGService:
    def __init__(self):
        self.retriever = Retriever()

    def ask(self, question: str, top_k: int = 3) -> dict:
        chunks = self.retriever.retrieve_chunks(
            question,
            top_k=top_k,
        )

        if not chunks:
            return {
                "answer": "No indexed passages were found.",
                "evidence": [],
                "input_tokens": 0,
                "output_tokens": 0,
                "stop_reason": "no_evidence",
            }

        result = LLMClient().answer(question, chunks)
        return {**result, "evidence": chunks}

    def close(self):
        self.retriever.close()