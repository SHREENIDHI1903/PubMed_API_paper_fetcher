from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print(f"✅ GROQ_API_KEY loaded: {api_key[:10]}...")  # Only show partial token
else:
    print("❌ GROQ_API_KEY not found. Is your .env file in the root folder?")
