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

from flaskext.babel import gettext as _
from jinja2 import TemplateNotFound

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
    try:
        form = RegisterForm()
    
        if request.method == 'POST' and form.validate():
            if User.search_by_name({"username": form.user_name.data}):
                flash("The email address has registered.")
            else:
                user = User(form.user_name.data, form.password.data)
                
                user.save()
                flash("Thank you for your registration! Please log in.")
                
                return redirect('/')

        return render_template('user_register.html', form = form)
    except:
        traceback.print_exc()

@user.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == 'POST' and form.validate():
        if User.check_user(form.user_name.data, form.password.data):
            user = User(form.user_name.data, form.password.data)
            g.user = user
            session['user_id'] = user.get_user_id()
            flash("Logged in!")
            
            return redirect(request.args.get("next") or '/myprofile')
        else:
            flash("Sorry, but you could not log in.")
    
    return render_template('user_index.html', form = form)

@user.route("/logout")
@login_required
def logout():
    g.user = None
    session.pop('user_id', None)
    flash("Logged out.")
    
    return redirect(url_for(".index"))
