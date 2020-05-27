# 列表推导式
list1 = [x for x in range(3)]
print(list1)

# 生成器，把列表推导式的[]改为(), 返回值为一个生成器对象，直接打印不能打印元素结果
# 生成器也是迭代器，迭代器可以通过for遍历打印
gen = (x for x in range(3))
print(gen)

for v in gen:
    print("v = ", v)