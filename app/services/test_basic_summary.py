# tests/test_summarizer_basic.py
from tkinter.ttk import Style

from colorama import Fore

from app.services.summarizer import summarize_conversation
from rich import print_json

def test_basic_summary():
    transcript = """
    Agent: Hi Sarah, I see you have the beginner Package.
    Customer: yes, but I want to cancel my service.
    Agent: I'm sorry to hear that. May I offer you free access for 3 months?
    Customer: That sounds good.
    """
    result = summarize_conversation(transcript)

    print("\n")
    print(Fore.LIGHTCYAN_EX +" -- -- -- Final Output-- -- -- ")
    print(Fore.LIGHTCYAN_EX + result)

if __name__ == "__main__":
    test_basic_summary()
