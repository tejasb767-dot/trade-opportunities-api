import os
import requests
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(query: str):

    # NewsAPI endpoint for fetching latest articles
    url = "https://newsapi.org/v2/everything"

    # Request parameters
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,  # limit results to reduce API usage
        "apiKey": NEWS_API_KEY,
    }

    try:

        # External API call
        response = requests.get(url, params=params)

        # Debug logs (useful during development / testing)
        print("QUERY:", query)
        print("STATUS:", response.status_code)
        print("DATA:", response.text[:200])

        data = response.json()

        articles = data.get("articles", [])

        text_data = []

        # Extract title + description to send to AI
        for a in articles:

            title = a.get("title", "")
            desc = a.get("description", "")

            if title:
                text_data.append(title)

            if desc:
                text_data.append(desc)

        # Combine text to single string for AI prompt
        return " ".join(text_data)

    except Exception as e:

        # Fail-safe to avoid breaking main API
        return ""


def get_market_data(sector: str):

    # Normalize input
    sector = sector.lower().strip()

    # Base search queries
    queries = [
        f"{sector}",
        f"{sector} news",
        f"{sector} india",
        f"{sector} stocks",
        f"{sector} market",
        f"{sector} latest news"
    ]

    # Extra keywords improve relevance for specific sectors
    if "pharma" in sector or "pharmaceutical" in sector:
        queries += [
            "pharma stocks india",
            "drug companies india",
            "healthcare sector india",
        ]

    if "bank" in sector:
        queries += [
            "bank stocks india",
            "banking sector india",
            "psu banks india",
        ]

    if "technology" in sector or "it" in sector:
        queries += [
            "it stocks india",
            "technology sector india",
            "software companies india",
        ]

    all_text = []

    # Collect news from multiple queries to improve AI accuracy
    for q in queries:

        text = fetch_news(q)

        if text and len(text) > 20:
            all_text.append(text)

    combined = " ".join(all_text).strip()

    # Ensure enough data before sending to AI
    if not combined or len(combined) < 80:
        return None

    # Limit size to avoid LLM token overflow
    return combined[:4000]