from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from project root

_client = None

def get_groq_client():
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not found in environment")
        _client = Groq(api_key=api_key)
    return _client
