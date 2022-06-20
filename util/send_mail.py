#coding:utf-8
"""
smtplib 用于邮件发送的动作
email 用于构建邮件内容
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from util.config_handler import yaml_data
from util.logger_handler import logger


def send_email(smtpserver,port,sender,psw,receiver,title,report_name):
    """
    邮件模板
    :param smtpserver:
    :param port:
    :param sender:
    :param psw:
    :param receiver:
    :return:
    """
    #创建附件实例
    msg = MIMEMultipart()
    #邮件主题
    msg['Subject'] = title
    msg['From'] = sender
    #接收人

    msg['to'] = receiver

    #正文内容
    main_body = """
                    <pre><h1>这是接口自动化测试报告，请查收！</h1></pre>
    """

    #添加正文到容器
    body = MIMEText(main_body,'html','utf-8')

    msg.attach(body)

    #添加附件到容器
    att = MIMEText(open(report_name,'rb').read(),'base64','utf-8')

    att['Content-Type'] = 'application/octet-sream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    msg.attach(att)

    #链接发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,psw)
        smtp.sendmail(sender,receiver.split(","),msg.as_string())
        print("发送邮件成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        logger.error(e)

    finally:
        #关闭服务器
        smtp.quit()


if __name__ == "__main__":
    smtpserver = yaml_data['mail']['smtp_server']
    port = yaml_data['mail']['port']
    sender = yaml_data['mail']['from_addr']
    psw = yaml_data['mail']['psw']
    receiver = yaml_data['mail']['to_addr']
    #receiver = "294927935@qq.com,543402697@qq.com"
    title = yaml_data['mail']['title']
    report_name = "D:\\Interface_automation\\report\\接口测试报告_2022-06-16_23_20_53.html"
    send_email(smtpserver, port, sender, psw, receiver, title, report_name)

