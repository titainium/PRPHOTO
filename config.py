#coding=utf-8
#!/usr/bin/env python

class ConfigObj(object):
    BABEL_DEFAULT_LOCALE = 'en'
    DEBUG = True
    UPLOAD_FOLDER = '/tmp/prphoto/media' and DEBUG or '/var/prphoto/media'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    
    #csrf
    WTF_CSRF_SECRET_KEY = 'FORM_SECRET'

    #PostgreSQL config
    #SQLALCHEMY_DATABASE_URI = 'postgres://jzp:123456@localhost/mydb'
    SQLALCHEMY_ECHO = True
    
    # static path
    STATIC_PATH = '../../static/'

    # session & cookie
    SECRET_KEY = 'whatafuckingday'
    SESSION_COOKIE_NAME = 'prphoto_session'
    SESSION_COOKIE_PATH = '/'
    SESSION_COOKIE_HTTPONLY = False

