#coding=utf-8
from usbase.apibase import ApiHandler
import usbase.models.operations as operations


class ApiList(ApiHandler):
    def __init__(self, name, enable, level, resType, url, remote):
        super(ApiList, self).__init__(name=name, enable=enable, level=level, resType=resType, url=url, remote=remote)

    def doGet(self, params, datas):
        ao = operations.ApiOperations()
        return super(ApiList, self).apiResult(ao.getList())

    def debug(self, params, datas):
        return super(ApiList, self).apiResult('Api Running')
