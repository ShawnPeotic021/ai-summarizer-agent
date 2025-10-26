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
    Agent: Hi Jane, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Ok, sounds good.
```

**Output:**

```json
    {
      "customer_name": "Jane",
      "product": "Basic Plan",
      "event": "request for more storage",
      "reason": "customer wanted more storage",
      "notes": [
        "offered Plus Plan with 200GB more for $5 extra",
        "customer accepted; service not cancelled"
      ],
      "summary": "Customer accepted the upgrade to Plus Plan and kept the service."
    }
```

**Input:**

```
    Agent: Hi Jay, I see you have the Starter Package.
    Customer: yes, but I want to cancel my service.
    Agent: I'm sorry to hear that. May I offer you free access for 3 months?
    Customer: Let me think.
```

**Output:**

```json
    {
      "customer_name": "Jay",
      "product": "Starter Package",
      "event": "cancel the service",
      "reason": "unknown (customer only said they want to cancel, no reason given)",
      "notes": [
        "offered 3 months free access",
        "customer undecided; service not yet cancelled"
      ],
      "summary": "Customer is considering the offer and has not made a final decision about cancelling the service."
    }
```

**Input:**

```
    Agent: Hi Thomas, I see you’re currently on the Premium Package.
    Customer: Yes, but I’d like to cancel my service.
    Agent: I’m sorry to hear that. How about I offer you 3 months of free access to see if that helps?
    Agent: Are you still there, Thomas?
```

**Output:**

```json
    {
      "customer_name": "Thomas",
      "product": "Premium Package",
      "event": "cancel the service",
      "reason": "unknown (customer only said they want to cancel)",
      "notes": [
        "offered 3 months of free access",
        "customer disappears; service not yet cancelled"
      ],
      "summary": "Customer requested cancellation, then the agent offered a retention deal, but the customer disappears."
    }
```

**Input:**

```
    Agent: Hi Alex, thanks for reaching out. How can I help you today?  
    Customer: I was charged this month, but I cancelled my Premium Package two months ago.  
    Agent: I see. Could you share the date of the charge and the last four digits of your card?  
    Customer: 1234; October 26th, 2025.  
    Agent: Thank you. I’ll issue a full refund for this charge within 3–5 business days.  
    Customer: Great, thank you. Will the same issue happen again?  
    Agent: You’re welcome. No, this issue won’t happen again — your account remains fully cancelled.
```

**Output:**

```json
    {
      "customer_name": "Alex",
      "product": "Premium Package",
      "event": "request_refund",
      "reason": "customer was charged after cancelling two months prior",
      "notes": [
        "confirmed billing error and offered full refund within 3–5 business days",
        "refund issued; account remains cancelled"
      ],
      "summary": "Customer reported being charged after cancelling the Premium Package two months ago. Agent confirmed the billing error, issued a refund, and verified that the account remains cancelled."
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

---

**MIT License © 2025 [Shawn Wang](https://github.com/ShawnPoetic021)**

---

Would you like me to add a short “Demo Screenshot” section with your current console output (the green ✅ Final structured result)?


