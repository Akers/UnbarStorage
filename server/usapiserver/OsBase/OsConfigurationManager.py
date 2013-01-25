#coding=utf-8
import os, json;

#----------------------------------------------------------------------
def load_os_conf(path, serverRoot):
	"""load OpenStorage Server Configurations"""
	filePath = "";
	fileName = "os_settings.json";
	if path.endswith("/") or path.endswith("\\"):
		filePath = path + fileName;
	else:
		filePath = path + "/" + fileName;
	
	if os.path.exists(filePath):
		jsonStr = open(filePath).read();
		jsonData = json.loads(jsonStr);
		
		#处理api dir
		jsonData['logs_path'] = parsePath(jsonData['logs_path'], serverRoot);
		
		result = {"error":0, "data": jsonData}
	else:
		result = {"error":101, "msg":"Settings File Not Found", "data":""}
		
	return result;

#----------------------------------------------------------------------
def parsePath(path, serverRoot):
	if path.startswith("/") or path.startswith("\\"):
		return serverRoot + path;



#----------------------------------------------------------------------
def load_api_conf():
	"""load apiplugins configuration"""
	result = "";
	return result;