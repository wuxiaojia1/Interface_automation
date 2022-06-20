#coding:utf-8
import unittest
from util.requests_handler import RequestHandler
from util.readExcel import ExcelHandler
import ddt
import json
from util.logger_handler import logger
from util.config_handler import yaml_data

#taest = [{'payload': "{'username':'wuxiaojia','pwd':'123456'}", 'test_result': None, 'actual_result': 0, 'case_id': 1, 'method': 'post', 'case_title': '正确用户名，正确密码', 'expected_result': 0, 'model_name': '登陆接口', 'url': '127.0.0.1:8888/login'}, {'payload': "{'username':'wuxiaojia1','pwd':'123456'}", 'test_result': None, 'actual_result': 0, 'case_id': 2, 'method': 'post', 'case_title': '错误用户名，正确密码', 'expected_result': 0, 'model_name': '登陆接口', 'url': '127.0.0.1:8888/login'}, {'payload': "{'username':'wuxiaojia','pwd':'1234567'}", 'test_result': None, 'actual_result': 0, 'case_id': 3, 'method': 'post', 'case_title': '正确用户名，错误密码', 'expected_result': 0, 'model_name': '登陆接口', 'url': '127.0.0.1:8888/login'}]
#用例文件
case_file = yaml_data['case']['file']

@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler(case_file)
    case_data = excel.read_excel('login')
    # print(case_data)
    def setUp(self):
        # 请求类实例化
        self.req = RequestHandler()
    def tearDown(self):
        # 关闭session管理器
        self.req.close_session()
    @ddt.data(*case_data)
    def test_login_success(self,items):
        print(items)
        logger.info('*'*88)
        logger.info('当前是第{0}条用例:{1}'.format(items['case_id'],items['case_title']))
        logger.info('当前用例的测试数据：{0}'.format(items))
        # # 请求接口
        print(json.loads(items['payload']))
        res = self.req.visit(method=items['method'],url=items['url'],data=json.loads(items['payload']))
        #接口返回数据转换为字典
        data = res.json()
        try:
            # 断言：预期结果与实际结果对比
            self.assertEqual(data['code'], items['expected_result'])
            logger.info(res)
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            result = 'Fail'
            raise e
        finally:
            # 将响应的状态码，写到excel的第9列，即写入返回的状态码
            TestLogin.excel.write_excel(case_file, 'login', items['case_id'] + 1,8, data['code'])
            # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel(case_file, 'login', items['case_id'] + 1,9, result)

if __name__ == '__main__':
        unittest.main()
