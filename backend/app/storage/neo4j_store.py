import os

from neo4j import GraphDatabase


class Neo4jStore:
    def __init__(self):
        self.database = os.environ["NEO4J_DATABASE"]
        self.driver = GraphDatabase.driver(
            os.environ["NEO4J_URI"],
            auth=(
                os.environ["NEO4J_USERNAME"],
                os.environ["NEO4J_PASSWORD"],
            ),
            connection_timeout=10,
            max_transaction_retry_time=10,
        )

    def ensure_schema(self):
        self.driver.execute_query(
            """
            CREATE CONSTRAINT nexus_document_source IF NOT EXISTS
            FOR (d:NexusDocument) REQUIRE d.source IS UNIQUE
            """,
            database_=self.database,
        )

        self.driver.execute_query(
            """
            CREATE CONSTRAINT nexus_chunk_identity IF NOT EXISTS
            FOR (c:NexusChunk)
            REQUIRE (c.source, c.chunk_id) IS UNIQUE
            """,
            database_=self.database,
        )

        self.driver.execute_query(
            """
            CREATE VECTOR INDEX nexus_brd_embeddings IF NOT EXISTS
            FOR (c:NexusChunk) ON (c.embedding)
            OPTIONS {indexConfig: {
                `vector.dimensions`: 384,
                `vector.similarity_function`: 'cosine'
            }}
            """,
            database_=self.database,
        )

        records, _, _ = self.driver.execute_query(
            """
            SHOW VECTOR INDEXES
            YIELD name, labelsOrTypes, properties, options
            WHERE name = 'nexus_brd_embeddings'
            RETURN labelsOrTypes, properties, options
            """,
            database_=self.database,
        )

        if not records:
            raise ValueError("Vector index 'nexus_brd_embeddings' was not found.")

        index = records[0]
        configuration = index["options"]["indexConfig"]
        dimensions = configuration.get("vector.dimensions")
        similarity = configuration.get("vector.similarity_function")
        labels = index["labelsOrTypes"]
        properties = index["properties"]

        if (
            labels != ["NexusChunk"]
            or properties != ["embedding"]
            or dimensions != 384
            or str(similarity).casefold() != "cosine"
        ):
            raise ValueError(
                "Expected 'nexus_brd_embeddings' on NexusChunk.embedding "
                "with 384 dimensions and cosine similarity. "
                f"Found labels={labels!r}, properties={properties!r}, "
                f"dimensions={dimensions!r}, similarity={similarity!r}."
            )

    def replace_document(self, source: str, rows: list[dict]):
        def replace(tx):
            # Updating this document node serializes writes for this source.
            tx.run(
                """
                MERGE (d:NexusDocument {source: $source})
                SET d.updated_at = datetime()
                """,
                source=source,
            ).consume()

            tx.run(
                """
                MATCH (c:NexusChunk {source: $source})
                DETACH DELETE c
                """,
                source=source,
            ).consume()

            tx.run(
                """
                UNWIND $rows AS row
                CREATE (c:NexusChunk)
                SET c = row
                """,
                rows=rows,
            ).consume()

        with self.driver.session(database=self.database) as session:
            session.execute_write(replace)

    def search(self, vector: list[float], top_k: int) -> list[dict]:
        records, _, _ = self.driver.execute_query(
            """
            CYPHER 25
            MATCH (c:NexusChunk)
            SEARCH c IN (
                VECTOR INDEX nexus_brd_embeddings
                FOR $embedding
                LIMIT $top_k
            ) SCORE AS score
            RETURN c.chunk_id AS chunk_id,
                   c.source AS source,
                   c.document_type AS document_type,
                   c.heading AS heading,
                   c.text AS text,
                   c.locations AS locations,
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


    def load_chunks_by_source(self, sources: list[str]) -> list[dict]:
        records, _, _ = self.driver.execute_query(
            """
            MATCH (c:NexusChunk)
            WHERE c.source IN $sources
            RETURN c.chunk_id AS chunk_id,
                   c.source AS source,
                   c.document_type AS document_type,
                   c.heading AS heading,
                   c.text AS text,
                   c.locations AS locations
            ORDER BY source, chunk_id
            """,
            sources=sources,
            database_=self.database,
            routing_="r",
        )

        chunks = [dict(record) for record in records]

        found_sources = {chunk["source"] for chunk in chunks}
        missing_sources = sorted(set(sources) - found_sources)

        if missing_sources:
            raise ValueError(
                f"No chunks found for: {', '.join(missing_sources)}. "
                "Check the filenames or ingest the missing documents first."
            )

        return chunks
