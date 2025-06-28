from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__, static_folder='static', template_folder='templates')
model = joblib.load('model/rf_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    # Read CSV file into a pandas DataFrame
    data = pd.read_csv(file)

    # Extract tool column
    tool_ids = data['tool']

    # Drop non-feature columns
    features = data

    # Make predictions using the Random Forest model
    predictions = model.predict(features)

    # Map predictions to labels
    data['prediction'] = predictions
    data['prediction'] = data['prediction'].map({0: 'Rework', 1: 'Reject'})

    # Return the results as HTML
    result = zip(tool_ids, data['prediction'])
    return render_template('results.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)
