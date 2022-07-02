#coding:utf-8

import unittest
from util.readCase import TestLogin
from BeautifulReport import BeautifulReport
import time
from util.config_handler import yaml_data
from util.send_mail import send_email


#用例执行
def  run_case():
    #继承测试用例套件
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTest(loader.loadTestsFromTestCase(TestLogin))
    #定义测试报告名称
    new = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_path = yaml_data['report']['path']
    report_name = report_path + "接口测试报告_" + new +".html"

    with open(report_name,"wb+") as file:
        result = BeautifulReport(suit)
        result.report(description='接口测试报告',filename='接口测试报告_'+ new,report_dir=report_path)
        #发送邮件报告,定义模板
        smtpserver = yaml_data['mail']['smtp_server']
        port = yaml_data['mail']['port']
        sender = yaml_data['mail']['from_addr']
        psw = yaml_data['mail']['psw']
        receiver = yaml_data['mail']['to_addr']
        title = yaml_data['mail']['title']
        #发送邮件
        send_email(smtpserver, port, sender, psw, receiver, title, report_name)

if __name__ == '__main__':
    run_case()








