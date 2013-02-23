#coding=utf-8
import usbase.rstformater as rsformat
import usbase.models as models


class ApiHandler(object):
    """docstring for ApiHandler"""
    def __init__(self, name='', enable=True, level=0, resType='json', url='', remote=False):
        self.__name = name
        self.__level = int(level)
        self.__suportRes = resType
        self.__enable = enable
        self.__url = url
        self.__remote = remote
        self.__res = None
        pass

    def execute(self, params={}, datas={}, method='get', res='json'):
        #check res
        if self.checkRes(res):
            self.__res = res
        else:
            resStr = ','.join(self.__suportRes)
            return self.apiError(296, "'%s' This api supported resources types below:'%s" % (res, resStr))
        #get client level when the api level is higher than 0(not a public api):
        level = 0
        if self.__level > 0:
            if 'token' in params:
                level = models.operations.Token.verify(token=params.get('token', ''))
                if level == -1:
                    return self.apiError(223)
                elif level == -2:
                    return self.apiError(224)
            elif 'app-key' in params:
                #get app-key and app-secret
                level = models.operations.ClientApp.check(appKey=params.get('app-key', ''), appSec=params.get('app-secret', ''))
            else:
                level = 0

        method = method.lower().strip()
        #when mod=debug exist, get function 'debug' inseted and skip level check
        mod = params.get('mod', False)  #or datas.get('mod', False)
        if mod and mod.lower() == 'debug':
            return self.debug(params, datas)
        
        #check client level
        if self.checkLevel(level):
            #call action function
            if method == 'get':
                return self.doGet(params, datas)
            elif method == 'post':
                return self.doGet(params, datas)
            elif method == 'delete':
                return self.doGet(params, datas)
            elif method == 'put':
                return self.doGet(params, datas)
            else:
                return self.apiError(301, "wanted one of bellow: 'get' 'post' 'put' or 'delete' but exepected %s" % method)
        else:
            return self.apiError(222, "This Api needs level high than: %s But your client level is: %s" % (self.__level, level))

    def apiResult(self, data, msg=''):
        return rsformat.resultf(data=data, msg=msg)
    
    def apiError(self, errNum, usrMsg=''):
        return rsformat.errorf(errNum, usrMsg)
    
    def checkLevel(self, level=0):
        if self.__level == 0:
            return True
        elif self.__level <= int(level):
            return True
        else:
            return False
    
    def checkRes(self, res):
        if res in self.__suportRes:
            return True
        else:
            return False
    
    #attribue getters:
    def getName(self):
        return self.__name
    
    def isEnable(self):
        return self.__enable
    
    def getLevel(self):
        return self.__level
    
    def getUrl(self):
        return self.__url
    
    def isRemote(self):
        return self.__remote
    
    def getSupportRes(self):
        return ','.join(self.__suportRes)
    
    
    def doGet(self, params, datas):
        return rsformat.jsonError(297, "current method: get")

    def doPost(self, params, datas):
        return rsformat.jsonError(297, "current method: post")

    def doDelete(self, params, datas):
        return rsformat.jsonError(297, "current method: delete")

    def doPut(self, params, datas):
        return rsformat.jsonError(297, "current method: put")

    def debug(self, params, datas):
        return self.apiError(297, "current method: debug")
