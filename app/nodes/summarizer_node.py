from textwrap import dedent
from langchain_core.prompts import ChatPromptTemplate
from app.core.llm_client import summarize_text

SYSTEM_PROMPT ="""
    You are an AI summarization assistant for customer support.

    Your goal: Extract structured details and summarize clearly.
    
    Rules:
    1) Output ONLY valid JSON (no markdown).
    2) Keys: "customer_name", "product", "reason", "notes", "summary".
    3) Determine FINAL OUTCOME using this rubric:
        - If the customer says “okay”, “keep”, “let’s stay”, or similar → service is kept.
        - If they say “cancel”, “end”, or explicitly refuse → service is cancelled.
        - Phrases like “might cancel” or “thinking to cancel” do NOT mean cancellation.
    4) Be concise and accurate.
    5) Use natural, human phrasing in "summary" 
    (e.g., “accepted retention offer and kept the service” instead of “declined cancellation offer”).
    
    Example:
    Transcript:
    Agent: You’re on the Starter plan.
    Customer: I want to cancel.
    Agent: I can give 3 months free.
    Customer: That works.
    
    Correct JSON:
    {"customer_name":"Sarah","product":"Starter","reason":"requested cancellation","notes":["accepted 3 months free"],"summary":"Customer accepted retention offer; service not cancelled."}

    """

def summarize_node(state):
    print("🟢 Running node: summarize_node")

    transcript = state["transcript"]
    # Force deterministic, low-temperature output
    summary = summarize_text(SYSTEM_PROMPT,transcript)

    return {"summary": summary}
