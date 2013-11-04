#coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""
import os
import time
import json
import traceback
import mock
from datetime import datetime
from PIL import Image
from hashlib import md5
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

from .models import Plan
from profile.models import Profile
from user.models import User
from utils.const import PASSWORD_KEYWORD
from utils.const import USER_KEY
from utils.login import login_required

plan = Blueprint('plan', __name__, template_folder = 'templates')


@plan.route('/plan/uploader',methods=['POST','GET'])
def uploader():
    base_path      = '/tmp/prphoto/original'
    thum_base_path = '/tmp/prphoto/thum'
    allow_files    = ['GIF', 'gif', 'JPG', 'jpg', 'PNG', 'png']
    thumb_max_size = (250,250)
    file        = request.files['Filedata']
    
    if request.method == 'POST':
        file        = request.files['Filedata']
        suf_fix     = file.filename.rsplit('.', 1)[1]
        
        if file and suf_fix in allow_files:
            # save original
            md5_key     = md5('{}{}'.format(time.time(),file.name)).hexdigest()
            dir1        = md5_key[0:2]
            dir2        = md5_key[2:4]
            dir3        = md5_key[4:6]
            file_path   = os.path.join(base_path,dir1,dir2,dir3)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name   = '{}.{}'.format(md5_key,suf_fix)
            full_path   = os.path.join(file_path,file_name)
            file.save(full_path)
            
            # save thumb
            file_path   = os.path.join(thum_base_path,dir1,dir2,dir3)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            thum_full_path   = os.path.join(file_path,file_name)
            try:
                im = Image.open(full_path)
            except IOError,e:
                return '0'
            
            try:
                im.thumbnail(thumb_max_size,Image.ANTIALIAS)
                im.convert('RGB').save(thum_full_path,'jpeg',quality=100)
            except Exception,e:
                return 'can not convert:{}'.format(e.message)
            else:
                return '{}/{}/{}/{}'.format(dir1,dir2,dir3,file_name)

    return 'post required'



@plan.route('/plan',methods=['GET'])
def plan_listing():
    return render_template('plan_index.html')


def format_user_fields(data,user_id):
    profile   = Profile.get_profile(user_id=user_id)
    for key in ['master-list','initiator-list','member-list']:
        if type(data.get(key)) in  [str,unicode]:
            data[key] += u',{}'.format(profile['profile']['nick_name'])
        else:
            data[key] = u'{}'.format(profile['profile']['nick_name'])
    return data

@plan.route('/plan/add', methods=['POST','GET'])
@login_required
def plan_add():
    if request.method == 'GET':
        return render_template('plan_add.html',**locals())
    
    # clear data
    data = request.form.to_dict()
    user_id = ObjectId(session['user_id'])
    data = format_user_fields(data,user_id)

    validated,message = Plan.validate(data)
    if validated:
        new_id = ObjectId()
        cleared_data = Plan.clear_data(data)
        res  = Plan().save(new_id,cleared_data)
        if res:
            return redirect('/plan/{}'.format(str(new_id)))
        return str(res)
    else:
        flash(message)
        return render_template('plan_add.html',**data)

@plan.route('/plan/update/<pid>', methods=['POST','GET'])
@login_required
def plan_update(pid):
    pid = ObjectId(pid)
    plan = Plan.get_detail(pid)

    # get request
    if request.method == 'GET':
        if plan:
            return render_template('plan_update.html',plan=plan)
        else:
            abort(404)
        return render_template('plan_add.html',**locals())
    
    # clear data
    data = request.form.to_dict()
    user_id = ObjectId(session['user_id'])
    data = format_user_fields(data,user_id)
    validated,message = Plan.validate(data)
    if validated:
        # update recored
        cleared_data = Plan.clear_data(data)
        res  = Plan().save(pid,cleared_data)
        if res:
            return redirect('/plan/{}'.format(str(pid)))
        return str(res)
    else:
        flash('error',message)
        return render_template('plan_update.html',**data)


@plan.route('/plan/<pid>', methods=['GET'])
def plan_detail(pid):
    pid = ObjectId(pid)
    plan = Plan.get_detail(pid)
    if plan:
        return render_template('plan_detail.html',plan=plan)
    
    abort(404)

@plan.route('/plan/check_user', methods=['POST', 'GET'])
def check_user():
    """
    the user auto complete ajax function.
    """
    users = Profile.get_fuzzy_results(request.args.get('nick_name'))
    
    if users:
        return json.dumps([user['profile']['nick_name'] for user in users])
    else:
        return json.dumps([''])

if __name__ == '__main__':
     with plan.test_request_context():
         print url_for('plan_add')
