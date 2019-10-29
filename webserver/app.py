
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Sailor!'

@app.route('/<username>')
def show_user_docs(username):
#returns the username, will return doc previews the User_id has access to.
    return 'Username: %s' % username

@app.route('/doc/<int:doc_id>')
def show_doc(doc_id):
#returns the doc_id, will return the doc if the user has access. Allow access modification in storage.
    return str(doc_id)

#will download the document from webserver to host machine.
def download_doc(doc_id):
    return True

@app.route('/doc/upload', methods=['GET', 'POST'])
#will recieve POST with username, pass, document path, filename to store for user.
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        static_file.save('/var/www/uploads/sampleFile.txt')

