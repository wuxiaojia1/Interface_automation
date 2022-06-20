#coding:utf-8
import logging
from util.config_handler import yaml_data
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
import re
import time
import os

class LoggerHandler(logging.Logger):
    #继承Logger类
    def __init__(self,name='root',level='DEBUG',file=None,format=None):
        #设置收集器
        super().__init__(name)
        #设置收集器级别
        self.setLevel(level)
        #设置日志格式
        fmt = logging.Formatter(format)
        #日志文件名称
        rq = time.strftime('%Y-%m-%d_%H', time.localtime(time.time()))
        #如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            log_file_handler = TimedRotatingFileHandler(filename=file + 'test_' + rq + '.log', when="D", interval=1,
                                                        backupCount=7)
            log_file_handler.suffix = "%Y-%m-%d_%H.log"
            log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
            log_file_handler.setLevel(level)
            log_file_handler.setFormatter(fmt)
            self.addHandler(log_file_handler)
        #设置streamHandler，输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)
#从yaml配置文件中读取loggin相关配置
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file=yaml_data['logger']['file'],
                       format=yaml_data['logger']['format'])
if __name__ == '__main__':
    logger.debug('哈哈')
    logging.info('你是')
    logging.warning('呼呼')


