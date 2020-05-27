# num_list = [11, 22, 33]
# for v in num_list:
#     print(v)

from collections import Iterable
import time

class MyList(object):
    def __init__(self):
        self.num_list = [] # 空列表

    def add(self, num):
        # 列表追加元素
        self.num_list.append(num)

    def aaa(self):
        return MyIterator() # 返回一个对象的引用


class MyIterator(object):
    def bbb(self):
        return 666

# 创建对象
num_list = MyList()

# 给对象添加内容
num_list.add(11)
num_list.add(22)
num_list.add(33)

# 第一次
tmp = num_list.aaa()

while True:
    v = tmp.bbb()
    print("v = ", v)
    time.sleep(0.5)

