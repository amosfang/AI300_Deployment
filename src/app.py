from flask import Flask, request, render_template
from model import Model
from input_processing import format_model_inputs
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST']) # Ensure that 'POST' has been added to methods
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        model_inputs = format_model_inputs(form_input)
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')

# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    model_inputs = format_model_inputs(request_data)
    prediction = Model().predict(model_inputs)

    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(debug=True)
