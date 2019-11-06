from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, MetaData, Table
import json

engine = create_engine('mysql://root@localhost:3306/SimpleStore', convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)
files = Table('files', metadata, autoload=True)
permissions = Table('permissions', metadata, autoload=True)

con = engine.connect()



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/api")
def index():
    command_desc = {
	"-u" : "This signifies that the username follows.",
	"-p" : "The password should follow the -p command.",
	"-extract" : "Following extract there should be a list of at least 1 file to be retrieved from the cloud on the form '-extract file1 file2 ...'.",
	"-push" : "This should have a list of at least 1 file to be put into the cloud. The format is as follows '-push file1 file2 file3'",
	"-share" : "This should be followed a list of files and then the name of the user that the files should be shared with. Format should follow '-share file1 file2 ... username",
	"-unshare" : "This should be followed a list of files and then the name of the user that the files should be unshared with. Format should follow '-share file1 file2 ... username",
	"-h" : "Opens the help menu. If help is desired for a particular command -h should be followed with the command signature i.e. '-h -push'",
	"-login" : "Should be followed by a username '-u' tag and a password 'p' tag each with corresponding login credentials. If both -u and -p are present the -login command will be signaled implicitly.",
	"-logout" : "Removes stored credentials",
	"-create" : "Indicates a new account should be made with given password and username./",
	"-delete" : "Used with a logged in account. Deletes the account."
    }
    return command_desc

@app.route("/api/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.data)
        username = request.json['username']
        password = request.json['password']
        return {"username": username, "password": password}
    else:
        return "Must POST to this endpoint to login a user."

@app.route("/api/newUser", methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        print(request.data)
        engine.connect().execute(Table('users', metadata, autoload=True).insert(), name=request.json['username'], password=request.json['password'])
        return {"status": "recieved"}
    else:
        return "Must POST to this endpoint to create a user account."

@app.route("/api/deleteUser", methods=['GET', 'POST'])
def deleteUser():
    if request.method == 'POST':
        print(request.data)
        username = request.json['username']
        password = request.json['password']
        return {"username": username, "password": password}
    else:
        return "Must POST to this endpoint to delete a user account."


if __name__ == "__main__":
    app.run(debug=True)
