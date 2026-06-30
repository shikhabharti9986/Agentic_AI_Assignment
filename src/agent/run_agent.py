from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def run_agent(question: str) -> str:
    """
    Run Gemini-powered store support agent.
    """

    system_prompt = """
    You are an online store support assistant.

    Help customers with:
    - order tracking
    - product recommendations
    - cheaper alternatives
    - product details

    Keep answers short and helpful.
    """

    prompt = f"""
    {system_prompt}

    Customer Question:
    {question}
    """

    try:
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            input=prompt,
        )

        return interaction.output_text

    except Exception as e:

        if "429" in str(e):
            return (
                "Free Gemini quota exceeded. "
                "Please wait and try again."
            )

        return f"Error: {str(e)}"
