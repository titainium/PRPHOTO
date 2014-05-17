#!/usr/bin/env python
# coding=utf8

#from prphoto import mongo
#from bson import ObjectId
from datetime import datetime


__all__ = ['Dirary']


class Dirary(object):
    ''' '''

    did = ''
    name = ''
    content = ''
    tags = []
    plan_id = None
    creator_id = None
    create_time = None

    def __init__(
        self,
        name=None,
        content=None,
        tags=None,
        plan_id=None,
        creator_id=None,
        create_time=None,
    ):
        self.name = name
        self.content = content
        self.tags = tags
        self.plan_id = plan_id
        self.creator_id = creator_id
        self.create_time = create_time or datetime.now()

    def get_dirary(self, did):
        ''' '''
        return mongo.db.dirary.find_one({'_id': ObjectId(did)}) or {}

    def insert(self):
        ''' '''
        r = {
            '_id': ObjectId(),
            'name': self.name,
            'content': self.content,
            'tags': self.tags,
            'plan_id': self.plan_id,
            'creator_id': self.creator_id,
            'create_time': self.create_time,
        }

        mongo.db.dirary.insert(r)

    def update(self, *args, **kwargs):
        ''' '''
        query_dict = {}

        #
        if self.gid is not None:
            query_dict.update({'_id': ObjectId(self.did)})

        if query_dict:
            mongo.db.dirary.update(
                query_dict,
                {'$set': kwargs},
            )

    def delete(self, did):
        ''' '''
        mongo.db.gallery.remove({'_id': ObjectId(did)})
