#coding=utf-8
#!/usr/bin/env python

import traceback

from flask import abort
from flask import Blueprint
from flask import flash
from flask import g
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session

from prphoto import bcrypt
from prphoto import db

from .forms import LoginForm
from .models import User

from utils.login import login_required

user = Blueprint('user', __name__, template_folder = 'templates')

@user.route('/', methods = ['GET'])
def index():
    login_form = LoginForm()
    return render_template('user_index.html', login_form = login_form)

@user.route('/register', methods = ['GET'])
def register():
    return jsonify({})

@user.route('/register', methods = ['POST'])
def save_register():
    db.session.begin(subtransactions = True)
    
    if not request.json or not 'username' in request.json:
        abort(400)
        
    try:
        exist_user = User.search_by_name(request.json['username'])
        
        if exist_user.count() > 0:
            return jsonify({'error_message': 'The username has registerd.'})
        else:
            user = User(request.json['username'], bcrypt.generate_password_hash(request.json['password']))
            
            db.session.add(user)
            db.session.commit()
            
            return jsonify({'ok_message': 'User registered success.'})
    except:
        db.session.rollback()
        traceback.print_exc()

@user.route('/login', methods = ['POST'])
def login():
    """
    login method, add user_id into session.
    """
    try:
        exist_user = User.search_by_name(request.json['username'])
        
        if exist_user.count() > 0 and bcrypt.check_password_hash(exist_user[0].password, request.json['password']):
            session['user_id'] = exist_user[0].id
            
            return jsonify({'ok_message': 'Login success!'})
        else:
            return jsonify({'error_message': "Sorry, but you could not log in."})
    except:
        traceback.print_exc()

@user.route("/logout", methods=['GET'])
@login_required
def logout():
    """
    logout method, remove the user_id out of session.
    """
    session.pop('user_id', None)
    return jsonify({})
