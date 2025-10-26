#from app.core.llm_client import summarize_text
from app.core.summarizer import summarize_text

from app.core.prompts import SUMMARIZER_SYSTEM_PROMPT

def summarize_node(state):
    print("🟢 Running node: Summarize_node")

    transcript = state["transcript"]
    # Force deterministic, low-temperature output
    summary = summarize_text(SUMMARIZER_SYSTEM_PROMPT,transcript)

    return {"summary": summary}
