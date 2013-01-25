##coding=utf-8
#from AkBsssServer.AkCore.AkMessager.ApiMessage import api_error
#import os,imp
#
#class ApiLoader(object):
#	API_MODELS = None
#
#	"""docstring for ApiLoader"""
#	def __init__(self):
#		super(ApiLoader, self).__init__()
#		self.API_MODELS = self.api_preload();
#
#	def api_preload(self) :
#		"Scan the apis dir and load the execute function from each api"
#		api_models = {};#initiative the API_MODELS
#		#get the path of apis dir
#		#ToDo: move the apis dir to configuration file
#		api_root_path = os.getcwd() + r'/AkBsssServer/AkCore/apis';
#		#scan the taxonomy dirs
#		for taxonomyPath in os.listdir(api_root_path):
#			taxonomyAbsPath = api_root_path + '/' + taxonomyPath;
#			if os.path.isdir(taxonomyAbsPath):
#				api_models[taxonomyPath] = {};
#				#scan the api dirs of curent taxonomy and load the execute funciton
#				for apiPath in os.listdir(''.join([api_root_path, '/', taxonomyPath])):
#					apiAbsPath = taxonomyAbsPath + '/' + apiPath;
#					if os.path.isdir(apiAbsPath):
#						#load the execute funciton from api execute.py
#						api_models[taxonomyPath][apiPath] = imp.load_source('functions', apiAbsPath+'/functions.py');
#		return api_models
#
#	def get_api_model(self, taxonomy, api_name) :
#		"Get an api executalbe model by api name and returns False when the api name isn`t exisit "
#		rst_val = None;
#		if self.API_MODELS == None : 
#			self.API_MODELS = api_preload();
#		elif taxonomy not in self.API_MODELS :
#			rst_val = api_error("undeclare api taxonomy");
#		elif api_name not in self.API_MODELS[taxonomy] or self.API_MODELS[taxonomy][api_name] == None :
#			rst_val = api_error("undeclare api name");
#		else :
#			rst_val = self.API_MODELS[taxonomy][api_name];
#		return rst_val;