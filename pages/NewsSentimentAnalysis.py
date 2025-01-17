import streamlit as st

# Streamlit App Title and Description
st.title("📰 Company News Sentiment Analysis")
st.markdown(
    """
This project uses the NewsAPI to retrieve recent news articles and uses a hugging face model to evaluate the sentiment
of each article and provides a visualisation for this along with the stock price for that company over the same period
of time.
"""
)
st.divider()

st.markdown("""
 **This project is a work in progress see my github page for the current progress.**
""")