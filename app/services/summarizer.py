# app/services/summarizer.py
from .llm_client import summarizer_graph
import json

def summarize_conversation(transcript: str):
    state = {"transcript": transcript}
    result = summarizer_graph.invoke(state)

    final_response = result["summary"]
    return final_response

