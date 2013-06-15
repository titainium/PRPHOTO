#coding=utf-8
#!/usr/bin/env python

import traceback

from flask import Blueprint
from flask import abort
from flask import flash
from flask import g
from flask import jsonify
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
        profile = Profile.get_profile(session['user_id'])
        user = User.get_user_by_id(session['user_id'])
        
        return render_template('profile_index.html',
                               profile = profile,
                               user = user
                               )
    except:
        traceback.print_exc()

@profile.route('/update_profile', methods=['POST'])
def update_profile():
    """
    Update the user profile and return the updated value
    """
    try:
        profile_params = {'nick_name': None,
                          'location': None,
                          'user_id': session['user_id']
                         }
        back_val = ''
        for key in profile_params.keys():
            if request.form.has_key(key):
                profile_params[key] = request.form.getlist(key)[0]
                back_val = request.form.getlist(key)[0]
                print 'x' * 20, '\n', request.form.getlist(key)
        
        profile = Profile(**profile_params)
        profile.save()
        
        print '*' * 20, '\n', back_val
        
        return back_val
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
