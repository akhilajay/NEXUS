import argparse
import json
import re
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

from app.models.requirements import RequirementsInventory
from app.storage.neo4j_store import Neo4jStore


BACKEND_DIR = Path(__file__).resolve().parents[2]

REQUIREMENT_ROW = re.compile(
    r"^\s*(BR-\d+|NFR-[A-Z]+-\d+)\s*\|"
)


def collect_expected_ids(chunks: list[dict]) -> dict[str, set[str]]:
    """Find explicit requirement IDs and the chunks that define them."""
    chunks_by_id: dict[str, set[str]] = {}

    for chunk in chunks:
        for line in chunk["text"].splitlines():
            match = REQUIREMENT_ROW.match(line)
            if match:
                requirement_id = match.group(1)
                chunks_by_id.setdefault(requirement_id, set()).add(
                    chunk["chunk_id"]
                )

    return chunks_by_id


def evaluate_ids(
    inventory: RequirementsInventory,
    chunks: list[dict],
) -> dict:
    expected_by_id = collect_expected_ids(chunks)

    if not expected_by_id:
        raise ValueError(
            "No numbered requirement rows were found. Check that the selected "
            "chunks contain rows in the format 'BR-004 | ...' or "
            "'NFR-AVL-001 | ...'."
        )

    actual_counts = Counter(
        requirement.requirement_id
        for requirement in inventory.requirements
        if requirement.requirement_id is not None
    )

    expected_ids = set(expected_by_id)
    actual_ids = set(actual_counts)

    missing_ids = sorted(expected_ids - actual_ids)
    unexpected_ids = sorted(actual_ids - expected_ids)
    repeated_ids = {
        requirement_id: count
        for requirement_id, count in sorted(actual_counts.items())
        if count > 1
    }

    return {
        "passed": not (missing_ids or unexpected_ids or repeated_ids),
        "expected_id_count": len(expected_ids),
        "matched_id_count": len(expected_ids & actual_ids),
        "unnumbered_record_count": sum(
            requirement.requirement_id is None
            for requirement in inventory.requirements
        ),
        "missing_ids": missing_ids,
        "unexpected_ids": unexpected_ids,
        "repeated_ids": repeated_ids,
        "source_chunks_for_missing_ids": {
            requirement_id: sorted(expected_by_id[requirement_id])
            for requirement_id in missing_ids
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check BA inventory IDs against the source documents."
    )
    parser.add_argument("--source", nargs="+", required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    args = parser.parse_args()

    load_dotenv(BACKEND_DIR / ".env", override=True)

    try:
        inventory = RequirementsInventory.model_validate_json(
            args.inventory.read_text(encoding="utf-8-sig")
        )

        store = Neo4jStore()
        try:
            chunks = store.load_chunks_by_source(args.source)
        finally:
            store.close()

        report = evaluate_ids(inventory, chunks)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Could not evaluate inventory: {exc}\n")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())