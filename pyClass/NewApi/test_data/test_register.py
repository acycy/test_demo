import unittest
from ddt import ddt, data
from NewApi.common.http_request import HttpRequest
from NewApi.common.do_excel import DoExcel
from NewApi.common import project_path
from NewApi.common.my_logger import MyLogger

my_log = MyLogger()
test_data = DoExcel(project_path.case_path, "register").read_data("RegisterCase")

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t = DoExcel(project_path.case_path, "register")

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    def test_cases(self,case):
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info("测试数据是{}".format(case))
        resp = HttpRequest().http_request(method,url,param)

        #比对
        try:
            self.assertEqual(eval(case["ExceptedResult"]),resp.json())
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
            raise e
        finally:
            #不论如何都要写回的数据放在finally里面
            self.t.write_data(case["CaseId"] + 1, 8, resp.text)#这里因为要写入的是字符串类的数据，不可以是json，所以使用的是text
            self.t.write_data(case["CaseId"] + 1, 9, TestResult)
        my_log.info("实际结果是{}".format(resp.json()))
