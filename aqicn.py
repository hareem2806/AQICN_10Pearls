import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the trained model
model = joblib.load("C:/Users/Lenovo/Downloads/aqi_prediction_model.pkl")

# Function to predict AQI category (5-very poor, 4-poor, 3-moderate, 2-fair, 1-good)
def predict_aqi(features):
    # Predict AQI using the trained model
    prediction = model.predict([features])[0]
    
    # If your model already predicts values in the range of 1-5, just return the value
    return round(prediction)  # Round to the nearest integer to get AQI category

# Streamlit app layout
st.title("🌱 Air Quality Index (AQI) Prediction 🌍")
st.write("This app predicts the Air Quality Index (AQI) based on various factors like CO, NO2, O3, PM2.5, and others. 🏩")

# User inputs
hour = st.slider("🕒 Hour of the day", 1, 24, 12)  # Updated for 1-24 hours
day = st.slider("🗓 Day of the week", 1, 7, 1)  # Updated for 1-7 days, Monday = 1, Sunday = 7
month = st.slider("🗓 Month", 1, 12, 5)
weekday = st.selectbox("🔣 Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
co = st.number_input("🌬️ CO (Carbon monoxide)", min_value=0.0, value=0.1)
no = st.number_input("🌬️ NO (Nitrogen monoxide)", min_value=0.0, value=0.02)
no2 = st.number_input("🌬️ NO2 (Nitrogen dioxide)", min_value=0.0, value=0.03)
o3 = st.number_input("🌬️ O3 (Ozone)", min_value=0.0, value=0.1)
so2 = st.number_input("🌬️ SO2 (Sulfur dioxide)", min_value=0.0, value=0.01)
pm2_5 = st.number_input("🌫️ PM2.5 (Particulate matter <2.5μm)", min_value=0.0, value=10.0)
pm10 = st.number_input("🌫️ PM10 (Particulate matter <10μm)", min_value=0.0, value=20.0)
nh3 = st.number_input("🌬️ NH3 (Ammonia)", min_value=0.0, value=0.05)

# Map weekday selection (1=Monday, 7=Sunday)
weekday_mapping = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}
weekday_num = weekday_mapping[weekday]

# Prepare the features for prediction
features = [hour, day, month, weekday_num, co, no, no2, o3, so2, pm2_5, pm10, nh3]

# Button to trigger prediction
if st.button("🔮 Predict AQI"):
    # Predict AQI category
    aqi_category = predict_aqi(features)
    
    # Display the result
    aqi_levels = {1: "Good 😇", 2: "Fair 😌", 3: "Moderate 😐", 4: "Poor 😷", 5: "Very Poor 🗭"}
    st.write(f"### The predicted AQI category is: **{aqi_levels[aqi_category]}**")

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
