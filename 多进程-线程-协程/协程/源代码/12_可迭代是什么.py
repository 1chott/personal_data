from collections import Iterable # Iterable可迭代的， 能迭代

filename = "hello.py"

# 通过for循环遍历打印每一个字符
# 迭代遍历
# 迭代有一个可以记住遍历的位置的对象
# 只能往前不会后退
for v in filename:
    print(v)

# 字符串，列表，元组，字典，可迭代，只要可迭代，就可以通过for循环取出元素
# 任何类型都可以迭代吗？      不是
# 如何判断一个类型是否可以迭代
# 可迭代有什么特点，有什么规定（今天要学习）

# 任何类型都可以迭代吗？      不是
# TypeError: 'int' object is not iterable
# for v in 666:
#     print(v)

# 如何判断一个类型是否可以迭代
# isinstance(666, Iterable)判断6666是否可以迭代，可以返回True, 失败返回False
print(isinstance(666, Iterable))
print(isinstance(filename, Iterable))

