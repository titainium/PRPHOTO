#coding=utf-8
#!/usr/bin/env python3

from inspect import getmembers
from inspect import isfunction

import os

from flask import Flask
from flask import send_from_directory
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy

from utils import filters
from utils.const import HOST, PORT

import config

app = Flask(__name__)
app.config.from_object('config.ConfigObj')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

#add customized jinja filters
cust_filters = {name: function
                  for name, function in getmembers(filters)
                  if isfunction(function)}

app.jinja_env.filters.update(cust_filters)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico',
                               mimetype = 'image/x-icon')

if __name__ == '__main__':
    def register_blueprints(app):
        from user.views import user
        from profile.views import profile
        #from plan.views import plan
    
        app.register_blueprint(user)
        app.register_blueprint(profile)
        #app.register_blueprint(plan)

    register_blueprints(app)
    app.run(host = HOST, port = PORT)
