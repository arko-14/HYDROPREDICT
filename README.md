# HYDROPREDICT
Project Overview

Groundwater is a critical resource that supports agriculture, drinking water, and industrial uses. The HYDROpredict project leverages environmental data to understand and forecast groundwater levels. By analyzing historical data such as temperature, precipitation, and groundwater levels, we aim to provide predictive insights that can aid in sustainable water management.

Objective:-

To explore how factors like temperature, precipitation, and seasonal changes impact groundwater levels and to create a predictive model for groundwater level trends.

# Key Features:-

Data Cleaning and Processing: Handles missing values, standardizes data formats, and ensures data consistency.

Exploratory Data Analysis (EDA): Identifies key trends, visualizes data patterns, and assesses correlations between variables.

Feature Engineering: Generates new features such as monthly averages and seasonal indicators.

Machine Learning Models: Uses regression and time-series models to predict groundwater levels based on environmental factors.

Visualization: Provides clear graphs and charts to show relationships, trends, and prediction accuracy.

DATA SETS:

Groundwater Level Data: Historical data on groundwater levels.

Climate Data: Temperature, soil moisture and precipitation records.

The project employs XGBoost for high accuracy after extensive model optimization and comparison with other models, including Random Forest and LightGBM.

# Model Description
Initial Model Selection
Random Forest Regressor: Used initially to predict groundwater levels and soil temperature. It employs an ensemble of decision trees to capture data patterns.
Hyperparameter Tuning
Grid and Random Search: Hyperparameters for Random Forest were tuned to optimize model performance.

# Pipeline of Multiple Models
Random Forest: Served as the starting model for predictions.
XGBoost: Adopted for its faster computation and superior accuracy in comparison to Random Forest. It builds an ensemble of trees incrementally, focusing on reducing errors from previous models.
LightGBM: Another gradient boosting method, faster for large datasets and often more efficient than other boosting methods.

# Final Model Selection
XGBoost: Chosen for its superior accuracy after hyperparameter tuning, outperforming both Random Forest and LightGBM models.

Data Preparation

Loading the Data: The datasets were imported into pandas DataFrames, including features like precipitation, soil temperature, year, and location.

Feature Engineering: Categorical features like location and month were encoded as binary/dummy variables for model compatibility.

Model Training and Evaluation

Training: The XGBoost model was trained using historical data, identifying relationships between environmental variables and groundwater levels/soil temperatures.

Evaluation Metrics:
MAE: Mean Absolute Error to measure prediction accuracy.
RMSE: Root Mean Squared Error, focusing on larger errors.
R² Score: Measures the proportion of variance explained by the model.

# Final Model Deployment
The XGBoost model was deployed to make real-time predictions of groundwater levels and soil temperature based on new input data.

# Frontend

Technologies Used
Streamlit: Used to build the interactive user interface, enabling seamless integration with Python code for real-time predictions.
Pandas: Used for managing and displaying input/output data.
CSS: Custom CSS for styling elements like buttons, text, and backgrounds.

Example Workflow
User Input: Select location, month, and precipitation using dropdowns and sliders.
Get Predictions: Click the "Get Predictions" button to generate groundwater level and soil temperature predictions.
Display Predictions: The predicted values are shown on the frontend.
Save Data: Users can save the input and predictions to a CSV file.
Usage
Clone the repository:
git clone https://github.com/your-username/hydropredict.git

# Install required dependencies:

pip install -r requirements.txt
Run the Streamlit app:
streamlit run app.py

# Conclusion
The XGBoost model, combined with a user-friendly frontend built using Streamlit, provides accurate real-time predictions of groundwater levels and soil temperatures, aiding in water and crop management.


