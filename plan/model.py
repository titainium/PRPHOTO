# coding=utf-8
#!/usr/bin/env python

"""
Implements plan's model

"""

from datetime import datetime
from mongoengine import *

__all__ = ['Plan']

class Plan(Document):
    master_id       = StringField()
    member_ids      = ListField(StringField())
    performer_ids   = ListField(StringField())
    name            = StringField()
    starts_at       = DateTimeField(default=datetime.now)
    ends_at         = DateTimeField()
    location        = StringField()
    equipments      = ListField(StringField())
    is_publick      = BooleanField(default=True)


if __name__ == '__main__':
    connect(host='localhost',db='test')
    p = Plan()
    p.save()
    print 'id',p.id
    pass

