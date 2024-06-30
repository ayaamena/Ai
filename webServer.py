import json
from flask import Flask, request, jsonify

from webPage import MrX7_GetPredictions

app = Flask(__name__)

# Assuming your model loading and prediction code is here
# ...

# MrX7 Help: This is a testing GET method to return prediction based on
# an already defined image in the server folder.
@app.route('/predict', methods=['GET'])
def predictGET():
    if request.method == 'GET':
        # Return predictions
        result = MrX7_GetPredictions(None)
        return jsonify({'predictions': json.dumps(str(result[0][0]))})

# Same as above but with POST method to add and specify your own IMAGE.
@app.route('/predict', methods=['POST'])
def predictPOST():
    if request.method == 'POST':
        # Return predictions
        request.files['image'].save('cp_' + request.files['image'].filename )
        result = MrX7_GetPredictions('cp_' + request.files['image'].filename)
        return jsonify({'predictions': json.dumps(str(result))})

@app.route('/endpoint', methods=['GET'])
def get_endpoint():
    if request.method == 'GET':
        # Assuming your endpoint is stored in a variable named 'endpoint'
        endpoint = "your_model_endpoint_here"
        return jsonify({'endpoint': endpoint})

if __name__ == '__main__': 
    app.run(debug=True,host="0.0.0.0", port=80)