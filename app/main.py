from flask import Flask, request, jsonify
from torch_utils import get_prediction
import json

app = Flask(__name__)

def preprocess_text(text):
    return text.replace('\t',' ').replace('\n',' ')

def filter_length_answers(json_result):
    result = []
    for qa_pair in json_result:
        lenght_of_answer = len(qa_pair["answer"]) 
        if(lenght_of_answer> 30):
            continue
        result.append(qa_pair)
    return result

@app.route('/questgen',methods=['GET','POST'])
def questgen():
    if request.method == 'POST':
        file = request.json
        content = file['json_payload']['content']
        data = preprocess_text(content)

        try:
            prediction = get_prediction(data)
            result = filter_length_answers(prediction)
            return json.dumps(result)

        except:
            return jsonify({'error': 'error during prediction'})

# print(get_prediction('Joanna is 24 years old and she is very kind.'))


