#coding=utf-8
from UsServer import UnbarStorageServer

#print os.listdir("/media/akers/DATA1/projects/python/UnbarStorage/server/usapiserver/ApiPlugs")

sevr = UnbarStorageServer()
sevr.runServer()
print "execute result => ", sevr.executeApi("user/login", "GET")

# import usbase.confmanage, os
#print 'test load xml conf => ', usbase.confmanage.load_xml_api_confs("%s%s%s%s%s"%(os.path.dirname(__file__), os.sep, 'ApiModules', os.sep, 'api_module_configs.xml'))
