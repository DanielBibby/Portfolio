import streamlit as st
import pandas as pd

st.title("🐍 Using reinforcement learning to play Snake", anchor=False)

st.divider()

snake_google_url = "https://www.google.com/search?q=snake+google&oq=snake+google&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMg0IARAAGIMBGLEDGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMjMzOWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
st.markdown(f"""
    Snake is a well-known computer game and in this project I
    trained an agent to play this game using reinforcement
    learning methods. If you're unfamiliar with this game
    you can play it in a Google tab [here]({snake_google_url}).

    The inspiration for this project comes from my interest in reinforcement
    learning and passion for wasting time playing snake. 
""")

st.header("My Project", anchor = False)

snake_github_url = "https://github.com/DanielBibby/Snake"
st.markdown("""
    This project can be viewed on my GitHub page [here](https://github.com/DanielBibby/Snake).
    
    I used Stable-baselines3, a reinforcement learning library in Python for this project where I created a custom 
    environment to implement the well-known game. I then manipulated the state representation, performed reward engineering,
    bias-reduction methods, hyperparameter optimisation and utilised visualisations and other metrics to create an agent that
    can play Snake autonomously. 
    
    I have limited resources available to me to train an agent, so this project aim is to create the best possible agent 
    while limiting training to 1_000_000 environment interactions. This is relatively few in a game like Snake where
    rewards are received sparsely. 
    
    I am still in the process of working on this project. I am currently perofrming a round of hyperparameter tuning to 
    find an efficient learning and exploration schedule. After this I will implement a full round of training, that is 
    to say a round of training with all 1_000_000 training steps being used. 
    
    The next step will likely be to perform more sophisticated reward engineering and further my bias reduction efforts.
    I may also implement imitation learning.
""")
