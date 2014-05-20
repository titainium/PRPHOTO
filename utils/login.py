# coding=utf-8
#!/usr/bin/env python

from flask import jsonify
from flask import redirect
from flask import session
from functools import wraps


__all__ = ['login_required']

def login_required(fn):
    """
    you can view this:
         http://flask.pocoo.org/docs/patterns/viewdecorators/
    """

    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if 'user_id' not in session.keys():
            return jsonify({'error_message': 'Please login first.'})
        return fn(*args, **kwargs)
    return decorated_view
