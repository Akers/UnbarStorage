#!/usr/bin/env python
#encoding=UTF-8
import sys,GLOBAL,json,types
import usbase.confmanage,usbase.apimanage
from usbase.uslogger import ServerLogger

SERVER_STATUS_STOPED = 0;
SERVER_STATUS_RUNNING = 1;
SERVER_STATUS_ERROR = -1;


########################################################################
class UnbarStorageServer:
	#----------------------------------------------------------------------
	def __init__(self, dbInstance=None):
		"""Construct"""
		self.__serverStatus = SERVER_STATUS_STOPED;

		#########Add Root Path##########

		if GLOBAL.SERVER_ROOT not in sys.path:
			sys.path.append(GLOBAL.SERVER_ROOT)

		#########init server############
		if(self.__loadConf() == False):
			self.__serverStatus = SERVER_STATUS_ERROR;

		GLOBAL.LOGGER = ServerLogger(self.__logDir, ServerLogger.NOTSET);
		self.__serverStatus = SERVER_STATUS_RUNNING;
		
		self.__serverStatus = SERVER_STATUS_RUNNING;
		self.__apiManager = usbase.apimanage.ApiManagerFactory().getInstance(apiPath=self.__apiDir)
		
		
	#----------------------------------------------------------------------
	def __loadConf(self):
		""""""
		suc = False;
		conf =  json.loads(usbase.confmanage.load_server_confs(GLOBAL.SERVER_ROOT, "settings.json"))
		if(conf['errnum'] == 0):
			data = conf.get('data', {});
			self.__dbConf = data.get('data_base', {});
			self.__apiDir = data.get('api_dir', '');
			self.__logDir = data.get('logs_path', '');
			GLOBAL.API_PATH = self.__apiDir
			suc = True;
		else:
			GLOBAL.LOGGER.logError("Failed On Loading Server Configuration ErrorCode:%s ErrorMsg:%s" % (conf['error'], conf['msg']));
		
		return suc;
		
	def executeApi(self, url, params={}, datas={}, method="get", resType='json'):
		return self.__apiManager.execApi(url=url , params=params, datas=datas, method=method, res=resType)
	
	def getServerStatus(self):
		return self.__serverStatus

	def getOsRoot(self):
		return GLOBAL.SERVER_ROOT;

	def __initDb(self, instance):
		"""init database"""
		db = None
		#传入一个工厂函数作为参数，以传入的工厂函数构建数据库处理对象
		if instance and type(instance) == types.FunctionType:
			db = instance(
				dbn=self.__dbConf.get('dbn', ''),
				dburl=self.__dbConf.get('dburl', ''), 
				db=self.__dbConf.get('db', ''),
				user=self.__dbConf.get('user', ''),
				pw=self.__dbConf.get('pw', ''),
			)

		return db