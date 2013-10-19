# coding=utf-8
#!/usr/bin/env python

from .const import PASSWORD_LENGTH

__all__ = ['password']

def password(value):
  return len(value) / PASSWORD_LENGTH * '*'
