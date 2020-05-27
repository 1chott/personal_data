import time

def work1():
    while True:
        print("work11111111")
        yield
        time.sleep(0.5)

def work2():
    while True:
        print("work22222222")
        yield
        time.sleep(0.5)


def main():
    # 根据生成器函数创建2个生成器对象
    w1 = work1()
    w2 = work2()
    print(w1, w2)

    while True:
        next(w1)
        next(w2)


if __name__ == '__main__':
    main()