import re

# re.sub(r"正在表达式", "替换的内容", "匹配的字符串")

# 和findall一样，找所有的，多了一个功能，替换
# 返回的结果，替换后的字符串
result = re.sub(r"\d+", "666", "python=5, cpp=3, go=2")
print(result)