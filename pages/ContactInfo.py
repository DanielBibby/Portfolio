import streamlit as st

st.title("😎 Contact Info", anchor=False)

st.divider()

st.markdown("""
#### Email: 12dbibb@gmail.com
#### Linkedin: [Daniel Bibby](https://www.linkedin.com/in/daniel-bibby-5149a91bb/)
#### GitHub: https://github.com/DanielBibby
""")

st.divider()

if st.button("Double Click For A Surprise!"):
    st.image("static/Suit_and_dog.jpg", width=750)