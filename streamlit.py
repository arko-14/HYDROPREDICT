import streamlit as st
import pandas as pd
import joblib  # Import joblib for loading the model

# Set page configuration for better layout
st.set_page_config(
    page_title="HYDROPREDICT 🌊",
    layout="wide",
)

# Custom CSS for styling
custom_css = """
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
<style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #e1f5fe;
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #0288d1;
        color: white;
    }
    h1 {
        color: #0288d1;
        text-align: center;
    }
    h3 {
        color: #0288d1;
    }
    .stButton>button {
        background-color: #0288d1;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
    }
    .stTextInput>div>input {
        border-radius: 5px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Title of the app
st.title("HYDROPREDICT - Where Temperature Meets Groundwater 🌊")

# Add some introductory text
st.write("""
### Welcome to HYDROPREDICT
This app predicts *groundwater level* and *soil temperature* based on the location, month, and precipitation data.
It helps to assess water and soil conditions, useful for farming, water management, and environmental studies.
""")

# Sidebar for User Inputs
st.sidebar.header('User Input Features')

# Location input: Dropdown with a scroll bar to select cities
location = st.sidebar.selectbox(
    'Select Location 🌍', 
    ['Bangalore', 'Chennai', 'Kolkata', 'Delhi'],
    help="Select a city to predict groundwater and soil temperature"
)

# Month input: Slider to select month (1-12)
month = st.sidebar.slider('Select Month 📅', 1, 12, 6)

# Precipitation input: Slider to select precipitation in mm
precipitation = st.sidebar.slider('Precipitation (mm) ☔', min_value=0, max_value=500, value=100)

# Function to collect the input data and display it
def user_input():
    data = {
        'Location': location,
        'Month': month,
        'Precipitation (mm)': precipitation
    }
    return data

# Get input from the user
input_data = user_input()

# Convert the input data into a DataFrame
input_df = pd.DataFrame(input_data, index=[0])

# Display the collected input data in a well-styled format
st.subheader('Your Input Data:')
st.write(input_df.style.highlight_max(axis=0))

# Placeholder for model predictions
st.subheader('Predicted Results:')

# Add a button to trigger predictions
if st.button('Get Predictions 🤖'):
    # Load the trained model from the specified path
    model_path = r"C:\Users\psand\Downloads\xgboost_model.joblib"  # Modify this with your joblib model path

    try:
        # Load the model with joblib
        model = joblib.load(model_path)  # Use joblib for loading

        # Prepare the input data in the same format your model expects
        model_input = input_df[['Month', 'Precipitation (mm)']]  # Example, modify as needed

        # Make the prediction
        prediction = model.predict(model_input)  # Use model.predict() for joblib model

        # Display predicted values with enhanced formatting
        st.success(f"*Predicted Groundwater Level:* {prediction[0][0]:.2f} meters 💧")
        st.success(f"*Predicted Soil Temperature:* {prediction[0][1]:.2f} °C 🌡")

    except Exception as e:
        st.error(f"Error loading model or making predictions: {str(e)}")

    # Add a Save Data button to save the input data and predictions
    if st.button("Save Data 💾"):
        # Add predictions to the input data
        input_df['Predicted Groundwater Level (m)'] = prediction[0][0]
        input_df['Predicted Soil Temperature (°C)'] = prediction[0][1]

        # Save to CSV (you can modify the file path if needed)
        input_df.to_csv('hydropredict_predictions.csv', mode='a', header=False, index=False)
        st.success("Data has been saved successfully! 🎉")
else:
    st.write("Click the button to get predictions.")

# Footer: Add additional information with improved styling
st.markdown("""
---
#### About HYDROPREDICT:
HYDROPREDICT provides predictions about groundwater levels and soil temperature based on environmental parameters like location, precipitation, and time of the year. The tool is especially useful for agriculture, water management, and environmental monitoring.

Feel free to experiment with the sliders and see how predictions change with different values!
""")
