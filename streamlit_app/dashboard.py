import streamlit as st
import requests

st.title("🔋 Energy Consumption Predictor")

surface = st.slider("Surface (m²)", 20, 200, 80)
occupants = st.slider("Number of occupants", 1, 6, 3)
isolation = st.selectbox("Insulation quality", ["poor", "average", "good"])

if st.button("Predict"):
    data = {
        "surface": surface,
        "occupants": occupants,
        "isolation": isolation
    }
    res = requests.post("http://localhost:5000/predict", json=data)
    prediction = res.json()["prediction"]
    st.success(f"Estimated consumption: {prediction} kWh")