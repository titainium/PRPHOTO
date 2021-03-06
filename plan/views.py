#coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""
import os
import time
import json
from hashlib import md5
import pickle
import traceback
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

from jinja2 import TemplateNotFound

from .models import Plan
from profile.models import Profile
from user.models import User
from utils.const import PASSWORD_KEYWORD
from utils.const import USER_KEY
from utils.login import login_required
from utils.weight import *
from config import fs

plan = Blueprint('plan', __name__, template_folder = 'templates')

# 上传图片时用到的配置信息
# 以后统一放到configs中去
base_path      = '/tmp/prphoto/original'
thum_base_path = '/tmp/prphoto/thum'
allow_files    = ['gif', 'jpg', 'png']
thumb_max_size = (250,250)

#@plan.route('/grid/<id>',methods=['GET'])
#def gridfile(id):
#    oid = ObjectId(id)
#    content = fs.get(oid).read()

#    return content

#@plan.route('/plan/uploader',methods=['POST','GET'])
#def uploader():
#    file        = request.files['Filedata']
#    
#    if request.method == 'POST':
#        #因为uploadify 上传不能自动带cookie，see http://www.uploadify.com/documentation/uploadify/using-sessions-with-uploadify/
#        from flask import current_app as app
#        from flask import _request_ctx_stack
#        request.cookies = {app.config['SESSION_COOKIE_NAME']: request.form.to_dict()['flask_session_cookie_name']}
#        _request_ctx_stack.top.session = app.open_session(request)

#        file        = request.files['Filedata']
#        suf_fix     = file.filename.rsplit('.', 1)[1].lower()
#        
#        if file and suf_fix in allow_files:
#            # save original
#            md5_key     = md5('{}{}'.format(time.time(),file.name)).hexdigest()
#            dir1        = md5_key[0:2]
#            dir2        = md5_key[2:4]
#            dir3        = md5_key[4:6]
#            file_path   = os.path.join(base_path,dir1,dir2,dir3)
#            if not os.path.exists(file_path):
#                os.makedirs(file_path)

#            file_name   = '{}.{}'.format(md5_key,suf_fix)
#            full_path   = os.path.join(file_path,file_name)
#            file.save(full_path)

#            # mark
#            #session['sample_images'] += '{},'.format(full_path)
#            
#            # save thumb
#            file_path   = os.path.join(thum_base_path,dir1,dir2,dir3)
#            if not os.path.exists(file_path):
#                os.makedirs(file_path)
#            thum_full_path   = os.path.join(file_path,file_name)
#            try:
#                im = Image.open(full_path)
#            except IOError,e:
#                return '0', 400
#            
#            try:
#                im.thumbnail(thumb_max_size,Image.ANTIALIAS)
#                im.convert('RGB').save(thum_full_path,'jpeg',quality=100)
#            except Exception,e:
#                return 'can not convert:{}'.format(e.message), 400
#            else:
#                return '{}/{}/{}/{}'.format(dir1,dir2,dir3,file_name)

#    return 'post required', 400

#@plan.route('/plan/',methods=['GET'])
#def plan_listing():
#    ad_plans = Plan.get_ad_plans()
#    user_plans = []
#    for init_plan in Plan.get_init_plans(ObjectId(session['user_id'])):
#        if init_plan not in user_plans:
#            user_plans.append(init_plan)
#    for master_plan in Plan.get_master_plans(ObjectId(session['user_id'])):
#        #if master_plan not in 
#        master_plans.append(master_plan)
#    for member_plan in Plan.get_member_plans(ObjectId(session['user_id'])):
#        member_plans.append(member_plan)
#    print '*' * 20, '\n', type(init_plans)
#    user_plans = list(set(init_plans) | set(master_plans) | set(member_plans))
#    
#    return render_template('plan_index.html')

#def format_user_fields(data,user_id):
#    profile   = Profile.get_profile(user_id=user_id)
#    for key in ['master-list','initiator-list','member-list']:
#        if type(data.get(key)) in  [str,unicode]:
#            data[key] += u',{}'.format(profile['profile']['nick_name'])
#        else:
#            data[key] = u'{}'.format(profile['profile']['nick_name'])
#    return data

#@plan.route('/plan/add', methods=['POST','GET'])
#@login_required
#def plan_add():
#    if request.method == 'GET':
#        #session['sample_images'] = ''
#        return render_template('plan_add.html',**locals())
#    
#    # clear data
#    data = request.form.to_dict()
#    user_id = ObjectId(session['user_id'])
#    data = format_user_fields(data,user_id)

