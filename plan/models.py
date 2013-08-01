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
    def get_detail(self,pid):
        """ detail for plan

        :param pid: ObjectId 
        :return: a dict or None
        """
        pass


if __name__ == '__main__':
    p = Plan()
    pass

