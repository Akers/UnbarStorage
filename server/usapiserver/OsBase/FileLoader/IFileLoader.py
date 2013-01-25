#coding=utf-8
import os;

########################################################################
class FileLoader:
	""""""

	#----------------------------------------------------------------------
	def __init__(self, path):
		"""Constructor"""
		self.__path = path;
		
	#----------------------------------------------------------------------
	def load_file(self):
		""""""
		rs = "";
		if os.path.exists(self.__path):
			__file = open(path);
			rs = __file.read();
			__file.close();
		return rs;
		
    
	