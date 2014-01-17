# coding=utf8

def paginate(rlst, sort_type, page,
             count, sort_reverse=True):
    '''
    分页和排序

    @rlst           -> mongodb查询结果集
    @sort_type      -> 排序类型
    @page           -> 页数
    @count          -> 每页记录数
    @sort_reverse   -> 正序，倒序

    @return (page_info, results)
    '''

    page_info = {}

    stlen = rlst.count()
    rlst.sort(sort_type, [-1, 1][sort_reverse==False])

    tp, r = divmod(stlen, count)
    tp = tp + 1 if r else tp 

    page = [page, 1][page < 1 or page > tp]

    page_info = {
        'page_totals': tp,
        'current_page': page,
        'count': count,
        'pre_page': page-1 if page > 1 else page,
        'sort_type': sort_type,
        'next_page': page+1 if page < tp else tp,
    }
    results = rlst[(page-1)*count: page*count]
    return page_info, list(results)