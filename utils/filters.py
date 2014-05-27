# coding=utf-8
#!/usr/bin/env python3

from .const import PASSWORD_LENGTH

__all__ = ['password', 'to_string', 'get_nick_name']

def password(value):
    return len(value) / PASSWORD_LENGTH * '*'

def to_string(val):
    return ','.join(val)

def get_nick_name(val):
    return ','.join([usr['profile']['nick_name'] for usr in val])
