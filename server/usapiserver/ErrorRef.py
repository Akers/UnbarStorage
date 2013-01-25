# -*- coding: utf-8 -*-
import sys

self = sys.modules[__name__]

def getmsg(errnum, language="EN"):
    languages = {"EN":'EN', 'CN':'CN'}
    try:
        error_lst = getattr(self, "ERR_REF_%s" % languages.get(language))
    except AttributeError:
        return "Unsupoted Languages:%s" % language
    for err in error_lst:
        msg = error_lst.get(err).get(errnum, None)
        if msg != None:
            break
    return "%s" % msg
    

# 出错代码参照表
ERR_REF_EN={
    'result_errors':{
        201: "File Not Found",#101，找不到指定文件
    },
    'server_errors':{
        101: "Server Configuration File Not Found"
    },
    'api_errors':{}
}

# 出错代码参照表
ERR_REF_CN={
    'result_errors':{
        201: "找不到指定文件",#101，找不到指定文件
    },
    'server_errors':{
        101: "服务器配置文件读取失败"
    },
    'api_errors':{}
}

########################Test#######################
def test():
    print "msg(101, EN) => %s" % getmsg(101, 'EN')
    print "msg(201, EN) => %s" % getmsg(201, 'EN')
    print "msg(301, EN) => %s" % getmsg(301, 'EN')
    print "msg(101, CN) => %s" % getmsg(101, 'CN')
    print "msg(201, CN) => %s" % getmsg(201, 'CN')
    print "msg(301, CN) => %s" % getmsg(301, 'CN')
    print "msg(201, FN) => %s" % getmsg(201, 'FN')
    print "msg(301, FN) => %s" % getmsg(301, 'FN')
    
if __name__ == '__main__':
    test()