import re

# 通过正则匹配字符串，成功返回一个有效的对象，失败返回None
result = re.match(r"hello", "aab")

if result: #不为None进入此条件
    # result.group()取出成功匹配的结果
    print("匹配结果为：", result.group())
else:
    print("匹配失败")