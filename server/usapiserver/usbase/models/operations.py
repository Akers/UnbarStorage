#!/usr/bin/env python
#encoding=UTF-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import calendar
import random
import po


#Create database engine
#create_engine(数据库://用户名:密码(没有密码则为空)@主机名:端口/数据库名',echo =True)
engine = create_engine('mysql://root:0000@localhost:3306/db_usdb', echo=True)
Session = sessionmaker(bind=engine)  #create session
session = Session()


def getSession():
    return session


def getUnixTimeNow():
    """获取当前时间并转换成Unix时间戳"""
    return calendar.timegm(datetime.utcnow().utctimetuple())


def generateID(len=16):
    """
    :param len: the length of id
    :return: an ID in given length
        when errors:
         -1: given param len is not a int number
         -2: given a len smaller than 0
    """
    try:
        len = int(len)
    except ValueError:
        return -1

    if len < 0:
        return -2


    d = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

    rs = []
    for x in range(len):
        rs.append(random.choice(d))

    return ''.join(rs)


class ApiOperations:
    """"""
    def getList(self):
        """
        :return:
        """
        import usbase.apimanage, GLOBAL
        apiLst = usbase.apimanage.ApiManagerFactory().getInstance(GLOBAL.API_PATH).getApiLst()
        rst = []
        if apiLst:
            for api in apiLst:
                api = apiLst.get(api)
                rs = {
                    'name': api.getName(),
                    'enable': api.isEnable(),
                    'level': api.getLevel(),
                    'url': api.getUrl(),
                    'resource': api.getSupportRes()
                }
                rst.append(rs)
        return rst


class UserOperations:
    @classmethod
    def get(cls, name=None, userId=None):
        pass

    @classmethod
    def create(cls, name, pwd, comp, manager, phone):
        user = po.User(uid=generateID(), name=name, pwd=pwd, comp_name=comp, manager=manager, comp_phone=phone)
        rs = True
        try:
            session.add(user)
            session.commit()
        except:
            session.rollback()
            rs = False

        return rs

    @classmethod
    def tryLogin(cls, usr, pwd):
        dbrs = session.query(po.User).filter(po.User.userName == usr).all()
        if len(dbrs) < 1:
            rst = -1  #return user not found
        elif pwd == dbrs[0].userPwd:  #登录成功返回用户组，以体现权限
            rst = {'uid': dbrs[0].userName, 'group': dbrs[0].userGroup}
        else:
            rst = -2
        return rst


class ClientApp:
    @classmethod
    def check(cls, appKey, appSec):
        """Verify Client App
        :param appKey: the app-key of a Client app
        :param appSec: the app secret of a Client app
        :return : when verify success return app level;
                  when app-key not found return -1;
                  when app-secret is not correct return -2;
        """
        dbrs = session.query(po.ClientApp.secret, po.ClientApp.level)\
            .filter(po.ClientApp.appkey == appKey)\
            .first()

        rs = -1
        if dbrs:
            if appSec == dbrs[0]:
                rs = dbrs[1]
            else:
                rs = -2
        else:
            rs = -1

        return rs


class Token:

    TOKEN_TIMEOUT = 1800

    @classmethod
    def get(cls, appKey, appSecret):
        """
        get app token
        :param appKey:
        :param appSecret:
        :return:
            returns token when sucess
            when cause errors returns error code bellows:
                -1: appKey not found
                -2: appSecret uncorrected
                -3: DataBase Error
        """
        rs = -1
        cLevel = ClientApp.check(appKey=appKey, appSec=appSecret)
        print 'cLevel => ', cLevel
        # cLevel = 10
        if cLevel >= 0:
            token = session.query(po.Token).filter(po.Token.client == appKey).first()
            if token:  #token 存在则更新token
                token.created = datetime.now()
            else:  #token不存在需新增token
                token = po.Token(token=generateID(),
                                 client=appKey,
                                 tokenType='client',
                                 created=datetime.now(),
                                 timeout=cls.TOKEN_TIMEOUT,
                                 level=cLevel)

                rs = token.token
                try:
                    session.add(token)
                    session.commit()
                except:
                    session.rollback()
                    rs = -3
        else:
            rs = cLevel
        return rs

    @classmethod
    def update(cls, token):
        pass

    @classmethod
    def verify(cls, token):
        """
        :param token:
        return: return client level --> ok
                -1 --> token not found
                -2 --> it's a overdue token
        """
        dbrs = session.query(po.Token.created, po.Token.timeout, po.Token.level)\
            .filter(po.Token.token == token)\
            .first()
        rs = -1
        if dbrs:
            timeLived = datetime.now() - dbrs[0]
            if dbrs[1] == 0 or timeLived.seconds <= int(dbrs[1]):
                rs = dbrs[2]
            else:
                rs = -2
        else:
            rs = -1

        return rs


print 'hey~'
# print Token.get(appKey='zN6o8k00', appSecret='9DuBbdC9Qykxyiyn6Uxe6xJc8FBowqgClV7KVsHZzoQuJ1dSKV')
# print Token.verify('5Ex4wXdVUIV4d837')
print 'appKey => ', generateID(8)
print 'appSecret => ', generateID(50)
print 'id => ', generateID(16)
# Token.get('v2b9ib72', 'asdfasfasdfasdf')