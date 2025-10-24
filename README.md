# ai-summarizer-agent

> Turn messy support conversations into clean, structured JSON summaries — powered by LLMs, FastAPI, and LangGraph.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen?logo=fastapi)
![LLM](https://img.shields.io/badge/LLM-OpenAI%2FClaude-orange?logo=openai)

---

##  Features

* Summarizes chat or voice transcripts
* Extracts: `customer_name`, `product`, `reason`, `notes`, `summary`
* Understands **final decisions** (cancel / retain / upgrade)
* Outputs **valid JSON only** (checked by Validator Node)
* Easy to extend with RAG, CRM webhooks, or databases

---

## Architecture

```
User → FastAPI endpoint (/summarize)
        ↓
Summarizer Node (LLM)
        ↓  ↑  (if invalid, go back to Summarizer)
Validator Node (JSON check) 
        ↓ (pass validation)
Structured result → DB / CRM (optional)
```

---

## Example

**Input:**

```
Agent: Hi Sarah, I see you have the Beginner Package.
Customer: I want to cancel my service.
Agent: I can give you free access for 3 months.
Customer: That sounds good.
```

**Output:**

```json
{
  "customer_name": "Sarah",
  "product": "Beginner Package",
  "reason": "requested cancellation",
  "notes": ["offered 3-month free access", "customer accepted offer"],
  "summary": "Customer accepted retention offer; service not cancelled."
}
```

---

## Setup

```bash
git clone https://github.com/ShawnPoetic021/ai-summarizer-agent.git
cd ai-summarizer-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Core Prompt

```text
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
   - Phrases like “might cancel” or “let me think” do NOT mean cancellation.
6) Be concise and accurate.
7) Use natural, human phrasing in "summary"
   (e.g., “accepted retention offer and kept the service” instead of “declined cancellation offer”).

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
      "reason": "wanted more storage but accepted upgrade",
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
      "reason": "considering cancellation",
      "notes": ["offered 3 months free access", "customer undecided; service not yet cancelled"],
      "summary": "Customer is considering the offer and has not made a final decision about cancelling the service."
    }
```
---

**MIT License © 2025 [Shawn Wang](https://github.com/ShawnPoetic021)**

---

Would you like me to add a short “Demo Screenshot” section with your current console output (the green ✅ Final structured result)?


