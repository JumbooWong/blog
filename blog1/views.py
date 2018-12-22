# 视图层
from django.shortcuts import render, redirect

from blog1.dao.messages import showMessage, addMessage
from blog1.seesions import sessionUpdate
from blog1.utils import http as hp
from blog1.domain import blog as bg
from blog1.domain import user as usr
import json
# 主页
def home(request):
    ## 获取blog列表
    blogStringList = bg.getBlogList()
    blogList = []
    for each in blogStringList:
        blog = bg.Blog(**each)
        blogList.append(blog)

    # 获取数据库中一共多少条数据
    sessionUpdate(request)
    request.session['url'] = request.path
    return render(request, 'home.html', {'blogList':blogList})


# 所有文章页面
def articles(request):
    sessionUpdate(request)
    request.session['url'] = request.path
    return render(request, 'articles.html')


# 相册页面
def albums(request):
    sessionUpdate(request)
    request.session['url'] = request.path
    return render(request, 'albums.html')


# 留言页面
def comments(request):
    sessionUpdate(request)
    if request.method == 'POST':
        concat = request.POST
        message = concat.get('message').strip()

        if request.session.get('user', False) and message:
            # request.session['message'] = None
            # 插入数据库
            add_status = addMessage(request.session['user']['acct'], message)
            if add_status:
                request.session['current_num'] = 1
                print('评论成功！')
            else:
                print('评论失败！')

    # 从数据库中读取评论数据
    comments = showMessage(request.session.get('max_message', 0), request.session['current_num'])
    request.session['url'] = request.path
    return render(request, 'comments.html', {'comments': comments})


# 单文章
def article(request):
    id = request.GET.get('id')
    blog = bg.getBlog(id)
    print(id)
    request.session['url'] = request.path
    return render(request, 'articles/article.html',{'blog':blog})


# 跳转到注册界面
def goToRegisterPage(request):
    return render(request, 'login/register.html')


# 注册
def register(request):
    concat = request.POST
    email = concat.get('email')
    acct = concat.get('acct')
    name = concat.get('name')
    mobile = concat.get('mobile')
    password = concat.get('password')
    re_password = concat.get('re_password')
    print(email, acct, name, mobile, password, re_password)

    body = {"acct": acct, "name": name, "mobile": mobile, "email": email, "password": password}

    # 发送http post请求
    url = "http://47.105.163.206:8003/user/register"
    hp.post(url, body)
    pre_url = request.session.get('url')
    return redirect(pre_url)


# 登录
def login(request):
    try:
        # request.session['login_stat'] = None
        concat = request.POST
        username = concat.get('username')
        password = concat.get('password')
        keep = concat.get('keep')  # 下次是否自动登录
        print(username, password, keep)
        pre_url = request.session.get('url')
        if username and password:
            user = usr.login(username,password)
            if (user):
                print("登录成功")
                request.session['user'] = user
                # 如果keep不为None，设置seesion
                if keep:
                    # 一个月后失效，以秒为单位
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    # 关闭浏览器就会失效
                    request.session.set_expiry(0)
                request.session['login_stat'] = '1'
            else:
                request.session['login_stat'] = '0'
                print("用户名密码错误")
        # else:
        #         #     print("用户名密码不能为空")
        #         #     request.session['login_stat'] = -1
        return redirect(pre_url)
    except:
        request.session['login_stat'] = '-1'
        print("连接异常")
        return redirect(pre_url)


# 退出登录
def logout(request):
    # request.session['user'] = None
    pre_url = request.session.get('url')
    request.session.pop('user')
    request.session['login_stat'] = '1'
    return redirect(pre_url)


# 关闭登录页面
def loginClose(request):
    pre_url = request.session.get('url')
    request.session['login_stat'] = '1'
    return redirect(pre_url)
