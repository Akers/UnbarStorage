# -*- coding: utf-8 -*-

# 出错代码参照表
ERR_REF_EN = {
    'unknows': {0: 'Un know Errors'},
    'io_errors': {
        101: "File Not Found",  #101，找不到指定文件
        102: "Server Configuration File Not Found"
    },
    'db_errors': {150: 'Unknow Database Error'},
    'api_errors': {
        200: 'User not exists',
        201: 'User password incorrect',
        221: 'AppSecret Uncorrected',
        222: 'Client level too low',
        223: 'token not found please check your request params',
        224: "overdue token please access api:'api/token' on POST method to re-apply an new api token",
        296: 'Unsupported resource type',
        297: 'Unsupport request method',
        298: 'Api Developing',
        299: 'Debug mod unsupported'
    },
    'params_errors': {
        301: 'Illegal param',
        302: 'need more params. this api needs params below'
    }
}

# 出错代码参照表
ERR_REF_CN={
    'result_errors':{
        201: u"找不到指定文件",#101，找不到指定文件
    },
    'server_errors':{
        101: u"服务器配置文件读取失败"
    },
    'api_errors':{}
}
