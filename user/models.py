# coding=utf-8
#!/usr/bin/env python

from prphoto import bcrypt
from prphoto import mongo

__all__ = ['User']

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def save(self):
        #FIXME here may be a bug -> can a username duplicated?
        # if the answer is No, here we should create a unique index with username
        # if the answer is Yes, why to allow this...
        mongo.db.users.insert(
            {
                "username": self.name,
                "password": bcrypt.generate_password_hash(self.password),
            },
            safe=True,
        )

    @classmethod
    def search_by_name(cls, name):
        '''
            search users collection by username column
            @name => target user
        '''
        return mongo.db.users.find_one({'username': name}) or {}

    
    @classmethod
    def check_user(cls, name, password):
        '''
            check the user by given (username, password)
            @name => target user
            @password => target user's password
        '''
        #flag = False
        user = mongo.db.users.find_one({'username': name}) or {}
        
        if not user:
            flag = False
        elif all([
            user.get('username', "") == name,
            bcrypt.check_password_hash(user.get("password", ""), password),
        ]):
            flag = True
        
        return flag
    
    @classmethod
    def get_user(cls, name, password):
        '''
            get user info by given name, password
            @name => target username
            @password => target user's password
        '''
        return mongo.db.users.find_one({
            'username': name,
            'Password': bcrypt.generate_password_hash(password),
        }) or {}
    
    @classmethod
    def get_user_by_id(cls, user_id):
        '''
            get the user info by given user_id.
            here the user_id is the ObjectId in python module <bson>
            like:
                from bson import ObjectId

            @user_id => the given ObjectId which can identify the user
        '''
        return mongo.db.users.find_one({'_id': user_id}) or {}

    def get_user_id(self):
        return mongo.db.users.find_one({'username': self.name}).get('_id')

    @classmethod
    def update_user_password(cls, username, password):
        '''
            update the given user's password.
            @username => the target username
            @password => the new password
        '''
        return mongo.db.users.update(
            {
                'username': username,
            },
            {
                "$set": {
                    'password': bcrypt.generate_password_hash(password),
                }
            },
            safe=True,
        )
