# coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

from datetime import datetime

__all__ = ['Plan']

class Plan(object):

    master_id       = '' 
    member_ids      = []
    performer_ids   = []
    name            = ''
    starts_at       = datetime.now()
    ends_at         = datetime.now()
    location        = ''
    equipments      = []
    is_public       = True

    def __init__(self):
        pass

    def save(self):
        pass

    
    @staticmethod
    def get_detail(self, pid):
        """
            detail for plan

            :param pid: ObjectId 
            :return: a dict or {} (when there is no such record)
        """
        return mongo.db.plan.find_one({'_id': pid}) or {}

    def save(self, plan_id, **kwargs):
        '''
            save the given plan

            :param plan_id: ObjectId
            :kwargs: the other input data

            :return: result of saving data by pymongo
        '''
        kwargs.update({'_id': plan_id})
        return mongo.db.plan.save(kwargs)


if __name__ == '__main__':
    p = Plan()
    pass

