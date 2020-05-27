# num_list = [11, 22, 33]
# for v in num_list:
#     print(v)

from collections import Iterable
from collections import Iterator
import time

class MyList(object):
    def __init__(self):
        self.num_list = [] # 空列表
        self.index = 0 # 记录位置

    def add(self, num):
        # 列表追加元素
        self.num_list.append(num)

    # 如果一个类型可以迭代，这个必须必须重写了__iter__()方法
    # __iter__()返回一个对象的引用，这个对象是谁无所谓, 左边下划线为2个，右边也是一样
    # 但是，这个对象的类中，需要重写__next__()方法
    def __iter__(self):
        return self # 返回一个对象的引用

    def __next__(self):
        if self.index < len(self.num_list):
            ret = self.num_list[self.index] # self.tmp_list[self.index]取出某个元素
            self.index += 1
            return ret
        else:
            # raise抛出异常， StopIteration为内部异常
            # StopIteration专门给for抛出，for循环捕获到StopIteration，自动跳出循环
            # for循环自动处理StopIteration
            raise StopIteration


# 创建对象
num_list = MyList()

# 给对象添加内容
num_list.add(11)
num_list.add(22)
num_list.add(33)

# for v in num_list:
#     print("v = ", v)
#     time.sleep(0.5)

# 第一次
tmp = num_list.__iter__()

while True:
    try:
        v = tmp.__next__()
        print("v = ", v)
    except StopIteration:
        print("遍历完成")
        break

"""
1) 一个类重写了__iter()__方法，它就是可迭代的对象
2) 一个类即重写__iter()__方法，又重写__next__()方法，它就是迭代器
3) 迭代器肯定是可迭代对象，可迭代的对象不一定是迭代器
4) 鱼肯定会游泳，会游泳的不一定是鱼
"""

print(isinstance(num_list, Iterable)) # 判断是否为可迭代对象
print(isinstance(num_list, Iterator)) # 判断是否为迭代器


