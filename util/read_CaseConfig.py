#coding:utf-8
from util.config_handler import yaml_data
from util.logger_handler import logger
from util.readExcel import ExcelHandler
import os
import itertools

case_file = yaml_data['case']['file']
excel_sheet = yaml_data['case']['sheet']
case_id = yaml_data['case']['case_id']

def caseConig():
    #判断测试用例是否为空
    if case_file == None:
        logger.error("测试用例目录不能为空，请配置好测试用例目录")
    #如果只有case_file存在值，判断是否为目录，获取文件中所有sheet
    elif case_file != None and excel_sheet == None and case_id == None:
        if os.path.isdir(case_file):
            dir_list = os.listdir(case_file)
            call_list = []
            for filename in dir_list:
                file_path = os.path.join(case_file,filename)
                excel = ExcelHandler(file_path)
                case_data = excel.all_sheet_call()
                call_list.append(case_data)
            #获取嵌套的列表返回一个新的迭代数据
            merge = itertools.chain.from_iterable(call_list)
            result = list(merge)
            return result
        else:
            #读取单个文件中所有sheet的测试用例数据
            excel = ExcelHandler(case_file)
            case_data = excel.all_sheet_call()
            return case_data
    #如果case_file和sheet不为空，判断case_file是否为目录，获取所有case_file文件中sheet
    elif case_file !=None and excel_sheet != None and case_id  == None:
        if os.path.isdir(case_file):
            dir_list = os.listdir(case_file)
            call_list = []
            for filename in dir_list:
                file_path = os.path.join(case_file,filename)
                excel = ExcelHandler(file_path)
                case_data = excel.all_sheet_call(excel_sheet = excel_sheet)
                call_list.append(case_data)
            merge = itertools.chain.from_iterable(call_list)
            result = list(merge)
            return result
        else:
            excel = ExcelHandler(case_file)
            case_data = excel.all_sheet_call(excel_sheet)
            return case_data
    # 如果case_file和case_id不为空，判断case_file是否为目录，获取所有case_file文件所有sheet的case_id
    elif case_file !=None and excel_sheet == None and case_id !=None:
        if os.path.isdir(case_file):
            dir_list = os.listdir(case_file)
            call_list = []
            for filename in dir_list:
                file_path = os.path.join(case_file,filename)
                excel = ExcelHandler(file_path)
                case_data = excel.all_sheet_call(case_id=case_id)
                call_list.append(case_data)
            merge = itertools.chain.from_iterable(call_list)
            result = list(merge)
            return result
        else:
            excel = ExcelHandler(case_file)
            case_data =  excel.all_sheet_call(case_id=case_id)
            return case_data
    # 如果case_file和case_id不为空，判断case_file是否为目录，获取所有case_file文件指定的sheet的case_id
    elif case_file !=None and excel_sheet != None and case_id !=None:
        if os.path.isdir(case_file):
            dir_list = os.listdir(case_file)
            call_list = []
            for filename in dir_list:
                file_path = os.path.join(case_file,filename)
                excel = ExcelHandler(file_path)
                case_data = excel.all_sheet_call(excel_sheet,case_id)
                call_list.append(case_data)
            merge = itertools.chain.from_iterable(call_list)
            result = list(merge)
            return result
        else:
            excel = ExcelHandler(case_file)
            case_data = excel.all_sheet_call(case_id=case_id)
            return case_data








if __name__ == "__main__":
    a = caseConig()
    print(a)

