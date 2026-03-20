import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables (.env)
load_dotenv()

# API key for Groq LLM service
API_KEY = os.getenv("GROQ_API_KEY")

# Groq client initialization (LLM provider)
client = Groq(api_key=API_KEY)


def analyze_market(sector: str, data: str) -> dict:

    try:

        # Prompt designed to force strict JSON output
        # Important for reliable parsing in backend
        prompt = f"""
        You are a professional stock market research analyst.

        Your job is to analyze latest Indian stock market news.

        IMPORTANT RULES:

        - Do NOT use general knowledge
        - Do NOT assume anything
        - If data is not related, say no data
        - Focus ONLY on sector: {sector}
        - Only Indian market, if gold, silver or metals related queries you can go for international market
        - Ignore unrelated news

        DATA:
        {data}


        Return ONLY JSON in this format:

        {{
        "current_trend": "...",
        "recent_events": ["...", "..."],
        "market_performance": "...",
        "investment_outlook": "...",
        "risks": ["...", "..."],
        "opportunities": ["...", "..."]
        }}

        Rules:

        - recent_events must be list
        - risks must be list
        - opportunities must be list
        - strings only
        - valid JSON only
        """

        # Debug log to verify what data is sent to AI
        print("DATA SENT TO AI:", data[:200])

        # LLM call
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        result = chat.choices[0].message.content.strip()

        # Convert AI JSON string → Python dict
        parsed = json.loads(result)

        return parsed

    except Exception as e:

        # Fallback response to avoid API crash if AI fails / invalid JSON
        return {
            "current_trend": "No clear trend",
            "recent_events": [],
            "market_performance": "Unknown",
            "investment_outlook": "Not available",
            "risks": [
                "Insufficient data"
            ],
            "opportunities": []
        }