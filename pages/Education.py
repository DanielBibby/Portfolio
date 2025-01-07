import streamlit as st

st.title("📚 Education", anchor=False)

st.divider()

st.markdown(
    """
    <h2 style="font-size:32px;">
        <span style="color:#3C1053;">University of Warwick</span> | Mathematics and Statistics MMathStat | First
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h2 style="font-size:24px;">
        Dissertation - First
    </h2>
    """,
    unsafe_allow_html=True,
)

st.write(
    """
My dissertation was a data science project where I used
high-frequency stock market data to explore the viability 
of applying 'the signature' of a stock price path in a financial analysis
setting.

I initially performed dimensionality reduction before
applying a novel clustering algorithm to identify repeated patterns in
the shape of stock price movements.

I then used applied random forrest classification to price and volatility prediction
as well as identifying spurious stock price behaviour. Here I used the stock price signature 
to extract features for use in model building. 
"""
)

st.markdown(
    """
    <h2 style="font-size:24px;">
        Awards
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
- Warwick Statistics Scholarship 2022
- Academic Excellence Prize 2022
- Academic Excellence Prize 2021
"""
)

st.markdown(
    """
    <h2 style="font-size:24px;">
        Module Topics
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
I took modules in the following areas:

- Statistical Learning
- Bayesian Methods
- Big Data 
- Monte Carlo Methods
- Actuarial Methods
- Mathematical Finance


"""
)


st.divider()
