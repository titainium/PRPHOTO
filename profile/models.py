# coding=utf-8
#!/usr/bin/env python

from prphoto import mongo

__all__ = ['Profile']

class Profile:
    def save(self):
        mongo.db.profiles.insert({"UserID": self.userID,
                               "NickName": self.nick_name,
                               "Location": self.location})
    
    @classmethod
    def get_profile(cls, user_id):
      return mongo.db.profiles.find_one({"UserID": user_id})
