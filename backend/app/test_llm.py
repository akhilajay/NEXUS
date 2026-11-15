from app.llm_client import LLMClient

# test_llm.py to verify the claude api integration with the LLMClient class. This script is intended for local testing and should not be used in production.
chunks = [
    {
        "chunk_id": "XATA_TODO_BRD-007",
        "source": "XATA_TODO_BRD.docx",
        "heading": "5. Users and Roles",
        "text": (
            "Employee: Create/manage own TODOs, view assigned TODOs, "
            "and update status.\n"
            "Team Lead: Create/assign TODOs, view team TODOs, "
            "and monitor overdue work.\n"
            "Administrator: Manage users and basic platform configuration."
        ),
    }
]

result = LLMClient().answer("What roles does the app require?", chunks)

print(result["answer"])
print(f"Input tokens: {result['input_tokens']}")
print(f"Output tokens: {result['output_tokens']}")
print(f"Stop reason: {result['stop_reason']}")