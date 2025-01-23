import streamlit as st

# Streamlit App Title and Description
st.title("📰 Company News Sentiment Analysis")
st.markdown(
    """
This project uses the NewsAPI to retrieve recent news articles and uses a hugging face model to evaluate the sentiment
of each article and provides visualisations for this along with the stock price for that company over the same period
of time.

Since this project only uses the free version of NewsAPI, only a subset of articles may be retrieved. 
"""
)
st.divider()

st.markdown("""
 **This project is deployed as a seperate app [here](https://danielbibby-news-sentiment-analysis.streamlit.app) or you 
 can clone it from [GitHub](https://github.com/DanielBibby/NewsAnalysis)**
""")