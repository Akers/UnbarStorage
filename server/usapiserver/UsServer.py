#coding=utf-8
import os,sys, GLOBAL;

from usbase.uslogger import ServerLogger
import usbase.confmanage
from usbase.apimanage import ApiManager

SERVER_STATUS_STOPED = 0;
SERVER_STATUS_RUNNING = 1;
SERVER_STATUS_ERROR = -1;


########################################################################
class UnbarStorageServer:
	#----------------------------------------------------------------------
	def __init__(self):
		"""Construct"""
		self.__serverStatus = SERVER_STATUS_STOPED;

		#########Add Root Path##########

		if GLOBAL.SERVER_ROOT not in sys.path:
			sys.path.append(GLOBAL.SERVER_ROOT)


	#----------------------------------------------------------------------	
	def runServer(self):
		"""Run Server"""
		if(self.__loadConf() == False):
			self.__serverStatus = SERVER_STATUS_ERROR;
		
		print self.__dbType + "\n";
		print self.__apiDir + "\n";
		print self.__logDir + "\n";
		
		
		GLOBAL.LOGGER = ServerLogger(self.__logDir, ServerLogger.NOTSET);
		GLOBAL.LOGGER.logInfo("Starting Server...");
		
		self.__serverStatus = SERVER_STATUS_RUNNING;
		
		GLOBAL.LOGGER.logInfo("Server Started Successfully");
		
		self.__serverStatus = SERVER_STATUS_RUNNING;
		
		self.__apiManager = ApiManager(self.__apiDir)
		
	#----------------------------------------------------------------------
	def __loadConf(self):
		""""""
		suc = False;
		conf =  usbase.confmanage.load_server_confs(GLOBAL.SERVER_ROOT, "settings.json");
		if(conf['error'] == 0):
			data = conf['data'];
			self.__dbType = data['data_base'];
			self.__apiDir = data['api_dir'];
			self.__logDir = data['logs_path'];
			suc = True;
		else:
			GLOBAL.LOGGER.logError("Failed On Loading Server Configuration ErrorCode:%s ErrorMsg:%s" % (conf['error'], conf['msg']));
		
		return suc;
			
	#----------------------------------------------------------------------
	def __regPackage(self, path):
		""""""
		
	
	def executeApi(self, url, method="GET"):
		print self.__apiManager.execApi(url, [])
		pass;
	
	def getOsRoot(self):
		return GLOBAL.SERVER_ROOT;