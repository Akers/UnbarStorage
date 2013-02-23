#coding=utf-8
__author__ = 'Akers'

from usbase.apibase import ApiHandler
import usbase.models.operations as operations
import usbase.rstformater as rsformat


class User(ApiHandler):
    def __init__(self, name, enable, level, resType, url, remote):
        super(User, self).__init__(name=name, enable=enable, level=level, resType=resType, url=url, remote=remote)

    def doPut(self, params, datas):
        usrName = params.get('username', False)
        if usrName == False:
            return False
        operations.UserOperations.create()
        pass

    def debug(self, params, datas):
        return super(User, self).apiResult('Api Running')
