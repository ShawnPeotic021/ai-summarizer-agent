# ai-summarizer-agent

> Turn messy support conversations into clean, structured JSON summaries — powered by LLMs, FastAPI, and LangGraph.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen?logo=fastapi)
![LLM](https://img.shields.io/badge/LLM-OpenAI%2FClaude-orange?logo=openai)

---

## 🚀 Features

* 🗣️ Summarizes chat or voice transcripts
* 🧩 Extracts: `customer_name`, `product`, `reason`, `notes`, `summary`
* 🧠 Understands **final decisions** (cancel / retain / upgrade)
* ✅ Outputs **valid JSON only** (checked by Validator Node)
* ⚙️ Easy to extend with RAG, CRM webhooks, or databases

---

## 🧱 Architecture

```
User → FastAPI endpoint (/summarize)
        ↓
Summarizer Node (LLM)
        ↓
Validator Node (JSON check)
        ↓
Structured result → DB / CRM (optional)
```

---

## 🧠 Example

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

## ⚙️ Setup

```bash
git clone https://github.com/ShawnPoetic021/ai-summarizer-agent.git
cd ai-summarizer-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🧩 Core Prompt

```text
You are an AI summarization assistant for customer support.
Extract structured details and summarize clearly.
Output ONLY valid JSON with keys:
"customer_name", "product", "reason", "notes", "summary".
Reflect the final customer decision accurately.
```

---

## Roadmap

* [x] Summarization API
* [x] JSON validation
* [ ] PostgreSQL / CRM integration
* [ ] RAG knowledge augmentation
* [ ] Cloud deployment (Render / AWS / Railway)

---

**MIT License © 2025 [Shawn Wang](https://github.com/ShawnPoetic021)**

---

Would you like me to add a short “Demo Screenshot” section with your current console output (the green ✅ Final structured result)?


