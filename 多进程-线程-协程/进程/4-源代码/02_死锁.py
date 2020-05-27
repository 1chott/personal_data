import time
import threading

g_num = 0

def table1(n, mutex):
    global  g_num
    for i in range(n):
        mutex.acquire(timeout=1) # 1秒后自动解锁
        g_num += 1
        mutex.release()  # 解锁

    print("table1111111 = , ", g_num)


def table2(n, mutex):
    global g_num
    for i in range(n):
        mutex.acquire(timeout=1) # 加锁
        g_num += 1
        mutex.release()  # 解锁

    print("table22222222 = , ", g_num)

def main():
    """程序入口"""

    # 创建锁，说默认是打开的
    # 返回一个对象
    mutex = threading.Lock()

    # 创建2个线程
    t1 = threading.Thread(target=table1, args=(5, mutex))
    t2 = threading.Thread(target=table2, args=(5, mutex))

    # 启动线程
    t1.start()
    t2.start()

    time.sleep(3) #保证子进程都指向完毕
    print("table33333333333 = , ", g_num)


if __name__ == '__main__':
    main()
