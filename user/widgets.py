# coding=utf-8
#!/usr/bin/env python3

from wtforms.widgets.html5 import EmailInput

__all__ = ['PREmailInput']

class PREmailInput(EmailInput):
    def __init__(self):
        super(PREmailInput, self).__init__()

    def __call__(self, field, **kwargs):
        kwargs['class'] = 'form-control'
        kwargs['placeholder'] = 'Email'
        
        return super(PREmailInput, self).__call__(field, **kwargs)
