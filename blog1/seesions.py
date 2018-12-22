from blog1.comments import showPageList
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
    request.session['page_num_list'] = showPageList(request.session.get('page_num'), request.session['show_num'])
    # print('主页的currentid',request.session.get('current_num'))
    if not request.session.get('current_num'):request.session['current_num'] = 1
    # request.session['current_num'] = 1