import os
from pathlib import Path

from sentence_transformers import SentenceTransformer


BACKEND_DIR = Path(__file__).resolve().parents[2]
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class EmbeddingService:
    def __init__(self):
        configured_path = os.getenv("EMBEDDING_MODEL_PATH")
        model_path = Path(
            configured_path or "models/all-MiniLM-L6-v2"
        )

        if not model_path.is_absolute():
            model_path = BACKEND_DIR / model_path

        if model_path.is_dir():
            model_location = str(model_path)
        elif configured_path:
            raise FileNotFoundError(
                f"Embedding model folder not found: {model_path}"
            )
        else:
            model_location = MODEL_NAME

        self.model = SentenceTransformer(
            model_location,
            device="cpu",
            local_files_only=True,
        )
        self.dimension = self.model.get_embedding_dimension()
        self.token_limit = self.model.max_seq_length

    def token_count(self, text: str) -> int:
        return len(
            self.model.tokenizer(
                text,
                add_special_tokens=True,
                truncation=False,
                verbose=False,  # Candidate chunks can exceed the limit.
            )["input_ids"]
        )

    def embed(self, text: str) -> list[float]:
        count = self.token_count(text)

        if count > self.token_limit:
            raise ValueError(
                f"Input contains {count} tokens. "
                f"Model limit is {self.token_limit}."
            )

        return self.model.encode(text).tolist()

    @staticmethod
    def passage_text(chunk: dict) -> str:
        return f"{chunk['heading']}\n\n{chunk['text']}"
