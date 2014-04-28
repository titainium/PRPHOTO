#coding=utf-8
#!/usr/bin/env python

import traceback

from flask import Blueprint
from flask import abort
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from flask.ext.babel import gettext as _
from jinja2 import TemplateNotFound

from prphoto import bcrypt
from prphoto import db

from .forms import LoginForm
from .forms import RegisterForm
from .models import User

from utils.login import login_required

user = Blueprint('user', __name__, template_folder = 'templates')

@user.route('/')
def index():
    try:
        form = LoginForm()
        
        return render_template('user_index.html', form = form)
    except TemplateNotFound:
        traceback.print_exc()

@user.route('/register', methods = ['GET', 'POST'])
def register():
    db.session.begin(subtransactions = True)
    
    try:
        form = RegisterForm()
    
        if request.method == 'POST' and form.validate():
            exist_user = User.search_by_name(form.user_name.data)
            
            if exist_user and exist_user[0]:
                flash("The email address has registered.")
            else:
                user = User(form.user_name.data, bcrypt.generate_password_hash(form.password.data))
                
                db.session.add(user)
                db.session.commit()
                flash("Thank you for your registration! Please log in.")
                
                return redirect('/')

        return render_template('user_register.html', form = form)
    except:
        db.session.rollback()
        traceback.print_exc()

@user.route('/login', methods = ['GET', 'POST'])
def login():
    """
    login method, add user_id into session.
    """
    try:
        form = LoginForm()
        
        if request.method == 'POST' and form.validate():
            exist_user = User.search_by_name(form.user_name.data)
            
            if exist_user and exist_user[0] and bcrypt.check_password_hash(exist_user[0].password, form.password.data):
                session['user_id'] = exist_user[0].id
                flash("Logged in!")
            
                return redirect(request.args.get("next") or '/')
            else:
                flash("Sorry, but you could not log in.")
        return render_template('user_index.html', form = form)
    except:
        traceback.print_exc()

@user.route("/logout/")
@login_required
def logout():
    session.pop('user_id', None)
    flash("Logged out.")
    
    return redirect(url_for(".index"))
