from flask import Flask, request, jsonify
import json
from .package.IntStream import IntStream
# from .config import *

leila_api=IntStream("0VJu0qb6zX5dxeios940p4hDChi15tcS8mnQ9YmS", "https://dev.jetty.com/v1/quote/quiz/next/leila1", "https://dev.jetty.com/v1/quote/quiz/next/leila2")

app = Flask(__name__)

@app.route('/')
def index():
    response = leila_api.insert_values()
    return jsonify(response)

if __name__ == '__main__':
    # This is used when running locally.
    app.run(host='127.0.0.1', port=8080, debug=True)
