# coding=utf-8
#!/usr/bin/env python

from flask import flash
from flask import redirect
from flask import session

__all__ = ['login_required']

def login_required(fn):
    def decorated_view(*args, **kwargs):
        if 'user_id' not in session.keys():
            flash('Please login first.')
            return redirect('/')
        return fn(*args, **kwargs)
    return decorated_view
