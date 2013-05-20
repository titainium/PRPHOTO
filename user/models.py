# coding=utf-8
#!/usr/bin/env python

from prphoto import bcrypt
from prphoto import mongo

__all__ = ['User']

class User:
    def __init__(self, name, password, active=True):
        self.name = name
        self.password = password
    
    def save(self):
        mongo.db.users.insert({"UserName": self.name,
                               "Password": bcrypt.generate_password_hash(self.password)})

    @classmethod
    def search_by_name(cls, name):
        return mongo.db.users.find(name).count()
    
    @classmethod
    def check_user(cls, name, password):
        user = mongo.db.users.find_one({'UserName': name})
        
        if user["UserName"] == name and \
           bcrypt.check_password_hash(user["Password"], password):
            return True
        
        return False
    
    @classmethod
    def get_user(cls, name, password):
        return cls(name, password)
    
    @classmethod
    def get_user_by_id(cls, user_id):
      return mongo.db.users.find_one({'_id': user_id})
    
    def get_user_id(self):
        user = mongo.db.users.find_one({'UserName': self.name})
        
        return user['_id']

