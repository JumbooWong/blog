from blog1.models import message_info
from django.core import serializers
from django.shortcuts import HttpResponse
import json
import time
def showMessage(max_floor):
    try:
        comments = []
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # test1 = comment_info(id=12345,user_id=1,user_name='jumbooo',content='第一条留言',create_time=create_time)
        # test1.save()
        res_data = message_info.objects.all().values('id','user_id','user_name','content','create_time')
        res = list(res_data)
        for ix,each in enumerate(res):
            if ix < max_floor:
                each['floor'] = str(ix+1)
                comments.append(each)
        # res_json = json.dumps(res)
        # for i in range(10):
        #     message_info.objects.create(id=i,user_id=1,user_name='jumbooo',content='第'+str(i+1)+'条留言',create_time=create_time)
    except:
        pass
    return comments
    # print(message_info.objects.all())









