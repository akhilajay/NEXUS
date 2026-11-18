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

    for block in blocks:
        heading = block["heading"]
        single_text = f"{heading}\n\n{block['text']}"

        if embeddings.token_count(single_text) > embeddings.token_limit:
            raise ValueError(
                f"{source}: {block['location']} under '{heading}' "
                "is too long as a single paragraph or table row. "
                "Split this block before ingestion."
            )

        if current_blocks and heading != current_heading:
            save_chunk()
            current_blocks = []

        current_heading = heading

        candidate_text = "\n\n".join(
            item["text"] for item in current_blocks + [block]
        )
        candidate = f"{heading}\n\n{candidate_text}"

        if (
            current_blocks
            and embeddings.token_count(candidate) > embeddings.token_limit
        ):
            save_chunk()
            current_blocks = []

        current_blocks.append(block)

    save_chunk()
    return chunks