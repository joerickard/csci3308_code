from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)


@app.route("/api/login", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.data)
        username = request.json['username']
        password = request.json['password']
        return username + ':' + password


if __name__ == "__main__":
    app.run(debug=True)
