
from NewApi.common import project_path
from NewApi.common import read_config
import re

#创建一个读取配置文件的类
config = read_config.ReadConfig(project_path.conf_path)

#读取配置文件
class GetDate(object):
    '''配置可变数值'''
    #类的反射
    COOKIES = None
    #LOAN_ID = None
    normal_user = config.get_str("data","normal_user")
    normal_pwd = config.get_str("data","normal_pwd")
    normal_member_id = config.get_str("data","normal_member_id")


def replace(target):
    p2 = '#(.*?)#'
    #使用while替换全部的数据
    while(re.search(p2,target)):
        #获取查找之后的对象
        m = re.search(p2, s2)
        # group(1)传参：只返回当前匹配字符
        key = m.group(1)
        value = getattr(GetDate, key)
        # 替换key和value
        target = re.sub(p2, value, target, count=1)
    return target


