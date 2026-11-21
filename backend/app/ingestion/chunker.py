from app.embeddings.embedding_service import EmbeddingService


def create_chunks(
    blocks: list[dict],
    source: str,
    document_type: str,
    embeddings: EmbeddingService,
) -> list[dict]:
    chunks = []
    current_blocks = []
    current_heading = None

    def save_chunk():
        if not current_blocks:
            return

        chunks.append({
            "chunk_id": f"{source}-{len(chunks) + 1:03d}",
            "source": source,
            "document_type": document_type,
            "heading": current_heading,
            "text": "\n\n".join(
                block["text"] for block in current_blocks
            ),
            "locations": [
                block["location"] for block in current_blocks
            ],
        })

    def fits(heading: str, text: str) -> bool:
        return embeddings.token_count(f"{heading}\n\n{text}") <= embeddings.token_limit

    def split_block(heading: str, text: str, location: str):
        if fits(heading, text):
            yield text
            return

        if len(text) <= 1 or not fits(heading, ""):
            raise ValueError(
                f"{source}: no room for text under {heading!r} at {location} "
                f"within the {embeddings.token_limit}-token limit."
            )

        # Prefer a word boundary near the middle. A long unbroken word
        # can still be split by character and checked using the tokenizer.
        middle = len(text) // 2
        boundary = text.rfind(" ", middle // 2, middle + 1)
        if boundary <= 0:
            boundary = middle
        yield from split_block(heading, text[:boundary].rstrip(), location)
        yield from split_block(heading, text[boundary:].lstrip(), location)

    for block in blocks:
        heading = block["heading"]
        if current_blocks and heading != current_heading:
            save_chunk()
            current_blocks = []

        current_heading = heading

        for part in split_block(heading, block["text"], block["location"]):
            if current_blocks:
                candidate_text = "\n\n".join(
                    [item["text"] for item in current_blocks] + [part]
                )
                if not fits(heading, candidate_text):
                    save_chunk()
                    current_blocks = []

            current_blocks.append({**block, "text": part})
    save_chunk()
    return chunks
