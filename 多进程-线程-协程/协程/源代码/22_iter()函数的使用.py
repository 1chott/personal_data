from collections import Iterable
from collections import Iterator

num_list = [11, 22, 33]

# 判断是不是可迭代对象，迭代器
# num_list它是可迭代对象，不是迭代器
print("isinstance(num_list, Iterable) = ", isinstance(num_list, Iterable))
print("isinstance(num_list, Iterator) = ", isinstance(num_list, Iterator))

# iter函数，把迭代对象转换为迭代器
tmp = iter(num_list)
print("isinstance(tmp, Iterator) = ", isinstance(tmp, Iterator))

for v in tmp:
    print("v = ", v)



