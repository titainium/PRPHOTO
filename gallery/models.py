#!/usr/bin/env python
# coding=utf8

from prphoto import mongo
from bson import ObjectId
from datetime import datetime

__all__ = ['Gallery']


class Gallery(object):
    ''' '''
    id = ''
    name = ''
    description = ''
    plan_id = None
    creator_id = None
    create_time = datetime.now()

    def __init__(
        self,
        name=None,
        description=None,
        plan_id=None,
        creator_id=None,
        create_time=None,
    ):
        ''' '''
        self.name = name
        self.description = description
        self.plan_id = plan_id
        self.creator_id = creator_id
        self.create_time = create_time 

    def get_gallery(self, gid):
        ''' '''
        return mongo.db.gallery.find_one({'_id': ObjectId(gid)}) or {}

    def insert(self):
        ''' '''
        r = {
            'name': self.name,
            'description': self.description,
            'plan_id': self.plan_id,
            'creator_id': self.creator_id,
            'create_time': self.create_time,
            '_id': ObjectId(),
        }

        mongo.db.gallery.insert(r)

    def update(self, *args, **kwargs): 
        ''' '''
        query_dict = {}

        #
        if self.gid is not None:
            query_dict.update({'_id': ObjectId(self.gid)})

        if query_dict:
            mongo.db.gallery.update(
                query_dict,
                {'$set': kwargs},
            )

    def delete(self, gid):
        ''' '''
        mongo.db.gallery.remove({'_id': ObjectId(gid)})
