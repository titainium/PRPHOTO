# coding=utf-8
#!/usr/bin/env python

from .const import PASSWORD_LENGTH

__all__ = ['password', 'to_string']

def password(value):
    return len(value) / PASSWORD_LENGTH * '*'

def to_string(val):
    return ','.join(val)
