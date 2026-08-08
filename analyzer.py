from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def analyze_ingredients(ingredients_text, skin_type):

    prompt = f"""
You are a skincare ingredient analyzer.

Skin Type: {skin_type}

Ingredients:
{ingredients_text}

Return ONLY valid JSON in exactly this format:

{{
    "safety_score": 0,
    "good": [],
    "moderate": [],
    "harmful": [],
    "good_count": 0,
    "moderate_count": 0,
    "harmful_count": 0,
    "suitability": "",
    "recommended_usage": ""
}}

Keep the response SHORT.
Do not explain anything outside the JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a skincare ingredient analyzer. Return only JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_completion_tokens=1000
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)