import usbase
from usbase.apihandler import ApiHandler

class LoginHandler(ApiHandler):
    """docstring for LoginHandler"""
    def __init__(self):
        super(LoginHandler, self).__init__()

    def execute(self):
        params = super(LoginHandler, self).getParams()
        print "LoginHandler executing~"
        for param in params:
            print "param => ", param


        