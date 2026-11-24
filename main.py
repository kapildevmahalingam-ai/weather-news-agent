"""Entry point: ask for a city and print today's weather news summary."""

from dotenv import load_dotenv

from weather_news.agent import run_weather_news


def main() -> None:
    load_dotenv()  # reads OPENAI_API_KEY from the .env file in this folder

    city = input("Which city? ").strip()
    if not city:
        raise SystemExit("No city entered.")

    run_weather_news(city)


if __name__ == "__main__":
    main()
