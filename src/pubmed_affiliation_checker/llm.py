# src/pubmed_affiliation_checker/llm.py

import os
import requests
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"  # Replace with another if preferred

def is_pharma_affiliation(affiliation: str, debug: bool = False) -> bool:
    """
    Uses Groq's LLM to determine if an affiliation string corresponds to a
    pharmaceutical, biotech, or commercial healthcare company.

    Args:
        affiliation (str): The full affiliation string to evaluate.
        debug (bool): If True, prints the LLM's raw response.

    Returns:
        bool: True if it's a company affiliation, False otherwise.
    """
    api_key: Optional[str] = os.getenv("GROQ_API_KEY")
    if not api_key:
        if debug:
            print("❌ GROQ_API_KEY not found. Did you forget to add it to your .env file?")
        return False

    prompt: str = (
        "Is this affiliation from a pharmaceutical, biotech, or commercial healthcare company? "
        "Respond only with 'Yes' or 'No' and a brief reason.\n\n"
        f"Affiliation: {affiliation}"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        reply: str = response.json()["choices"][0]["message"]["content"].strip()
        
        if debug:
            print(f"\n🧠 LLM response:\n{reply}")

        return reply.lower().startswith("yes")
    
    except requests.exceptions.RequestException as e:
        if debug:
            print(f"⚠️ Request to Groq API failed: {e}")
        return False
    except KeyError as e:
        if debug:
            print(f"⚠️ Unexpected response format: {e}")
        return False
