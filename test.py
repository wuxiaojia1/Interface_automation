#coding:utf-8
import flask
import json
from flask import request



"""
flask:web框架，通过flask提供的装饰器@server.route（）将普通函数转换为服务器

"""

#创建一个服务，把当前的python文件当成一个服务器
server = flask.Flask(__name__)

#@server.route()转换为服务，登陆接口的路径和请求方式
@server.route('/login',methods=['get','post'])
def login():
    #获取通过url请求传参的数据
    username = request.values.get('name')
    #获取url请求中的密码和明文
    pwd = request.values.get('pwd')
    #判断用户名和密码不能为空
    if username and pwd:
        if username == 'wuxiaojia' and pwd == '1234':
            resu = {'code':200,'message':'登陆成功'}
            return json.dumps(resu,ensure_ascii=False) # 将字典转换为字符串
        else:
            resu = {'code':-1,'message':'账号密码错误'}
            return json.dumps(resu,ensure_ascii=False)
    else:
        resu = {'code':10001,'message':'参数不能为空'}
        return json.dumps(resu,ensure_ascii=False)

if __name__ == "__main__":
    server.run(debug=True,port=8888,host='127.0.0.1')

