from flask import Flask, request, jsonify
from torch_utils import get_prediction

app = Flask(__name__)

@app.route('/questgen',methods=['POST'])
def questgen():
    if request.method == 'POST':
        file = request.files.get('file')

        # try:
        
        data = file.read()
        prediction = get_prediction(data)
        return prediction

        # except:
        #     return jsonify({'error': 'error during prediction'})


