#coding=utf-8
import confmanage,rstformater,os,sys,imp,GLOBAL

class ApiManager():

	"""docstring for ApiLoader"""
	def __init__(self, apiPath):
		self.__apiPath = apiPath
		self.__apiConfs = self.preloadApilst()

	def execApi(self, api_url, api_params):
		'''
			execute the execution function in api handler then return a api result
		'''
		api = self.searchApi(api_url).get('data', {})
		print 'api => ', api
		api_handler = self.getApiHandler(api.get('handler'))
		print 'api_handler => ', api_handler
		handler =  api_handler.get('data')
		exec_func = getattr(handler, 'execute')
		print 'handler attr execute = ', exec_func
		# api_rst = self.invok_api_execfunc(api_handler)
		return rstformater.jsonRst(exec_func())

	def preloadApilst(self):
		"""API列表预加载，解析api_conf.json配置文件并将api列表加载到内存"""
		GLOBAL.LOGGER.logInfo("Preloading api list...")
		#获取Api配置
		api_confs =  confmanage.load_xml_api_confs(self.__apiPath)
		if api_confs.get('error') == 0 :
			if 'data' in api_confs :
				#结果集完好，读取api_list
				rst_val = api_confs.get('data')
			else :
				GLOBAL.LOGGER.logError("Configuations result format error")
				rst_val = None
		else :
			GLOBAL.LOGGER.logError("Unable to load api configuations ErrorCode:%s ErrorMessage:'%s'" % (api_confs['error'], api_confs['msg']))
			rst_val = None
		return rst_val
		
	def searchApi(self, url='', name=''):
		'''Search api conf in api list'''
		if self.__apiConfs == None :
			self.__apiConfs = self.preload_apilst()
		
		rst_val = None
		if len(url) > 0:
			for api in self.__apiConfs :
				for apiurl in api.get('resources').get('urls'):
					if apiurl == url:
						rst_val = rstformater.jsonRst(api)
						break
				if rst_val != None:
					break
		elif len(name) > 0:
			for api in self.__apiConfs:
				if api.get('name') == name:
					rst_val = rstformater.jsonRst(api)
					break
		else:
			rst_val = rstformater.jsonError(301, 'Api not found!')

		return rst_val

	def getApiHandler(self, handler):
		'''get api handler instance'''
		print 'param: handler => ', handler

		# modelPath = handler.get('modelPath', '')

		modulePath = "%s%s%s" % (self.__apiPath, os.sep, handler.get('modelPath', ''))
		moduleName = handler.get('modelName', '')
		handlerClassName = handler.get('className', '')
		print 'modelPath => ', modulePath
		rst = ''

		#load model imp.load_source
		handlerModule = imp.load_source(moduleName, "%s%s%s.py"%(modulePath, os.sep, moduleName))
		handlerClass = getattr(handlerModule, handlerClassName)
		p = handlerClass()
		p.setParam('param1', 'pv')
		print 'p.getParam => ', p.getParam('param1')
		print p.execute()
		print 'handlerClass => ', handlerClass
		# handlerModel = imp.load_module(moduleName, *imp.find_module(moduleName, modulePath))
		print 'handlerModule => ', handlerModule


		# if os.path.exists(modelPath):
		# 	imp.load_model('')
		# 	rst = rstformater.jsonRst(imp.load_source(handler.get('className', ''), modelPath))
		# 	print 'rst => ', rst
		# else:
		# 	rst = rstformater.jsonError(302, 'Handler File Not Found')
		# # print handler_path

		return rst
	
	def setParams(self, handlerClass, params={}):
		if handlerClass != None:
			handlerClass.setParams(params)
			rst = True
		else :
			rst = False
		return rst

	def invok_api_execfunc(self, handler):
		'''invok the api execution function'''
		pass
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		