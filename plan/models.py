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

    def get_plans(self):
        '''
            get whole plans

            :return: plan list
        '''
        return mongo.db.plan.find()
    
    @staticmethod
    def validate(data):
        """ Validate  data that submitted from user
        """
        # required fields
        for field in ['title']:
            if not data.has_key(field):
                return False
        # TODO
        return True

    @staticmethod
    def clear_data(data):
        """ clear data

        :param data: a dict object
        :return : a dict object be cleared
        """
        print 'data',data,type(data)
        # convert string to list
        for key in ['tags']:
            data[key] = data[key].split(',')

        # some others
        # TODO
        return data


    def get_plans_by_public(self, is_public=True):
        '''
            get plans by is_public

            :param is_public: boolean
            :return: plan list with checking is_public
        '''
        return filter(
            lambda x: x.get('is_public', False) == is_public,
            self.get_plans()
        )


if __name__ == '__main__':
    p = Plan()
    pass

