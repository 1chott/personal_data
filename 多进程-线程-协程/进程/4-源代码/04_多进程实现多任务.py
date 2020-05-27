import multiprocessing, time

def fendian1():
    while True:
        print("正在经营分店111111111111111")
        time.sleep(1)

def fendian2():
    while True:
        print("正在经营分店222222222222222")
        time.sleep(1)

def main():
    # 创建2进程
    # 功能：创建进程，返回一个对象
    # 参数使用和线程一样
    p1 = multiprocessing.Process(target=fendian1)
    p2 = multiprocessing.Process(target=fendian2)

    # 不能直接调用进程处理函数，需要通过start间接调用
    p1.start()
    p2.start()

    while True:
        print("正在经营总店3333333333333")
        time.sleep(1)

if __name__ == '__main__':
    main()

