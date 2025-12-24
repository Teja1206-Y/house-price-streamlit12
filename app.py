import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load trained model (.pkl)
# -----------------------------
with open(r"C:\Users\tejes\Houseprice ML\modelHousepred.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏠 House Price Prediction")
st.write("Enter the house details to predict the price")

# -----------------------------
# User Inputs
# -----------------------------
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0.0, max_value=10.0, value=2.0)
sqft_living = st.number_input("Sqft Living Area", min_value=100, max_value=10000, value=1800)
view = st.selectbox("View Rating (0–4)", [0, 1, 2, 3, 4])
sqft_above = st.number_input("Sqft Above", min_value=100, max_value=10000, value=1500)
sqft_basement = st.number_input("Sqft Basement", min_value=0, max_value=5000, value=300)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Price 💰"):
    input_data = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        view,
        sqft_above,
        sqft_basement
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"🏷️ Estimated House Price: **₹ {prediction:,.2f}**")

# --------------------------
