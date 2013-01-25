#coding=utf-8
import IFileLoader.FileLoader;
import json;

########################################################################
class JsonFileLoader(IFileLoader.FileLoader):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, path):
		"""Constructor"""
		IFileLoader.FileLoader.__init__(self, path);
		
	#----------------------------------------------------------------------
	def load_file(self):
		""""""
		result = "";
		jsonStr = IFileLoader.FileLoader.load_file();
		if jsonStr != "" :
			result = json.JSONDecoder.decode(jsonStr);
			
		return(result);
		
    
	