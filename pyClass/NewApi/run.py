#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time: 2019/3/16 11:46
# @Author：Viola
# @File: run.py

import unittest
import HTMLTestRunnerNew
from NewApi.test_data import test_recharge
from NewApi.test_data import  test_register
from  NewApi.test_data import test_addload
from NewApi.test_data import  test_invest
from NewApi.common import project_path

#新建一个测试集
suite = unittest.TestSuite()

#添加测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_invest.TestCases))

#执行用例，生成测试报告
with open(project_path.report_path, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="测试报告",
                                              description="测试报告",
                                              tester="lala")
    #执行用例，传入测试集
    runner.run(suite)



