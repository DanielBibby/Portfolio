import streamlit as st

# Title of the app
st.title("Basic Streamlit App")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Add your widgets here!")

# Main content
st.write("Welcome to your basic Streamlit app!")
st.write("You can start adding your components here.")

# Example input field
user_input = st.text_input("Enter something:")
if user_input:
    st.write(f"You entered: {user_input}")

# Example button
if st.button("Click Me"):
    st.write("Button clicked!")

# Example slider
slider_value = st.slider("Pick a number", 0, 100)
st.write(f"Slider value: {slider_value}")

# Footer
st.write("---")
st.write("Build upon this structure to create your app!")
