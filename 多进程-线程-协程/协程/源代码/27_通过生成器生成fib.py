

# 带有yield关键字的函数不是函数，是生成器
# yield的作用，可以让代码暂停执行
def create_fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

# 返回值不是yield返回的内容， fib_nums它是一个生成器对象，和yield后面有没有跟返回值没有任何关系
# fib_nums和yield关键字有关
fib_nums = create_fib(10)
print(fib_nums)

# v = next(fib_nums)
# print("v = ", v)
#
# v = next(fib_nums)
# print("v = ", v)
#
# v = next(fib_nums)
# print("v = ", v)

# while True:
#     try:
#         v = next(fib_nums)
#         print("v = ", v)
#     except StopIteration:
#         print("遍历完成")
#         break

for v in fib_nums:
    print("v = ", v)


