# coding=utf8
#!/usr/bin/env python


__all__ = ['album_weight', plan_weight]


def album_weight(album_p_count, total_p_count):
    '''
    @album_p_count      -> album中相片数量
    @total_p_count      -> 全站相片数量

    @return album_p_count/total_p_count
    '''

    default_accuracy = 10000.

    return int((album_p_count/(total_p_count * 1.)*default_accuracy)) / default_accuracy


def plan_weight(plan_type):
    '''
    @plan_type          -> plan类型

    @return plan weight
    '''
    classes         = 'non-business' #now 4 clases: non-business, business, donate, advertisement
    plan_weight_mapper = {
        'genera': .1,
        'non-business': .2,
        'business': .15,
        'donate': .15,
        'advertisement': .2,
    }

    return plan_weight_mapper[plan_type]