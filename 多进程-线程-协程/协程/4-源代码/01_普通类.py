
class MyList(object):
    def __init__(self):
        self.num_list = [] # 空列表
        self.index = 0 # 记录位置

    def add(self, num):
        # 列表追加元素
        self.num_list.append(num)

    def aaa(self):
        return self # 返回一个对象的引用

    def bbb(self):
        if self.index < len(self.num_list):
            ret = self.num_list[self.index] # self.tmp_list[self.index]取出某个元素
            self.index += 1
            return ret
        else:
            raise StopIteration


# 创建对象
num_list = MyList()

# 给对象添加内容
num_list.add(11)
num_list.add(22)
num_list.add(33)

# 第一次
tmp = num_list.aaa()

while True:
    try:
        v = tmp.bbb()
        print("v = ", v)
    except StopIteration:
        print("遍历完成")
        break


