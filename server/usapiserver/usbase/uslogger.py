#encoding=utf8
import types, logging, time, os


########################################################################
class ServerLogger:
	""""""
	
	NOTSET = logging.NOTSET;
	DEBUG = logging.DEBUG;
	INFO = logging.INFO;
	WARNING = logging.WARNING;
	ERROR = logging.ERROR;
	CRITICAL = logging.CRITICAL;
	
	
	#----------------------------------------------------------------------
	def __init__(self, logDir, level = logging.NOTSET):
		"""Constructor"""
		#当level不是整形时，默认为NOTSET
		self.__logLevel = (type(level) == types.IntType and level) or logging.NOTSET;
		
		self.__logDir = logDir;
		
		self.__logger = self.__initLogger();
	
	
	#----------------------------------------------------------------------
	def logError(self, msg):
		"""append a error to log file"""
		self.__logger.error(msg);
		
	#----------------------------------------------------------------------
	def logInfo(self, msg):
		"""append a info to log file"""
		self.__logger.info(msg);
		
	#----------------------------------------------------------------------
	def setLevel(self, level):
		""""""
		#当level参数为整形，__logLevel的值为 level 否则为0
		self.__logger.setLevel((type(level) == types.IntType and level) or 0);
		
		
	#----------------------------------------------------------------------
	def __initLogger(self):
		""""""
		logger = logging.getLogger();
		timeStr = time.strftime('%Y-%m-%d', time.localtime());
		if not (self.__logDir.endswith("/") or self.__logDir.endswith("\\")):
			self.__logDir += "/";
		
		logPath = self.__logDir + timeStr + ".log";
		if not os.path.exists(self.__logDir):
			os.mkdir(self.__logDir);
		if (not os.path.exists(logPath)) and os.path.isfile(logPath):
			os.open(logPath, "w").close();
#			os.mknod(logPath)
		#create handlers:
		file_hdlr = logging.FileHandler(logPath);
		console_hdlr = logging.StreamHandler();
		
		#log fomat
		formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s');
		file_hdlr.setFormatter(formater);
		console_hdlr.setFormatter(formater);
		
		#add handler to logger
		logger.addHandler(file_hdlr);
		logger.addHandler(console_hdlr)
		logger.setLevel(self.__logLevel);
		return logger;
	