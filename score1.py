import json
import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    # Load the model from the registered model in the workspace
    model_path = Model.get_model_path('TextModel')
    model = joblib.load(model_path)

def run(data):
    try:
        # Parse the input data
        data = json.loads(data)
        # Assuming input data is a JSON array of feature arrays
        input_data = np.array(data['data'])
        
        # Make prediction
        predictions = model.predict(input_data)
        
        # Convert predictions to a list
        result = predictions.tolist()
        
        # Return the result as JSON
        return json.dumps({"result": result})
    except Exception as e:
        return json.dumps({"error": str(e)})
