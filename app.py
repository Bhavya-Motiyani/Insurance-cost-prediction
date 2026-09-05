import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the flask app
app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('Insurance_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: 'insurance_model.pkl' not found. Make sure the model file is in the correct directory.")
    exit()

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    # The final model uses ['age', 'bmi', 'smoker', 'children']
    # Ensure they are converted to the correct data types
    try:
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        
        # The 'smoker' value is mapped from the form's 'yes'/'no'
        smoker_val = request.form['smoker']
        smoker = 1 if smoker_val.lower() == 'yes' else 0

        # Create the feature array for prediction in the correct order
        features = [age, bmi, smoker, children]
        final_features = [np.array(features)]
        
        # Make the prediction
        prediction = model.predict(final_features)

        # Format the output
        output = round(prediction[0], 2)

        # Render the page with the prediction result
        return render_template('index.html', prediction_text=f'Predicted Insurance Charge: ${output}')

    except Exception as e:
        # Handle errors gracefully
        return render_template('index.html', prediction_text=f'Error: Please check your inputs. Details: {e}')

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
