"""Run the BA checks and render a functional solution document."""

import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def run_stage(module: str, *args: str) -> int:
    return subprocess.run([sys.executable, "-m", module, *args], check=False).returncode


def render_document(inventory: dict, clarifications: dict, sources: list[str]) -> str:
    lines = [
        "# Functional solution",
        "",
        "**Review draft**",
        "",
        "## Source documents",
        "",
        *[f"- {source}" for source in sources],
    ]

    for kind, heading in (
        ("functional", "Functional requirements and business rules"),
        ("non_functional", "Non-functional requirements"),
    ):
        lines.extend(["", f"## {heading}", ""])
        for requirement in inventory["requirements"]:
            if requirement["kind"] != kind:
                continue
            req_id = requirement["requirement_id"]
            prefix = f"**{req_id}** — " if req_id else ""
            references = ", ".join(
                f"`{source['chunk_id']}`" for source in requirement["sources"]
            )
            lines.append(f"- {prefix}{requirement['statement']} ({references})")

    lines.extend(["", "## Clarifications and decisions", ""])
    if not clarifications["results"]:
        lines.append("No clarification questions were raised.")

    for result in sorted(clarifications["results"], key=lambda item: item["question_id"]):
        lines.extend([
            f"### Question {result['question_id']}",
            "",
            result["question"],
            "",
        ])
        if result.get("answer"):
            lines.extend([result["answer"], ""])
        for evidence in result["evidence"]:
            lines.append(f"- `{evidence['chunk_id']}` — {evidence['quote']}")
        if result.get("remaining_question"):
            lines.extend(["", f"**Decision pending** — {result['remaining_question']}"])
        if result.get("proposed_assumption"):
            lines.extend([
                "",
                f"**Provisional assumption** — {result['proposed_assumption']}",
                f"**Rationale** — {result['assumption_rationale']}",
            ])
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def validate_clarification_coverage(inventory: dict, report: dict) -> None:
    expected = {
        number: question["question"]
        for number, question in enumerate(inventory["open_questions"], start=1)
    }
    results = report["results"]
    observed = Counter((item["question_id"], item["question"]) for item in results)
    if observed != Counter(expected.items()):
        raise ValueError("Clarification results do not match the inventory questions.")
    valid_statuses = {"answered", "partially_answered", "needs_human_review"}
    if report["processing_error_count"] or any(
        item["status"] not in valid_statuses for item in results
    ):
        raise ValueError("One or more clarification questions failed to process.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, help="Reuse an existing BA inventory.")
    parser.add_argument("--model", help="Defaults to ANTHROPIC_MODEL.")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix="ba-", dir=args.output_dir)).resolve()
    inventory_path = run_dir / "requirements_inventory.json"
    eval_path = run_dir / "requirements_inventory.eval.json"
    clarification_path = run_dir / "ba_clarifications.json"
    document_path = run_dir / "functional_solution.md"
    handoff_path = run_dir / "ba_handoff.json"

    handoff = {"status": "processing_error", "sources": args.source, "artifacts": {}}
    model_args = ["--model", args.model] if args.model else []
    inventory_args = ["--inventory", str(args.inventory)] if args.inventory else []

    try:
        handoff["stage"] = "inventory_evaluation"
        code = run_stage(
            "app.agents.ba_agent", "--source", *args.source,
            "--output", str(inventory_path), *inventory_args, *model_args,
        )
        if eval_path.is_file():
            handoff["artifacts"]["evaluation"] = str(eval_path)
        if code == 1 and eval_path.is_file():
            evaluation = read_json(eval_path)
            if evaluation["status"] == "needs_human_review":
                handoff["status"] = "needs_human_review"
                handoff["artifacts"]["draft_inventory"] = evaluation["inventory_path"]
                return 1
        if code != 0 or read_json(eval_path)["status"] != "passed":
            raise ValueError(f"BA inventory stage did not pass (exit {code}).")
        handoff["artifacts"]["inventory"] = str(inventory_path)
        inventory = read_json(inventory_path)

        handoff["stage"] = "clarification"
        code = run_stage(
            "app.agents.ba_clarify", "--source", *args.source,
            "--inventory", str(inventory_path), "--output", str(clarification_path),
            *model_args,
        )
        if clarification_path.is_file():
            handoff["artifacts"]["clarifications"] = str(clarification_path)
        if code != 0:
            raise ValueError(f"Clarification did not finish successfully (exit {code}).")
        clarifications = read_json(clarification_path)
        validate_clarification_coverage(inventory, clarifications)

        handoff["stage"] = "functional_document"
        document_path.write_text(
            render_document(inventory, clarifications, args.source), encoding="utf-8"
        )
        handoff["artifacts"]["functional_document"] = str(document_path)
        handoff["open_decision_count"] = sum(
            item["status"] != "answered" for item in clarifications["results"]
        )
        handoff["status"] = "ready_for_handoff"
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        handoff["error"] = str(exc)
        print(f"BA workflow failed: {exc}", file=sys.stderr)
        return 2
    finally:
        write_json(handoff_path, handoff)
        print(f"BA status: {handoff['status']}")
        print(f"BA handoff: {handoff_path}")


if __name__ == "__main__":
    raise SystemExit(main())
