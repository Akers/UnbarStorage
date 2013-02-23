#coding=utf-8
'''
Created on 2013-1-2

@author: Akers
'''
import json,os,rstformater

#----------------------------------------------------------------------
def load_server_confs(sevrRoot, confPath):
    """load OpenStorage Server Configurations"""
    filePath = ""
    fileName = "server.setting"
    if isEndWithSlash(confPath):
        filePath = confPath + fileName
    else:
        filePath = appendBackSlash(sevrRoot) + confPath

    if os.path.exists(filePath):
        jsonStr = open(filePath).read()
        jsonData = json.loads(jsonStr)

        #处理相对路径
        jsonData['api_dir'] = parsePath(jsonData['api_dir'], sevrRoot)
        jsonData['logs_path'] = parsePath(jsonData['logs_path'], sevrRoot)

        result = rstformater.jsonRst(jsonData)
    else:
        result = rstformater.jsonError(101, "Server Configuration File Not Found path:'%s'" % confPath)

    return result


#----------------------------------------------------------------------
def load_json_api_confs(api_path, select=[]):
    result = ""
    if os.path.isdir(api_path) :
        api_path = "%s%s%s" % (api_path, '' if api_path.endswith(os.sep) else os.sep, "api_conf.json")
    if not os.path.exists(api_path) :
        result = rstformater.jsonError(101, "Path Not Found :'%s'" % api_path)
    else :
        #load json file
        json_obj = json.loads(open(api_path).read())
        #create api conf list
        result = {}
        for conf in json_obj['api_list'] :
            if conf['load'] :
                if conf['tax'] not in result :
                    result[conf['tax']] = {}
                result[conf['tax']][conf['name']] = {u'enable':conf.get('enable'),
                                                     u'method':conf.get('method'),
                                                     u'handler':''.join([appendBackSlash(conf.get('url')), conf.get('handler')]),
                                                     u'level':conf.get('level'),
                                                     u'support_result':conf.get('support_result'),
                                                     u'url':conf.get('url') }
        result = rstformater.jsonRst(result)
    return result

#----------------------------------------------------------------------
def load_xml_api_confs(api_path, select=[]):
    result = ""          
    
    if os.path.isdir(api_path) :
        api_path = "%s%s%s" % (api_path, '' if api_path.endswith(os.sep) else os.sep, "api_module_configs.xml")
    if not os.path.exists(api_path) :
        result = rstformater.jsonError(101, "Path Not Found :'%s'" % api_path)
    else :
        #import
        from xml.sax import make_parser
        parser = make_parser()
        handler = __make_confxml_handler()
        parser.setContentHandler(handler)
        try:
            parser.parse(open(api_path, "r"))
        except Exception:
            result = rstformater.jsonError(101, "Exception :'%s'" % Exception.message)
        
        result = rstformater.jsonRst(handler.apimodlelist)

    return result

  
#----------------------------------------------------------------------
def isEndWithSlash(path):
    if path.endswith("/") or path.endswith("\\") : 
        return True
    else :
        return False
    
#----------------------------------------------------------------------   
def appendBackSlash(path):
    if isEndWithSlash(path) : 
        return path
    else :
        return path + os.sep
    

#----------------------------------------------------------------------
def parsePath(path, serverRoot):
    """
            将相对路径中的"/"转换成主模块根目录
    """
    result = path
    if path.startswith("/") or path.startswith("\\"):
        result = serverRoot + path
        
    return result

#----------------------------------------------------------------------
def __make_confxml_handler():
    from xml.sax.handler import ContentHandler
    
    class ApiModelContentHandler(ContentHandler):
        '''节点处理顺序 标签开始 => 子节点 => 文本标签 => 标签结束'''
        def __init__(self):
            self.apimodlelist = None
            self.apimodle = None
            self.currenttag = None
            self.resources = None
            self.handler = None
            self.content = ''
        
        def startElement(self, name, attrs):
            if name == 'api_list':
                self.apimodlelist = []
            elif name == 'api_module':# api_model element
                self.apimodle = {
                     'name':attrs.get('name'), 
                     'load': attrs.get('load', False),
                     'enable': attrs.get('enable', False),
                     'level': attrs.get('level')}
            elif name == 'resource':# api_model/resources element
                self.resources = {'resType':attrs.get('resType', '').split(','),'url':attrs.get('url', '')}
            elif name == 'handler':
                self.handler = {'remote':attrs.get('remote', 'False')}
            self.currenttag = name
        
        def endElement(self, name):
            if name == 'resource':
                self.apimodle.update({'resources': self.resources})
            elif name == 'handler':
                # self.handler = self.content
                dotCount = self.content.count('.')
                if dotCount == 1:
                    strs = self.content.split('.')
                    path = strs[0]
                    className = strs[1]

                    lstSlashIndex = path.find('/') > 0 and path.rindex('/')

                    if lstSlashIndex:
                        name = path[lstSlashIndex+1 : len(path)]
                    else:
                        name = path

                    self.handler.update({'modulePath':path, 'moduleName':name, 'className': className})
                else:
                    print "格式错误:", self.content,"正确格式为dir/HandlerFileName.ClassName"

            elif name == 'api_module':
                self.apimodle.update({'handler': self.handler})
                self.apimodlelist.append(self.apimodle)

            self.content = ''
        
        def characters(self, content):
            self.content += content.strip()
    
    return ApiModelContentHandler()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    