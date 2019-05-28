

import os


#该文件的路径
path_1 = os.path.realpath(__file__)

#使用切割方式获取该项目的路径
project_path = os.path.split(os.path.split(path_1)[0])[0]

#测试用例的路径
case_path = os.path.join(project_path,"test_data","test_api.xlsx")

#测试报告的路径
report_path = os.path.join(project_path,"test_result","test_report","test_report.html")

#日志的路径
log_path = os.path.join(project_path,"test_result","test_log","test.log")

#配置文件的路径
conf_path = os.path.join(project_path,"conf","case.conf")
