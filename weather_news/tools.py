"""Tools the agent can call."""

from ddgs import DDGS
from ddgs.exceptions import DDGSException


def search_weather_news(city: str) -> str:
    """Search the web for today's weather news for a given city.

    Use this tool only when the user asks about the current weather or
    weather news for a specific city today. Do not use it for general
    trivia, history, or forecasts for other days.

    Args:
        city: The name of the city to get today's weather news for.

    Returns:
        A string containing up to 5 recent news results about the city's weather.
    """
    try:
        results = DDGS().news(query=f"{city} weather today", max_results=5)
    except DDGSException:
        return f"No recent weather news found for {city}."
    return str(results)
