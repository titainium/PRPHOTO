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

from .models import Profile
from user.models import User
from utils.login import login_required

profile = Blueprint('profile', __name__, template_folder = 'templates')

@profile.route('/myprofile')
@login_required
def my_profile():
    try:
        profile = Profile.get_profile(session['userID'])
        user = User.get_user_by_id(session['userID'])
        
        return render_template('profile_index.html',
                               profile = profile,
                               user = user
                               )
    except:
        traceback.print_exc()

def update_profile(**kw):
    try:
        profile = Profile.get_profile(session['userID'])
        user = User.get_user_by_id(session['userID'])
        
        if 'nick_name' in kw and kw['nick_name']:
            pass
    
        if request.method == 'POST' and form.validate():
            if User.searchByName({"UserName": form.user_name.data}) != 0:
                flash("The email address has registered.")
            else:
                user = User(form.user_name.data, form.password.data)
                
                user.save()
                flash("Thank you for your registration! Please log in.")
                
                return redirect('/')

        return render_template('register.html', form = form)
    except:
        traceback.print_exc()

"""@user.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == 'POST' and form.validate():
        if User.checkUser(form.user_name.data, form.password.data):
            user = User(form.user_name.data, form.password.data)
            g.user = user
            session['userID'] = user.getUserID()
            flash("Logged in!")
            
            return redirect(request.args.get("next") or url_for(".index"))
        else:
            flash("Sorry, but you could not log in.")
    
    return render_template('index.html', form = form)

@user.route("/logout")
@login_required
def logout():
    g.user = None
    session.pop('userID', None)
    flash("Logged out.")
    
    return redirect(url_for(".index"))"""
