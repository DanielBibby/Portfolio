import streamlit as st

# Streamlit configuration for Claude-inspired theme
st.set_page_config(
    page_title="Home Page",
    page_icon=":briefcase:",
    initial_sidebar_state="expanded",
    menu_items={
        "Report a bug": "mailto:12dbibb@gmail.com",
    },
    layout="centered",
)

st.header("Daniel Bibby Portfolio", anchor=False)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.header("About Me", anchor=False)
    st.markdown(
        """
    👨‍💻 Data scientist with experience spanning
    academic research, fintech and the public 
    sector. 
    
    🎓 University of Warwick - Mathematics and Statistics 
    (MMathStat) - Fisrt
    
    📍 London, GB
    
    
    """
    )

with col2:
    st.image("static/Daniel_streamlit_photo.png")

st.divider()
