import streamlit as st

pages = {
    "": [
        st.Page("pages/Home.py", title="Homepage", icon="🏠"),
        st.Page("pages/Education.py", title="Education", icon="📚"),
        st.Page("pages/WorkExperience.py", title="Work Experience", icon="📈"),
        st.Page("pages/ContactInfo.py", title="Contact", icon = "😎")
    ],
    "Personal Projects": [
        st.Page("pages/Snake.py", title="Snake", icon="🐍"),
        st.Page("pages/Dashboarding.py", title="Dashboarding and APIs", icon="📊"),
        st.Page("pages/NewsSentimentAnalysis.py", title="Company News Sentiment Analysis", icon="📰"),
    ],
}

pg = st.navigation(pages)
pg.run()
