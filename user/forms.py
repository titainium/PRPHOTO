#coding=utf-8
#!/usr/bin/env python

import re

from flask.ext.wtf import Form
from flask.ext.wtf import Required
from flask.ext.wtf import TextField

from widgets import LoginPwdField
from widgets import LoginUserField
from widgets import PwdField
from widgets import UserNameField

__all__ = ['LoginForm', 'RegisterForm']

class RegisterForm(Form):
    user_name = UserNameField("User Name", validators=[Required()])
    password = PwdField("Password", validators=[Required()])
    
    def validate(self):
        rv = Form.validate(self)

        if not rv:
            return False

        username = self.user_name.data
        email = re.compile('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        
        if not username or len(username) == 0:
            self.user_name.errors.append('Please input email address as username')

            return False

        if not email.match(username):
            self.user_name.errors.append('The email address is in a wrong format')

            return False

        return True

class LoginForm(Form):
    user_name = LoginUserField("User Name", validators=[Required()])
    password = LoginPwdField("Password", validators=[Required()])
    
    def validate(self):
        rv = Form.validate(self)

        if not rv:
            return False

        username = self.user_name.data
        email = re.compile('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        
        if not username or len(username) == 0:
            self.user_name.errors.append('Please input email address as username')

            return False

        if not email.match(username):
            self.user_name.errors.append('The email address is in a wrong format')

            return False

        return True

