from flask import Flask, request, render_template
from flask_restful import Resource, Api
import json

UPLOAD_FOLDER = '/Upload/'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/api/login", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return username + ':' + password
    else:
        return "Hello Sailor!"


if __name__ == "__main__":
    app.run(debug=True)
