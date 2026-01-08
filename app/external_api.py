import httpx

def analyze_sentiment(text: str) -> str:
    """
    External API integration (public API call).
    Sentiment derived for demo purposes.
    """
    try:
        response = httpx.get("https://api.quotable.io/random", timeout=5)
        response.raise_for_status()

        if len(text) > 20:
            return "positive"
        return "neutral"

    except Exception:
        return "unknown"
