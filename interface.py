import streamlit as st
import requests
import json
# Title of the Streamlit app
st.title("California Housing Price Predictor")

st.write("This app allows you to test an API that predicts average house values based on input features.")

# Input fields for the API
st.sidebar.header("Input Features")

# Feature inputs
med_inc = st.sidebar.number_input("Median Income (in tens of thousands):", min_value=0.0, step=0.1)
house_age = st.sidebar.number_input("Housing Median Age:", min_value=0, step=1)
avg_rooms = st.sidebar.number_input("Average Rooms Per Household:", min_value=0.0, step=0.1)
avg_bedrooms = st.sidebar.number_input("Average Bedrooms Per Household:", min_value=0.0, step=0.1)
population = st.sidebar.number_input("Population:", min_value=0, step=1)
households = st.sidebar.number_input("Households:", min_value=0, step=1)
lat = st.sidebar.number_input("Latitude:", min_value=-90.0, max_value=90.0, step=0.1)
lon = st.sidebar.number_input("Longitude:", min_value=-180.0, max_value=180.0, step=0.1)

# API URL input
api_url = st.text_input("API URL", placeholder="Enter the API endpoint here",value="http://127.0.0.1:8000/predict"
)

# Predict button
if st.button("Predict"):
    if not api_url:
        st.error("Please provide the API URL.")
    else:
        # Prepare input data
        input_data = {
            "MedInc": med_inc,
            "HouseAge": house_age,
            "AveRooms": avg_rooms,
            "AveBedrms": avg_bedrooms,
            "Population": population,
            "AveOccup": households,
            "Latitude": lat,
            "Longitude": lon
        }

        try:
            # Make a POST request to the API
            response = requests.post(api_url, json=input_data)

            if response.status_code == 200:

                data = json.loads(response.text)

                prediction = data["median_house_value"][0]
                if prediction is not None:
                    st.success(f"The predicted average house value is: ${prediction*100000:,.2f}")
                else:
                    st.error("The API response did not contain a prediction.")
            else:
                st.error(f"Failed to get a prediction. API responded with status code {response.status_code} and message: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while trying to connect to the API: {e}")

# to run the interface, run the following command in the terminal:
# streamlit run interface.py