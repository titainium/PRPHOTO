# coding=utf8
#!/usr/bin/env python
from .const import DEFAULT_ACCURACY

__all__ = ['album_weight', 'plan_weight']


def album_weight(album_p_count, total_p_count):
    '''
    @album_p_count      -> album中相片数量
    @total_p_count      -> 全站相片数量

    @return album_p_count/total_p_count
    '''
    return int((album_p_count/(total_p_count * 1.)* DEFAULT_ACCURACY)) / DEFAULT_ACCURACY


def plan_weight(plan_type):
    '''
    @plan_type          -> plan类型

    @return plan weight
    '''
    classes         = 'non-business' #now 4 clases: non-business, business, donate, advertisement
    plan_weight_mapper = {
        'general': .1,
        'non-business': .2,
        'business': .15,
        'donate': .15,
        'advertisement': .2,
    }

    return plan_weight_mapper[plan_type]
