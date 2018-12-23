
from math import ceil
from blog1.dao import messages
#更新评论相关内容
def sessionUpdate(request):
    message_count = messages.messageCount()
    # 每页显示max_message条数据
    max_message = 2
    request.session['max_message'] = max_message
    # 总页数
    page_num = ceil(message_count / max_message)
    request.session['page_num'] = page_num
    request.session['show_num'] = 3
    current = request.session.get('current_num','1')
    change_type = request.session.get('change','no')
    if change_type == 'next':
        current += 1
    elif change_type == 'pre':
        current = current-request.session['show_num']+1
        request.session['page_num_list'] = showPageList(request.session.get('page_num'), request.session['show_num'],                                                     current=current)
    elif change_type == 'del':
        mod = current % request.session['show_num']
        print('xianzaishi:', current,request.session['page_num'])
        if mod == 0:
            current = max(current - request.session['show_num'] +1,1)
        elif mod != 1:
            current = current - mod + 1
        request.session['page_num_list'] = showPageList(request.session.get('page_num'), request.session['show_num'],current=current,type = 'del')
            # request.session['page_num_list'] = showPageList(request.session.get('page_num'),
            #                                                 request.session['show_num'], current=current, type='del')

    if not request.session.get('current_num'):request.session['current_num'] = 1
    # request.session['current_num'] = 1

    # 首页显示多少个页码
def showPageList(page_num, show_num, current=1, type='next'):
    page_list = []
    if type == 'next':
        print('total page num',page_num)
        num = min(page_num - current + 1, show_num)
        for i in range(current, current + num):
            page_list.append(i)
    elif type == 'pre':
        for i in range(current - show_num + 1, current + 1):
            page_list.append(i)
    elif type == 'del':
        num= min(page_num - current + 1, show_num)
        for i in range(current,current+num):
            page_list.append(i)
    return page_list