import time
import threading

g_num = 0

def table1(n):
    global  g_num
    for i in range(n):
        g_num += 1

    print("table1111111 = , ", g_num)


def table2(n):
    global g_num
    for i in range(n):
        g_num += 1

    print("table22222222 = , ", g_num)

def main():
    """程序入口"""

    # 创建2个线程
    t1 = threading.Thread(target=table1, args=(1000000, ))
    t2 = threading.Thread(target=table2, args=(1000000, ))

    # 启动线程
    t1.start()
    t2.start()

    time.sleep(3) #保证子进程都指向完毕
    print("table33333333333 = , ", g_num)


if __name__ == '__main__':
    main()