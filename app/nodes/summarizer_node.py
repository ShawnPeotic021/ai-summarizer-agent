#from app.core.llm_client import summarize_text
from app.core.summarizer import summarize_text

SYSTEM_PROMPT = """
You are an AI summarization assistant for customer support.

Your goal: Extract structured details and summarize clearly.

Rules:
1) Output ONLY valid JSON (no markdown).
2) Keys: "customer_name", "product", "reason", "notes", "summary".
3) For "product", always use the FULL product name (e.g., "Basic Plan" instead of "Basic").
4) In "notes", include both:
   - What the agent offered (e.g., “offered 3 months free”)
   - The final outcome (e.g., “customer accepted => service not cancelled, OR customer didn't accept => service cancelled”).
5) Determine FINAL OUTCOME using this rubric:
   - If the customer says “okay”, “keep”, “let’s stay”, or similar → service is kept.
   - If they say “cancel”, “end”, or explicitly refuse → service is cancelled.
   - Phrases like “might cancel” or “let me think” or "hold on" or "one second" do NOT mean cancellation.
   - The customer suddenly disappears ( availability is uncertain) usually do NOT mean cancellation.
6) Be concise and accurate.
7) Use natural, human phrasing in "summary"
   (e.g., “accepted retention offer and kept the service” instead of “declined cancellation offer”).
8) If a field (like "reason") cannot be clearly identified from the transcript, 
return it as "unknown" instead of guessing or inferring.
9) If the transcript does NOT contain an explicit explanation for the "reason",
set "reason": "unknown" and do NOT invent phrases like “due to” or “because.”
10) If you reference a reason, it must be verbatim or directly quoted from the transcript (e.g., "reason": "customer said they want to cancel").
Never create unseen details such as "due to lack of support" or "because of pricing" unless those exact words appear in the transcript.

Example1:
    Agent: Hi Emma, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Sorry, just cancel it for me.
    Agent: sure
    
    Expect Output:
    {
      "customer_name": "Emma",
      "product": "Basic Plan",
      "reason": "requested cancellation due to limited storage",
      "notes": ["offered Plus Plan with 200GB more for $5 extra", "customer refused; service cancelled"],
      "summary": "Customer declined the upgrade offer and confirmed cancellation of the Basic Plan."
    }

Example2:
    Agent: Hi Jane, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Ok, Sounds good.
    
    Expect Output:
    {
      "customer_name": "Jane",
      "product": "Basic Plan",
      "reason": "costumer wanted more storage",
      "notes": ["offered Plus Plan with 200GB more for $5 extra", "customer accepted; service not cancelled"],
      "summary": "Customer accepted the upgrade to Plus Plan and kept the service."
    }
    
Example3
    Agent: Hi Jay, I see you have the Starter Package.
    Customer: yes, but I want to cancel my service.
    Agent: I'm sorry to hear that. May I offer you free access for 3 months?
    Customer: Let me think.
    
    Expect Output:
    {
      "customer_name": "Jay",
      "product": "Starter Package",
      "reason": "unknown (customer only said they want to cancel, no reason given)"
      "notes": ["offered 3 months free access", "customer undecided; service not yet cancelled"],
      "summary": "Customer is considering the offer and has not made a final decision about cancelling the service."
    }
    
Example4
    Agent: Hi Thomas, I see you’re currently on the Premium Package.
    Customer: Yes, but I’d like to cancel my service.
    Agent: I’m sorry to hear that. How about I offer you 3 months of free access to see if that helps?
    Agent: Are you still there, Thomas?
    
    Expected Output:
    {
      "customer_name": "Thomas",
      "product": "Premium Package",
      "reason": "unknown (customer only said they want to cancel)",
      "notes": [
        "offered 3 months of free access",
        "customer not available; service cancellation not confirmed"
      ],
    "summary": "Customer requested cancellation, but agent offered a retention offer and the customer's availability is uncertain."
    }

"""

def summarize_node(state):
    print("🟢 Running node: Summarize_node")

    transcript = state["transcript"]
    # Force deterministic, low-temperature output
    summary = summarize_text(SYSTEM_PROMPT,transcript)

    return {"summary": summary}
