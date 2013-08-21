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

from bson import ObjectId
from flask.ext.babel import gettext as _
from jinja2 import TemplateNotFound

from .models import Profile
from user.models import User
from utils.const import PASSWORD_KEYWORD
from utils.const import USER_KEY
from utils.login import login_required

profile = Blueprint('profile', __name__, template_folder = 'templates')

@profile.route('/myprofile')
@login_required
def my_profile():
    try:
        #profile = Profile.get_profile(session['user_id'])
        user = User.get_user_by_id(ObjectId(session['user_id']))
        
        if user.has_key(USER_KEY):
	  nick_name = user[USER_KEY]['nick_name']
	  location = user[USER_KEY].get('location','unknow')
	else:
	  nick_name = ''
	  location = ''
        
        return render_template('profile_index.html',
                               #profile = profile,
                               user = user,
                               nick_name = nick_name,
                               location = location
                               )
    except:
        traceback.print_exc()

@profile.route('/update_profile', methods=['POST'])
def update_profile():
    """
    Update the user profile and return the updated value
    """
    try:
        update_keys = ['nick_name',
                       'location',
                       ]
        #profile_params = {'user_id': session['user_id'],}
        back_val = ''
        for key in update_keys:
            if request.form.has_key(key):
                back_val = Profile.update_profile(session['user_id'], **{key: request.form.getlist(key)[0]})
                back_val = request.form.getlist(key)[0]
        
        #profile = Profile(**profile_params)
        #profile.save()
        
        return back_val
    except:
        traceback.print_exc()

@profile.route('/update_user', methods=['POST'])
def update_user():
    """
    Update the user's password
    """
    try:
        back_val = {}
        if request.form.has_key(PASSWORD_KEYWORD):
            back_val = User.update_user_password(user_id = ObjectId(session['user_id']), password = request.form.getlist(PASSWORD_KEYWORD)[0])
        
        if back_val and not back_val['err']:
            return_val = request.form.getlist(PASSWORD_KEYWORD)[0]
        
        
        return len(return_val) * '*'
    except:
        traceback.print_exc()
