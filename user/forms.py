# coding=utf-8
#!/usr/bin/env python3

from flask_wtf import Form

from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import length

from .widgets import PREmailInput

__all__ = ['LoginForm']

class LoginForm(Form):
    username = EmailField(label = 'username',
                          validators = [DataRequired(),
                                        Email(),
                                        length(max = 80)
                                        ],
                          widget = PREmailInput()
                          )
    password = PasswordField(label = 'password',
                             validators = [DataRequired()]
                             )
