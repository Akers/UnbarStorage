#coding=utf-8
'''
Created on 2013-1-2

@author: Akers
'''
import json,os,rstformater,imp


#----------------------------------------------------------------------
def load_server_confs(sevrRoot, confPath):
    """load OpenStorage Server Configurations"""
    filePath = "";
    fileName = "server.setting";
    if isEndWithSlash(confPath):
        filePath = confPath + fileName;
    else:
        filePath = appendBackSlash(sevrRoot) + confPath;
    
    if os.path.exists(filePath):
        jsonStr = open(filePath).read();
        jsonData = json.loads(jsonStr);
        
        #处理相对路径
        jsonData['api_dir'] = parsePath(jsonData['api_dir'], sevrRoot);
        jsonData['logs_path'] = parsePath(jsonData['logs_path'], sevrRoot);
        
        result = rstformater.jsonRst(jsonData)
    else:
        result = rstformater.jsonError(101, "Server Configuration File Not Found path:'%s'" % confPath)
        
    return result;


#----------------------------------------------------------------------
def load_json_api_confs(api_path, select=[]):
    result = ""
    print 'api_path => %s' % api_path
    print 'is_dir => %s' % os.path.isdir(api_path)
    if os.path.isdir(api_path) :
        api_path = "%s%s%s" % (api_path, '' if api_path.endswith(os.sep) else os.sep, "api_conf.json")
    if not os.path.exists(api_path) :
        result = rstformater.jsonError(101, "Path Not Found :'%s'" % api_path)
    else :
        #load json file
        json_obj = json.loads(open(api_path).read())
        print "json_obj => %s" % json_obj
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
        print result
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
        #load xml file
#        if len(result) < 1 or result['error'] == 0:
            
#        json_obj = json.loads(open(api_path).read())
#        #create api conf list
#        result = {}
#        for conf in json_obj['api_list'] :
#            if conf['load'] :
#                if conf['tax'] not in result :
#                    result[conf['tax']] = {}
#                result[conf['tax']][conf['name']] = {u'enable':conf.get('enable'),
#                                                     u'method':conf.get('method'),
#                                                     u'handler':''.join([appendBackSlash(conf.get('url')), conf.get('handler')]),
#                                                     u'level':conf.get('level'),
#                                                     u'support_result':conf.get('support_result'),
#                                                     u'url':conf.get('url') }
#        result = rstformater.jsonRst(result)
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
        return path + os.sep;
    

#----------------------------------------------------------------------
def parsePath(path, serverRoot):
    """
            将相对路径中的"/"转换成主模块根目录
    """
    result = path;
    if path.startswith("/") or path.startswith("\\"):
        result = serverRoot + path;
        
    return result;
    
#----------------------------------------------------------------------
def __make_confxml_handler():
    from xml.sax.handler import ContentHandler
    
    class ApiModelContentHandler(ContentHandler):
        '''节点处理顺序 标签开始 => 子节点 => 文本标签 => 标签结束'''
        apimodlelist = None
        apimodle = None
        currenttag = None
        resources = None
        url = None
        urls = None
        handler = None
        content = ''
        
        def startElement(self, name, attrs):
            print "start element => ", name
            if name == 'api_list':
                self.apimodlelist = []
            elif name == 'api_model':# api_model element
                self.apimodle = {
                     'name':attrs.get('name'), 
                     'load': attrs.get('load'), 
                     'enable': attrs.get('enable'), 
                     'enable': attrs.get('enable'), 
                     'level': attrs.get('level')}
                pass
            elif name == 'resources':# api_model/resources element
                self.resources = {'method':attrs.get('method'),'xml':attrs.get('xml'),'json':attrs.get('json'), 'urls':[]}
                pass
            elif name == 'url':
                self.urls = []
            elif name == 'handler':
                self.handler = {'remote':attrs.get('remote', 'False')}
            self.currenttag = name
        
        def endElement(self, name):
            if name == 'resources':
                self.resources.update({'urls': self.urls})
                self.apimodle.update({'resources': self.resources})
            elif name == 'url':
                self.urls.append(self.content)
            elif name == 'handler':
                self.handler.update({'class':self.content})
            elif name == 'api_model':
                self.apimodlelist.append(self.apimodle)
            self.content = ''
        
        def characters(self, content):
            self.content += content.strip()
    
    return ApiModelContentHandler()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    