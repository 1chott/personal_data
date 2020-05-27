import re

# re.sub(r"正在表达式", 函数名字, "匹配的字符串")

# 函数必须有参数，就是一个正则对象
# 函数的返回值，字符串，就是替换的内容
def change(tmp):
    # print(tmp.group()) #取出匹配后的内容
    # int(tmp.group()) 字符串转换为整型，+10
    a = int(tmp.group()) + 10

    #  str(a)整型转换为字符串
    return str(a)

# 和findall一样，找所有的，多了一个功能，替换
# 返回的结果，替换后的字符串
result = re.sub(r"\d+", change, "python=5, cpp=3, go=2")

print(result)


ret = re.sub(r" +", ":", "a  b   c   d e f", 4)
print(ret)
print(type(ret))
ret1 = re.match(r"2", "2")
print(type(ret1))
ret3 = re.finditer(r"as.", "ababsbsbababsbabsdbashasdhsdasjassaudsadusadjsajdsafufsaisadjadsai")
print(ret3)
