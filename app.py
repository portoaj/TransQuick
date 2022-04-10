from flask import Flask, render_template, request
from summarize import summarize

import asyncio
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    input = request.data.decode('UTF-8')
    output = asyncio.run(summarize(input))
    return {'summary': output}

if __name__ == '__main__':
    app.run(debug=True)