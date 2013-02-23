#!/usr/bin/env python
#encoding=UTF-8
from multiprocessing import connection

import webpy

appKey = '2cn2w4I9YJxO5L1Z'
appSecret = 'CLLX2XroDLYbizIWJjXI2jDL2FtJqCSqWXWVX5iqaSEMEG4Q0G'
token = None
urls = (
    '', "Index",
    'status', 'ApiStatus',
    'admin', 'AdminIndex',
    'admin/login', 'Login',
    'admin/dev', 'DeveloperIndex',
    'admin/dev/reg', 'DeveloperReg',
    'admin/manage', 'ServerManage'
)
app_admin = webpy.application(urls, globals())
render_index = webpy.template.render('usadmin/templates/', base='layout')
render_admin = webpy.template.render('usadmin/templates/admin/', base='../layout')
render_dev = webpy.template.render('usadmin/templates/dev/', base='../layout')


class Index:
    def GET(self):
        return render_index.index()


class ApiStatus:
    def GET(self):
        return render_index.apistatus()


class Login:
    def GET(self):
        return render_admin.login()

    def POST(self):
        params = webpy.input()
        webpy.ctx.session.uid = params.get('username', False)
        webpy.ctx.session.group = params.get('group', False)
        raise webpy.seeother('admin/manage')


class AdminIndex:
    def GET(self):
        if webpy.ctx.session.get('group', False):
            return webpy.ctx.session.group
        else:
            webpy.seeother('admin/login')


class ServerManage:
    def GET(self):
        return webpy.ctx.session.get('group', False)


class DeveloperReg:
    def GET(self):
        return render_dev.reg()

    def POST(self):
        import json, httplib
        params = webpy.input()
        apiParam = {
            'username': params.get('username', ''),
            'userpwd': params.get('username', ''),
            'compName': params.get('username', ''),
            'compManager': params.get('username', ''),
            'compPhone': params.get('username', '')
        }
        conn = httplib.HTTPConnection()
        return 'posting'
