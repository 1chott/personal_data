import re

# result = re.match(r"\d+", "999")
# result = re.match(r"\d+", "python = 999")
# 默认就是从头开始找
# result = re.match(r"^\d+", "999")
# result = re.search(r"\d+", "999")

# search和match区别，search不是从头开始找，只要找到合适的，就提取，只能找一次
result = re.search(r"\d+", "python = 999, aaaa = 888")
print(result.group())