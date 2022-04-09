from flask import Flask, request
from summarize import summarize
import sys
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', methods=['POST'])
def result():
    input = request.data.decode('UTF-8')
    return str(summarize(input))

if __name__ == '__main__':
    app.run(debug=True)