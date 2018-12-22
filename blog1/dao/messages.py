from blog1.models import message_info
from django.core import serializers
import json
import time


# 评论查询
def showMessage(max_floor, current_page):
    try:
        comments = []
        # test1 = comment_info(id=12345,user_id=1,user_name='jumbooo',content='第一条留言',create_time=create_time)
        # test1.save()
        res_data = message_info.objects.all().order_by('-id').values('id', 'user_id', 'user_name', 'content',
                                                                     'create_time')
        last_floor = message_info.objects.all().count()
        first = (current_page - 1) * max_floor
        res = list(res_data)[first:first + max_floor]
        for ix, each in enumerate(res):
            if ix < max_floor:
                each['floor'] = str(last_floor - ix - first)
                comments.append(each)
                # res_json = json.dumps(res)
                # for i in range(10):
                #     message_info.objects.create(id=i,user_id=1,user_name='jumbooo',content='第'+str(i+1)+'条留言',create_time=create_time)
    except:
        pass
    return comments
    # print(message_info.objects.all())


# 评论增加
def addMessage(user_name, message):
    try:

        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # test1 = comment_info(id=12345,user_id=1,user_name='jumbooo',content='第一条留言',create_time=create_time)
        # test1.save()
        message_info.objects.create(user_id=1, user_name=user_name, content=message, create_time=create_time)
        return 1
    except:
        return 0


# 查询总量
def messageCount():
    return message_info.objects.all().count()


# 删除评论
def deleteMessage(id):
    try:
        message_info.objects.filter(id=id).delete()

        return 1
    except:
        return 0
