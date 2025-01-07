import streamlit as st
import pandas as pd

st.title("🐍 Using reinforcement learning to play Snake", anchor=False)

st.divider()

snake_google_url = "https://www.google.com/search?q=snake+google&oq=snake+google&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMg0IARAAGIMBGLEDGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMjMzOWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
st.markdown(
    f"""
    Snake is a well-known computer game and in this project I
    trained an agent to play this game using reinforcement
    learning methods. If you're unfamiliar with this game
    you can play it in a Google tab [here]({snake_google_url}).

    The inspiration for this project comes from my interest in reinforcement
    learning and passion for wasting time playing snake. 
"""
)

st.header("My Project", anchor=False)

snake_github_url = "https://github.com/DanielBibby/Snake"
st.markdown(
    """
    This project can be viewed on my GitHub page [here](https://github.com/DanielBibby/Snake).
    
    I used Stable-baselines3, a reinforcement learning library in Python for this project where I created a custom 
    environment to implement the well-known game. I have limited resources available to me to train an agent, so this project aim is to create the best possible policy
    while limiting training to 1 million environment interactions. This is relatively few in a game like Snake where 
    food is sparse in the environment.
    s
    The following techniques are used:
    - Deep learning
    - Hyperparameter tuning 
    - Imitation learning
    - Model Selection
    - Reward engineering
    - State space manipulation
    
    I am currently wrapping this project up, currently I am implementing imitation learning as the final method.
"""
)
