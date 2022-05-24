# import contextlib
from flask import Flask, request
# from flask_cors import CORS, cross_origin
import json

# from app.models.question import Question
from app.mcq_generation import MCQGenerator

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

MCQ_Generator = MCQGenerator()

# @app.route("/")
# @cross_origin()
# def hello():
#     return json.dumps('Hello to Leaf!')


@app.route("/questgen", methods=["POST"])
# @cross_origin()
def questgen():
    #postman
    # text = request.form['text']

    payload = json.loads(request.data)['json_payload']
    text = payload['content']
    count = 7 # if payload['count'] == '' else int(payload['count'])
    
    questions = MCQ_Generator.generate_mcq_questions(text, count)
    result = list(map(lambda x: json.dumps(x.__dict__), questions))

    return json.dumps(result)


# if __name__ == '__main__':
#     from werkzeug.serving import run_simple
#     run_simple('localhost', 9002, app)


