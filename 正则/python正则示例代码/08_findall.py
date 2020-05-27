import re

# findall和search区别，findall匹配所有的，找到后，以列表返回，无需调用group
result = re.findall(r"\d+", "python = 999, aaaa = 888")
print(result)
for i in result:
    print(i)