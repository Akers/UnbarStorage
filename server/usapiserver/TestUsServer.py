#coding=utf-8
import json
from UsServer import UnbarStorageServer

sevr = UnbarStorageServer()
# print "execute result => ", sevr.executeApi("user/login", "GET")

print sevr.executeApi('apiadmin/apilist', {'mod':'listall'}, {'token', '1GvS4B6K'}, 'get')


# path = 'a/b/c'
# sub = 'a/b'
# print len(path)
# print path[path.rindex('/')+1:len(path)]
