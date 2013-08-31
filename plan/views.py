#coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

import json
import traceback
import mock
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

@plan.route('/plan',methods=['GET'])
def plan_listing():
    return render_template('plan_index.html')


@plan.route('/plan/add', methods=['POST','GET'])
@login_required
def plan_add():
    if request.method == 'GET':
        return render_template('plan_add.html',**locals())
    
    # clear data
    data = request.form.to_dict()
    validated,message = Plan.validate(data)
    if validated:
        new_id = ObjectId()
        cleared_data = Plan.clear_data(data)
        res  = Plan().save(new_id,cleared_data)
        if res:
            return redirect('/plan/{}'.format(str(new_id)))
        return str(res)
    else:
        flash('error',message)
        return render_template('plan_add.html',**data)

@plan.route('/plan/<pid>', methods=['GET'])
def plan_detail(pid):
    # mock
    #pid = ObjectId(pid)
    plan = Plan.get_detail(pid)
    return str(plan)
    if plan:
        return render_template('plan_detail.html',locals())
    
    abort(404)

@plan.route('/plan/check_user', methods=['POST', 'GET'])
def check_user():
    """
    the user auto complete ajax function.
    """
    user = Profile.check_exists(request.args.get('nick_name'))
    
    if user:
        return json.dumps([user['profile']['nick_name']])
    else:
        return json.dumps([''])

if __name__ == '__main__':
     with plan.test_request_context():
         print url_for('plan_add')
