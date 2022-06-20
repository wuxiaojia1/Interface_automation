#coding:utf-8
import requests
import json

class RequestHandler:

    def __init__(self):
        """
        session 管理器
        """
        self.session = requests.session()

    def visit(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        return self.session.request(method,url,params=params,data=data,json=json,headers=headers,**kwargs)


    def close_session(self):
        """
        关闭session
        :return:
        """
        self.session.close()

if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login'
    payload = {
        "name":"wuxiaojia",
        "pwd":"123456"
    }
    # req = requests.post(url,data=payload)
    req = RequestHandler()
    login_res = req.visit('post',url,data=payload)
    data = login_res.json()
    print(data["code"])
    print(login_res.status_code)
    print(login_res.text)
