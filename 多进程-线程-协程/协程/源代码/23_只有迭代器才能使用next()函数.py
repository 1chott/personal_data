from collections import Iterable
from collections import Iterator

num_list = [11, 22, 33]

# 判断是不是可迭代对象，迭代器
# num_list它是可迭代对象，不是迭代器
print("isinstance(num_list, Iterable) = ", isinstance(num_list, Iterable))
print("isinstance(num_list, Iterator) = ", isinstance(num_list, Iterator))

"""
# 只有迭代器才能使用next()函数
while True:
    try:
        # TypeError: 'list' object is not an iterator
        v = next(num_list)
        print("v = ", v)
    except StopIteration:
        print("遍历完成")
        break
"""

# iter函数，把迭代对象转换为迭代器，返回一个新的对象
tmp = iter(num_list)
print("isinstance(tmp, Iterator) = ", isinstance(tmp, Iterator))

while True:
    try:
        v = next(tmp)
        print("v = ", v)
    except StopIteration:
        print("遍历完成")
        break




