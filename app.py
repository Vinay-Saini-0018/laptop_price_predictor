import streamlit as st
import joblib
import numpy as np
import pandas as pd


pkl_model=joblib.load("final_model.pkl")
data = joblib.load("data.pkl")

st.title("Laptop Price Prediction")

#brand
company = st.selectbox("Brand", data['Company'].unique())

#model
model = st.selectbox("model",data["Model"].unique())

#OS
os = st.selectbox("Operating system", data['OS'].unique())

#Processor
processor = st.selectbox("processor", data['Processor'].unique())

#Core
core = st.selectbox("core", data['Core'].unique())

#Graphics
graphics = st.selectbox("graphics", data['Graphics'].unique())

#Ram
ram = st.selectbox("RAM", data['Ram'].unique())

#SSD
ssd = st.selectbox("SSD", data['SSD'].unique())

#Display
display = st.selectbox("display", data['Display'].unique())


user_input = pd.DataFrame([{
    'Company':company,
    'Model':model,
    'OS':os,
    'Processor':processor,
    'Core':core,
    'Graphics':graphics,
    'Ram':ram,
    'SSD':ssd,
    'Display':display
}])

if st.button("Predict"):
    prediction = pkl_model.predict(user_input)
    st.success(f"your price is ₹{prediction}")