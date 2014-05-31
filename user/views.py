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
    register_form = LoginForm()
    
    return render_template('user_index.html',
                            login_form = login_form,
                            register_form = register_form
                            )

@user.route('/register/', methods = ['POST'])
def save_register():
    db.session.begin(subtransactions = True)
        
    try:
        register_form = LoginForm()
        
        if register_form.validate_on_submit():
          exist_user = User.search_by_name(register_form.username.data)
        
          if exist_user:
            flash('The email address has been used, please change another one.')
            
            return redirect('/')
        else:
            user = User(register_form.username.data,
                        bcrypt.generate_password_hash(register_form.password.data)
                        )
            
            db.session.add(user)
            db.session.commit()
            
            flash('User registered success, thank you!')
            
            return redirect('/')
    except:
        db.session.rollback()
        traceback.print_exc()

@user.route('/login/', methods = ['POST'])
def login():
    """
    login method, add user_id into session.
    """
    try:
        login_form = LoginForm()
        
        if login_form.validate_on_submit():
            exist_user = User.search_by_name(login_form.username.data)
        
            if exist_user is not None and bcrypt.check_password_hash(exist_user.password,
                                                                      login_form.password.data):
                session['user_id'] = exist_user.id
            
                return redirect("/")
            else:
                flash("Please check the username and password, and login again!")
                return render_template('user_index.html',
                                login_form = login_form,
                                register_form = LoginForm()
                                )
        
        flash("Please check the username and password, and login again!")
        return render_template('user_index.html',
                                login_form = login_form,
                                register_form = LoginForm()
                                )
    except:
        traceback.print_exc()

@user.route("/logout/", methods=['GET'])
@login_required
def logout():
    """
    logout method, remove the user_id out of session.
    """
    session.pop('user_id', None)
    return redirect('/')
