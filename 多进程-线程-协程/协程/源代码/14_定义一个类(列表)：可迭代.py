# num_list = [11, 22, 33]
# for v in num_list:
#     print(v)

from collections import Iterable

class MyList(object):
    def __init__(self):
        self.num_list = [] # 空列表

    def add(self, num):
        # 列表追加元素
        self.num_list.append(num)

    # 如果一个类型可以迭代，这个必须必须定义了__iter__()方法
    def __iter__(self):
        pass



# 创建对象
num_list = MyList()

# 给对象添加内容
num_list.add(11)
num_list.add(22)
num_list.add(33)

# 判断num_list是否可迭代
print(isinstance(num_list, Iterable)) # 返回True

# TypeError: iter() returned non-iterator of type 'NoneType'
# 类型错误
for v in num_list:
    print(v)
