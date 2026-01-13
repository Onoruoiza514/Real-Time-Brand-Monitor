import sys
from src.scraper import RedditRSSScraper
from src.analyzer import SentimentAnalyzer
from src.loggers import logger
from src.exceptions import CustomException


def run_monitor(keyword):
    try:
        # Initialize our tools
        scraper = RedditRSSScraper()
        analyzer = SentimentAnalyzer()

        logger.info(f"--- Starting Reputation Monitor for: {keyword} ---")

        # 1. Scrape data
        posts = scraper.fetch_data(keyword, limit=10)

        if not posts:
            print(f"No recent vibes found for {keyword}.")
            return

        # 2. Analyze and Display
        print(f"\nREPUTATION REPORT FOR: {keyword.upper()}")
        print("=" * 40)

        for i, post in enumerate(posts, 1):
            # We analyze the 'summary' or 'title'
            text_to_analyze = post.get('title', '')
            vibe = analyzer.get_sentiment(text_to_analyze)

            print(f"{i}. POST: {text_to_analyze[:75]}...")
            print(f"   VIBE: {vibe['label']} (Score: {vibe['score']})")
            print(f"   LINK: {post.get('link')}")
            print("-" * 40)

        logger.info("Monitor run completed successfully.")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    run_monitor("Tesla Cars")