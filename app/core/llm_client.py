import os
from colorama import Fore,Style
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

MODEL = "meta-llama/Llama-3.2-3B-Instruct"
print(Fore.LIGHTMAGENTA_EX + "Current Model: " ,  MODEL + Style.RESET_ALL)

env = load_dotenv()  # loads .env automatically into memory

# Initialize Hugging Face inference client
client = InferenceClient(
    provider="novita",
    api_key=os.environ["HF_TOKEN"],
)

def summarize_text(system_prompt: str, transcript: str):
    """Send text to LLM and return summarized response."""
    completion = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript},
        ]
    )
    return completion.choices[0].message.content



