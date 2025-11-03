# app.py

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Insecure use of debug mode in production (B703)
    if app.debug:
        return "Debug mode is ON. This is a security risk in production."
    return "Welcome to the secure Flask app!"

@app.route('/echo')
def echo():
    user_input = request.args.get('input', '')
    # Potential XSS vulnerability if user_input is not properly escaped (B308)
    return render_template_string(f"<h1>You entered: {user_input}</h1>")

@app.route('/eval')
def evaluate():
    code_to_execute = request.args.get('code', '')
    # Insecure use of eval() (B307)
    try:
        result = eval(code_to_execute)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    # Insecure use of app.run with debug=True in production (B703)
    app.run(debug=True, host='0.0.0.0', port=5000)
