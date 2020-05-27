import multiprocessing, time, os

def fendian1():
    while True:
        # os.getpid()获取当前的进程号, os.getppid()获取父进程号
        print("正在经营分店1111, pid = %d, ppid = %d"%(os.getpid(), os.getppid()))
        time.sleep(1)

def fendian2():
    while True:
        print("正在经营分店2222, pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
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
        # pid, process id
        # ppid, parent process id
        # os.getpid()获取当前的进程号
        print("正在经营总店333, pid = ", os.getpid())
        time.sleep(1)

if __name__ == '__main__':
    main()

