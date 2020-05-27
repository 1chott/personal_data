import multiprocessing, time

g_num = 123

def fendian1():
    global g_num
    g_num = 666
    print("fendian111111 = ", g_num)

def fendian2():
    print("fendian222222 = ", g_num)

def main():
    # 创建2进程
    p1 = multiprocessing.Process(target=fendian1)
    p2 = multiprocessing.Process(target=fendian2)

    # 不能直接调用进程处理函数，需要通过start间接调用
    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print("父进程 = ", g_num)



if __name__ == '__main__':
    main()

