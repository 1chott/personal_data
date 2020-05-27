import re

# 需求：匹配163邮箱

buf = ["mike@163.com", "lily@163.comheihei", ".com.mikejiang@qq.com", "aabbcc@163acom"]

for tmp in buf:
    result = re.match(r"\w{4,15}@163\.com$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")