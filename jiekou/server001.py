from flask import Flask,request
import json
import logging

server = Flask(__name__)
logconfig = logging.basicConfig(filename='log.txt',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
@server.route('/index/<name>',methods = ['get','post'])
def ali(name):
    server.logger.info("请求地址为：%s" % request.url)
    res = {"code":"0","message":"success"}
    return json.dumps(res)

server.run(host='0.0.0.0',port='6339',debug=True)