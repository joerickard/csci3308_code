from flask import Flask, request, send_from_directory, send_file, render_template
from flask_restful import Resource, Api
from database import db_session
from models import User, File, Permission
import json
import os

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/api")
def index():
    command_desc = {
    "-u" : "This signifies that the username follows.",
    "-p" : "The password should follow the -p command.",
    "-extract" : "Following extract there should be a list of at least 1 file to be retrieved from the cloud on the form '-extract file1 file2 ...'.",
    "-push" : "This should have a list of at least 1 file to be put into the cloud. The format is as follows '-push file1 file2 file3'",
    "-share" : "This should be followed a list of files and then the name of the user that the files should be shared with. Format should follow '-share file1 file2 ... username",
    "-unshare" : "This should be followed a list of files and then the name of the user that the files should be unshared with. Format should follow '-unshare file1 file2 ... username",
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
        q = db_session().query(User).filter(User.username == username).first()
        if (q and q.password == password):
            return {"method": "login", "username": username, "password": password, "status": "recieved", "loggedin":True}
        else:
            return {"method": "login", "username": username, "password": password, "status": "recieved", "loggedin":False}
    else:
        return render_template('login.html')


@app.route("/api/newUser", methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        print(request.data)
        username = request.json['username']
        password = request.json['password']
        u = User(username, password)
        q = db_session().query(User).filter(User.username == username).count()
        if (q == 0):
            connection = db_session()
            connection.add(u)
            connection.commit()
            return {"method": "newUser", "username": username, "password": password, "status": "recieved", "created": True}
        else:
            return {"method": "newUser", "username": username, "password": password, "status": "recieved", "created": False}

    else:
        return render_template('create_an_acount.html')

@app.route("/api/deleteUser", methods=['GET', 'POST'])
def deleteUser():
    if request.method == 'POST':
        print(request.data)
        username = request.json['username']
        password = request.json['password']
        connection = db_session()
        q = db_session().query(User).filter(User.username == username).first()

        ident = None
        if (q and q.password == password):
            ident = q.uid
        if (ident != None):
            connection.query(User).filter(User.uid == ident).delete()
            connection.commit()
            return {"method": "deleteUser", "username": username, "password": password, "status": "recieved", "deleted": True}
        else:
            return {"method": "deleteUser", "username": username, "password": password, "status": "recieved", "deleted": False}
    else:
        return "Must POST to this endpoint to delete a user account."

@app.route("/api/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print('f:', f)

        resp = json.load(request.files['json'])
        print('resp:' ,resp)

        connection = db_session()
        userTableEntry = connection.query(User).filter(User.username == resp['username']).first()
        filePath = './webserver/files/'+f.filename
        if (len(connection.query(File).filter(File.filepath == filepath).first()) == 0):
            newFile = File(f.filename, filePath)
            connection.add(newFile)
            connection.commit()

        fileTableEntry = connection.query(File).filter(File.filepath == filePath).first()
        newPermission = Permission(fileTableEntry.fid, userTableEntry.uid)
        connection.add(newPermission)
        connection.commit()

        f.save(filePath)
        return {"status": "recieved"}
    else:
        return "Must POST to this endpoint to delete a user account."

@app.route("/api/download", methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        r = request.json
        file = r['file']
        connection = db_session()
        uid = connection.query(User.uid).filter(User.username == r['username'], User.password == r['password']).first()
        fid = connection.query(File.fid).filter(File.filename == file).first()
        if (uid is not None and fid is not None):
            if (connection.query(Permission).filter(Permission.fid == fid[0], Permission.uid == uid[0]).first() is not None):
                file = connection.query(File.filename).filter(File.fid == fid[0]).first()[0]
                return send_file(os.path.dirname(os.path.abspath(__file__)) + '/files/' + file,attachment_filename=file,as_attachment=True)

        return {'status':False}
    else:
        return "Must POST to this endpoint to delete a user account."

@app.route("/api/share", methods=['GET', 'POST'])
def share():
    if request.method == 'POST':
        r = request.json
        print(r)
        connection = db_session()
        # Get relevant user ids
        orig_uid = connection.query(User.uid).filter(User.username == r['username']).first()
        recip_uid = connection.query(User.uid).filter(User.username == r['recipient']).first()
        file_id = connection.query(File.fid).filter(File.filename == r['file']).first()
        if (file_id is not None):
            file_permissions = connection.query(Permission).filter(Permission.fid == file_id).all()
            for f in file_permissions:

                if (f.uid == orig_uid[0]):
                    connection.add(Permission(file_id, recip_uid))
                    connection.commit()
                    return {"status": True}


        return {"status": False}
    else:
        return "Must POST to this endpoint to delete a user account."

@app.route("/api/unshare", methods=['GET', 'POST'])
def unshare():
    if request.method == 'POST':
        r = request.json
        print(r)
        connection = db_session()
        # Get relevant user ids
        orig_uid = connection.query(User.uid).filter(User.username == r['username']).first()
        recip_uid = connection.query(User.uid).filter(User.username == r['recipient']).first()
        file_id = connection.query(File.fid).filter(File.filename == r['file']).first()
        if (file_id is not None and recip_uid is not None):
            file_permissions = connection.query(Permission).filter(Permission.fid == file_id).all()
            b = False
            for f in file_permissions:

                if (f.uid == orig_uid[0]):
                    b = True
                    break

            if (b):
                for f in file_permissions:
                    if (f.uid == recip_uid[0]):
                        pid = connection.query(Permission.pid).filter(Permission.fid == file_id[0], Permission.uid == recip_uid[0]).all()
                        if (pid is not None):
                            connection.query(Permission).filter(Permission.pid == pid[0]).delete()
                            connection.commit()
                            return {"status": True}

        return {"status": False}
    else:
        return "Must POST to this endpoint to delete a user account."

if __name__ == "__main__":
    app.run(debug=True)