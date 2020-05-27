fib_nums = [] #空列表

# 假如要生成100个数，列表需要100个元素空间
# 通过普通函数生成fib
def create_fib(n):
    a = 0
    b = 1

    for i in range(n):
        fib_nums.append(a)
        a, b = b, a+b

create_fib(5)

for v in fib_nums:
    print(v)


