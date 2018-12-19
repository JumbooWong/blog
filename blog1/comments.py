#首页显示多少个页码
def showPageList(page_num,show_num,current=1,type='next'):
    page_list = []
    if type == 'next':
        # print('total page num',page_num)
        num = min(page_num - current + 1, show_num)
        for i in range(current,current+num):
            page_list.append(i)
    else:
        for i in range(current-show_num+1,current+1):
            page_list.append(i)
    return page_list

#返回指定页面
import re

from django.shortcuts import redirect

def commentPage(request):
    url =request.path
    print(request.session['current_num'])
    pre_url = request.session.get('url')
    if 'next' in url:
        if (request.session['current_num'] + 1) > request.session['page_num']:
            return redirect(pre_url)
        elif request.session['current_num'] % request.session['show_num'] != 0:
            request.session['current_num'] += 1
            return redirect(pre_url)

        else:
            request.session['current_num'] += 1
            request.session['page_num_list'] = showPageList(request.session['page_num'],request.session['show_num'],current=request.session['current_num'])

    elif 'pre' in url:
        if request.session['current_num'] % request.session['show_num'] != 1:
            request.session['current_num'] -= 1
            return redirect(pre_url)
        elif (request.session['current_num'] - 1) < 1:
            return redirect(pre_url)
        else:
            request.session['current_num'] -= 1
            request.session['page_num_list'] = showPageList(request.session['page_num'],request.session['show_num'],current=request.session['current_num'],type='pre')

    else:
        current_num = int(re.findall('\d',url)[0])
        request.session['current_num'] = current_num
    return redirect(pre_url)


