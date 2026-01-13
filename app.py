import streamlit as st
import pandas as pd
from src.scraper import RedditRSSScraper
from src.analyzer import SentimentAnalyzer

# Page Config
st.set_page_config(page_title="Brand Vibe Monitor", page_icon="📈", layout="wide")

# Initialize our logic
scraper = RedditRSSScraper()
analyzer = SentimentAnalyzer()

st.title("🛡️ Real-Time Brand Reputation Monitor")
st.markdown("Enter a brand name below to see what Redditers thinks in real-time.")

# 1. User Input
target_brand = st.text_input("Brand/Keyword to track:", placeholder="e.g. Tesla, Binance, ChatGPT, Nigerian Air")
search_button = st.button("Run Analysis")

if search_button and target_brand:
    with st.spinner(f"Searching Reddit for '{target_brand}'..."):
        # 2. Get Data
        raw_data = scraper.fetch_data(target_brand, limit=10)

        if not raw_data:
            st.warning("No recent mentions found. Try a different keyword.")
        else:
            # 3. Analyze Data
            processed_results = []
            for item in raw_data:
                vibe = analyzer.get_sentiment(item['title'])
                processed_results.append({
                    "Title": item['title'],
                    "Sentiment": vibe['label'],
                    "Score": vibe['score'],
                    "Link": item['link']
                })

            df = pd.DataFrame(processed_results)

            # 4. Beautiful Dashboard Elements
            avg_score = df['Score'].mean()

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Overall Vibe", vibe['label'], delta=f"{avg_score:.2f}")
            with col2:
                pos_count = len(df[df['Sentiment'] == 'Positive'])
                st.metric("Positive Posts", f"{pos_count}", delta_color="normal")
            with col3:
                neg_count = len(df[df['Sentiment'] == 'Negative'])
                st.metric("Negative Posts", f"{neg_count}", delta_color="inverse")

            st.divider()

            # 5. Display the Table
            st.subheader("Latest Mentions & Analysis")
            # We use st.dataframe for an interactive table
            st.dataframe(df, use_container_width=True)

            # 6. Simple Chart
            st.subheader("Sentiment Distribution")
            st.bar_chart(df['Sentiment'].value_counts())