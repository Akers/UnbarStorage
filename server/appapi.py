#!/usr/bin/env python
#encoding=UTF-8
import os,sys,webpy
from usapiserver.UsServer import UnbarStorageServer

ROOT_PATH = os.path.dirname(__file__)
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

urls = (
    #URI格式为 (URL路径)/.(资源类型)
    '/(.+)\.(json|xml|yaml|html|txt)', "ApiAssignment",
)


class ApiAssignment:
    """ApiURI请求分派"""
    def __init__(self):
        self.usServer = UnbarStorageServer(webpy.database)
        # print 'server status => ', self.usServer.getServerStatus()

    def GET(self, url, resType):
        return self.__executApi(url, resType, 'get')

    def POST(self, url, resType):
        return self.__executApi(url, resType, 'post')

    def DELETE(self, url, resType):
        return self.__executApi(url, resType, 'delete')

    def PUT(self, url, resType):
        return self.__executApi(url, resType, 'put')

    def __executApi(self, url, resType, method):
        params = webpy.input()
        datas = webpy.data()
        api_rst = self.usServer.executeApi(url, params=params, datas=datas, resType=resType, method=method)
        return api_rst

app_api = webpy.application(urls, globals())