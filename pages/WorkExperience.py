import streamlit as st
import webbrowser

st.title("📈 Work Experience", anchor=False)

st.divider()

col1, col2 = st.columns(2)

with col2:
    st.image("static/Logo-Faculty-700x280px-black-rgb.jpg", width=250)

    if st.button(label="Faculty Website"):
        webbrowser.open("https://faculty.ai/")

with col1:
    st.markdown(
        """
        <h2 style="font-size:32px;">
            <span style="color:#DB622A;">Faculty AI</span> | Data Science Fellowship
        </h2>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
I completed two weeks of intense training learning 
about modern machine learning and data science techniques
used in industry before completing a short project
for the Veterinary Medicines Directorate.

My project tasked me with classifying specialist 
calf-rearing farms in GB and calculating mortality
rates for them. With no labelled data I used the
knowledge of industry experts and movement data of
cows to engineer an interpretable solution. 

I validated solutions through a round of EDA, 
looking at farms on the edge case of my model and 
aggregating data from farms on either side of the
classification. My work revealed information about
the cattle industry that will inform decision making
internally and may be used in published reports.

For this project I used Python, SQLite, Jupyter and Git.

"""
)

st.divider()

col3, col4 = st.columns(2)

with col4:
    st.image("static/tamarix.png", width=250)

    if st.button(label="Tamarix Website"):
        webbrowser.open("https://tamarix.tech/")

with col3:
    st.markdown(
        """
        <h2 style="font-size:32px;">
            <span style="color:#5245A0;">Tamarix Tech</span> | Data Science Internship
        </h2>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
I was the sole contributor to an automation pipeline
that used LLMs for structured data extraction from 
financial PDFs. 

Used Python, Langchain, Docker, Git, MongoDB and 
other tools in this role while working in an Agile 
framework.

Delivered the following features:

- Analytics framework used for BAU monitoring and 
targeted performance improvements.

- Benchmarking tool used to evaluate the impact of 
pipeline changes before deployment.

- Building out codebase to allow for swift updates in
line with industry changes.

- NLP based ranking system for pages based on fields
to be extracted.
"""
)

st.divider()
