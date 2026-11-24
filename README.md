# Weather News Agent

An AutoGen agent that takes a city name, searches today's weather news with the
free, keyless [DuckDuckGo search](https://pypi.org/project/ddgs/) package, and
replies with a 3-line summary.

The agent uses one tool, `search_weather_news(city)`. AutoGen reads the tool's
name, type hints and docstring to decide when to call it.

## Project structure

```
.
├── main.py                 # Entry point: asks for a city and runs the agent
├── weather_news/
│   ├── __init__.py
│   ├── agent.py            # Builds the AutoGen agent and runs it
│   └── tools.py            # search_weather_news() tool (DuckDuckGo news search)
├── requirements.txt        # Python dependencies
├── .env.example            # Template for the environment file
└── .gitignore
```

## Requirements

- Python 3.10 or newer
- An OpenAI API key (the search itself needs no key)

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS / Linux
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key. Copy `.env.example` to `.env` and fill it in:

   ```
   OPENAI_API_KEY=sk-...
   ```

   `.env` is listed in `.gitignore`, so your key is not committed.

## Usage

```bash
python main.py
```

```
Which city? Chennai
---------- ToolCallRequestEvent (weather_news) ----------
search_weather_news(city='Chennai')
---------- TextMessage (weather_news) ----------
Chennai is expecting moderate rain soon, with significant showers forecasted from November 24 to 26.
The India Meteorological Department warns of heavy rainfall across the city this week.
Residents should prepare for thunderstorms and gusty winds as the northeast monsoon intensifies.
```

## Notes

- Search results depend on DuckDuckGo's news index. Small towns and villages often
  return no results, and the agent will say so.
- The model is `gpt-4o-mini`. Change `MODEL_NAME` in `weather_news/agent.py` to use another model.
- `reflect_on_tool_use=True` makes the agent write a summary from the search results
  instead of printing the raw output.
