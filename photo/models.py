#!/usr/bin/env python
# coding=utf8

from prphoto import mongo
from bson import ObjectId
from datetime import datetime

__all__ = ['Photo']


class Photo(object):
    ''' '''
    pid = ObjectId()
    name = ''
    description = ''
    photo = ''
    plan_id = None
    gallery_id = None
    creator_id = None
    create_time = None
    exif = []

    def __init__(
        self,
        name='',
        description='',
        photo=None,
        plan_id=None,
        gallery_id=None,
        creator_id=None,
        create_time=None,
        exif=None,
    ):

        self.name = name
        self.description = description
        self.photo = photo
        self.plan_id = plan_id
        self.gallery_id = gallery_id
        self.creator_id = creator_id
        self.create_time = create_time or datetime.now()
        self.exif.append(exif) 

    def get_photo(self, pid):
        ''' '''
        return mongo.db.photo.find_one({'_id': ObjectId(gid)}) or {}

    def insert(self):
        ''' '''
        r = {
            '_id': ObjectId(),
            'name': self.name,
            'description': self.description,
            'photo': self.photo,
            'plan_id': self.plan_id,
            'gallery_id': self.gallery_id,
            'creator_id': self.creator_id,
            'create_time': self.create_time,
            'exif': self.exif,
        }

        mongo.db.photo.insert(r)

    def update(self, *args, **kwargs):
        ''' '''
        query_dict = {}

        #
        if self.gid is not None:
            query_dict.update({'_id': ObjectId(self.pid)})

        if query_dict:
            mongo.db.photo.update(
                query_dict,
                {'$set': kwargs},
            )

    def delete(self, pid):
        ''' '''
        mongo.db.photo.remove({'_id': ObjectId(pid)})
