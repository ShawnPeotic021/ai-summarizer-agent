import requests, json
from colorama import Fore,Style

MODEL = "llama3.2:1b"   # or any local model you pulled

print(Fore.LIGHTMAGENTA_EX + "Current Model: " ,  MODEL + Style.RESET_ALL)

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
        print(line)
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data and "content" in data["message"]:
                full_response += data["message"]["content"]

    return full_response.strip()









