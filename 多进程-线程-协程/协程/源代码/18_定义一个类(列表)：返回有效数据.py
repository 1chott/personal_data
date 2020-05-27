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

    # 如果一个类型可以迭代，这个必须必须重写了__iter__()方法
    # __iter__()返回一个对象的引用，这个对象是谁无所谓, 左边下划线为2个，右边也是一样
    # 但是，这个对象的类中，需要定义__next__()方法
    def __iter__(self):
        return MyIterator(self) # 返回一个对象的引用

# 创建另外一个类，这个类专门用于计算位置，返回内容
# 迭代有一个可以记住遍历的位置的对象
# 只能往前不会后退
class MyIterator(object):
    def __init__(self, mylsit_obj):
        self.index = 0   # 专门用于记录位置
        # print("list = ", mylsit_obj.num_list)
        self.tmp_list = mylsit_obj.num_list

    def __next__(self):
        # len(self.tmp_list)列表元素个数
        if self.index < len(self.tmp_list):
            ret = self.tmp_list[self.index] # self.tmp_list[self.index]取出某个元素
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

for v in num_list:
    print("v = ", v)
    time.sleep(0.5)
