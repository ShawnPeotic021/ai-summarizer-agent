import os
from colorama import Fore,Style
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser

from app.core.summary_schema import SummarySchema

env = load_dotenv()  # loads .env automatically into memory

MODEL = "meta-llama/Llama-3.2-3B-Instruct"
print(Fore.LIGHTMAGENTA_EX + "Current Model: " ,  MODEL + Style.RESET_ALL)


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
        response_format={"type": "json_object"},  # ✅ strict JSON mode
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript},
        ]
    )
    return completion.choices[0].message.content









