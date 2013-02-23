#!/usr/bin/env python
#encoding=UTF-8

import webpy

urls = (
	'', "Index",
	'status', 'ApiStatus'
)

render = webpy.template.render('usadmin/templates/', base='layout')

class Index():
	def GET(self):
		return render.index()

class ApiStatus():
	def GET(self):
		return render.apistatus()


app_index = webpy.application(urls, globals())