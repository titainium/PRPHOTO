#!/usr/bin/env python
# coding=utf8

from prphoto import db

from user.models import User

__all__ = ['Dirary']

class Dirary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(120), unique=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relation('User', backref = db.backref('profile', lazy = 'dynamic'))

    def __init__(self, nickname = None, location = None):
        self.nickname = nickname
        self.location = location

    def __repr__(self):
        return '<Profile %r>' % self.nickname
    
    @classmethod
    def get_by_userid(cls, user_id):
        return db.session.query(cls).filter(cls.user_id == user_id).all()
