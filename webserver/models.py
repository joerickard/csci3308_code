from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

users = Table('users', metadata,
    Column('uid', Integer, primary_key=True),
    Column('username', String(255), unique=True),
    Column('password', String(255), unique=True)
)
mapper(User, users)

class File(object):
    query = db_session.query_property()

    def __init__(self, fileName=None, filePath=None):
        self.filePath = filePath
        self.fileName = fileName

    def __repr__(self):
        return '<File %r>' % (self.fileName)

files = Table('files', metadata,
    Column('fid', Integer, primary_key=True),
    Column('fileName', String(255), unique=True),
    Column('filePath', String(255), unique=True)
)
mapper(File, files)

class Permission(object):
    query = db_session.query_property()

    def __init__(self, fileID=None, userID=None):
        self.fileID = fileID
        self.userID = userID

    def __repr__(self):
        return '<Permission %r, %r>' % (self.userID, self.fileID)

permissions = Table('permissions', metadata,
    Column('pid', Integer, primary_key=True),
    Column('fileID', Integer, unique=True),
    Column('userID', Integer, unique=True)
)
mapper(Permission, permissions)