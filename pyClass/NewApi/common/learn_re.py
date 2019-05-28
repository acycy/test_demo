import re

target = "{'user_name':'#name#';'user_age':'#age#'}"
# 使用#限定查找范围，()表示正则表达式里面组的概念，使用.对字符匹配，使用*表示匹配多次 使用？表示该规则之匹配一次
p2 = '#(.*?)#'

m = re.findall(p2,target)
print(m)