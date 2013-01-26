#coding=utf-8
from UsServer import UnbarStorageServer


sevr = UnbarStorageServer()
sevr.runServer()
print "execute result => ", sevr.executeApi("user/login", "GET")

# path = 'a/b/c'
# sub = 'a/b'
# print len(path)
# print path[path.rindex('/')+1:len(path)]
