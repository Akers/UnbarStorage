#coding=utf-8
'''
Created on 2013-1-19

@author: akers
'''
import types,json,ErrorRef

def getmsg(errnum, language="EN"):
    languages = {"EN":'EN', 'CN':'CN'}
    try:
        error_lst = getattr(ErrorRef, "ERR_REF_%s" % languages.get(language))
    except AttributeError:
        return -1
    for err in error_lst:
        msg = error_lst.get(err).get(errnum, None)
        if msg != None:
            break
    return "%s" % msg

# format a result set as api error
def errorf(errNum, userMsg="", lang="EN", data=None, resType="json"):
    resType = resType.strip().lower()
    if resType == 'json':
        return jsonError(errNum, userMsg, lang, data)
    
# format a result set as normal api result
def resultf(msg="", data=None, resType="json"):
    resType = resType.strip().lower()
    if resType == 'json':
        return jsonRst(data=data, msg=msg)
    
# format a result set as api message
def messagef(userMsg="", data=None, resType="json"):
    resType = resType.strip().lower()
    if resType == 'json':
        return jsonMsg(msg=userMsg, data=data)
        
        

#----------------------------------------------------------------------
def jsonError(errNum, userMsg='', lang="EN", data=None):
    if len(userMsg) > 0:
        userMsg = ":%s"%userMsg
    rst = {"errnum":errNum, "msg":'%s%s'%(getmsg(errNum, lang), userMsg), 'data':data}
    return json.dumps(rst)


#----------------------------------------------------------------------
def jsonMsg(msg, errNum=0, data=None):
    rst = {}
    if errNum > 0:
        rst.update({"errnum":errNum})
    rst.update({"msg":msg, "data":""})
    return rst
    
    
#----------------------------------------------------------------------
def jsonRst(data=None, msg = ""):
    rst = {'errnum': 0, 'msg': msg, 'data': data}
    # rst['error'] = '0'
    # rst['msg'] = msg
    # rst['data'] = data
    return json.dumps(rst)
    # return {"error":0, "msg":msg, "data":json.dumps(rst)}