import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Basic validation
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
