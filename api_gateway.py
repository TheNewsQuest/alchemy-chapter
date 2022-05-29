from flask import Flask, request, jsonify
import json

from app.mcq_generation import MCQGenerator

app = Flask(__name__)

@app.route("/questgen", methods=["POST"])
def questgen():
    payload = json.loads(request.data)
    text = payload['content']
    count = 5 # if payload['count'] == '' else int(payload['count'])
    
    questions = MCQ_Generator.generate_mcq_questions(text, count)
    result = list(map(lambda x: x.__dict__, questions))

    return jsonify(result)

if __name__ == '__main__':
    MCQ_Generator = MCQGenerator(is_verbose=True)
    app.run(debug=True, port=9090)


