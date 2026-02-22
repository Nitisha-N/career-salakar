import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_PROMPT = """
You are Career Salakar — a sharp, structured, strategic career advisor.

Rules:
- Be concise (max 250 words unless absolutely necessary).
- Do NOT write essays.
- Do NOT give medical disclaimers unless the question is medical.
- Give structured guidance.
- Start with a short direct answer.
- Then give 3–5 bullet points.
- End with 1 thoughtful follow-up question.
- Focus on clarity and self-reflection.

Tone:
Professional. Calm. Insightful. Not robotic.
"""

def generate_response(conversation_history):
    try:
        formatted_history = SYSTEM_PROMPT + "\n\n"

        for role, message in conversation_history:
            if role == "user":
                formatted_history += f"User: {message}\n"
            else:
                formatted_history += f"Assistant: {message}\n"

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=formatted_history
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
