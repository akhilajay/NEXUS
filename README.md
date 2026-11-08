# NEXUS

NEXUS is a Python-based project for ingesting BRD documents, chunking them, and embedding the resulting text into Neo4j for semantic search.

## Requirements

On a fresh Windows machine, install:

- Git
- Python 3.10 or newer
- A Neo4j instance (for example Neo4j Aura or a local Neo4j database)

## Fresh setup on Windows

From PowerShell:

```powershell
git clone <repo-url>
cd NEXUS

py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r .\backend\requirement.txt
```

Create a local environment file at `backend/.env` with the required values:

```env
NEO4J_URI=neo4j+s://<your-instance>.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=<your-neo4j-password>
ANTHROPIC_API_KEY=<your-anthropic-api-key>
```

If you are using a local Neo4j instance, `NEO4J_URI` may look like:

```env
NEO4J_URI=bolt://localhost:7687
```

## Run the project

From the project root, activate the virtual environment if it is not already active:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 1) Chunk the BRD document

```powershell
python .\backend\app\ingestion\chunk_brd.py
```

This reads the BRD file and writes JSON chunks to:

```text
backend\data\output\brd_chunks.json
```

### 2) Preview embeddings

```powershell
python .\backend\app\embeddings\brd_vectors.py preview
```

### 3) Upload embeddings to Neo4j

```powershell
python .\backend\app\embeddings\brd_vectors.py upload
```

### 4) Search semantically

```powershell
python .\backend\app\embeddings\brd_vectors.py search "What is the project objective?"
```

## Notes

- The repository already ignores `backend/.env` in Git via `.gitignore`.
- If `backend/data/output/brd_chunks.json` is missing, run the chunking step before embedding or searching.
- The project expects Neo4j to already be running and reachable using the values in `backend/.env`.
