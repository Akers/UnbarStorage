#coding=utf-8
'''
Created on 2013-1-19

@author: akers
'''
import json

#----------------------------------------------------------------------
def jsonError(errNum, msg, data=None):
    return {"error":errNum, "msg":msg, "data":""}
    
    
#----------------------------------------------------------------------
def jsonRst(data, msg = ""):
    return {"error":0, "msg":msg, "data":data}    