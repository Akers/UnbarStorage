#!/usr/bin/env python
#encoding=UTF-8
from usbase.apibase import ApiHandler
import usbase.rstformater as rsformat
import usbase.models.operations as modelOperator
import json,webpy

class UserLogin(ApiHandler):
    def __init__(self,name, enable, level, resType, url, remote):
        super(UserLogin, self).__init__(name=name, enable=enable, level=level, resType=resType, url=url, remote=remote)

    def doGet(self, params, datas):
        return self.__doLogin(params);

    def doPost(self, params, datas):
        return self.__doLogin(params);

    def __doLogin(self, params):
        user = params.get('usr', None)
        pwd = params.get('pwd', None)
        if user == None or pwd == None:
            return rsformat.jsonError(302, userMsg="'usr', 'pwd'")
        #返回结果如下：
            #-1表示用户不存在，
            #密码不正确返回-2
            #若登录成功则返回group字段
        rst = modelOperator.UserOperations.tryLogin(params.get('usr', ''), params.get('pwd', ''))
        if rst < 0:
            if rst == -1:
                return rsformat.jsonError(200)
            if rst == -2:
                return rsformat.jsonError(201)

        return super(UserLogin, self).apiResult(rst)

    def debug(self, params, datas):
        return super(UserLogin, self).apiResult('Api Running')