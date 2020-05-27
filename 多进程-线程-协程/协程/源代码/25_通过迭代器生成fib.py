# 根据上一个数生成下一个数(生成器，生成器也是迭代器)，无需先拷贝到列表中，节省内存

class Fib(object):
    # n代表元素个数
    def __init__(self, n):
        self.n = n # 元素个数
        # 前2个数的内容
        self.a = 0
        self.b = 1
        #记录位置的变量
        self.index = 0

    # 可迭代对象，重写__iter__()方法
    def __iter__(self):
        return self # 返回一个对象的引用

    # 迭代器需要重写__next__()方法
    def __next__(self):
        if self.index < self.n:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return  ret
        else:
            raise StopIteration

# 创建迭代器对象
fib_nums = Fib(5)

for v in fib_nums:
    print(v)

