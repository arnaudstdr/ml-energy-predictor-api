import streamlit as st
import requests

st.title("Energy Consumption Predictor")

surface = st.number_input("Surface (m²)", min_value=10, max_value=500, value=80)
occupants = st.number_input("Number of occupants", min_value=1, max_value=10, value=3)
isolation = st.selectbox("Insulation quality", ["poor", "average", "good"])

if st.button("Predict"):
    data = {
        "surface": surface,
        "occupants": occupants,
        "isolation": isolation
    }
    response = requests.post("http://localhost:5000/predict", json=data)
    prediction = response.json()["prediction"]
    st.success(f"Estimated consumption: {prediction:.2f} kWh")