#!/usr/bin/env python
#encoding=UTF-8
import webpy,appapi,appadmin

urls = (
	'/(.*)/', 'redirect',
	'/api', appapi.app_api,  #绑定api子应用
	'/', appadmin.app_admin  #绑定admin子应用
)

app = webpy.application(urls, globals())
#创建Session
session = webpy.session.Session(app, webpy.session.DiskStore('sessions'), initializer={'uid', 'group'})
#关闭调试模式
webpy.config.debug = False

def session_hook():  #通过Session钩子函数绑定session到共用上下文
	webpy.ctx.session = session

app.add_processor(webpy.loadhook(session_hook))

class redirect:  #将以'/'结尾的URL视为无'/'的URL
	def GET(self, path):
		webpy.seeother('/' + path)

if __name__ == '__main__':  #程序主入口
	app.run()