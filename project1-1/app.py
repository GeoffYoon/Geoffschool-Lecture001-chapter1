from flask import Flask
from flask import request
from flask import send_file
import json
import util
import operation

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('static/index.html')

@app.route('/compute', methods = ['POST'])
def compute():
    params = json.loads(request.get_data())
    operands = params.get('operands')
    operators = params.get('operators')

    operator_counts = len(operators)
    for i in range(operator_counts):
        operator = operators.pop()
        operand2 = util.stringToNumber(operands.pop())
        operand1 = util.stringToNumber(operands.pop())
        operands.append(operation.binaryOperate(operand1, operand2, operator))

    answer = operands.pop();

    return {'message' : 'success', 'answer' : answer}

if __name__ == '__main__':  # pragma: no cover
    app.run(port=8080)