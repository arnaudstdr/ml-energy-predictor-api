import joblib
import pandas as pd

model = joblib.load("app/model.pkl")

def predict_consumption(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]