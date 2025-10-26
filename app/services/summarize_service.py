#summarize_service.py

from colorama import Fore,Style
from rich import print_json

from app.core.graph_builder import build_graph,Context
import time

from app.schemas.summary_schema import SummarySchema
from app.services.storage_service import save_summary_to_crm

transcript1 = '''
    Agent: Hi Emma, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 100GB more for $5 extra per month.
    Customer: Sorry, just cancel it for me.
    Agent: sure
    '''
transcript2 = '''
    Agent: Hi Jane, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Ok, Sounds good.
    '''
transcript3 = '''
    Agent: Hi Thomas, I see you have the Premium Package.
    Customer: yes, but I want to cancel my service.
    Agent: I'm sorry to hear that. May I offer you free access for 3 months?
    Customer: Hold on.
    Agent: Sure.
    '''
transcript4 = '''
    Agent: Hi Thomas, I see you’re currently on the Premium Package.
    Customer: Yes, but I’d like to cancel my service.
    Agent: I’m sorry to hear that. How about I offer you 3 months of free access to see if that helps?
    Agent: Are you still there, Thomas?
    '''

def summarize_from_transcript(transcript: str, user_id: str = "1"):
    # Initialize agent
    start_time_01 = time.time()
    summarizer_agent = build_graph()
    end_time_01 = time.time()

    config = {"configurable": {"thread_id": "1"}}

    elapsed_01 = end_time_01 - start_time_01
    print(Fore.LIGHTMAGENTA_EX + f"Graph building time {elapsed_01: .6f}" + Style.RESET_ALL)
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
    readable_text = f"""
    🧾 Summary for {clean_summary.get('customer_name', 'Unknown')}:
    - Product: {clean_summary.get('product', 'N/A')}
    - Reason: {clean_summary.get('reason', 'N/A')}
    - Notes: {', '.join(clean_summary.get('notes', []))}
    - Summary: {clean_summary.get('summary', '')}
    ⏱️ Execution time: {elapsed}s
    """.strip()

    return {
        "elapsed": elapsed,
        "formatted_text": readable_text,
        "storage_result": clean_summary
    }
