import pandas as pd
from prophet import Prophet
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import io
from PIL import Image
import base64
from plotly.graph_objs import Image as PlotlyImage

def preprocess_data(file_path):
    """we are only doing .csv and .parquet in this example"""
    if('.csv' in file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_parquet(file_path)
    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
    df = df.rename(columns={'lpep_pickup_datetime': 'ds', 'tip_amount': 'y'})
    return df

def train_model(df):
    model = Prophet()
    model.fit(df)
    return model


def make_forecast(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


def visualize_forecast(forecast):
    fig = px.line(forecast, x='ds', y='yhat', title='Forecast')
    fig.update_traces(line=dict(color='blue'))
    return pio.to_html(fig, full_html=False)


def visualize_components(model, forecast):

    fig = model.plot_components(forecast)

    # Save the plot to a BytesIO object and encode it as base64
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return f'<img src="data:image/png;base64,{plot_url}"/>'