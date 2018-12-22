from blog1.utils import http as hp
from myblog import config


class User:
    def __init__(self, id, acct, name, mobile, email, description, status, password, createtime, lastlogintime):
        self.id = id
        self.acct = acct
        self.name = name
        self.mobile = mobile
        self.email = email
        self.description = description
        self.status = status
        self.password = password
        self.createtime = createtime
        self.lastlogintime = lastlogintime


def login(username, password):
    url = config.USER_URL + "login?username=" + username + "&password=" + password
    user = hp.get(url)
    return user
