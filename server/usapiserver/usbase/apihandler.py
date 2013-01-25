#coding=utf-8
import rstfomater


class ApiHandler():
    """docstring for ApiHandler"""
    def __init__(self):
        self.__params = {}

    def ececute(self):
        return rstfomater.jsonError(0, 'NotImplementedError')

    def setParams(self, params={}):
        self.__params.update(params)
        return self

    def setParam(self, key, val):
        self.__params.update({key: val})
        return self

    def getParams(self):
        return self.__params

    def getParam(self, key):
        return self.__params.get('key', None)