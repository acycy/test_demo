
import unittest
from ddt import ddt, data
from NewApi.common.http_request import HttpRequest
from NewApi.common.do_excel import DoExcel
from NewApi.common import project_path
from NewApi.common.my_logger import MyLogger
from NewApi.common.get_data import GetDate
from NewApi.common.do_mysql import DoMysql

my_log = MyLogger()
test_data = DoExcel(project_path.case_path, "addload").read_data("AddLoanCASE")
COOKIES = None

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t = DoExcel(project_path.case_path, "addload")

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    def test_cases(self,case):

        global TestResult
        #global COOKIES
        method = case['Method']
        url = case['Url']

        #替换load_id，此时已经查询到了我们之前的loanid
        if case['Params'].find('loanid') != -1:
            param = eval(case['Params'].replace('loanid', str(getattr(GetDate, 'LOAN_ID'))))  # 因为拿到的数据是int类型 replace只能用在字符串之间的替换 所以用str强转一下
        else:
            param = eval(case['Params'])  # 请求参数

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        #my_log.info("测试数据是{}".format(case))
        resp = HttpRequest().http_request(method,url,param,cookies = getattr(GetDate,"COOKIES"))
        my_log.info("实际结果是{}".format(resp.json()))

        # 判断是否要查询数据库,查询获取loanid
        if case['Sql'] != None:  # 如果sql语句不为None 那就是要进行数据库的查询操作
            loan_id = DoMysql().do_mysql(eval(case['Sql'])['Sql'], 1)  # 返回的是元组，所以我们存储数据的时候 最好是根据索引拿到值之后 再去做进一步操作
            setattr(GetDate, 'LOAN_ID', loan_id[0])  # 利用反射


        #增加判断如果cookie不为空就更新cookies的值，这样可以获取最新的cookies值
        if resp.cookies:
            #COOKIES = resp.cookies
            setattr(GetDate,"COOKIES",resp.cookies)

        #进行断言写入数据
        TestResult = "None"
        try:
            self.assertEqual(eval(case["ExceptedResult"]),resp.json())
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
            raise e
        finally:
            #不论如何都要写回的数据放在finally里面
            self.t.write_data(case["CaseId"] + 1, 9, resp.text)#这里因为要写入的是字符串类的数据，不可以是json，所以使用的是text
            self.t.write_data(case["CaseId"] + 1, 10, TestResult)






