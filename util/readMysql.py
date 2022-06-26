#coding:utf-8

import pymysql
from util.config_handler import yaml_data
from util.logger_handler import logger

mysql_info = {
        "host": yaml_data['mysql']['host'],
        "port": yaml_data['mysql']['port'],
        "user": yaml_data['mysql']['user'],
        "passwd": yaml_data['mysql']['password'],
        "db": yaml_data['mysql']['db']
}


class MysqlUtil():
    """
    mysql 数据库相关操作

    连接数据库信息：mysql_info

    创建游标：mysql_execute

    查询某个字段对应的字符串：mysql_getstring

    查询一组数据： mysql_getrows

    关闭mysql连接：mysql_close
    """

    def  __init__(self):
        self.db_info = mysql_info
        #连接方式
        self.conn = MysqlUtil.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        """
        静态方法，从连接池中取出连接
        :param db_info:
        :return:
        """
        try:
            conn = pymysql.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db']
                                   )
            return conn
        except Exception as a:
            logger.error("数据库链接异常：%s"%a)


    def mysql_execute(self,sql):
        """执行sql语句"""
        cur = self.conn.cursor()
        try:
            #执行sql
            cur.execute(sql)
        except Exception as a:
            #有异常的话回滚
            self.conn.rollback()
            logger.error("执行sql语句出现异常：%s"%a)
        else:
            cur.close()
            #无异常时提交事务
            self.conn.commit()


    def mysql_getrows(self,sql):
        '''返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            logger.error("执行sql语句出现异常%s"%a)
        else:
            rows =cur.fetchall()
            cur.close()
            print(rows)
            return rows

    def  mysql_getstring(self,sql):
        '''查询某个字段的对应值'''
        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
              for i in row:
                return i


    def mysql_close(self):
        '''关闭 mysql'''
        try:
            self.conn.close()
        except Exception as a:
            logger.error("数据库关闭时异常：%s"%a)


if __name__ == "__main__":
    mysql = MysqlUtil()
    sql = "select * from liuyan;"
    #sql1 = "insert into liuyan(name,liuyan) values('吴晓佳','测试')"
    sql2 = "select name from liuyan where liuyan = '吴晓佳'"
    #mysql.mysql_execute(sql1)
    #mysql.mysql_getrows(sql2)
    s = mysql.mysql_getstring(sql2)
    print(s)


