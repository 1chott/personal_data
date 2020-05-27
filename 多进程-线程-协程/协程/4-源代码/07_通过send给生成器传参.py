"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

# 带有yield关键字的函数不是函数，是生成器
# yield的作用，可以让代码暂停执行
def create_fib(n):
    a = 0
    b = 1
    for i in range(n):
        # 第一次调用，暂停，执行到yield a右边，左边还没有执行到
        #下一次执行，从yield a的左边执行
        value = yield a
        print("value = ", value)
        if value == 666:
            a = 8
            b = 13
        elif value == 555:
            a = 3
            b = 5

        a, b = b, a+b


# 返回值不是yield返回的内容， fib_nums它是一个生成器对象，和yield后面有没有跟返回值没有任何关系
# fib_nums和yield关键字有关
fib_nums = create_fib(3)

# next(fib_nums)和fib_nums.send(None)等待
# v = next(fib_nums)

# send可以唤醒yield，通过也可以给yield的左边变量传参
# TypeError: can't send non-None value to a just-started generator
# 第一次调用不能传参
# v = fib_nums.send(None)
v = next(fib_nums)
print("v = ", v)

v = fib_nums.send(666)
print("v = ", v)

v = fib_nums.send(555)
print("v = ", v)




