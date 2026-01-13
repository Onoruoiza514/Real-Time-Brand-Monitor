import sys
import re
from textblob import TextBlob

from src.loggers import logger
from src.exceptions import CustomException


class SentimentAnalyzer:
    def __init__(self):
        logger.info("Sentiment Analyzer initialized.")

    def clean_text(self, text):
        if not text or not isinstance(text, str):
            return ""

        # Remove HTML comments
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Decode HTML entities
        text = re.sub(r'&nbsp;|&#32;', ' ', text)

        # Normalize whitespace
        text = " ".join(text.split())

        return text

    def get_sentiment(self, text):
        """
        Performs sentiment analysis using TextBlob.
        Polarity range: -1 (negative) to +1 (positive).
        """
        try:
            cleaned_text = self.clean_text(text)

            if not cleaned_text:
                return {
                    "label": "Neutral",
                    "score": 0.0,
                    "subjectivity": 0.0
                }

            blob = TextBlob(cleaned_text)
            polarity = blob.sentiment.polarity

            if polarity > 0.1:
                label = "Positive"
            elif polarity < -0.1:
                label = "Negative"
            else:
                label = "Neutral"

            return {
                "label": label,
                "score": round(polarity, 2),
                "subjectivity": round(blob.sentiment.subjectivity, 2)
            }

        except Exception as e:
            logger.error(f"Error analyzing text: {str(e)}")
            raise CustomException(e, sys)
