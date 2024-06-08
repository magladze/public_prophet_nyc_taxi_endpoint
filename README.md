# Forecasting Web Application with Prophet

## Introduction

Prophet is a forecasting tool developed by Facebook's Core Data Science team. Released in 2017, Prophet is designed to handle time series data and make projections based on historical data. It is particularly adept at managing daily observations with seasonal effects and holidays. With its intuitive interface and robust capabilities, Prophet has become a popular choice for analysts and data scientists.

This repository contains a web application built using Flask that leverages Prophet for time series forecasting. The application allows users to upload datasets, train a model, and visualize forecasts and model components. 

## Libraries Involved

1. **Pandas**: A powerful data manipulation library in Python used for reading and preprocessing datasets.
2. **Prophet**: A forecasting tool developed by Facebook, used here for time series forecasting.
3. **Flask**: A lightweight web application framework in Python used to create the web interface.
4. **Plotly**: A graphing library used for creating interactive visualizations.
5. **Matplotlib**: Another plotting library used for visualizing model components.

## File Structure

```
- app/
  - static/
  - templates/
    - index.html
    - forecast.html
  - model/
    - prophet_model.py
  - app.py
  - requirements.txt
```

### File Descriptions

#### 1. `prophet_model.py`
This file contains the core logic for data preprocessing, model training, forecasting, and visualization.

- **Functions**:
  - `preprocess_data(file_path)`: Reads the dataset from the provided file path (supports `.csv` and `.parquet` formats), converts the date column to datetime, and renames the columns to be compatible with Prophet.
  - `train_model(df)`: Trains a Prophet model using the preprocessed dataframe.
  - `make_forecast(model, periods)`: Generates a forecast for the specified number of periods using the trained model.
  - `visualize_forecast(forecast)`: Creates an interactive line plot of the forecast using Plotly and returns it as HTML.
  - `visualize_components(model, forecast)`: Plots the forecast components (trend, seasonality, etc.) using Matplotlib, encodes the plot as a base64 string, and returns it as HTML.

#### 2. `app.py`
This file sets up the Flask application and defines the endpoints for file upload and prediction.

- **Endpoints**:
  - `/`: Renders the homepage where users can upload datasets and request real-time predictions.
  - `/upload`: Handles file uploads, preprocesses the data, trains the model, makes forecasts, and renders the forecast and components.
  - `/predict`: Handles real-time predictions based on a default dataset and user-specified periods, then renders the forecast and components.

#### 3. `templates/index.html`
This HTML template provides the user interface for uploading datasets and entering periods for real-time predictions.

- **Sections**:
  - File upload form.
  - Real-time prediction form.

#### 4. `templates/forecast.html`
This HTML template displays the forecast results and component plots.

- **Sections**:
  - Forecast plot.
  - Component plots.

#### 5. `requirements.txt`
Lists all the Python dependencies required to run the application.

## Use-Cases and Expansions

### Use-Cases

1. **Business Forecasting**: Businesses can use this application to forecast sales, revenue, or other key metrics based on historical data.
2. **Stock Price Prediction**: Financial analysts can upload historical stock price data to forecast future prices.
3. **Weather Forecasting**: Meteorologists can use this tool to predict weather patterns based on historical weather data.
4. **Demand Planning**: Supply chain managers can forecast demand for products to optimize inventory levels.

### Expansions

1. **Additional Data Formats**: Extend the application to support more data formats like Excel or JSON.
2. **Advanced Model Configuration**: Allow users to configure advanced settings of the Prophet model, such as seasonalities and holidays.
3. **User Authentication**: Implement user authentication to save and manage multiple forecasts.
4. **API Integration**: Integrate with external APIs to fetch real-time data for predictions.

## Supported Datasets

The application currently supports datasets in CSV and Parquet formats. The datasets should have a datetime column and a target variable column. Example datasets include:

- Historical sales data with columns for date and sales amount.
- Stock price data with columns for date and closing price.
- Weather data with columns for date and temperature.

## Business Applications

1. **Retail**: Retailers can use this tool to forecast sales and optimize stock levels, reducing overstock and stockouts.
2. **Finance**: Financial institutions can predict market trends and stock prices, aiding in investment decisions.
3. **Manufacturing**: Manufacturers can forecast demand for raw materials and finished goods, improving production planning.
4. **Logistics**: Logistics companies can predict shipment volumes, optimizing route planning and resource allocation.

## Running the Application

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000/` in your web browser to access the application.

## Conclusion

This web application provides a powerful and flexible platform for time series forecasting using Prophet. Whether you are a business analyst, financial expert, or data scientist, this tool can help you make informed decisions based on historical data trends. 


