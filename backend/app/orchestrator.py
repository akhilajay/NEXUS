"""Run the NEXUS BA and SA stages and publish a human-review handoff."""

import argparse
from collections import Counter
import json
import logging
import os
from pathlib import Path
import subprocess
import sys
from time import perf_counter


LOG = logging.getLogger(__name__)


def read_object(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def artifact(handoff: dict, name: str, handoff_path: Path) -> Path:
    path = (handoff_path.parent / handoff["artifacts"][name]).resolve()
    if not path.is_file():
        raise ValueError(f"Missing {name} artifact: {path}")
    return path


def run_agent(module: str, args: list[str]) -> int:
    started = perf_counter()
    LOG.info("Starting %s. Agent output follows.", module)
    with subprocess.Popen(
        [sys.executable, "-u", "-m", module, *args],
        cwd=Path(__file__).resolve().parents[1],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    ) as process:
        for line in process.stdout:
            LOG.info("[%s] %s", module, line.rstrip("\r\n"))
        exit_code = process.wait()
    LOG.info("%s exited with code %d after %.1fs.", module, exit_code, perf_counter() - started)
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--source", nargs="+", help="Source document names stored in Neo4j.")
    inputs.add_argument("--ba-handoff", type=Path, help="Reuse a completed BA run.")
    parser.add_argument("--sa-handoff", type=Path, help="Reuse an SA run with --ba-handoff.")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--model")
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--rework-rounds", type=int, choices=(0, 1), default=1)
    args = parser.parse_args()
    if args.sa_handoff and not args.ba_handoff:
        parser.error("--sa-handoff requires --ba-handoff.")
    if min(args.batch_size, args.max_tokens) < 1:
        parser.error("--batch-size and --max-tokens must be positive.")

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [orchestrator] %(message)s", datefmt="%H:%M:%S")
    started = perf_counter()
    output = args.output_dir.resolve()
    try:
        output.mkdir(parents=True)
    except OSError as exc:
        parser.exit(2, f"Cannot create run directory {output}: {exc}\n")
    trace = output / "workflow_trace.log"
    file_handler = logging.FileHandler(trace, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] [orchestrator] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    ))
    LOG.addHandler(file_handler)
    LOG.info("Run trace: %s", trace)
    manifest = output / "workflow_handoff.json"
    state = {"status": "running", "stage": "ba", "trace_log": str(trace)}
    model_args = ["--model", args.model] if args.model else []

    def save_state() -> None:
        temporary = manifest.with_suffix(".tmp")
        temporary.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        temporary.replace(manifest)

    LOG.info("[1/5 Setup] Created run directory %s.", output)
    save_state()
    try:
        ba_exit = 0
        if args.ba_handoff:
            ba_path = args.ba_handoff.resolve()
            LOG.info("[2/5 BA] Reusing %s.", ba_path)
        else:
            ba_root = output / "ba"
            LOG.info("[2/5 BA] Running requirements workflow for %s.", ", ".join(args.source))
            ba_exit = run_agent("app.agents.ba_workflow", [
                "--source", *args.source, "--output-dir", str(ba_root), *model_args,
            ])
            handoffs = list(ba_root.glob("ba-*/ba_handoff.json"))
            if len(handoffs) != 1:
                raise ValueError(f"Expected one BA handoff, found {len(handoffs)} (exit {ba_exit}).")
            ba_path = handoffs[0]
        ba = read_object(ba_path)
        state["ba_handoff"] = str(ba_path)
        LOG.info("[2/5 BA] Handoff status: %s.", ba["status"])
        if ba["status"] == "needs_human_review" and ba_exit in (0, 1):
            state["status"] = "blocked_for_ba_review"
            LOG.warning("[2/5 BA] Human review required. SA skipped.")
            return 1
        if ba_exit or ba["status"] != "ready_for_handoff":
            raise ValueError(f"BA stopped with status {ba['status']} (exit {ba_exit}).")
        state["functional_document"] = str(artifact(ba, "functional_document", ba_path))

        state["stage"] = "sa"
        save_state()
        if args.sa_handoff:
            sa_path = args.sa_handoff.resolve()
            LOG.info("[3/5 SA] Reusing %s.", sa_path)
        else:
            sa_output = output / "sa"
            LOG.info("[3/5 SA] Generating architecture from %s.", ba_path)
            LOG.info("[3/5 SA] Batch size=%d, max tokens=%d, rework rounds=%d.",
                     args.batch_size, args.max_tokens, args.rework_rounds)
            sa_exit = run_agent("app.agents.sa_agent", [
                "--ba-handoff", str(ba_path), "--output-dir", str(sa_output),
                "--batch-size", str(args.batch_size), "--max-tokens", str(args.max_tokens),
                "--rework-rounds", str(args.rework_rounds), *model_args,
            ])
            if sa_exit:
                raise ValueError(f"SA exited with code {sa_exit}.")
            sa_path = sa_output / "sa_handoff.json"

        state["sa_handoff"] = str(sa_path)
        LOG.info("[4/5 Validation] Checking %s against the BA run.", sa_path)
        sa = read_object(sa_path)
        if sa["status"] != "ready_for_review" or sa["scope"] != "full_draft":
            raise ValueError("SA must publish a full draft ready for review.")
        if (sa_path.parent / sa["ba_handoff"]).resolve() != ba_path or sa["sources"] != ba["sources"]:
            raise ValueError("The SA handoff belongs to a different BA run.")
        artifacts = {
            key: str(artifact(sa, key, sa_path))
            for key in ("architecture_json", "architecture_document", "architecture_drawio", "architecture_mermaid")
        }
        mappings = read_object(Path(artifacts["architecture_json"]))["requirement_mappings"]
        counts = Counter(row["status"] for row in mappings)
        statuses = ("addressed", "gap", "requires_decision")
        if counts.keys() - set(statuses) or len({row["record_id"] for row in mappings}) != len(mappings):
            raise ValueError("SA coverage contains invalid statuses or duplicate requirement records.")
        coverage = {status: counts[status] for status in statuses}
        if coverage != sa["coverage_counts"]:
            raise ValueError("SA coverage counts disagree with the architecture mappings.")
        LOG.info("[4/5 Validation] Verified %d artifacts and %d requirement mappings.",
                 len(artifacts), len(mappings))
        state.update(
            stage="review", status="ready_for_review",
            architecture_artifacts=artifacts, coverage_counts=coverage,
            open_requirement_ids=[
                row["record_id"] for row in mappings if row["status"] != "addressed"
            ],
        )
        LOG.info("[5/5 Review] Ready for human review. Addressed=%d, gaps=%d, decisions required=%d.",
                 coverage["addressed"], coverage["gap"], coverage["requires_decision"])
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        state.update(status="failed", error=str(exc))
        LOG.error("Workflow failed during %s: %s", state["stage"], exc)
        return 2
    finally:
        save_state()
        LOG.info("Run ended with status %s after %.1fs.", state["status"], perf_counter() - started)
        LOG.info("Workflow handoff: %s", manifest)
        LOG.removeHandler(file_handler)
        file_handler.close()


if __name__ == "__main__":
    raise SystemExit(main())
