from flask import Flask, request, jsonify
import json

from app.mcq_generation import MCQGenerator

app = Flask(__name__)

MCQ_Generator = MCQGenerator()


@app.route("/questgen", methods=["POST"])
def questgen():

    payload = json.loads(request.data)
    text = payload['content']
    count = 5 
    
    questions = MCQ_Generator.generate_mcq_questions(text, count)
    result = list(map(lambda x: x.__dict__, questions))

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, port=5000)


