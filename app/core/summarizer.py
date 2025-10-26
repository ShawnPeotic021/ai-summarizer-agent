import requests, json
from app.core.llm_client_local import MODEL


def summarize_text(system_prompt: str, transcript: str):
    """Send text to local Ollama model and return summarized response."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript}
        ],
        "options": {"temperature": 0}
    }

    response = requests.post("http://localhost:11434/api/chat", json=payload)

    full_response = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            #print(data)
            if "message" in data and "content" in data["message"]:
                full_response += data["message"]["content"]

    #print(f"full_reponse: {full_response} + {type(full_response)}")
    return full_response.strip()
