# coding=utf-8
#!/usr/bin/env python3

from wtforms.widgets.core import PasswordInput

__all__ = ['PRPasswordInput'
           ]

class PRPasswordInput(PasswordInput):
    def __init__(self):
        super(PRPasswordInput, self).__init__()

    def __call__(self, field, **kwargs):
        kwargs['class'] = 'form-control'
        kwargs['placeholder'] = 'Password'
        
        return super(PRPasswordInput, self).__call__(field, **kwargs)
