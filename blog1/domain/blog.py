from blog1.utils import http as hp
from myblog import config


class Blog:
    def __init__(self, id, title, content, createTime, modifyTime, readTime):
        self.id = id
        self.title = title
        self.content = content
        self.createTime = createTime
        self.modifyTime = modifyTime
        self.readTime = readTime


def getBlogList():
    url = config.BLOG_URL + "getAll"
    blogList = hp.get(url)
    return blogList


def getBlog(id):
    url = config.BLOG_URL + "get?id=" + str(id)
    blog = hp.get(url)
    content = blog.get('content', '').replace('\n', '<br>')
    blog['content'] = content
    return blog
