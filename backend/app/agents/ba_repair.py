import argparse
import json
import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

from app.agents.ba_agent import BA_INSTRUCTIONS, validate_source_references
from app.agents.ba_eval import evaluate_ids
from app.models.requirements import Requirement, RequirementsInventory
from app.storage.neo4j_store import Neo4jStore


BACKEND_DIR = Path(__file__).resolve().parents[2]


def recover_requirement(
    client: Anthropic,
    model: str,
    requirement_id: str,
    evidence: list[dict],
) -> Requirement:
    request = {
        "task": (
            f"Recover only the requirement with ID {requirement_id}. "
            "Return a requirements inventory containing exactly one requirement "
            "and an empty open_questions list."
        ),
        "output_schema": RequirementsInventory.model_json_schema(),
        "evidence": evidence,
    }

    response = client.messages.create(
        model=model,
        max_tokens=2048,
        system=BA_INSTRUCTIONS,
        messages=[
            {
                "role": "user",
                "content": json.dumps(request, ensure_ascii=False),
            }
        ],
    )

    if response.stop_reason != "end_turn":
        raise ValueError(f"Unexpected Claude stop reason: {response.stop_reason}")

    text = "".join(
        block.text for block in response.content if block.type == "text"
    )
    candidate = RequirementsInventory.model_validate_json(text)

    returned_ids = [item.requirement_id for item in candidate.requirements]
    if returned_ids != [requirement_id] or candidate.open_questions:
        raise ValueError(
            f"Expected only {requirement_id} and no open questions. "
            f"Received IDs: {returned_ids!r}."
        )

    validate_source_references(candidate, evidence)
    return candidate.requirements[0]


def repair_missing_ids(
    inventory: RequirementsInventory,
    chunks: list[dict],
    model: str | None,
    max_attempts: int,
) -> tuple[RequirementsInventory, dict]:
    working = inventory.model_copy(deep=True)
    report = evaluate_ids(working, chunks)

    if not report["missing_ids"]:
        return working, report

    if not model:
        raise ValueError("Pass --model or set ANTHROPIC_MODEL in backend/.env.")

    with Anthropic() as client:
        for attempt in range(1, max_attempts + 1):
            print(f"\nRepair round {attempt}/{max_attempts}")

            for requirement_id in report["missing_ids"]:
                chunk_ids = set(
                    report["source_chunks_for_missing_ids"][requirement_id]
                )
                evidence = [
                    chunk for chunk in chunks if chunk["chunk_id"] in chunk_ids
                ]

                try:
                    requirement = recover_requirement(
                        client, model, requirement_id, evidence
                    )
                except ValueError as exc:
                    print(f"  {requirement_id}: repair rejected ({exc})")
                    continue

                working.requirements.append(requirement)
                print(f"  {requirement_id}: recovered and validated")

            report = evaluate_ids(working, chunks)
            if not report["missing_ids"]:
                break

    return working, report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Recover missing numbered BA requirements and rerun evaluation."
    )
    parser.add_argument("--source", nargs="+", required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", help="Claude model ID. Defaults to ANTHROPIC_MODEL.")
    parser.add_argument("--max-attempts", type=int, default=2)
    args = parser.parse_args()

    if args.max_attempts < 1:
        parser.error("--max-attempts must be at least 1.")
    if args.inventory.resolve() == args.output.resolve():
        parser.error("--output must be different from --inventory.")

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

        print("Initial evaluation")
        print(json.dumps(evaluate_ids(inventory, chunks), indent=2))

        repaired, report = repair_missing_ids(
            inventory=inventory,
            chunks=chunks,
            model=args.model or os.getenv("ANTHROPIC_MODEL"),
            max_attempts=args.max_attempts,
        )
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Could not run BA repair: {exc}\n")

    print("\nFinal evaluation")
    print(json.dumps(report, indent=2))

    if not report["passed"]:
        print("Evaluation failed. Review the remaining findings.")
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        repaired.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Saved evaluated inventory to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())