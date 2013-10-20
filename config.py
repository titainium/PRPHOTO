#coding=utf-8
#!/usr/bin/env python

class ConfigObj(object):
    BABEL_DEFAULT_LOCALE = 'en'
    DEBUG = True
    SECRET_KEY = 'FORM_SECRET'
    UPLOAD_FOLDER = '/tmp/prphoto/media' and DEBUG or '/var/prphoto/media'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

