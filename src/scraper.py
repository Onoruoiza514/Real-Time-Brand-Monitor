import feedparser
import sys
import urllib.parse
import time
from datetime import datetime

from src.loggers import logger
from src.exceptions import CustomException


class RedditRSSScraper:
    def __init__(self):
        self.base_url = "https://www.reddit.com/search.rss?q="
        self.headers = {
            "User-Agent": "AppreLab-AI-Research/1.0 (contact: ai@apprelab.com)"
        }
        logger.info("Reddit RSS Scraper initialized.")

    def is_real_post(self, entry):
        """
        A real Reddit post always contains '/comments/' in the URL.
        This filters out subreddit landing pages and community descriptions.
        """
        link = entry.get("link", "")
        return "/comments/" in link

    def fetch_data(self, keyword, limit=10):
        """
        Fetch recent Reddit posts via RSS search.

        :param keyword: Search keyword (e.g. 'Tesla stock')
        :param limit: Number of posts to return
        :return: List of structured post dictionaries
        """
        try:
            encoded_query = urllib.parse.quote(keyword)
            rss_url = f"{self.base_url}{encoded_query}&sort=new"

            logger.info(f"Fetching Reddit RSS data from: {rss_url}")

            feed = feedparser.parse(
                rss_url,
                request_headers=self.headers
            )

            if feed.bozo:
                logger.warning("RSS feed parsing encountered issues.")

            posts = []

            for entry in feed.entries:
                # Filter out non-post entities
                if not self.is_real_post(entry):
                    continue

                post = {
                    "title": entry.get("title"),
                    "link": entry.get("link"),
                    "author": entry.get("author", "unknown"),
                    "published": self._parse_date(entry),
                    "summary": self._clean_text(entry.get("summary", "")),
                    "source": "reddit"
                }

                posts.append(post)

                #  Apply limit AFTER filtering
                if len(posts) >= limit:
                    break

            logger.info(f"Fetched {len(posts)} Reddit posts for keyword: {keyword}")
            return posts

        except Exception as e:
            logger.error(f"Reddit RSS scraping failed: {str(e)}")
            raise CustomException(e, sys)

    @staticmethod
    def _parse_date(entry):
        """Safely parse published date."""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime.fromtimestamp(
                time.mktime(entry.published_parsed)
            ).isoformat()
        return None

    @staticmethod
    def _clean_text(text):
        """Basic text cleanup for RSS summaries."""
        if not text:
            return ""

        return (
            text.replace("\n", " ")
            .replace("&amp;", "&")
            .replace("&#32;", " ")
            .strip()
        )

if __name__ == "__main__":
    scraper = RedditRSSScraper()
    entries = scraper.fetch_data("tesla cars", limit=5)

    for i, entry in enumerate(entries, start=1):
        print(f"{i}. {entry['title']}")
        print(entry["link"])
        print(entry["author"])
        print(entry["published"])
        print(entry["summary"])
        print(entry["source"])
        print()
