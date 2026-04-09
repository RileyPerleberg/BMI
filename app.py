import streamlit as st
import pandas as pd
import math
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")

st.write("Enter your weight in kilograms and height in meters.")

# User inputs
weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Height (m)", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI category
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.info("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.info("Category: Overweight")
        else:
            st.info("Category: Obese")
    else:
        st.error("Height must be greater than 0.")
