from blog1.models import comment_info
import time
def test():
    try:
        create_time = time.strftime("%Y-%m-%d", time.localtime())
        # test1 = comment_info(id=12345,user_id=1,user_name='jumbooo',content='第一条留言',create_time=create_time)
        # test1.save()
        comment_info.objects.create(id=21345,user_id=1,user_name='jumbooo',content='第一条留言',create_time=create_time)
    except:pass
    print(comment_info.objects.all())