#    # valid sample_images
#    sample_images = data.get('photosPath','').split(';')
#    if len(sample_images) <1 or len(sample_images) >4:
#        flash('需要1到4张样例图片')
#        return render_template('plan_add.html',**data)

#    # save pic
#    samples = []
#    for relative_path in sample_images:
#        if not relative_path:continue
#        tmp_file_path = os.path.join(base_path,relative_path)
#        with open(tmp_file_path) as f:
#            # 存储图片文件到mongodb中，并返回一个oid
#            # 将oid保存到samples字段中，以便显示
#            oid = fs.put(f,content_type="image/jpeg",filename=md5(tmp_file_path).hexdigest())
#            samples.append(oid)

#    validated,message = Plan.validate(data)
#    if validated:
#        new_id = ObjectId()
#        cleared_data = Plan.clear_data(data)
#        cleared_data['samples'] = samples
#        cleared_data['starts_at'] = datetime.now()
#        cleared_data['ends_at'] = ''
#        cleared_data['location'] = ''
#        cleared_data['is_public'] = True
#        cleared_data['classes'] = 'general'
#        cleared_data['weight'] = .1
#        res = Plan().save(new_id,cleared_data)
#        
#        if res:
#            return redirect('/plan/{}'.format(str(new_id)))
#        return str(res)
#    else:
#        flash(message)
#        return render_template('plan_add.html',**data)

#@plan.route('/plan/update/<pid>', methods=['POST','GET'])
#@login_required
#def plan_update(pid):
#    pid = ObjectId(pid)
#    plan = Plan.get_detail(pid)

#    # get request
#    if request.method == 'GET':
#        if plan:
#            return render_template('plan_update.html',plan=plan)
#        else:
#            abort(404)
#        return render_template('plan_add.html',**locals())
#    
#    # clear data
#    data = request.form.to_dict()
#    user_id = ObjectId(session['user_id'])
#    data = format_user_fields(data,user_id)

#    sample_images = filter(lambda x:x, data.get('photosPath','').split(';'))
#    if len(sample_images) <1 or len(sample_images) >4:
#        flash(u'需要1到4张样例图片')
#        return render_template('plan_update.html',plan=plan)


#    # save pic
#    samples = []
#    for relative_path in sample_images:
#        # 如果relative_path是一个objectid,说明是已经上传过的旧图片
#        # 这里直接跳过不处理
#        if type(relative_path) is ObjectId:continue
#        
#        # 如果relative_path 是一个文件系统的相对路径
#        # 则将文件读取写入mongdb，并将得到的oid放入plan['samples']中
#        tmp_file_path = os.path.join(base_path,relative_path)
#        if not os.path.isfile(tmp_file_path):
#            #samples.remove(relative_path)
#            continue

#        with open(tmp_file_path) as f:
#            # 存储图片文件到mongodb中，并返回一个oid
#            # 将oid保存到samples字段中，以便显示
#            oid = fs.put(f,content_type="image/jpeg",filename=md5(tmp_file_path).hexdigest())
#            #samples.remove(relative_path)
#            samples.append(oid)

#    
#    validated,message = Plan.validate(data)
#    if validated:
#        # update recored
#        cleared_data = Plan.clear_data(data)
#        cleared_data['samples'] = samples
#        cleared_data['weight'] = plan_weight(plan['classes'])
#        res = Plan().save(pid,cleared_data)
#        if res:
#            return redirect('/plan/{}'.format(str(pid)))
#        return str(res)
#    else:
#        flash('error',message)
#        return render_template('plan_update.html',**data)


#@plan.route('/plan/<pid>', methods=['GET'])
#def plan_detail(pid):
#    pid = ObjectId(pid)
#    plan = Plan.get_detail(pid)
#    if plan:
#        #img = fs.get(plan['samples'][0]).read()
#        return render_template('plan_detail.html',plan=plan)
#    
#    abort(404)

#@plan.route('/plan/check_user', methods=['POST', 'GET'])
#def check_user():
#    """
#    the user auto complete ajax function.
#    """
#    users = Profile.get_fuzzy_results(request.args.get('nick_name'))
#    
#    if users:
#        return json.dumps([user['profile']['nick_name'] for user in users])
#    else:
#        return json.dumps([''])

#if __name__ == '__main__':
#     with plan.test_request_context():
#         print url_for('plan_add')
