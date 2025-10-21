import json
import os

import colorama
from colorama import Fore,Style
from huggingface_hub import InferenceClient

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langgraph.constants import END
from langgraph.graph import StateGraph
from networkx.algorithms.bipartite import color
from rich import print_json
import json


MODEL = "meta-llama/Llama-3.2-3B-Instruct"
print(Fore.LIGHTMAGENTA_EX + "Current Model: " ,  MODEL + Style.RESET_ALL)

env = load_dotenv()  # loads .env automatically into memory

# Initialize Hugging Face inference client
client = InferenceClient(
    provider="novita",
    api_key=os.environ["HF_TOKEN"],
)

# Define tools
# Define summarization helper
def summarize_text(prompt: str):
    completion = client.chat.completions.create(
        model= MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return completion.choices[0].message.content

# Augment the LLM with tools
# define state


# Add Node
# --- Node: summarize transcript ---
def summarize_node(state):
    print("🟢 Running node: summarize_node")

    transcript = state["transcript"]
    prompt = ChatPromptTemplate.from_template("""
        You are an AI summarization assistant for customer support.
        Extract structured details and summarize clearly.
        Return JSON with fields:
        customer_name, product, reason, notes[], summary.

        Transcript:
        {transcript}
        """)
    # Render prompt and send to summarizer
    rendered_prompt = prompt.format(transcript=transcript)
    summary = summarize_text(rendered_prompt)

    result = {"summary": summary}

    return result


# define the workflow logic
# --- Build LangGraph ---
graph = StateGraph(dict)
graph.add_node("summarizer", summarize_node)
graph.set_entry_point("summarizer")
graph.add_edge("summarizer", END)

summarizer_graph = graph.compile()

print("📘 Graph structure:")
print(json.dumps({
    "nodes": list(graph.nodes),
    "edges": [list(e) for e in graph.edges],
}, indent=2))
print("\n")
