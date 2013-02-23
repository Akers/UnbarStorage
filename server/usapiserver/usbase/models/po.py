#!/usr/bin/env python
#encoding=UTF-8
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import relation
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  #create po base class


class User(Base):
    __tablename__ = 'us_user'  #table name
    userId = Column('user_id', String(16), primary_key=True)
    userName = Column('user_name', String(12), primary_key=True)
    userGroup = Column('user_group', String(20), default='none')
    userPwd = Column('user_pwd', String(100), nullable=False)
    compName = Column('comp_name', String(30), nullable=False)
    compType = Column('comp_type', String(20), default='undefined')
    compManager = Column('comp_manager', String(8), nullable=False)
    compPhone = Column('comp_phone', Integer(12), nullable=False)
    status = Column('status', String(20), default='unaudited')

    def __init__(self, uid, name, pwd, comp_name, manager, comp_phone,
                 group='none', comp_type='undefined', status='unaudited'):
        self.userId = uid
        self.userName = name
        self.userGroup = group
        self.userPwd = pwd
        self.compName = comp_name
        self.compType = comp_type
        self.compManager = manager
        self.compPhone = comp_phone
        self.status = status


class ClientApp(Base):
    __tablename__ = 'us_app'  #table name
    appkey = Column('app_key', String(16), primary_key=True)
    devloper = Column('devloper', String(8), nullable=False)
    secret = Column('app_secret', String(50), primary_key=True)
    level = Column('app_level', Integer(2), nullable=False)
    status = Column('app_status', String(10), nullable=False)

    def __init__(self, appkey, devloper, secret, level, status):
        self.appkey = appkey
        self.devloper = devloper
        self.secret = secret
        self.level = level
        self.status = status


class Token(Base):
    __tablename__ = 'us_tokens'
    token = Column('token', String(16), primary_key=True)
    client = Column('client', String(16), ForeignKey("us_app.app_key"))
    tokenType = Column('type', String(10), nullable=True)
    created = Column('created', DateTime(), nullable=False)
    timeout = Column('timeout', Integer(16), nullable=False)
    level = Column('level', Integer(2), nullable=False, default=0)

    #relationship:
    # app = relation('ClientApp', order_by="ClientApp.appkey", backref="token")
    
    def __init__(self, token, client, tokenType, created, timeout, level):
        self.token = token
        self.client = client
        self.tokenType = tokenType
        self.created = created
        self.timeout = timeout
        self.level = level

    def __repr__(self):
        return "token: %s, client: %s, type: %s, created: %s, timeout: %d, level: %d"\
            % (self.token, self.client, self.tokenType, self.created, self.timeout, self.level)

