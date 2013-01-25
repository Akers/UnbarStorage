#coding=utf-8

class ApiModel():
    ''''''
    __params = {}

    def setParams(self, params={}):
        self.__params.update(params)
        return self

    def setParam(self, key, val):
        self.__params.update({key: val})
        return self

    def getParams(self):
        return self.__params

    def getParam(self, key, val):
        pass