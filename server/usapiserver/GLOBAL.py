#coding=utf-8
'''
Created on 2013-1-18

@author: akers
'''

import os

SERVER_ROOT = os.path.dirname(__file__)
LIB_PATH = "%s%s%s" % (SERVER_ROOT, os.sep, "libs")
LOGGER = None

#def IMPORT_XPATH():
#    print libs.xpath
##    return sys.modules["%s%s%s" % (LIB_PATH, os.sep, "xpath")]
