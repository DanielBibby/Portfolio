import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit App Title and Description
st.title("🌦 Weather Dashboard")
st.markdown(
    """
This application demonstrates how to use Streamlit for:
- API interaction
- Data visualisation
- Creating an interactive dashboard

The app fetches weather data from the Open-Meteo API and displays the information.
"""
)
st.divider()

# Sidebar for User Input
st.markdown(
    """
    #### Location Input
"""
)

location = st.selectbox(
    "Where would you like to be?", ("Burgess Hill", "Nepal", "Miami")
)

if location == "Burgess Hill":
    longitude = -0.1436
    latitude = 50.9542
elif location == "Nepal":
    longitude = 84.1240
    latitude = 28.3949
elif location == "Miami":
    longitude = -80.1918
    latitude = 25.7617
else:
    st.error("Invalid option")


# Fetch Data from Open-Meteo API
@st.cache_data
def fetch_weather_data(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None


# Process Weather Data
def process_weather_data(api_data):
    hourly_data = api_data["hourly"]
    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])
    return df


def plot_weather_data(df):
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        x="time",
        y="temperature_2m",
        data=df,
        color="orange",
        linewidth=2,
        label="Temperature (°C)",
        ax=ax,
    )
    ax.set_title("Temperature", fontsize=16, weight="bold")
    ax.set_xlabel("Day", fontsize=12)
    ax.set_ylabel("Temperature (°C)", fontsize=12)
    ax.tick_params(axis="x", rotation=45)
    ax.legend(fontsize=10)
    st.pyplot(fig)

    # Bar plot for precipitation
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="time", y="precipitation", data=df, color="blue", alpha=0.7, ax=ax)
    ax.set_title("Hourly Precipitation", fontsize=16, weight="bold")
    ax.set_xlabel("Day", fontsize=12)
    ax.set_ylabel("Precipitation (mm)", fontsize=12)


    unique_days = df["time"].dt.strftime("%Y-%m-%d").unique()
    day_start_indices = [
        df[df["time"].dt.strftime("%Y-%m-%d") == day].index[0] for day in unique_days
    ]
    ax.set_xticks(day_start_indices)
    ax.set_xticklabels(unique_days, rotation=45, ha="right")

    st.pyplot(fig)


# Main App Logic
if st.button("Fetch Weather Data"):
    weather_data = fetch_weather_data(latitude, longitude)

    if weather_data:
        df_weather = process_weather_data(weather_data)

        st.subheader("Weather Data (Hourly)")
        st.dataframe(df_weather)

        plot_weather_data(df_weather)
    else:
        st.error("Unable to fetch or process data.")
