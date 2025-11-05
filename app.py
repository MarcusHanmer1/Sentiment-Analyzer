# Cplt and web help used

import os
import requests

import streamlit as st
import pandas as pd

from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# API and analyzer

load_dotenv()
api_key = os.getenv("news_api_key")

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):

    scores = analyzer.polarity_scores(text)
    return scores['compound']

def get_news_articles(query, api_key):
 
    if not api_key:
        return None,
        
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&language=en&sortBy=publishedAt&pageSize=50"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":
            return data["articles"], None
        else:
            return None, data.get("message", "Unknown API error")
            
    except Exception as e:
        return None, f"A script error occurred: {e}"


# UI

st.set_page_config(page_title = "Live news sentiment analyzer", layout = "wide")
st.title("📈 Live Financial News Sentiment Analyzer")
st.subheader("Powered by NewsAPI.org and VADER")

query = st.text_input("Enter a company name or stock ticker ('Tesla', 'AAPL', etc):", "Tesla")

if st.button("Analyze sentiment"):
    if not query:
        st.error("Please enter a topic to search")
    else:
        with st.spinner(f"Fetching and analyzing news for '{query}'..."):
            articles, error = get_news_articles(query, api_key)
            
            if error:
                st.error(error)
            elif not articles:
                st.warning("No articles found for this topic")
            else:
                df = pd.DataFrame(articles)
                
                df = df[['title', 'description', 'url', 'publishedAt']]
                df.dropna(inplace = True)
                df['sentiment'] = df['title'].apply(get_sentiment)
                
                avg_sentiment = df['sentiment'].mean()
                
                st.subheader(f"Overall sentiment for '{query}': {avg_sentiment:.3f}")
                
                if avg_sentiment > 0.05:
                    st.success("Sentiment: Positive ✅")
                elif avg_sentiment < -0.05:
                    st.error("Sentiment: Negative ❌")
                else:
                    st.info("Sentiment: Neutral 😐")
                
                st.subheader("Analyzed articles:")
                
                df_display = df[['sentiment', 'title', 'description', 'url']]
                st.dataframe(df_display, use_container_width=True)

                st.success("Analysis complete")