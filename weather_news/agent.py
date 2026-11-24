"""Builds the Weather News agent and runs it for a city."""

import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from weather_news.tools import search_weather_news

MODEL_NAME = "gpt-4o-mini"

SYSTEM_MESSAGE = (
    "You are a weather news reporter. When the user gives a city, call the "
    "search_weather_news tool for that city, then reply with exactly 3 lines. "
    "Each line must be one short sentence, and each sentence must go on its own "
    "line separated by a newline character. Do not put two sentences on the same "
    "line. No headings, no bullet points, no numbering, no extra text before or after."
)


def get_api_key() -> str:
    """Return OPENAI_API_KEY from the environment, or exit with a clear message."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            "OPENAI_API_KEY is not set. Add it to a .env file in the project folder "
            "(see .env.example) or set it as an environment variable."
        )
    return api_key


def run_weather_news(city: str) -> None:
    """Ask the agent for today's weather news for `city` and print the reply."""
    model_client = OpenAIChatCompletionClient(model=MODEL_NAME, api_key=get_api_key())

    agent = AssistantAgent(
        name="weather_news",
        model_client=model_client,
        tools=[search_weather_news],
        system_message=SYSTEM_MESSAGE,
        reflect_on_tool_use=True,
    )

    async def run() -> None:
        try:
            await Console(agent.run_stream(task=f"What is today's weather news for {city}?"))
        finally:
            await model_client.close()

    asyncio.run(run())
