from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('C:\\Users\\Viviktha\\Downloads\\RandomForestModel (2).joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uoloaded', 400
    file = request.files['file']
    
    if file.filename =='':
        return 'No selected file', 400
    
    #reading excel file into a pandas DataFrame
    data = pd.read_excel(file)
    
    #Make predictions using the Random Forest model
    predictions = model.predict(data)
    
    #Add predictions as a new column
    data['prediction'] = predictions
    data['prediction'] = data['prediction'].map({1: 'Rework', 0:'Reject'})

    #Return the results as HTML 
    result = zip(data['tool'], data['prediction'])
    return render_template('results.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)