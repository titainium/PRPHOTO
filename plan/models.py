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
    status          = 'New' #total 4 status: New, Process, Done, Dropped

    def __init__(self):
        pass
    
    @staticmethod
    def get_detail(pid):
        """
            detail for plan

            :param pid: ObjectId 
            :return: a dict or {} (when there is no such record)
        """
        return mongo.db.plan.find_one({'_id': pid}) or {}

    def save(self, plan_id=None, data=None):
        '''
            save the given plan

            :param plan_id: ObjectId
            :kwargs: the other input data

            :return: result of saving data by pymongo
        '''
        is_new = plan_id is None
        if is_new:
            return mongo.db.plan.insert(data)
        else:
            data.update({'_id':plan_id})
            return mongo.db.plan.save(data)

    def get_plans(self):
        '''
            get whole plans

            :return: plan list
        '''
        return mongo.db.plan.find()
    
    @staticmethod
    def validate(data):
        """  Validate the data submitted from user

        :return: result,message
        """
        
        # required fields
        for field in ['title','status']:#,'description']:
            if not data.get(field):
                return False,'field {} is required'.format(field)

            if field == 'status':
                if data[field].upper() not in ['NEW','PROCESS','DONE','DROPPED']:
                    return False,'field {}: value error'.format(field)

        # lenght limit (string)
        for field,min,max in [('title',5,300)]:
            if data.get(field):
                if not min <= len(data[field]) <= max:
                    return False,'field {}:lenght of value must in {}~{}'.format(field,min,max)

        # lenght limit (list)
        for field,min,max in  [('tag-list',1,100),('master-list',1,100),('initiator-list',1,100),('equipment-list',1,100)]:
            if data.get(field):
                if not min <= len(data[field].split(',')) <= max:
                    return False,'field {}:lenght of value must in {}~{}'.format(field,min,max)

        return True,'success'

    @staticmethod
    def clear_data(data):
        """ clear data

        :param data: a dict object
        :return: a dict object that was cleared
        """
        cleared_data = {}

        for key in ['title','description','status']:
            if data.has_key(key):
                cleared_data[key] = data.get(key)
            if key == 'status':
                cleared_data[key] = data.get(key,'').upper()

        # convert string to list
        for key in ['tag-list','master-list','initiator-list','equipment-list']:
            if data.has_key(key):
                _key = key.replace('-list','s')
                cleared_data[_key] = data[key].split(',')

        # do some others
        return cleared_data

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

