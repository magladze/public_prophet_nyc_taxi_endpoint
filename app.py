from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model.prophet_model import preprocess_data, train_model, make_forecast, visualize_forecast, visualize_components

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists('uploads/'):
    os.makedirs('uploads/')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        df = preprocess_data(file_path)
        model = train_model(df)
        forecast = make_forecast(model, periods=30)

        forecast_html = visualize_forecast(forecast)
        components_html = visualize_components(model, forecast)

        return render_template('forecast.html', forecast_html=forecast_html, components_html=components_html)


@app.route('/predict', methods=['POST'])
def predict():
    periods = int(request.form['periods'])
    df = preprocess_data('default_data.csv')  # Replace with the actual dataset path or handle dynamically
    model = train_model(df)
    forecast = make_forecast(model, periods=periods)

    forecast_html = visualize_forecast(forecast)
    components_html = visualize_components(model, forecast)


    return render_template('forecast.html', forecast_html=forecast_html, components_html=components_html)


if __name__ == '__main__':
    app.run(debug=True)