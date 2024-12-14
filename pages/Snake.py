import streamlit as st
import pandas as pd

st.title("🐍 Using reinforcement learning to play Snake", anchor=False)

st.divider()

st.header("Introduction", anchor=False)

snake_google_url = "https://www.google.com/search?q=snake+google&oq=snake+google&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMg0IARAAGIMBGLEDGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMjMzOWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
st.markdown(f"""
    Snake is a well-known computer game and in this project I
    trained an agent to play this game using reinforcement
    learning methods. If you're unfamiliar with this game
    you can play it in a Google tab [here]({snake_google_url}).

    The inspiration for this project comes from my interest in reinforcement
    learning and passion for wasting time playing snake. 
""")

st.header("Reinforcement Learning Introduction", anchor = False)

st.markdown("""
    Reinforcement learning (RL) is a way to teach a machine how to 
    effectively pick an **action** when interacting with the **environment** it 
    exists in to obtain a maximum **reward**s.
    
    The ideas of action, environment and reward vary depending on the situation
    problem being solved, for example:
""")

rl_dict = {
    "Application": ["Self Driving Car", "Chess", "Snake"],
    "Environment": ["Roads and surrounding area", "Chess Board", "nxn grid"],
    "Action": ["Driving operations", "Valid Moves", "Left, Right, Straight"],
    "Reward": ["Safe arrival at destination", "Winning Game", "Eat food"],
}

rl_df = pd.DataFrame(
    rl_dict
)

st.table(rl_df)

st.markdown("""
    Efficient reinforcement learning depends on efficiently
    exploring an environment to find the best way to make
    decisions. 
    
    Within reason one can engineer the environment representation
    as I will demonstrate later. It is far easier to engineer the 
    reward function to optimise performance. 
""")

st.markdown("""
    The decision making part of RL is the **policy**. At a high level this can 
    be thought of as the brain of the **agent**. A policy will observe the state
    of the world it lives in and output an action believed to be best in some 
    sense.
    
    There are lots of different algorithms that can be used to extract value
    from experiences of the agent.
""")


st.markdown("""
    To summarise, RL can be broken down into the following parts.
""")


st.latex(r"""
    \begin{aligned}
    S & = \text{State: the observable environment} \\
    A & = \text{Action: the set of possible actions (action space)} \\
    R(s, a) & = \text{Reward: the reward function for state } s \text{ and action } a \\
    \pi(s) & = \text{Policy: the agent's decision-making strategy for state } s
    \end{aligned}
""")

st.header("My Methodology", anchor=False)

st.markdown("""
    Explain first hyper params and stuff. 
    
    Provide some results here.
""")


st.markdown(
    """
    <h2 style="font-size:28px;">
        Efficient State Representation 
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    Here I decrease the size of the state space to 25% of it's original size. 
    This improves the ability of the agent to explore the state space.    
    
    Snake has rotational symetry. 
    
    Observe the four states below
    
    Have four states here with the obvious symetry
    """)

st.markdown("""
    Explain the transofrmation.
""")

st.markdown("""
    Display Reulsts in Training speed
""")

st.markdown(
    """
    <h2 style="font-size:28px;">
        Improving Reward Function
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    Notice the long life but low score.
""")

st.markdown("""
    Explain the change to reward function
""")

st.markdown(
    """
    <h2 style="font-size:28px;">
        Randomising reset
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    Explain the issue.
""")

st.markdown("""
    Explain the solution
""")

st.markdown("""
    Show results.
""")

st.markdown(
    """
    <h2 style="font-size:28px;">
        Picking the best model.
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    Explain problem
""")

st.markdown("""
    Explain solution
""")

st.markdown("""
    Show results
""")
