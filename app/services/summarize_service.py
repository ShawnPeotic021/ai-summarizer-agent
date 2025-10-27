#summarize_service.py
from colorama import Fore,Style
from rich import print_json

from app.core.graph_builder import build_graph,Context
import time

from app.schemas.summary_schema import SummarySchema
from app.services.storage_service import save_summary_to_crm

def summarize_from_transcript(transcript: str, user_id: str = "1"):
    # Initialize agent
    start_time_01 = time.time()
    summarizer_agent = build_graph()
    end_time_01 = time.time()

    config = {"configurable": {"thread_id": "1"}}

    elapsed_01 = end_time_01 - start_time_01

    print("\n")
    #print(Fore.LIGHTMAGENTA_EX + f"Agent Graph has been built" + Style.RESET_ALL)
    # Run agent
    # `thread_id` is a unique identifier for a given conversation.

    start_time = time.time()

    response = summarizer_agent.invoke(
        {"transcript": transcript},
        config=config,
        context=Context(user_id="1")
    )

    clean_summary = response.get("validated_summary", {})["summary"]
    print("\n")
    print("✅ Final structured result:")
    print_json(data=clean_summary,indent=2)

    end_time = time.time()
    elapsed = end_time - start_time
    print("\n")
    print(Fore.LIGHTMAGENTA_EX + f"⏱️ Execution time: {elapsed:.2f} seconds" + Style.RESET_ALL)

    # Convert to Pydantic model
    #summary_obj = SummarySchema(**clean_summary)

    # ✅ Store structured summary (async in future)
    #store_result = save_summary_to_crm(summary_obj)

    # Return readable result for frontend

    return {
        "elapsed": elapsed,
        "storage_result": clean_summary
    }
