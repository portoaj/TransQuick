from flask import Flask, render_template, request, jsonify
from summarize import summarize
import sys
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    input = request.data.decode('UTF-8')
    return {'summary': (str(summarize(input)))}

if __name__ == '__main__':
    app.run(debug=True)