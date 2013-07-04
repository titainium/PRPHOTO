# coding=utf-8
#!/usr/bin/env python

from prphoto import mongo

from bson import ObjectId   # for the user's id is ObjectId

__all__ = ['Profile']

class Profile(object):
    ''' user's profile infomation.  '''
    def __init__(self, username=None, user_id=None, nick_name=None, location=None):
        self.username = username
        self.user_id = user_id
        self.nick_name = nick_name
        self.location = location

    def save(self):
        ''' add a profile to some user.  '''
        query_dict = {}

        # init the query_dict for query record
        if self.user_id is not None:
            query_dict.update({'_id': ObjectId(self.user_id)})

        if self.username is not None:
            query_dict.update({'username': self.username})

        if not query_dict:
            pass
        else:
            mongo.db.users.update(
                query_dict,
                {"$set": {
                    'profile': {
                        "nick_name": self.nick_name,
                        "location": self.location,
                    },
                }},
                safe=True,
            )


    @classmethod
    def get_profile(cls, user_id=None, username=None):
        '''
            get user's profile by user_id or username
            @user_id => the target user's id
            @username => the target user's name
        '''
        result = {}
        query_dict = {}
        if user_id:
            query_dict.update({'_id': ObjectId(user_id)})
        if username:
            query_dict.update({'username': username})

        if not query_dict:
            pass
        else:
            result = mongo.db.users.find_one(query_dict) or {}

        return result

    @classmethod
    def update_profile(cls, user_id, **kwargs):
        ''' update user_id by given args '''
        cur_profile = mongo.db.users.find_one(
            {'_id': ObjectId(user_id)}
        ).get('profile', {})

        cur_profile.update(kwargs)

        return mongo.db.users.update(
            {'_id': ObjectId(user_id)},
            {"$set": {'profile': cur_profile}},
            save=True,
        )
