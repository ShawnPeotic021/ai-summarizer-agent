#app.core.graph_builder.py
import json
from dataclasses import dataclass


from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import END
from langgraph.graph import StateGraph


from app.nodes.summarizer_node import summarize_node
from app.nodes.validator_node import validator_node

from typing import TypedDict


# --- Define workflow state schemas ---
class GraphState(TypedDict):
    transcript: str
    summary: str | None
    validated_summary: dict | None
    valid: bool | None

# Define context schemas
@dataclass
class Context:
    """Custom runtime context schemas."""
    user_id: str

def should_retry(state: dict) -> str:
    return "validator->end" if state.get("valid") else "validator->summarizer"

def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("summarizer", summarize_node)
    graph.add_node("validator", validator_node)

    graph.set_entry_point("summarizer")
    graph.add_edge("summarizer", "validator")
    graph.add_conditional_edges(
        "validator", should_retry,
        {"validator->end": END, "validator->summarizer": "summarizer"}
    )

    print("📘 Graph structure:")
    print(json.dumps({
        "nodes": list(graph.nodes),
        "edges": [list(e) for e in graph.edges],
    }, indent=2))
    print("\n")

    checkpointer = InMemorySaver()
    return graph.compile(checkpointer=checkpointer)
