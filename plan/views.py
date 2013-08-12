#coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

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
from flaskext.babel import gettext as _
from jinja2 import TemplateNotFound

from .models import Plan
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
    form = PlanForm()
    return render_template('plan_detail.html',locals())

@plan.route('/plan/<pid>', methods=['GET'])
def plan_detail(pid):
    # mock
    Plan = mock.Mock()
    pid = ObjectId(pid)
    plan = Plan.get_detail(pid)
    if plan:
        return render_template('plan_detail.html',locals())
    abort(404)
