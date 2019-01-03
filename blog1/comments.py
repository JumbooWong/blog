

#返回指定页面
import re
from blog1.seesions import showPageList,sessionUpdate
from django.shortcuts import redirect

def commentPage(request):
    url =request.path
    request.session['change'] = 'no'
    pre_url = request.session.get('url')
    if 'next' in url:
        if (request.session['current_num'] + 1) > request.session['page_num']:
            return redirect(pre_url)
        elif request.session['current_num'] % request.session['show_num'] != 0:
            request.session['current_num'] += 1
            return redirect(pre_url)
        else:
            request.session['current_num'] += 1
            request.session['change'] = 'next'
            request.session['page_num_list'] = showPageList(request.session['page_num'],request.session['show_num'],current=request.session['current_num'])

    elif 'pre' in url:
        if request.session['current_num'] % request.session['show_num'] != 1:
            request.session['current_num'] -= 1
            return redirect(pre_url)
        elif (request.session['current_num'] - 1) < 1:

            return redirect(pre_url)
        else:
            request.session['change'] = 'pre'
            request.session['current_num'] -= 1
            request.session['page_num_list'] = showPageList(request.session['page_num'],request.session['show_num'],current=request.session['current_num'],type='pre')

    else:
        current_num = int(re.findall('\d',url)[0])
        # current_num = request.GET.get('page')
        print(current_num)
        request.session['current_num'] = current_num

    return redirect(pre_url)

from blog1.dao.messages import deleteMessage,messageCount
# from math import ceil
#删除评论
def commentDel(request):
    url = request.path
    id,floor = int(re.findall('\d+',url)[0]),int(re.findall('\d+',url)[1])
    # id = request.GET.get('id')
    # floor = request.GET.get('floor')
    show_num = request.session.get('show_num')
    message_count = messageCount()
    del_status = deleteMessage(id)
    if del_status:
        if floor == 1 :  #and floor!= message_count
            request.session['current_num'] -= 1
            print('删除后的页码',request.session['current_num'])
        request.session['change'] = 'del'
        print('删除成功！')
    else:print('删除失败！')
    pre_url = request.session.get('url')
    return redirect(pre_url)