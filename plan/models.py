# coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

from datetime import datetime
from prphoto import mongo

__all__ = ['Plan']

class Plan(object):
    initiator_ids   = []
    master_ids      = []
    member_ids      = []
    tags            = []
    equipments      = ''
    title           = ''
    description     = ''
    starts_at       = datetime.now()
    ends_at         = None
    location        = ''
    is_public       = True

    def __init__(self):
        pass
    
    @staticmethod
    def get_detail(self, pid):
        """
            detail for plan

            :param pid: ObjectId 
            :return: a dict or {} (when there is no such record)
        """
        return mongo.db.plan.find_one({'_id': pid}) or {}

    def save(self, plan_id=None, **kwargs):
        '''
            save the given plan

            :param plan_id: ObjectId
            :kwargs: the other input data

            :return: result of saving data by pymongo
        '''
        is_new = plan_id is None
        if is_new:
            return mongo.db.plan.insert(kwargs)
        else:
            kwargs.update({'_id': plan_id})
            return mongo.db.plan.save(kwargs)


if __name__ == '__main__':
    p = Plan()
    pass

