import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("car_price_model.pkl")

st.title("Car Price Prediction App")
st.write("Fill in the car details below to predict the price.")

# Input fields
carwidth = st.slider("Car Width", 60.0, 75.0, 65.0)
curbweight = st.slider("Curb Weight", 1500, 4000, 2500)
enginesize = st.slider("Engine Size", 60, 350, 120)
horsepower = st.slider("Horsepower", 50, 300, 100)
citympg = st.slider("City MPG", 10, 50, 25)
highwaympg = st.slider("Highway MPG", 10, 60, 30)

fueltype = st.selectbox("Fuel Type", ['gas', 'diesel'])
aspiration = st.selectbox("Aspiration", ['std', 'turbo'])
doornumber = st.selectbox("Door Number", ['two', 'four'])
drivewheel = st.selectbox("Drive Wheel", ['fwd', 'rwd', '4wd'])
carbody = st.selectbox("Car Body", ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'])

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[carwidth, curbweight, enginesize, horsepower, citympg, highwaympg,
                            fueltype, aspiration, doornumber, drivewheel, carbody]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Car Price: ${prediction[0]:,.2f}")
