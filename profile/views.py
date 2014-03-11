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

from flask.ext.babel import gettext as _
from jinja2 import TemplateNotFound

from prphoto import bcrypt
from prphoto import db

from .models import Profile
from user.models import User
from utils.const import PASSWORD_KEYWORD
from utils.const import USER_KEY
from utils.login import login_required

profile = Blueprint('profile', __name__, template_folder = 'templates')

@profile.route('/myprofile/')
@login_required
def my_profile():
    try:
        profile = Profile.get_by_userid(session['user_id'])
        user = User.get_user_by_id(session['user_id'])
        
        if profile and profile[0]:
            nickname = profile[0].nickname
            location = profile[0].location
        else:
	        nickname = ''
	        location = ''
        
        return render_template('profile_index.html',
                               user = user,
                               nickname = nickname,
                               location = location
                               )
    except:
        traceback.print_exc()

@profile.route('/update_profile', methods=['POST'])
def update_profile():
    """
    Update the user profile and return the updated value
    """
    db.session.begin(subtransactions = True)
    
    try:
        update_keys = ['nickname',
                       'location',
                       ]
        back_val = ''
        profile = Profile.get_by_userid(session['user_id'])
        
        for key in update_keys:
            if request.form.has_key(key) and len(profile) > 0:
                setattr(profile[0], key, request.form.getlist(key)[0])
                db.session.add(profile[0])
                db.session.commit()
                
                back_val = getattr(profile[0], key)
                break
            elif request.form.has_key(key) and len(profile) == 0:
                print 'x' * 20, '\n', key
                profile = Profile()
                user = User.get_user_by_id(session['user_id'])
                profile.user = user
                
                setattr(profile, key, request.form.getlist(key)[0])
                db.session.add(profile)
                db.session.commit()
                
                back_val = getattr(profile, key)
                break
                
        return back_val
    except:
        db.session.rollback()
        traceback.print_exc()

@profile.route('/update_user', methods=['POST'])
def update_user():
    """
    Update the user's password
    """
    db.session.begin(subtransaction = True)
    
    try:
        back_val = {}
        if request.form.has_key(PASSWORD_KEYWORD):
            user = User.get_user_by_id(session['user_id'])
            user.password = bcrypt.generate_password_hash(request.form.getlist(PASSWORD_KEYWORD)[0])
            
            db.session.add(user)
            db.session.commit()
            
            back_val = request.form.getlist(PASSWORD_KEYWORD)[0]
        
        return len(return_val) * '*'
    except:
        db.session.rollback()
        traceback.print_exc()
