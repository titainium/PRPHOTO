#coding=utf-8
#!/usr/bin/env python

from flask.ext.wtf import Field
from flask.ext.wtf.html5 import EmailInput
from flask.ext.wtf import PasswordInput

__all__ = ['LoginPwdField', 'LoginUserField', 'UserNameField', 'PwdField']

class UserNameInput(EmailInput):
    def __init__(self, label = None, validators = None):
        super(UserNameInput, self).__init__()
        self.label = label
        self.validators = validators
    
    def __call__(self, field, **kwargs):
        kwargs['class'] = 'input-block-level'
        kwargs['placeholder'] = 'Email address'
        kwargs['value'] = ''
        kwargs['data-required'] = 'true'
        kwargs['data-describedby'] = "email-description"
        kwargs['data-description'] = 'email'
        
        return super(UserNameInput, self).__call__(field, **kwargs)

class LoginUserInput(EmailInput):
    def __init__(self, label = None, validators = None):
        super(LoginUserInput, self).__init__()
        self.label = label
        self.validators = validators
    
    def __call__(self, field, **kwargs):
        kwargs['class'] = 'span2'
        kwargs['placeholder'] = 'Email address'
        kwargs['value'] = ''
        kwargs['data-required'] = 'true'
        kwargs['data-describedby'] = "email-description"
        kwargs['data-description'] = 'email'
        
        return super(LoginUserInput, self).__call__(field, **kwargs)

class PwdInput(PasswordInput):
    def __init__(self, label = None, validators = None):
        super(PwdInput, self).__init__()
        self.label = label
        self.validators = validators
        self.input_type = 'password'
    
    def __call__(self, field, **kwargs):
        kwargs['class'] = 'input-block-level'
        kwargs['placeholder'] = 'Password'
        kwargs['value'] = ''
        kwargs['data-required'] = 'true'
        kwargs['data-describedby'] = "pwd-description"
        kwargs['data-description'] = 'password'
        
        return super(PwdInput, self).__call__(field, **kwargs)

class LoginPwdInput(PasswordInput):
    def __init__(self, label = None, validators = None):
        super(LoginPwdInput, self).__init__()
        self.label = label
        self.validators = validators
        self.input_type = 'password'
    
    def __call__(self, field, **kwargs):
        kwargs['class'] = 'span2'
        kwargs['placeholder'] = 'Password'
        kwargs['value'] = ''
        kwargs['data-required'] = 'true'
        kwargs['data-describedby'] = "pwd-description"
        kwargs['data-description'] = 'password'
        
        return super(LoginPwdInput, self).__call__(field, **kwargs)

class UserNameField(Field):
    widget = UserNameInput()

class LoginUserField(Field):
    widget = LoginUserInput()

class PwdField(Field):
    widget = PwdInput()

class LoginPwdField(Field):
    widget = LoginPwdInput()
