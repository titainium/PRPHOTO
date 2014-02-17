#coding=utf-8
#!/usr/bin/env python
import pymongo
from gridfs import GridFS

class ConfigObj(object):
    BABEL_DEFAULT_LOCALE = 'en'
    DEBUG = True
    SECRET_KEY = 'FORM_SECRET'
    UPLOAD_FOLDER = '/tmp/prphoto/media' and DEBUG or '/var/prphoto/media'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"

    #PostgreSQL config
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/prphoto'
    
    #MongoDB address
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DB_NAME = 'prphoto'

    # cookie name 
    SESSION_COOKIE_NAME = 'prphoto_session'
    SESSION_COOKIE_PATH = '/'
    SESSION_COOKIE_HTTPONLY = False

db = getattr(pymongo.MongoClient(ConfigObj.MONGO_HOST, ConfigObj.MONGO_PORT),
        ConfigObj.MONGO_DB_NAME)
fs = GridFS(db)

