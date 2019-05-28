

import requests

class HttpRequest(object):
    '''用于完成http的get和post请求，并返回结果'''
    def http_request(self,method,url,param,cookies=None):
        '''根据请求方法选择post或者get请求
        method:post get http请求方法
        url:发送请求的地址
        param:随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文
        '''
        #为什么这里需要upper？
        if method.upper() == "GET":
            try:
                rtype = requests.get(url=url, params=param,cookies=cookies)
            except Exception as e:
                print("GET请求出错，错误是{}".format(e))
        elif method.upper() == "POST":
            try:
                rtype = requests.post(url=url, data=param,cookies=cookies)
            except Exception as e:
                print("POST请求出错，错误是{}".format(e))
        else:
            print("请求方法不支持")
            rtype = None
        return rtype

if __name__ == '__main__':
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    method = "POST"
    # 以字典的方式存储数据
    param = {"mobilephone":"13420190312","pwd":"123456"}

    #测试类
    test_case = HttpRequest()
    res = test_case.http_request(method, url, param)
    print(res.text)
    print(res.cookies)
