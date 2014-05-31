# coding=utf-8
#!/usr/bin/env python3

from prphoto import db

__all__ = ['User']

class User(db.Model):
    __tablename__ = "prphoto_user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256), unique=True)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_active(self):
        return self.active
        
    def __repr__(self):
        return '<User %r>' % self.username
    
    @classmethod
    def search_by_name(cls, name):
        return db.session.query(cls).filter(cls.username == name).first()
    
    @classmethod
    def get_user_by_id(cls, user_id):
        return db.session.query(cls).get(user_id)
