# coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

from datetime import datetime
from prphoto import mongo
from profile.models import Profile

__all__ = ['Plan']

class Plan(object):
    initiator_ids   = []
    master_ids      = []
    member_ids      = []
    tags            = []
    samples         = []
    equipments      = ''
    title           = ''
    description     = ''
    starts_at       = datetime.now()
    ends_at         = None
    location        = ''
    is_public       = True
    status          = 'New' #total 4 status: New, Process, Done, Dropped
    classes         = 'general' #now 5 clases: general, non-business, business, donate, advertisement
    weight          = .1

    def __init__(self):
        pass


    @staticmethod
    def get_interested_counts(pid):
        ''' '''
        r = mongo.db.plan.find_one({'_id': pid}, {'interested_ids', 1}) or {}
        return len(r.get('interested_ids', []))
    
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
        for field in ['title','status','description']:
            if not data.get(field):
                return False,'field {} is required'.format(field)

            if field == 'status':
                if data[field].upper() not in ['NEW','PROCESS','DONE','DROPPED']:
                    return False,'field {}: value error'.format(field)

        # lenght limit (string)
        for field,min,max in [('title',5,300)]:
            if data.get(field):
                if not min <= len(data[field]) <= max:
                    return False,'field {}:lenght of this value must be in {}~{}'.format(field,min,max)

        # lenght limit (list)
        for field,min,max in  [('tags',1,100),('master-list',1,100),('initiator-list',1,100),('equipment-list',1,100),('member-list',1,100)]:
            if data.has_key(field):
                if not min <= len(data[field].split(',')) <= max or not data[field]:
                    return False,'field {}:lenght of this value must be in {}~{}'.format(field,min,max)

        # check users
        for field in ['master-list','initiator-list','member-lis']:
            if data.has_key(field):
                for nick_name in data[field].split(','):
                    if nick_name and not Profile.check_exists(nick_name):
                        return False,u'nick name:{} does not exists'.format(nick_name)

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
        for key in ['tag-list','master-list','initiator-list','equipment-list','member-list','tags']:
            if data.has_key(key):
                if key.endswith('-list'):
                    _key = key.replace('-list','s')
                elif key.endswith('s'):
                    _key = key
                cleared_data[_key] = list(set(data[key].split(',')))

                if _key in ['masters','initiators','members']:
                    users = []
                    for nick_name in cleared_data[_key]:
                        profile = Profile.get_profile(nick_name=nick_name)
                        if profile:
                            users.append(profile)
                        cleared_data[_key] = users

        # do some others
        return cleared_data

    @staticmethod
    def get_ad_plans():
        return mongo.db.plan.find().sort("wight", 1).limit(5)
    
    @staticmethod
    def get_init_plans(user_id):
        return mongo.db.plan.find({'initiators._id': user_id})
    
    @staticmethod
    def get_master_plans(user_id):
        return mongo.db.plan.find({'masters._id': user_id})
    
    @staticmethod
    def get_member_plans(user_id):
        return mongo.db.plan.find({'members._id': user_id})

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

