#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str_param>')
def print_string(str_param):
    print('hello')
    return f"hello"

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(map(str, range(parameter))) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
