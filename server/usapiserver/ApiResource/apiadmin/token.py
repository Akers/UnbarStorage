#coding=utf-8
from usbase.apibase import ApiHandler
import usbase.models.operations as operations
import usbase.rstformater as rsformat


class Token(ApiHandler):
    def __init__(self, name, enable, level, resType, url, remote):
        super(Token, self).__init__(name=name, enable=enable, level=level, resType=resType, url=url, remote=remote)

    # def doGet(self, params, datas):
    #     ao = operations.ApiOperations()
    #     return json.dumps(ao.getList())

    def doPost(self, params, datas):
        """Create token for client"""
        appKey = params.get('app-key', False)
        appSec = params.get('app-secret', False)
        if appKey and appSec:
            token = operations.Tkoen.get(appKey, appSec)
            if token == -1:
                return super(Token, self).apiError(223)
            elif token == -2:
                return super(Token, self).apiError(221)
            elif token == -3:
                return super(Token, self).apiError(150)
            elif token:
                return super(Token, self).apiResult(data={'token', token})
            else:
                return super(Token, self).apiError(0)

    def debug(self, params, datas):
        return rsformat.jsonRst(data='', msg="apilist running currectly")